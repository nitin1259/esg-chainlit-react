import os

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

os.environ["AZURE_OPENAI_API_KEY"] = "a31b5dcb986d4480a067344fdd352814"
load_dotenv()


'''
OPENAI_API_TYPE = "azure"
OPENAI_API_VERSION = "2024-02-15-preview"
OPENAI_API_BASE = r"https://openaisatheesh.openai.azure.com/"
OPENAI_API_KEY = "a31b5dcb986d4480a067344fdd352814" 
DEPLOYMENT_NAME = "openapiendpoint"


from dotenv import load_dotenv

os.environ["OPENAI_API_TYPE"] = OPENAI_API_TYPE
os.environ["OPENAI_API_VERSION"] = OPENAI_API_VERSION
os.environ["OPENAI_API_BASE"] = OPENAI_API_BASE
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

print(OPENAI_API_BASE)

os.environ["AZURE_OPENAI_ENDPOINT"] = OPENAI_API_BASE
os.environ["AZURE_OPENAI_API_KEY"] = OPENAI_API_KEY
load_dotenv()
'''

loader = UnstructuredFileLoader('2021-annual-report.pdf')
documents = loader.load()


#text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=30, 
    separators=["\n\n", "\n", " ", ""]
)

texts = text_splitter.split_documents(documents)

#embeddings = OpenAIEmbeddings(model="openapiendpoint")
embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=r"https://openaisatheesh.openai.azure.com/",
    azure_deployment="openapiembeddings",
    openai_api_version="2024-02-15-preview",
)


doc_search = Chroma.from_documents(texts,embeddings)
#chain = RetrievalQA.from_chain_type(llm=AzureOpenAI(azure_endpoint=r"https://openaisatheesh.openai.azure.com/",openai_api_version="2024-02-15-preview",azure_deployment="openapiendpoint",model_kwargs={'engine':'gpt-35-turbo'}),chain_type='stuff', retriever = doc_search.as_retriever()))

chain = RetrievalQA.from_chain_type(llm=AzureOpenAI(azure_endpoint=r"https://openaisatheesh.openai.azure.com/",openai_api_version="2024-02-15-preview",azure_deployment="openapiendpoint"),chain_type='stuff', retriever = doc_search.as_retriever())

query = 'Describe how COVID-19 has impacted the world'
print(chain.run(query))


