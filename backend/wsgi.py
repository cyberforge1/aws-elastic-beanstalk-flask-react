# backend/wsgi.py

from dotenv import load_dotenv
import os

# Load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
