import os
from dotenv import load_dotenv

# Force load the .env file
load_dotenv(override=True)

# Tableau Credentials
TABLEAU_SERVER = os.getenv("TABLEAU_SERVER")
TABLEAU_TOKEN_NAME = os.getenv("TABLEAU_TOKEN_NAME")
TABLEAU_TOKEN_VALUE = os.getenv("TABLEAU_TOKEN_VALUE")
TABLEAU_SITE_ID = os.getenv("TABLEAU_SITE_ID")

# Slack Credentials
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

# Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Simple Check
if not TABLEAU_SERVER or not SLACK_WEBHOOK_URL:
    print("⚠️ Warning: .env variables might be missing.")
else:
    print("✅ Configuration loaded.")