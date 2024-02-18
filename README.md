# Welcome to Polygot.AI

to run: `pip install -r requirements.txt && reflex run`

Make sure to include your OpenAI and/or TogetherAI API key in the `.env` file.

## Inspiration
As members of immigrant families, we often encounter the significant challenge of language barriers when communicating with family members in our home countries. This issue has become more prevalent since the onset of the COVID-19 pandemic, leading to missed opportunities and lack of meaningful connections with long distance family members. While the straightforward solution might seem to be speaking the language at home and utilizing educational platforms like DuoLingo or Babbel for practice, it's not as simple as it appears. People often lose motivation or focus solely on obtaining the correct answers on these apps. This challenge inspired us to create a more engaging and interactive conversational companion. By offering users the opportunity to engage in real conversations, this tool enhances language practice and improves proficiency through repeated speaking iterations.

## What it does
Our web platform offers users the opportunity to learn various languages through a tailored lesson plan upon selecting a language. It includes sub-lessons that involve engagement with articles or short videos on specific topics. This design emulates the interactive experience of a traditional classroom setting.

Following the consumption of these materials, users engage with AI Chat Companion for a unique twist on language learning: voice-to-voice conversations. Users speak into the microphone, and their input is processed in real time. The AI companion analyzes the spoken responses and replies with audio feedback. Conversations are seamlessly conducted and can be concluded using a language-specific keyword(eg "terminador" for Spanish).

The AI focuses primarily on understanding, with grammar and punctuation as secondary feedback priorities. We had the intent of fostering a conversational environment that enhances speaking skills and provides a comprehensive speaking experience for learners.

## How we built it
Our product was developed using a combination of various technologies and frameworks to ensure an ideal interactive user experience.

For image conversion, we utilized Covertio, which is a tool used for converting JPEG images into SVG format, which allows us to integrate a high quality vector graphic into the website's UI. The user interface was designed using Reflex, which is a flexible, open-source, full stack python framework which allowed for an efficient deployment of the app. The framework unified front and backend, which allowed us to implement both purely in python. We adopted a sidebar template from Reflex to organize content and ensure an intuitive navigation experience for users.

Python was the core of our AI functionality, where the chatbot service and speech-to-text and text-to-speech processing was developed using Python, Open AI APIs, and Speech Text from Google Cloud. The use of Python allowed for access to diverse libraries and frameworks that support AI. The chatbot was integrated using Python enabling real time interactions with users. The component was crucial for simulating the conversation experience.

For speech recognition and synthesis, we used Google Cloud's Speech Text APIs, which provided the backbone for our backend implementation for accurate NLP training, and our basis for prompt engineering. The speech detection feature on google cloud allowed for strong capabilities in audio processing. The Open AI API allowed for real time translation within a language during conversations.

## Challenges we ran into
The development process involved navigating through a complex landscape of technical challenges. One of our initial struggles was dealing with framework compatibility. The integration of Reflex, which is a significantly different framework compared to Node.js and React, led to a fairly substantial learning curve. Understanding the framework required time to understand the components and best practices to ensure a responsive design. We were able to perform comprehensive research as a team and speak with the sponsors for any issues we had. We performed extensive testing to ensure compatibility.

Configuring speech-to-text service to accurately recognize and process spoken language presented difficulties with dialects, accents, and other background noise. Effective prompt engineering that elicited useful responses form the chatbot while ensuring flow of conversation was difficult. We were able to utilize Google Cloud's Speech Text API for its real time speech recognition capabilities. We applied practices in natural language processing and conducted user testing to refine interactions.

Deciding on the best platform for speech-to-text development involved in evaluating various options based on latency was another difficulty, along with ensuring the chat bot remained on topic with coherent responses were some of the final backend challenges.

## Accomplishments that we're proud of
We are proud of figuring out and programming an organized UI platform using an architecture and framework we had no experience with. Working together as a team and problem solving with each through issues in speech to text interpretation, prompt engineering, and training the LLM is something we feel great about.

## What we learned
We learned that pivoting to a brand new UI platform with no prior knowledge about is a challenging task, especially regarding the difficulty of having a comprehensive understanding within the duration of the hackathon. We learned how to implement OpenAI APIs and Speech Text APIs from Google Cloud, and the development behind creating speech(from user) to speech(chatbot) communication. We also learned how to divide and conquer, as well as work together on tasks that were difficult.

## What's next for Polyglot.AI
Fine tuning the LLM for a more structured response from the chat bot would make the learning experience more ideal. Improving our UIUX process and design it to be more interactive and flow more effectively. Improving the environment of the platform to make the communication purely as speech to speech.