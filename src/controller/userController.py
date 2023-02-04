import sqlite3

def read_users():
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        return users
    except:
        return {"code": 404, "message": "Nenhum usuário encontrado"}
    finally:
        conn.close()

def create_user(userCreate):
    name, email, password = userCreate.values()
    try:
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
        return user
    except:
        return {"code": 404, "message": "Email já cadastrado"}
    finally:
        conn.close()
        
def update_user(updateUser):
    idUser, name, email = updateUser.values()
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id = ?", (idUser,))
        user = c.fetchone()
        
        if user[1] == name and user[2] != email:
            c.execute("UPDATE users SET email = ? WHERE id = ?", (email, idUser))
            conn.commit()
            return("Alterações de email realizadas")
        else: 
            if user[1] != name and user[2] == email:
                c.execute("UPDATE users SET name = ? WHERE id = ?", (name, idUser))
                conn.commit()
                return("Alterações de nome realizadas")
            else:
                if user[1] != name and user[2] != email:
                    c.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, idUser))
                    conn.commit()
                    return("Alterações de nome e email realizadas")
                else:
                    if user[1] == name and user[2] == email:
                        return("Não há alterações")
    except:
        return {"code": 404, "message": "Usuário não encontrado"}
    finally:
        conn.close()


def delete_user(identifier):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("DELETE FROM users WHERE id = ?", (identifier,))
        conn.commit()
        return {"code": 200, "message": "Usuário deletado com sucesso"}
    except:
        return {"code": 404, "message": "Usuário não encontrado"}
    finally:
        conn.close()