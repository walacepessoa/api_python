API Livros com Flask + Waitress

📁 Estrutura de arquivos do projeto
projeto/
├── app.py               # Código principal da API
├── run_production.py    # Script para rodar em produção
├── requirements.txt     # Dependências do projeto
└── README.txt           # Instruções

✅ 1. Pré-requisitos
Python 3.x instalado
pip funcionando no terminal
Editor de código (ex: VS Code)

🚀 2. Instalação das dependências
Abra o terminal (cmd, PowerShell ou Git Bash) na pasta do projeto e execute:

pip install -r requirements.txt
📦 3. Conteúdo do requirements.txt
Coloque esse conteúdo no arquivo:

flask
waitress
🧠 4. Explicação dos arquivos
app.py: Define os dados e os endpoints da API.
run_production.py: Usa o servidor Waitress para rodar a API em modo produção.
requirements.txt: Lista de bibliotecas necessárias.

▶️ 5. Como rodar a API em produção
No terminal, execute:

python run_production.py
Se tudo estiver certo, verá algo como:

Serving on http://0.0.0.0:5000
Acesse em: http://localhost:5000/livros

📌 Observações
Em produção, não use app.run().

Waitress é estável e recomendado para Windows.
Se quiser publicar a API na internet, pode usar ferramentas como ngrok ou serviços de hospedagem (Render, Heroku, etc.).
