import sqlite3

def read_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users

def find_user_by_email(email:str, password:str):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    print(email, password)
    try:
        c.execute("SELECT * FROM users WHERE email = ? AND password = ? ", (email, password,))
        idUser, nameDoBanco, emailDoBanco, passwordDoBanco = c.fetchone()
        user = {
            "id": idUser,
            "name": nameDoBanco,
            "email": emailDoBanco,
        }
        return user
    except:
        return {"code": 404, "message": "Email ou senha incorretos"}
    finally:
        conn.close()

def create_user(userCreate):
    name, email, password = userCreate.values()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    idUser, name, email, password = c.fetchone()
    user = {
        "id": idUser,
        "name": name,
        "email": email,
    }
    conn.commit()
    conn.close()
    return user

def update_user(updateUser):
    idUser, name, email = updateUser.values()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (idUser,))
    user = c.fetchone()
    
    if user[1] == name and user[2] != email:
        c.execute("UPDATE users SET email = ? WHERE id = ?", (email, idUser))
        conn.commit()
        conn.close()
        return("Alterações de email realizadas")
    else: 
        if user[1] != name and user[2] == email:
            c.execute("UPDATE users SET name = ? WHERE id = ?", (name, idUser))
            conn.commit()
            conn.close()
            return("Alterações de nome realizadas")
        else:
            if user[1] != name and user[2] != email:
                c.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, idUser))
                conn.commit()
                conn.close()
                return("Alterações de nome e email realizadas")
            else:
                if user[1] == name and user[2] == email:
                    return("Não há alterações")


def delete_user(identifier):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM users WHERE id = ?", (identifier,))
        idUser, name, email, password = c.fetchone()
        print(identifier)
        user = {
            "code": 200,
            "id": idUser,
            "name": name,
            "email": email,
            "message": "Usuário deletado com sucesso"
        }
        if identifier != None and user != None:
            c.execute("DELETE FROM users WHERE id = ?", (identifier,))
            conn.commit()
            conn.close()
            return user
        else:
            conn.commit()
            conn.close()
            return("Não há usuário para deletar")
    except:
        return {"code": 404, "message": "Usuário não encontrado"}