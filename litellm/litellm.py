import competion from litellm
import os

os.environ["OPENAI_API_KEY"] = "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"

response = completion(
    model="gpt-3.5-turbo",
    messages=[{"content": "Hello, how are you?", "role": "user"}]
)
