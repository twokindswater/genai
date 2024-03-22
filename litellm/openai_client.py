import os
import openai

TOKEN = os.getenv("OPENAI_API_KEY")
print("TOKEN:", TOKEN)

# TOKEN = os.getenv("OPENAI_API_KEY")
# print("TOKEN:", TOKEN)

client = openai.OpenAI(api_key=TOKEN, base_url="http://0.0.0.0:4000")

response = client.chat.completions.create(model="gpt-3.5-turbo-0125", messages=[
    {
        "role": "user",
        "content": "who is the US president in 2020"
    }
])

print(response)
