Nexus Data Agent
Autonomous Revenue Intelligence System
Nexus is a full-stack intelligent agent designed to transform raw sales and weather data into strategic insights. Unlike traditional dashboards, Nexus autonomously ingests, analyzes, visualizes, and communicates performance metrics—bridging the gap between operational data and executive decision-making.

📖 Overview
Nexus operates as a modular pipeline with five integrated components:

Autonomous ETL Pipeline: Cleanses and transforms raw data into structured metrics.

Generative AI Analyst: Interprets trends using LLaMA-3 and delivers strategic recommendations.

Tableau Cloud Sync: Ensures real-time dashboard updates via Hyper API.

Slack Alerting System: Pushes executive summaries and metric highlights to stakeholders.

Streamlit Command Center: Offers live monitoring and predictive simulations.

🏗️ Architecture
[Looks like the result wasn't safe to show. Let's switch things up and try something else!]

The system architecture follows a linear data flow:

Raw Data Ingestion → Sales and weather data are extracted and stored locally.

ETL Processing → Data is cleaned, normalized, and enriched with derived metrics.

AI Analysis → Groq-powered LLaMA-3 models generate contextual insights.

Visualization Sync → Data is converted to .hyper format and uploaded to Tableau Cloud.

Slack Notifications → High-level summaries are sent to designated channels.

Frontend Interface → Streamlit dashboard enables real-time control and simulation.

✨ Key Features
Autonomous ETL Pipeline
Zero-touch ingestion of CSV data

Anomaly detection and metric computation (ROI, Spend Efficiency)

Persistent local data lake for historical analysis

Generative AI Analyst
Powered by Groq (LLaMA-3 70B)

Correlates sales performance with weather disruptions

Outputs executive-level recommendations

Tableau Cloud Integration
Hyper API via Pantab and Tableau Server Client (TSC)

Automated overwrite and refresh of cloud dashboards

Slack Alerting
Push-based notifications using Slack SDK/Webhooks

Highlights revenue, spend, and weather anomalies

Streamlit Command Center
Interactive "What-If" simulator for strategy testing

Live system metrics and AI chat interface

⚙️ Tech Stack
Layer	Technologies Used
Core Engine	Python 3.10+
Data Engineering	Pandas, Pantab, Tableau Server Client (TSC)
AI Integration	Groq API (LLaMA-3 70B)
Visualization	Tableau Cloud
Frontend Interface	Streamlit
Notifications	Slack SDK / Webhooks
🚀 Installation & Setup
1. Clone the Repository
bash
git clone https://github.com/aashvixcodes/Nexus-Data-Agent.git
cd Nexus-Data-Agent
2. Install Dependencies
bash
pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root directory:

ini
# Tableau Cloud Credentials
TABLEAU_SERVER="https://prod-useast-a.online.tableau.com"
TABLEAU_SITE_ID="your-site-id"
TABLEAU_TOKEN_NAME="your-token-name"
TABLEAU_TOKEN_VALUE="your-token-value"

# AI & Notifications
GROQ_API_KEY="gsk_..."
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/..."
4. Launch the Agent
bash
streamlit run app.py
📊 Usage Workflow
Open the dashboard at http://localhost:8501  


Trigger the ETL job via sidebar control
Monitor real-time metrics and AI-generated strategy
View updated Tableau dashboards
Receive Slack alerts with executive summaries

📄 License
Distributed under the MIT License. See LICENSE for details.

Built by Aashvi 
