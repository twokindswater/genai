import competion from litellm

response = completion(
    model="gpt-3.5-turbo",
    messages=[{"content": "Hello, how are you?", "role": "user"}]
)
