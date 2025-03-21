# Importa a biblioteca mysql.connector, que permite conectar o Python ao MySQL
import mysql.connector
import bcrypt

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

# Executa o comando SQL para criar uma tabela 'users' no banco de dados
cursor.execute('''
    CREATE TABLE users (
    id int auto_increment not null,
    nome varchar(100),
    email varchar(100) UNIQUE,
    senha varchar(255),
    primary key (id)
    )default charset = utf8;
''')
print('*=*=*' * 5)  # Para adicionar uma linha antes
print(' CADASTRO USUÁRIOS ', end='')  # Para imprimir sem quebra de linha
print('*=*=*' * 5)  # Para adicionar uma linha depois
nome = input("Digite o nome: ")
email = input("Digite o email: ")
senha  = input("Digite a senha: ")

# Gerar hash da senha corretamente
salt = bcrypt.gensalt()
senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)

# Insere os dados fornecidos pelo usuário (nome, email, senha) na tabela 'users'
cursor.execute("INSERT INTO users (nome,email,senha) VALUES (%s,%s,%s)",(nome,email,senha_hash))

# Confirma a inserção dos dados no banco de dados
conexao.commit()
# Exibe uma mensagem informando que o cadastro foi realizado com sucesso
print("Usuário Cadastrado com sucesso!")

# Imprime uma mensagem para indicar que a lista de usuários será exibida
print("\nListas usuários")

# Executa a consulta SQL para selecionar todos os registros da tabela 'users
cursor.execute("SELECT * FROM users")

# Obtém todos os registros retornados pela consulta e armazena em 'usuarios'

usuarios = cursor.fetchall()

# Laço que percorre cada tupla na lista de 'usuarios'

for usuario in usuarios:
    # Exibe cada tupla (registro) do usuário no console

    print(usuario)
# Fecha o cursor, liberando os recursos do banco de dados

cursor.close()
# Fecha a conexão com o banco de dados, liberando os recursos
conexao.close()