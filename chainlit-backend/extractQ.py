import os
import re
from dotenv import load_dotenv
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import AzureOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv


loader = UnstructuredFileLoader('Survey-Questionnire-Part3.pdf')
documents = loader.load()
print(type(documents))
print(documents[0].page_content)


question_patterns = [
    r'\b(does|provide|describe|identify|who|what|when|where|why|how)\b.*\?',
    r'.*\?'
]

# Step 3: Extract questions
extracted_questions = []
for pattern in question_patterns:
    extracted_questions.extend(re.findall(pattern, documents[0].page_content))

# Step 4: Refinement (if necessary)

# Step 5: Output or further processing
for question in extracted_questions:
    print(question)
