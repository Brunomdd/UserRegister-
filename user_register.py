# Importa a biblioteca mysql.connector, que permite conectar o Python ao MySQL
import mysql.connector

# Estabelece a conexão com o banco de dados MySQL
# A função connect() é usada para criar uma conexão com o servidor MySQL
conexao = mysql.connector.connect(
    host='localhost',    # Define o host como 'localhost', ou seja, o banco de dados está rodando localmente na máquina
    user='root',         # Define o nome do usuário como 'root' (usuário padrão no MySQL)
    password='',         # A senha é deixada em branco, o que pode ser o caso se o MySQL não exigir senha para o usuário 'root'
    database='create_users'  # Define o banco de dados ao qual a conexão será feita, no caso, 'create_users'
)

# Cria um cursor, que é um objeto usado para executar comandos SQL e recuperar resultados do banco de dados
cursor = conexao.cursor()
