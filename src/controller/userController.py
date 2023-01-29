import sqlite3

def find_user_by_email(email:str):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = c.fetchone()
    conn.close()
    return user

def create_user(name, email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()
    conn.close()

def read_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users

def update_user(id, name, email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (id,))
    user = c.fetchone()
    if user[1] == name and user[2] != email:
        c.execute("UPDATE users SET email = ? WHERE id = ?", (email, id))
        conn.commit()
        conn.close()
        return("Alterações de email realizadas")
    else: 
        if user[1] != name and user[2] == email:
            c.execute("UPDATE users SET name = ? WHERE id = ?", (name, id))
            conn.commit()
            conn.close()
            return("Alterações de nome realizadas")
        else:
            if user[1] != name and user[2] != email:
                c.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, id))
                conn.commit()
                conn.close()
                return("Alterações de nome e email realizadas")
            else:
                if user[1] == name and user[2] == email:
                    return("Não há alterações")

def delete_user(email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE email = ?", (email,))
    conn.commit()
    conn.close()

