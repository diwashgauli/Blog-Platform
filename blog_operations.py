from database import get_connection

def add_post(title, content, category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title, content, category) VALUES (?, ?, ?)',
                   (title, content, category))
    conn.commit()
    conn.close()

def view_posts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts ORDER BY timestamp DESC')
    posts = cursor.fetchall()
    conn.close()
    return posts

def update_post(post_id, new_title, new_content, new_category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE posts
        SET title = ?, content = ?, category = ?
        WHERE id = ?
    ''', (new_title, new_content, new_category, post_id))
    conn.commit()
    conn.close()

def delete_post(post_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
