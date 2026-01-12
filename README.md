# 🔮 Nexus Data Agent  
### *Autonomous Revenue Intelligence System*

**Nexus** is an autonomous revenue intelligence system that transforms raw sales and weather data into actionable executive insights.  
It goes beyond traditional dashboards by automatically ingesting data, generating AI-driven analysis, refreshing live Tableau dashboards, and proactively delivering strategic summaries via **Slack**, all without manual intervention.  
it bridges the gap between operational metrics and decision-making by combining data engineering, generative AI, and cloud BI into a single intelligent pipeline.

---

## 🎯 Why Nexus?

Most organizations rely on static dashboards that:
- Update infrequently  
- Require manual interpretation  
- Depend heavily on analysts for insights  

---

## 📖 Overview

Nexus operates as a modular pipeline with five integrated components:

- **Autonomous ETL Pipeline:** Cleanses and transforms raw data into structured metrics  
- **Generative AI Analyst:** Interprets trends using LLaMA-3 and delivers strategic recommendations  
- **Tableau Cloud Sync:** Ensures real-time dashboard updates via Hyper API  
- **Slack Alerting System:** Pushes executive summaries and metric highlights to stakeholders  
- **Streamlit Command Center:** Offers live monitoring and predictive simulations  

---

## 🏗️ Architecture
<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/5f0889c9-0556-4587-99cc-067c1995f6fb" />

1. **Raw Data Ingestion**  
   Sales and weather data are extracted and stored locally  

2. **ETL Processing**  
   Data is cleaned, normalized, and enriched with derived metrics  

3. **AI Analysis**  
   Groq-powered **LLaMA-3 (70B)** generates contextual insights  

4. **Visualization Sync**  
   Data is converted to `.hyper` format and uploaded to Tableau Cloud  

5. **Slack Notifications**  
   Executive summaries are sent to designated Slack channels  

6. **Frontend Interface**  
   Streamlit dashboard enables real-time control and simulations  

---

## ✨ Key Features

### 🔄 Autonomous ETL Pipeline
- Zero-touch ingestion of CSV data  
- Anomaly detection and metric computation (ROI, Spend Efficiency)  
- Persistent local data lake for historical analysis  

### 🧠 Generative AI Analyst
- Powered by **Groq (LLaMA-3 70B)**  
- Correlates sales performance with weather disruptions  
- Outputs executive-level recommendations  

### 📊 Tableau Cloud Integration
- Hyper API via **Pantab** and **Tableau Server Client (TSC)**  
- Automated overwrite and refresh of cloud dashboards  

### 💬 Slack Alerting
- Push-based notifications using Slack SDK / Webhooks  
- Highlights revenue, spend, and weather anomalies  

### 🎛️ Streamlit Command Center
- Interactive **What-If simulator** for strategy testing  
- Live system metrics and AI chat interface  

---

## ⚙️ Tech Stack

| Layer | Technologies |
|------|-------------|
| Core Engine | Python 3.10+ |
| Data Engineering | Pandas, Pantab, Tableau Server Client (TSC) |
| AI Integration | Groq API (LLaMA-3 70B) |
| Visualization | Tableau Cloud |
| Frontend Interface | Streamlit |
| Notifications | Slack SDK / Webhooks |

---

## 🧩 Use Cases

- **Marketing Teams:** Optimize ad spend based on revenue ROI and weather impact  
- **Sales Leaders:** Track performance trends and receive risk alerts  
- **Executives:** Get daily strategy briefs without opening dashboards  
- **Operations Teams:** Simulate outcomes using what-if analysis
- 
---

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/aashvixcodes/Nexus-Data-Agent.git
cd Nexus-Data-Agent
```

2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Set Up Environment Variables
Create a .env file in the project root:
```bash
touch .env
```
Add the following configuration:

# Tableau Cloud Credentials
TABLEAU_SERVER=https://prod-in-a.online.tableau.com
TABLEAU_SITE_ID=your-site-id
TABLEAU_TOKEN_NAME=your-token-name
TABLEAU_TOKEN_VALUE=your-token-value
TABLEAU_DATASOURCE_NAME=your datasourcxe name

# AI & Notifications
GROQ_API_KEY=gsk_...
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
SLACK_CHANNEL_ID=your channel id
SLACK_TOKEN=your token

4️⃣ Run the Application
```bash
streamlit run app.py
```

📊 Usage Workflow

Open the dashboard:
```bash
http://localhost:8501

```
Trigger the daily ETL job from the Streamlit sidebar

Monitor real-time metrics and AI-generated insights

View updated dashboards in Tableau Cloud

Receive Slack alerts with executive summaries


📄 License
Distributed under the MIT License.
See LICENSE for more information.

Built with ❤️ by Aashvi




