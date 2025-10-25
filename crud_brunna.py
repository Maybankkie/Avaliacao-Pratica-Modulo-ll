import sqlite3

conexao = sqlite3.connect('escola.db', timeout=20)

cursor = conexao.cursor()

print('conexão criada com sucesso')

cursor.execute('''

    CREATE TABLE IF NOT EXISTS alunos (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL          
    )


                ''')

cursor.execute("INSERT INTO alunos ('nome','email','idade') VALUES (?,?,?)",('Maria','mariafernanda3@gmail.com',14))
cursor.execute("INSERT INTO alunos ('nome','email','idade') VALUES (?,?,?)",('Eduardo','eduardoribeiro3@gmail.com',13))

conexao.commit()

conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()


consulta = cursor.execute("SELECT * FROM alunos")

for lista in consulta.fetchall():
    print(lista)

cursor.execute("UPDATE alunos SET idade = ? WHERE email = ?", ('mariafernanda3@gmail.com',14))
conexao.commit()

cursor.execute("DELETE from alunos WHERE nome = ?", ('Maria',))
conexao.commit()
conexao.close()