import reflex as rx
from openai import OpenAI
import requests
import os
from dotenv import load_dotenv

DISCUSSION1_PROMPT = """
Eres un profesor de español dando una clase sobre cambio climático. Su estudiante acaba de ver un video y su trabajo es asegurarse de que comprenda firmemente los conceptos cubiertos.

Aquí hay un resumen:
El cambio climático es el resultado del aumento anormal de la temperatura del planeta, provocado por las actividades humanas.
Este fenómeno aumenta e intensifica los desastres naturales como huracanes, sequías e inundaciones, afectando la seguridad alimentaria y los medios de vida de poblaciones enteras.
El aumento de los gases de efecto invernadero ha provocado desequilibrios ambientales, resultando en importantes pérdidas económicas; en el caso de Costa Rica, más de 710 millones de dólares.
Costa Rica cuenta con áreas y ecosistemas especialmente vulnerables a los efectos del cambio climático, como manglares, arrecifes y zonas montañosas.
Los impactos del cambio climático incluyen consecuencias ecológicas, económicas y sociales, como la escasez de agua, problemas en la generación de electricidad debido a las sequías y el aumento de zonas propensas a inundaciones.
Finalmente, el video sugiere que, a pesar de ser una amenaza, el cambio climático también representa una oportunidad, posiblemente en alusión a la posibilidad de tomar medidas para mitigar sus efectos y adaptarse a los cambios.

El estudiante responderá al mensaje: Resuma el vídeo, por favor. ¿Cuáles son los tres puntos principales?

Su trabajo es decidir si el estudiante ha satisfecho la pregunta. Si han proporcionado con precisión tres puntos cubiertos en el video, entonces usted puede decir "¡Genial! Puede pasar a la siguiente discusión. No les dé las respuestas si están fuera de tema; en su lugar, simplemente guíe al estudiante de regreso a El tema." "

Siéntase libre de pedirle al estudiante que explique más sobre un punto, pero también sea generoso al decidir si uno de los puntos que menciona coincide con un punto planteado en el video.

El estudiante es un hablante nativo de inglés, así que asegúrese de corregir sus errores gramaticales u ortográficos, o sugerirle un mejor vocabulario para que lo use. También anime al estudiante a permanecer en español si cambia al inglés. Ajusta la dificultad de tu vocabulario dependiendo de qué tan cómodo se sienta el estudiante con el español.

Antes de profundizar en las preguntas, se preguntará al alumno su reacción ante el vídeo. Siempre que ofrezcan una reacción razonable, puedes continuar respondiendo a sus pensamientos y pedirles que procedan a resumir los puntos principales del video.
SÓLO DEBES responder en español.
"""

load_dotenv()
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


class QA(rx.Base):
    """A question and answer pair."""
    question: str
    answer: str


DEFAULT_CHATS = {
    "Discussion1": [],
    "Discussion2": []
}


class ChatState(rx.State):
    """Define empty state to allow access to rx.State.router."""

    chats: dict[str, list[QA]] = DEFAULT_CHATS
    current_chat: str = "Discussion1"
    question: str
    processing: bool = False
    api_type: str
    prompt: str

    def set_chat(self, chat_name: str):
        self.current_chat = chat_name

    def add_ai_chat(self, ai_chat):
        prompt = QA(question="", answer=ai_chat)
        self.chats[self.current_chat].append(prompt)

    def clear_chat(self, chat_name: str):
        DEFAULT_CHATS[chat_name] = []

    def set_prompt(self, prompt: str):
        self.prompt = prompt

    def set_discussion1(self):
        self.clear_chat("Discussion1")
        self.current_chat = "Discussion1"
        self.set_prompt(DISCUSSION1_PROMPT)
        self.add_ai_chat("Antes de resumir el vídeo, da brevemente tu reacción. ¿Qué opinas?")

    async def process_question(self, form_data: dict[str, str]):
        question = form_data["question"]
        if question == "":
            return

        model = self.openai_process_question

        async for value in model(question):
            yield value

    async def openai_process_question(self, question: str):
        """Get the response from the API.

        Args:
            form_data: A dict with the current question.
        """
        qa = QA(question=question, answer="")
        self.chats[self.current_chat].append(qa)
        self.processing = True
        yield
        messages = [
            {"role": "system", "content": self.prompt}
        ]
        for qa in self.chats[self.current_chat]:
            messages.append({"role": "user", "content": qa.question})
            messages.append({"role": "assistant", "content": qa.answer})
        messages = messages[:-1]
        print(messages)
        session = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            stream=True,
        )
        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer_text = item.choices[0].delta.content
                if answer_text is not None:
                    self.chats[self.current_chat][-1].answer += answer_text
                yield
        self.processing = False
