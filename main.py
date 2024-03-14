from openai import AzureOpenAI # This test openai version is 1.13.3
import json

# Load config values
with open(r'config.json') as config_file:
    config_details = json.load(config_file)

client = AzureOpenAI(
  azure_endpoint = config_details["OPENAI_API_BASE"], 
  api_key=config_details["OPENAI_API_KEY"],
  api_version=config_details["OPENAI_API_VERSION"]
)

# 
content = 'Azure authentication'


def create_diagram(content):

    print("Creating a diagram. Please wait...")

    message_text = [
        {"role":"system",
        "content":"You are tasked with illustrating Azure learners using mermaid diagrams. Here is a question to help you get started."},
        {"role":"user",
        "content":content}
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


create_diagram(content)