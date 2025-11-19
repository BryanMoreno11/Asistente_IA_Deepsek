from langchain_core.prompts import PromptTemplate

QA_TEMPLATE_PROMPT = PromptTemplate(
    input_variables=["chat_history","context", "question"],
    template=(
        "--- HISTORIAL ---\n"
        "{chat_history}\n"
        "-----------------\n\n"

        "--- PREGUNTA DEL Estudiante ---\n"
        "{question}\n"
        "-------------------------------\n\n"

        "Respuesta útil para el estudiante en un tono amable:"
    )
)