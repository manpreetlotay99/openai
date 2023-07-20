from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from productspecifications.productspecifications import ProductSpecifications

product_type = input("Enter the product type: ")
product_description = input("Enter the product description: ")

product = ProductSpecifications(product_type, product_description)
product.get_specifications()

