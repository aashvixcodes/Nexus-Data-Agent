import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq Client
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def train_model(df):
    """Train a simple regression model."""
    X = df[['marketing_spend']]
    y = df['revenue']
    model = LinearRegression()
    model.fit(X, y)
    return model

def get_ai_recommendation(current_spend, predicted_revenue, past_revenue_avg):
    """Get smart strategy from Groq AI."""
    try:
        prompt = f"""
        You are a Senior Revenue Analyst.
        - Hist Avg Revenue: ₹{past_revenue_avg:,.0f}
        - Current Spend: ₹{current_spend:,.0f}
        - Predicted Rev: ₹{predicted_revenue:,.0f}
        
        Compare Predicted vs Historical.
        If predicted is lower, suggest aggressive changes.
        If higher, suggest optimization.
        Give a 1-sentence recommendation strictly under 20 words.
        Start with "Recommendation:".
        """

        chat_completion = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",  # ✅ FIX: Updated to working model
            temperature=0.7,
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        print(f"❌ Groq Error: {e}")
        return "Recommendation: Check marketing ROI manually."

def analyze_revenue(df):
    """Main analysis function."""
    print("Running AI analysis...")
    model = train_model(df)
    
    # ✅ FIX: Warning removed by using DataFrame instead of list
    latest_spend = df['marketing_spend'].iloc[-1]
    input_data = pd.DataFrame([[latest_spend]], columns=['marketing_spend'])
    prediction = model.predict(input_data)[0]
    
    past_avg = df['revenue'].mean()
    recommendation = get_ai_recommendation(latest_spend, prediction, past_avg)
    
    print(f"{recommendation}")
    print(f"Predicted Revenue: ₹{prediction:,.0f}")
    
    return recommendation, prediction