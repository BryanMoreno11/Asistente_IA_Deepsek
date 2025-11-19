from services.llm_generator import DeepseekLLM, LLMReasoner
from config import settings
from prompts.prompt_templates import QA_TEMPLATE_PROMPT
from services.memory_manager import MemoryManager
class RAGPipeline:
    def __init__(self):
       
        self.memory_manager = MemoryManager()
        self.reasoner = LLMReasoner(
            llm=DeepseekLLM(api_key=settings.DEEPSEEK_API_KEY),
            prompt_template=QA_TEMPLATE_PROMPT,
            memory_manager=self.memory_manager,
        )

    def answer_query(self,session_id: str, query: str) -> str:
        try:
            return self.reasoner.generate_answer(session_id, query)
        except Exception as e:
            print(f"[ERROR] Fallo al responder la consulta: {e}")
            return "Ocurrió un error al procesar su pregunta. Por favor, intente nuevamente más tarde."
        

