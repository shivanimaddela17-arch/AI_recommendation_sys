import gradio as gr
import os
import gradio as gr
from google import genai

# Read Gemini API Key from Hugging Face Secrets
client = genai.Client(api_key="AQ.Ab8RN6KwaZ0BinyHtL1Q5c9knERsTtqHGQQ-gNkVdUHEZN0tXw")

def recommend(category, interests):
    prompt = f"""
You are an AI Recommendation System.

Category:
{category}

User Interests:
{interests}

Recommend the Top 5 items.

For each recommendation provide:

1. Name
2. Short Description
3. Why it matches the user's interests.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"

theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="indigo",
    neutral_hue="slate",
).set(
    button_primary_background_fill="#2563eb",
    button_primary_background_fill_hover="#1d4ed8",
    button_primary_text_color="white",
    block_radius="12px",
)

demo = gr.Interface(
    fn=recommend,
    inputs=[
        gr.Textbox(
            label="📂 Recommendation Category",
            placeholder="Movies, Books, Courses, Travel, etc."
        ),
        gr.Textbox(
            label="📝 Describe Your Interests",
            lines=5,
            placeholder="Example: I enjoy AI, Machine Learning, Python, and Data Science."
        ),
    ],
    outputs=gr.Textbox(
        label="✨ AI Recommendations",
        lines=15
    ),
    title="🤖 AI Recommendation System",
    description="""
Get personalized recommendations powered by **Google Gemini AI**.

Choose a category and describe your interests to receive the top 5 recommendations.
""",
    submit_btn="🚀 Get Recommendations",
    clear_btn="🗑️ Clear",
    theme=theme,
)
demo.launch()