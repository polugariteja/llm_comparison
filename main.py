import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

generation_config = {
    "max_output_tokens": 100
}

app = FastAPI()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize model
model = genai.GenerativeModel(
    "gemini-flash-latest",
    generation_config=generation_config
)

@app.post("/")
async def quote_generator():
    try:
        prompt = "Where is malla reddy university"
        response = model.generate_content(prompt)

        if not response:
            raise ValueError("Empty response received")

        return {"quote": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
