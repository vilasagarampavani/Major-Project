from pyngrok import ngrok
import os
from dotenv import load_dotenv

load_dotenv()
ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN"))
ngrok.kill()
public_url = ngrok.connect(8501)
print(f"Public URL: {public_url}")
