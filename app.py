from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os

app = FastAPI()

# Store your API key as an environment variable
client = genai.Client(api_key="AQ.Ab8RN6IpPjgpI72sAdrtFwY6xqHKqVuoMIQf4IMm4ZZOPaiX5g")

class RecommendationRequest(BaseModel):
    category: str
    interests: str

@app.post("/recommend")
def recommend(req: RecommendationRequest):

    prompt = f"""
    You are an AI Recommendation System.

    Category: {req.category}

    User Interests:
    {req.interests}

    Recommend the top 5 items.

    For each recommendation provide:
    1. Name
    2. Short description
    3. Why it matches the user's interests
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "category": req.category,
        "interests": req.interests,
        "recommendations": response.text
    }