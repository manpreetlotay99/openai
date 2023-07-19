import os
import pandas as pd
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

openai.api_type = "azure"
openai.api_version = "2023-05-15"

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

class ProductKeyGenerator:
       
    def generate_product_keys(self, product_type):
        review_template = f'Write the possible keywords for the specifications of the given product type. Only write the keyword headings like: brand, color, rest may vary for different products: {product_type}'
        prompt_template = ChatPromptTemplate.from_template(review_template)
        messages = prompt_template.format_messages(text=product_type)
        chat = ChatOpenAI(temperature=0.0, engine="GPT3-5")
        response = chat(messages)
        print(response.content)
        return response.content  # Return the generated keys
        

    def generate_filled_description(self, product_description, possible_keys):
        review_template2 = f'For the keywords generated {possible_keys}, find their values in the provided product_description, if any value is not there just print none. Print the output in dictionary structure that is keyword and its value: {product_description}'
        prompt_template = ChatPromptTemplate.from_template(review_template2)
        messages = prompt_template.format_messages(text=product_description)
        chat = ChatOpenAI(temperature=0.0, engine="GPT3-5")
        response = chat(messages)
        print(response.content)

def main():
    product_key_generator = ProductKeyGenerator()
    product_type = input("Enter the product type: ")

    possible_keys = product_key_generator.generate_product_keys(product_type)

    product_description = input("Enter the product description: ")
    filled_description = product_key_generator.generate_filled_description(product_description,possible_keys)



if __name__ == "__main__":
    main()