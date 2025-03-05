import openai
import os 
import litellm

client = openai.OpenAI(
    api_key=os.environ.get("LITELLM_API_KEY"),
    base_url="https://llmproxy.ai.orange" # LiteLLM Proxy is OpenAI compatible, Read More: https://docs.litellm.ai/docs/proxy/user_keys
)

response = client.chat.completions.create(
    model="openai/gpt-4o-mini", # model to send to the proxy
    messages = [
        {
            "role": "user",
            "content": "this is a test request, write a short poem"
        }
    ]
)

litellm.api_key = os.environ.get("LITELLM_API_KEY")
litellm.api_base = "https://llmproxy.ai.orange"
response = litellm.completion(
  model="openai/gpt-4o-mini",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)

print(response)