API Livros com Flask + Waitress
-------------------------------
<p>
📌 Projeto: API Livros (app.py)<br/>
Descrição:<br/>
API REST para gerenciamento de livros, desenvolvida em Python usando o microframework Flask. O projeto é executado pelo arquivo principal app.py e utiliza o servidor Waitress para produção, garantindo estabilidade e performance.<br/>
<br/>
🚀 Tecnologias utilizadas<br/>
<br/>
Python 3<br/>
Flask (app.py)<br/>
Waitress<br/>
JSON<br/>
Git<br/>
VS Code<br/>
</p>
<p>
✅ 1. Pré-requisitos<br/>
Python 3.x instalado<br/>
pip funcionando no terminal<br/>
Editor de código (ex: VS Code)<br/>

🚀 2. Instalação das dependências<br/>
Abra o terminal (cmd, PowerShell ou Git Bash) na pasta do projeto e execute:<br/>
pip install -r requirements.txt<br/>

📦 3. Conteúdo do requirements.txt<br/>
Coloque esse conteúdo no arquivo:<br/>
flask<br/>
waitress<br/>

🧠 4. Explicação dos arquivos<br/>
app.py: Define os dados e os endpoints da API.<br/>
run_production.py: Usa o servidor Waitress para rodar a API em modo produção.<br/>
requirements.txt: Lista de bibliotecas necessárias.<br/>

▶️ 5. Como rodar a API em produção<br/>
No terminal, execute:<br/>

python run_production.py<br/>
Se tudo estiver certo, verá algo como:<br/>

Serving on http://0.0.0.0:5000<br/>
Acesse em: http://localhost:5000/livros<br/>

📌 Observações<br/>
Em produção, não use app.run().<br/>

Waitress é estável e recomendado para Windows.<br/>
Se quiser publicar a API na internet, pode usar ferramentas como ngrok ou serviços de hospedagem (Render, Heroku, etc.).<br/>
</p>
### Criar o banco e tabela 
<p>
✅ 1. Instale o SQLite (opcional)<br/>
SQLite já vem embutido no Python através do módulo sqlite3, então não precisa instalar nada adicional.<br/>

✅ 2. Adicione dependências no requirements.txt<br/>
pip install -r requirements.txt<br/>

✅ 3. Crie o banco de dados e a tabela (init_db.py)<br/>
python init_db.py<br/>
</p>

### Incluindo livros via json<br/>
<p>
Execute o metodo POST com o exemplo de livro em json<br/>
{<br/>
    "titulo": "Dom Casmurro",<br/>
    "autor": "Machado de Assis"<br/>
}<br/>
</p>
<p>
📁 Estrutura de arquivos do projeto<br/>
</p>
<p>
projeto/<br/>
├── app.py               ← Código principal da API<br/>
├── run_production.py    ← Script para rodar em produção<br/>
├── requirements.txt     ← Dependências do projeto<br/>
├── livros.db            ← será criado automaticamente<br/>
├── init_db.py           ← Crie o banco de dados e a tabela<br/>
└── requirements.txt     ← Adicione dependências no requirements.txt<br/>
└── README.txt           ← Instruções<br/>
</p>

### Criado por:<br/>
Walace Pessôa<br/>
Rio de Janeiro, Brasil<br/>
V01.01.00
