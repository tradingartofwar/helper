from flask import Flask, render_template, request, jsonify
import openai
import os
import csv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

# Initialize Flask app
app = Flask(__name__)

# Load OpenAI API key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the FAQs from a local CSV file
def load_faqs():
    faqs = []
    with open('faqs.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            faqs.append(row)
    return faqs

faq_data = load_faqs()

# Load the product catalog from a local CSV file
def load_products():
    products = []
    with open('products.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

product_data = load_products()

# Langchain LLM setup for sales
llm = OpenAI(temperature=0, openai_api_key=openai.api_key)

# Create a prompt template for the Langchain sales agent system
sales_prompt = PromptTemplate(
    input_variables=["product", "price", "availability", "description", "question"],
    template="""
    You are a helpful sales agent. The user asked: {question}.
    The product is {product}, priced at ${price}. Availability: {availability}.
    Here is the product description: {description}.
    Provide a helpful response based on the user's question.
    """
)

sales_chain = LLMChain(llm=llm, prompt=sales_prompt)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")

    # Check if the input matches any FAQ in the CSV
    for faq in faq_data:
        if user_input.lower() in faq['Question'].lower():
            # If a match is found in the FAQ, return the FAQ answer
            return jsonify({"response": faq['Answer']})

    # Check if the input matches any product in the CSV
    for product in product_data:
        if product['ProductName'].lower() in user_input.lower():
            # If a product match is found, run it through Langchain
            sales_answer = sales_chain.run({
                "product": product['ProductName'],
                "price": product['Price'],
                "availability": product['Availability'],
                "description": product['Description'],
                "question": user_input
            })
            return jsonify({"response": sales_answer})

    # If no match is found, call OpenAI API through Langchain
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    # Extract the assistant's reply from OpenAI's response
    bot_reply = response.choices[0].message.content

    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
