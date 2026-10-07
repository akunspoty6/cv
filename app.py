from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
import db
import functools
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize Database
db.init_db()

def login_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ==================== PUBLIC ROUTES ====================

@app.route('/')
def index():
    conn = db.get_db()
    profile = dict(conn.execute('SELECT * FROM profile LIMIT 1').fetchone() or {})
    
    skills_raw = conn.execute('SELECT * FROM skills ORDER BY level DESC').fetchall()
    skills_by_category = {}
    for s in skills_raw:
        cat = s['category']
        if cat not in skills_by_category:
            skills_by_category[cat] = []
        skills_by_category[cat].append(dict(s))
        
    experiences = [dict(r) for r in conn.execute('SELECT * FROM experiences ORDER BY order_num ASC, id DESC').fetchall()]
    education = [dict(r) for r in conn.execute('SELECT * FROM education ORDER BY order_num ASC, id DESC').fetchall()]
    projects = [dict(r) for r in conn.execute('SELECT * FROM projects ORDER BY order_num ASC, id DESC').fetchall()]
    
    conn.close()
    return render_template('index.html', profile=profile, skills=skills_by_category, experiences=experiences, education=education, projects=projects)

# ==================== AUTH ROUTES ====================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        conn = db.get_db()
        admin = conn.execute('SELECT * FROM admin WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if admin and check_password_hash(admin['password_hash'], password):
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error="Username atau Password salah!")
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('login'))

# ==================== ADMIN ROUTES ====================

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

# ==================== API ROUTES ====================

@app.route('/api/profile', methods=['GET', 'POST'])
@login_required
def api_profile():
    conn = db.get_db()
    if request.method == 'GET':
        profile = dict(conn.execute('SELECT * FROM profile LIMIT 1').fetchone() or {})
        conn.close()
        return jsonify(profile)
    
    if request.method == 'POST':
        data = request.json
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE profile SET 
            full_name=?, title=?, tagline=?, bio=?, email=?, phone=?, location=?, github=?, linkedin=?, avatar_url=?
            WHERE id=1
        ''', (
            data.get('full_name'), data.get('title'), data.get('tagline'), data.get('bio'), 
            data.get('email'), data.get('phone'), data.get('location'), data.get('github'), 
            data.get('linkedin'), data.get('avatar_url')
        ))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "message": "Profile updated!"})

# Generic API functions for tables
def table_api(table_name):
    conn = db.get_db()
    if request.method == 'GET':
        items = [dict(r) for r in conn.execute(f'SELECT * FROM {table_name}').fetchall()]
        conn.close()
        return jsonify(items)
        
    elif request.method == 'POST':
        data = request.json
        cursor = conn.cursor()
        
        # Identify columns
        cols = [c for c in data.keys() if c != 'id']
        vals = [data[c] for c in cols]
        
        if data.get('id'): # Update
            set_clause = ', '.join([f"{c}=?" for c in cols])
            cursor.execute(f'UPDATE {table_name} SET {set_clause} WHERE id=?', (*vals, data['id']))
        else: # Insert
            cols_str = ', '.join(cols)
            qmarks = ', '.join(['?'] * len(cols))
            cursor.execute(f'INSERT INTO {table_name} ({cols_str}) VALUES ({qmarks})', vals)
            
        conn.commit()
        conn.close()
        return jsonify({"success": True})
        
    elif request.method == 'DELETE':
        item_id = request.json.get('id')
        conn.execute(f'DELETE FROM {table_name} WHERE id=?', (item_id,))
        conn.commit()
        conn.close()
        return jsonify({"success": True})

@app.route('/api/skills', methods=['GET', 'POST', 'DELETE'])
@login_required
def api_skills():
    return table_api('skills')

@app.route('/api/experiences', methods=['GET', 'POST', 'DELETE'])
@login_required
def api_experiences():
    return table_api('experiences')

@app.route('/api/education', methods=['GET', 'POST', 'DELETE'])
@login_required
def api_education():
    return table_api('education')

@app.route('/api/projects', methods=['GET', 'POST', 'DELETE'])
@login_required
def api_projects():
    return table_api('projects')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
