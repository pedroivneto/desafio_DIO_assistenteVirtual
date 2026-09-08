import os
from dotenv import load_dotenv

# Carrega o arquivo .env localizado na mesma pasta
load_dotenv()

GEMINI_API_KEY  = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("A chave GEMINI_API_KEY não foi encontrada no arquivo .env!")