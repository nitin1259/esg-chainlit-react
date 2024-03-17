import os
from openai import AzureOpenAI


#client = AzureOpenAI(
  #azure_endpoint = "https://openaisatheesh.openai.azure.com/",
  #api_key="a31b5dcb986d4480a067344fdd352814",
  #api_version="2024-02-15-preview"
#)

os.environ["AZURE_OPENAI_API_KEY"] = "a31b5dcb986d4480a067344fdd352814"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://openaisatheesh.openai.azure.com/"

from langchain_openai import AzureOpenAIEmbeddings

embeddings = AzureOpenAIEmbeddings(
    azure_deployment="openapiembeddings",
    openai_api_version="2024-02-15-preview"
)

text = "this is a test document"

query_result = embeddings.embed_query(text)

doc_result = embeddings.embed_documents([text])

print(doc_result[0][:5])


#message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"Hi"}]
#message_text = [{"role":"system","content":"what is capital of India?"}]

#completion = client.chat.completions.create(
  #model="openapiendpoint", # model = "deployment_name"
  #messages = message_text,
  #temperature=0.7,
  #max_tokens=800,
  #top_p=0.95,
  #frequency_penalty=0,
  #presence_penalty=0,
  #stop=None
#)

#print(completion)