import os
import openai

TOKEN = "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"
print("TOKEN:", TOKEN)

client = openai.OpenAI(api_key=TOKEN, base_url="http://0.0.0.0:8000")

response = client.chat.completions.create(model="gpt-3.5-turbo", messages = [
    {
        "role": "user",
        "content": "where is the biggest company?"
    }
])

print(response.choices[0].message.content)