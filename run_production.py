from waitress import serve
# Certifique-se de que isso corresponde ao nome do seu arquivo e objeto Flask
from app import app

serve(app, host="0.0.0.0", port=5000)
