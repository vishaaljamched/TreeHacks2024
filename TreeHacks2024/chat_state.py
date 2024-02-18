import reflex as rx
from openai import OpenAI
import requests
import os
from dotenv import load_dotenv
from TreeHacks2024.backend.speechToText import main

from .prompts import DISCUSSION1_PROMPT, DISCUSSION2_PROMPT
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

    def set_discussion2(self):
        self.clear_chat("Discussion1")
        self.clear_chat("Discussion2")
        self.current_chat = "Discussion2"
        self.set_prompt(DISCUSSION2_PROMPT)
        self.add_ai_chat("Antes de resumir el vídeo, da brevemente tu reacción. ¿Qué opinas?")

    def set_discussion1(self):
        self.clear_chat("Discussion1")
        self.clear_chat("Discussion2")
        self.current_chat = "Discussion1"
        self.set_prompt(DISCUSSION1_PROMPT)
        self.add_ai_chat("Antes de resumir el vídeo, da brevemente tu reacción. ¿Qué opinas?")
   
    async def transcribe_question(self):
        question = main()
        if question == "":
            return

        model = self.openai_process_question

        async for value in model(question):
            yield value
    
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
