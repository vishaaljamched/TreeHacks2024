import reflex as rx
from openai import OpenAI
import requests
import os
from dotenv import load_dotenv
load_dotenv()
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
client = OpenAI(api_key=TOGETHER_API_KEY, base_url='https://api.together.xyz')
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
    current_chat = "Discussion1"
    question: str
    processing: bool = False
    api_type: str

    def set_chat(self, chat_name: str):
        self.current_chat = chat_name

    def clear_chat(self, chat_name: str):
        DEFAULT_CHATS[chat_name] = []

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
        print(question)
        self.chats[self.current_chat].append(qa)
        self.processing = True
        yield
        messages = [
            {"role": "system", "content": "You are a Spanish teacher, teaching a class in Spanish on climate change. You must respond to all messages in Spanish."}
        ]
        for qa in self.chats[self.current_chat]:
            messages.append({"role": "user", "content": qa.question})
            messages.append({"role": "assistant", "content": qa.answer})
        messages = messages[:-1]
        session = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=messages,
            stream=True,
        )
        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                answer_text = item.choices[0].delta.content
                self.chats[self.current_chat][-1].answer += answer_text
                self.chats = self.chats
                yield
        self.processing = False