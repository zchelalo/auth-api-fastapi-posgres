from jwt import encode, decode
from dotenv import load_dotenv
import os

load_dotenv()
JWT_KEY = os.getenv("JWT_KEY")

def create_token(data: dict) -> str:
  token: str = encode(payload=data, key=JWT_KEY, algorithm="HS256")
  return token

def validate_token(token: str) -> dict:
  data: dict = decode(token, key=JWT_KEY, algorithms=["HS256"])
  return data