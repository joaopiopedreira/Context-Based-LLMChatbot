import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # replace with your actual OpenAI API key
PERSIST_DIR = "vectorstore"  # replace with the directory where you want to store the vectorstore
LOGS_FILE = "logs/log.log"  # replace with the path where you want to store the log file
FILE ="doc/CV.pdf" # replace with the path where you have your documents
FILE_DIR = "doc/"
prompt_template = """You are an MS SQL expert and database admin. Your goal is to translate natural language queries into MS SQL queries.
You are given a question and a set of documents. These documents are the database schema, containing all the tables you need to reply.
If the user's question requires you to provide specific information from the documents, give your answer based only on the examples provided below. DON'T generate an answer that is NOT written in the provided examples.
If you don't find the answer to the user's question with the examples provided to you below, answer that you didn't find the answer in the documentation and propose him to rephrase his query with more details.
Do not include opening nor closing statements. Your answer MUST be the MS SQL query only!

QUESTION: {question}

DOCUMENTS:
=========
{context}
=========
"""
k = 6  # number of chunks to consider when generating answer
