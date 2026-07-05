import gradio as gr
import requests

FastAPI_URL = "http://localhost:8000/recommend"

def recommend(category, interests):
    response = requests.post(
        FastAPI_URL,
        json={
            "category": category,
            "interests": interests
        }
    )

    if response.status_code == 200:
        return response.json()["recommendations"]
    else:
        return "Error connecting to FastAPI."

demo = gr.Interface(
    fn=recommend,
    inputs=[
        gr.Textbox(label="Recommendation Category (Movies, Books, Courses, etc.)"),
        gr.Textbox(label="Describe Your Interests", lines=5)
    ],
    outputs=gr.Textbox(label="AI Recommendations", lines=15),
    title="AI Recommendation System",
    description="Enter a category and your interests to receive personalized AI recommendations."
)

demo.launch()