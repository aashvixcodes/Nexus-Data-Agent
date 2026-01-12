# 🔮 Nexus Data Agent  
### *Autonomous Revenue Intelligence System*

**Nexus** is a full-stack intelligent agent designed to transform raw sales and weather data into strategic insights.  
Unlike traditional dashboards, Nexus autonomously ingests, analyzes, visualizes, and communicates performance metrics — bridging the gap between operational data and executive decision-making.

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

**Linear Data Flow:**

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

