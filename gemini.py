import os
from dotenv import load_dotenv
import google.generativeai as genai

# Specify the path to your .env file if it's not in the same directory
dotenv_path = os.path.join(os.path.dirname(__file__), 'APIKEY.env')
load_dotenv(dotenv_path)


class GeminiAI:
    def __init__(self):
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

        if not self.GOOGLE_API_KEY:
            raise ValueError("No GOOGLE_API_KEY found in environment variables.")

        genai.configure(api_key=self.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")

    def generateResponse(self, input_text):
        response = self.model.generate_content(input_text)

        return response.text