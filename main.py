import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# CREATE DATABASE meubanco

# Conexão com o banco de dados.
Session = sessionmaker(bind=db)
session = Session()

# I/0
# I = input (Entrada)
# O = output (Saída)

# Abrindo uma conexão
Base = declarative_base()

# Criando tabela.
class Usuario(Base):
    # Definindo nome da tablea
    __tablename__ = "usuarios"

    # Definindo atributos da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

# Salvar banco de dados
# for i in range(2)
    # nome = input("Digite o seu nome: ")
    # email = input("Digite a sua idade: ")
    # senha = input("Digite a sua senha: ")

    # usuario = Usuario(nome=nome, senha=senha, email=email)
    # session.add(usuario)
    #session.commit()

# usuario = Usuario("Ruan", "Ruan@gmail.com", "123")
usuario = Usuario(nome="Ruan", email="Ruan@gmail.com", senha="123")
session.add(usuario)
session.commit()

# Mostrando conteúdo do banco de dados.
# SELECT * FROM Usuarios
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome}  - {usuario.email}")

# pip install sqlalchemy
# ORM
