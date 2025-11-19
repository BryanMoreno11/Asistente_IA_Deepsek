import sys
import os
current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root_dir = os.path.join(current_script_dir, '..')
sys.path.append(project_root_dir)

#region Importaciones
import time
import os
from services.document_processing import (
    extract_text_from_pdf,
    split_with_token_chunker,
    sanitize_text
    
)

from config import settings

#Extración de texto
if __name__ == "__main__":
    print("Iniciando el procesamiento de documentos PDF...")
    startTime= time.time()
    all_docs = []
    for filename in os.listdir(settings.PDF_FOLDER):
        if filename.endswith(".pdf"):
            print(f"Procesando {filename}...")
            pdf_path = os.path.join(settings.PDF_FOLDER, filename)
            doc = extract_text_from_pdf(pdf_path)
            chunks = split_with_token_chunker(doc,pdf_path,filename)
            clean_chunks = sanitize_text(chunks)
            for chunk in chunks:
                print("El contenido es", chunk.page_content, "\n")
            all_docs.extend(chunks)
    endTime= time.time()
    elapsedTime= (endTime-startTime)/60
    print(f"Tiempo de ejecución: {elapsedTime:.2f} minutos")