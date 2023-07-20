import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API configurations
openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

class ProductSpecifications: 
    def __init__(self, product_type, product_description):
        # Initialize instance variables
        self._product_type = product_type
        self._product_description = product_description
       
    def _generate_specifications_keywords(self):
        # Generate possible keywords for product specifications
        review_template = f'Write the possible keywords for the specifications of the given product type. Only write the keyword headings like: brand, color, rest may vary for different products: {self._product_type}'
        prompt_template = ChatPromptTemplate.from_template(review_template)
        messages = prompt_template.format_messages(text=self._product_type)
        chat = ChatOpenAI(temperature=0.0, engine="GPT3-5")
        response = chat(messages)
        return response.content.strip()  # Return the generated keys

    def _generate_specifications_values(self, possible_keys):
        # Generate values for the specified keywords in the product description
        review_template2 = f'For the keywords generated {possible_keys}, find their values in the provided product_description, if any value is not there just print none. Print the output in dictionary structure that is keyword and its value: {self._product_description}'
        prompt_template = ChatPromptTemplate.from_template(review_template2)
        messages = prompt_template.format_messages(text=self._product_description)
        chat = ChatOpenAI(temperature=0.0, engine="GPT3-5")
        response = chat(messages)
        return response.content.strip()

    def get_specifications(self):
        # Generate specifications keywords
        possible_keys = self._generate_specifications_keywords()

        # Generate specifications values
        specifications_values = self._generate_specifications_values(possible_keys)

        # Display generated keywords and values
        print("Generated Keywords:", possible_keys)
        print("Generated Values:", specifications_values)


def main():
    # Prompt user to enter product type and description
    product_type = input("Enter the product type: ")
    product_description = input("Enter the product description: ")

    # Create an instance of ProductSpecifications class
    product_keyvalue_generator = ProductSpecifications(product_type, product_description)

    # Display values for the specified keywords in the product description
    product_keyvalue_generator.get_specifications()


if __name__ == "__main__":
    main()
