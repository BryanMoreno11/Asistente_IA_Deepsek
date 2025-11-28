from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DEEPSEEK_API_KEY: str = "sk-1b4ca7947f3e41b18202953faf567e7b"
    API_CHAT_ENDPOINT: str = "http://localhost:5000/api/chat"
    MONGODB_URI:str="mongodb://localhost:27017/"
    MONGODB_COLLECTION:str="asistenteIA"
    MAX_MSGS_HISTORY:int=8
    SESSION_ID:int=1
    MODEL_NAME:str="deepseek-chat"
    MODEL_URL:str="https://api.deepseek.com"

    class Config:
        env_file = ".env"

settings = Settings()