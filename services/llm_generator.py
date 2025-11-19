from openai import OpenAI
from prompts.system_prompts import RAG_SYSTEM_PROMPT
from typing import List
from langchain.schema import Document
from langchain_core.messages import BaseMessage,trim_messages, HumanMessage, AIMessage

from config import settings

class DeepseekLLM:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=False,
        )
        return response.choices[0].message.content

class LLMReasoner:
    def __init__(self, llm: DeepseekLLM, prompt_template, memory_manager):
        self.llm = llm
        self.prompt_template = prompt_template
        self.memory_manager = memory_manager

    @staticmethod
    def render_history(msgs: list[BaseMessage]) -> str:
        LMAP = {"human": "HUMANO", "ai": "ASISTENTE"}
        return "\n".join(f"{LMAP.get(m.type, m.type).upper()}: {m.content}" for m in msgs)
    

    def generate_answer(self,session_id: str, query: str) -> str:
        #Obtención del hisorial de conversación
        history = self.memory_manager.get_memory(session_id)
        trimmed = trim_messages(
            history.messages,
            token_counter=len,
            max_tokens=settings.MAX_MSGS_HISTORY,
            strategy="last",
            start_on="human",
            include_system=True,
    )
        chat_history = self.render_history(trimmed)
        #Documentos recuperados
        system_prompt = RAG_SYSTEM_PROMPT
        # El prompt donde se inserta contexto y pregunta, para el rol user
        user_prompt = self.prompt_template.format( chat_history=chat_history, question=query)
        # Generar respuesta
        answer = self.llm.generate(system_prompt=system_prompt, user_prompt=user_prompt)
        #Guardar Pregunta y respuesta en la BD
        history.add_message(HumanMessage(query))
        history.add_message(AIMessage(answer))
        return answer
