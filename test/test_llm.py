import sys
import os
current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root_dir = os.path.join(current_script_dir, '..')
sys.path.append(project_root_dir)



from services.rag_pipeline import RAGPipeline

def main():
    pipeline = RAGPipeline()
    print("Sistema RAG listo. Escribe 'salir' para terminar.")
    while True:
        query = input("Pregunta: ")
        if query.lower() == "salir":
            break
        respuesta = pipeline.answer_query(query)
        print(f"Respuesta: {respuesta}\n")

if __name__ == "__main__":
    main()
