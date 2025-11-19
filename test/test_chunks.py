# consultar_chunks.py
import sys
import os
current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root_dir = os.path.join(current_script_dir, '..')
sys.path.append(project_root_dir)

from services.indexing import load_vector_store
from config import settings


def print_chunks_by_uid(uid: str):
    """
    Carga el índice vectorial y busca e imprime todos los chunks
    pertenecientes a un UID de documento específico.
    """
    # Llama a la función de tu módulo de indexación para cargar el índice
    store = load_vector_store(settings.FAISS_PATH, settings.EMBEDDING_MODEL)
    if store is None:
        print("El índice vectorial no se encontró. Asegúrate de que exista la carpeta 'faiss_index'.")
        return

    v_dict = store.docstore._dict
    chunks_found = False
    
    for k, doc in v_dict.items():
        # Usa .get() para evitar errores si 'document_uid' no existe
        if doc.metadata.get('document_uid') == uid:
            chunks_found = True
            print("--------------------------------------------------")
            print(f"ID del Chunk: {k}")
            print(f"Fuente del documento: {doc.metadata.get('source')}")
            print("--- Contenido del Chunk ---")
            print(doc.page_content)
            print("--------------------------------------------------")

    if not chunks_found:
        print(f"No se encontraron chunks para el documento con UID: {uid}")

if __name__ == "__main__":
    # --- Configuración para la búsqueda ---
    # Coloca aquí el UID del documento que quieres consultar.
    UID_A_BUSCAR = 'd20c5abe-bee0-47eb-b90a-d82e99e56677'

    if UID_A_BUSCAR == 'tu_uid_aqui':
        print("Por favor, reemplaza 'tu_uid_aqui' con el UID del documento que quieres buscar.")
    else:
        print(f"Buscando chunks para el UID: {UID_A_BUSCAR}")
        print_chunks_by_uid(UID_A_BUSCAR)