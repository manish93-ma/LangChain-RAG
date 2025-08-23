from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GAMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",max_completion_token = 10,
        google_api_key=api_key
)

result = model.invoke("suggest me 5 indian male names")

print(result.content)
