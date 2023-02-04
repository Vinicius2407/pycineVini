from sqlalchemy import Boolean, Column, Integer, String

import sys
sys.path.append("src\database")
import database

class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)