import os
import openai
client = openai.OpenAI(
    api_key=os.environ["CAM_API_KEY"],
    base_url="https://llm.hpc.cam.ac.uk" # LiteLLM Proxy is OpenAI compatible, Read More: https://docs.litellm.ai/docs/proxy/user_keys
)

response = client.chat.completions.create(
    model="llama-cam", # model to send to the proxy
    messages = [
        {
            "role": "user",
            "content": "I went to the"
        }
    ],
    temperature=0.8
)

print(response)
