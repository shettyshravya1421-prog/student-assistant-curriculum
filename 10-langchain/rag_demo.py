from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

my_model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-20b"
)

found_info = "A linked list connects items using pointers."

my_prompt = ChatPromptTemplate.from_template(
    "Here is some info: {info}\nNow answer this question: {question}"
)

my_chain = my_prompt | my_model

answer = my_chain.invoke({
    "info": found_info,
    "question": "What is a linked list?"
})

print(answer.content)