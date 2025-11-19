import sys
import os
import time
current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root_dir = os.path.join(current_script_dir, '..')
sys.path.append(project_root_dir)

from services.retriever import DocumentRetriever

def main():
    timeStart = time.time()
    retriever = DocumentRetriever()
    query = "18.	¿Cuál es la frecuencia y método recomendado de deshoje de protección para minimizar cicatrices y asegurar la calidad de la fruta?"
    docs = retriever.retrieve(query)
    timeEnd = time.time()
    elapsed_time = (timeEnd - timeStart)/60  # Convertir a minutos
    print(f"Tiempo de ejecución: {elapsed_time:.2f} minutos")
    print(f"Se encontraron {len(docs)} documentos relevantes:\n")
    for i, doc in enumerate(docs, start=1):
        page = doc.metadata.get("page", "N/A")
        print(f"--- Documento {i} (página {page}) ---")
        print(doc.page_content)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
