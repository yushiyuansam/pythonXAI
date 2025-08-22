import openai  # pip install openai -U
from dotenv import load_dotenv  # pip install python-dotenv -U
import os

load_dotenv()  # 載入 .env 檔案內容

openai.api_key = os.getenv("OPENAI_API_KEY")
history = [{"role": "system", "content": f"請用繁體中文進行後續對話"}]
while True:
    user_input = input("你:")
    if user_input == "exit":
        break
    history.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model="gpt-5-mini",
        messages=history,
    )

    assistant_message = response.choices[0].message.content
    history.append({"role": "assistant", "content": assistant_message})
    print(f"AI:{assistant_message}")
