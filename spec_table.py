import os
import pandas as pd
import openai
import warnings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

openai.api_type = "azure"
openai.api_version = "2023-05-15"

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")


customer_review = input(print("please enter the details:"))


review_template = '''
f"Create a table from the following product description:Table:"
text: {text}
'''

prompt_template = ChatPromptTemplate.from_template(review_template)
messages = prompt_template.format_messages(text=customer_review)
chat = ChatOpenAI(temperature=0.0, engine="GPT3-5")
response = chat(messages)
print(response.content)


