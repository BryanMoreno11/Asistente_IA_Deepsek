from flask import Blueprint, request, jsonify
from services.rag_pipeline import RAGPipeline
from config import settings

bp_rag = Blueprint("asistant_routes", __name__)
pipeline = RAGPipeline() 

@bp_rag.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    query = data.get("question")
    session_id  = settings.SESSION_ID
    if not query or not session_id:
        return jsonify({"error": "Faltan parámetros (question, session_id)."}), 400

    try:
        answer = pipeline.answer_query(session_id,query)
        return jsonify({"answer": answer}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

