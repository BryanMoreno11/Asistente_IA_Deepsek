# services/memory_manager.py
from langchain_mongodb import MongoDBChatMessageHistory
from config import settings


class MemoryManager:
    """Devuelve una memoria por usuario con ventana k."""
    def __init__(self):
        self.uri = settings.MONGODB_URI

    def get_memory(self, session_id: str):
        return MongoDBChatMessageHistory(
            connection_string=self.uri,
            session_id=session_id,        # ← clave por usuario
            collection_name= settings.MONGODB_COLLECTION,
            create_index=True,
            history_size=None
        )
       
