import os
import sys

current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root_dir = os.path.join(current_script_dir, '..')
sys.path.append(project_root_dir)

from services.transcription import transcribe_audio
from services.rag_pipeline import RAGPipeline


def main():
    pipeline = RAGPipeline()
    audio_file = os.path.join(project_root_dir, 'sample_question_es.mp3')
    text = transcribe_audio(audio_file)
    print(f"Pregunta transcrita: {text}")
    respuesta = pipeline.answer_query(text)
    print(f"Respuesta: {respuesta}\n")


if __name__ == '__main__':
    main()