import pandas as pd
from datetime import datetime
import os
import random

# Import modules
from config import TABLEAU_SERVER
from tableau_manager import publish_to_tableau
from slack_notifier import send_slack_alert
from groq_ai import get_ai_recommendation

# --- STEP 1: EXTRACT ---
def extract_raw_data():
    print("1️⃣ [EXTRACT] Ingesting raw data...")
    raw_payload = {
        "timestamp": datetime.now().strftime("%Y-%m-%d"),
        "total_sales_value": random.randint(80000, 150000),       
        "ad_budget": random.randint(3000, 8000),                  
        "sky_condition": random.choice(["Sunny", "Stormy", "Clear Sky", "Rainy", "Cloudy"]) 
    }
    return raw_payload

# --- STEP 2: TRANSFORM ---
def transform_data(raw_data):
    print("2️⃣ [TRANSFORM] Cleaning data...")
    transformed = {
        "date": raw_data["timestamp"],
        "revenue": raw_data["total_sales_value"],
        "marketing_spend": raw_data["ad_budget"],
        "weather": raw_data["sky_condition"]
    }
    
    if transformed["marketing_spend"] > 0:
        roi = (transformed["revenue"] - transformed["marketing_spend"]) / transformed["marketing_spend"]
    else:
        roi = 0
    transformed["roi"] = round(roi, 2)
    return transformed

# --- STEP 3: LOAD ---
def load_data(clean_data):
    print("3️⃣ [LOAD] Saving to CSV...")
    df = pd.DataFrame([clean_data])
    file_path = "sales_data.csv"
    
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)
    return df

# --- ORCHESTRATOR ---
def run_pipeline():
    print("🚀 ETL Pipeline Started...")
    
    # ETL Steps
    raw = extract_raw_data()
    clean_data_dict = transform_data(raw)
    load_data(clean_data_dict)
    
    # Trigger External Systems
    print("4️⃣ [ACTION] Triggering External Systems...")
    
    # 1. Update Tableau Data
    publish_to_tableau() 
    
    # 2. Get AI Insight
    insight = get_ai_recommendation(clean_data_dict['revenue'], clean_data_dict['weather'])
    
    # 3. Send Slack Text Alert
    send_slack_alert(insight, clean_data_dict['revenue'], clean_data_dict['weather'])
    
    print("✅ ETL Job Finished Successfully.")
    return clean_data_dict

if __name__ == "__main__":
    run_pipeline()