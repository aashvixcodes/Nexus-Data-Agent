import os
from groq import Groq
from config import GROQ_API_KEY

def get_ai_recommendation(current_revenue, weather_info):
    """
    Sends revenue and weather data to Groq (Llama 3) 
    to get a strategic recommendation.
    """
    try:
        # 1. Initialize Groq Client
        client = Groq(api_key=GROQ_API_KEY)

        # 2. Create the Prompt
        system_prompt = (
            "You are an expert Data Strategy Consultant for a retail business. "
            "Analyze the data provided and give a short, actionable strategy (max 2 sentences). "
            "Focus on marketing spend, inventory, or pricing."
        )
        
        user_message = (
            f"Current Projected Revenue: ₹{current_revenue}\n"
            f"Current Weather: {weather_info}\n\n"
            "Based on this, what should we do today?"
        )

        # 3. Call the AI Model
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
        )

        # 4. Return the Answer
        return chat_completion.choices[0].message.content

    except Exception as e:
        print(f"❌ AI Error: {e}")
        return "⚠️ AI Service Unavailable. Proceed with standard protocol."