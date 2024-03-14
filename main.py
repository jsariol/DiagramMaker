import os
from openai import AzureOpenAI  # This test openai version is 1.13.3
import json

# Load config values
with open(r'config.json') as config_file:
    config_details = json.load(config_file)

client = AzureOpenAI(
  azure_endpoint = config_details["OPENAI_API_BASE"], 
  api_key=config_details["OPENAI_API_KEY"],
  api_version=config_details["OPENAI_API_VERSION"]
)

url = 'https://learn.microsoft.com/en-us/azure/app-service/overview'
question_num = 5


def create_question(url, question_num):

    print("Creating a question based on the URL. Please wait...")

    message_text = [
        {"role":"system",
        "content":"You provide a problem against Azure learners. Please create a four-choice question based on the contents of the specified URL. Make a set of questions and answers. Please include a brief explanation of the answer. The number of questions to create is "+str(question_num)+"."},
        {"role":"user",
        "content":url}
    ]

    completion = client.chat.completions.create(
    model=config_details["DEPLOYMENT_NAME"], # model = "deployment_name"
    messages = message_text,
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
    )

    print(completion.choices[0].message.content)


create_question(url, question_num)