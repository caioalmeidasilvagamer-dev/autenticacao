# Sistema de Autenticação

Aplicação web com cadastro, login e controle de acesso por cargo, feita com Flask e SQLite.

## Tecnologias

- Python
- Flask
- SQLite
- Werkzeug (hash de senha)
- HTML e CSS

## Como rodar

1. Instale as dependências:
   pip install flask

2. Rode o servidor:
   python app.py

3. Acesse no navegador:
   http://localhost:5000/cadastro

## Funcionalidades

- Cadastro de usuário com senha criptografada
- Login com verificação de hash
- Sessão persistente entre páginas
- Controle de acesso por cargo (usuário e admin)
- Página protegida — redireciona pro login se não autenticado
- Logout com limpeza de sessão