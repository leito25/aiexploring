import openai
import os

client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://uai-litellm.internal.unity.com/"
)

try:
    response = client.chat.completions.create(
        model="anthropic.claude-haiku-4-5-20251001",
        messages=[{"role": "user", "content": "Hello!"}],
        extra_body={
            "metadata": {
                "tags": ["production", "customer-support", "urgent"],
                "generation_name": "support-bot",
                "trace_user_id": "user-123"
            }
        }
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")