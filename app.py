import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import time

# Imports
from main import run_pipeline 
from groq_ai import get_ai_recommendation

st.set_page_config(page_title="RevenueAI Copilot", page_icon="🚀", layout="wide")

# --- SIDEBAR CONTROL ---
st.sidebar.title("⚙️ Operations")
st.sidebar.write("Control Center for RevenueAI")

if st.sidebar.button("🔄 Run Daily ETL Job", type="primary"):
    with st.spinner("🚀 Running Data Pipeline..."):
        latest_data = run_pipeline()
        st.success("Pipeline Executed! Slack Alert Sent.")
        time.sleep(1)
        st.rerun()

# --- MAIN PAGE ---
st.title("🚀 RevenueAI Copilot")
st.markdown("### *Intelligent Sales Automation System*")

# Load Data for Metrics
try:
    df = pd.read_csv("sales_data.csv")
    if not df.empty:
        latest = df.iloc[-1]
        latest_rev = latest.get('revenue', 0)
        latest_spend = latest.get('marketing_spend', 0)
        latest_weather = latest.get('weather', 'Unknown')
        latest_roi = latest.get('roi', 0.0)
    else:
        latest_rev, latest_spend, latest_weather, latest_roi = 0, 0, "Unknown", 0
except:
    latest_rev, latest_spend, latest_weather, latest_roi = 0, 0, "Unknown", 0

# Metrics Display
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="💰 Today's Revenue", value=f"₹{latest_rev:,}")
with col2:
    st.metric(label="📉 Marketing Spend", value=f"₹{latest_spend:,}")
with col3:
    st.metric(label="🚀 ROI", value=f"{latest_roi}x")
with col4:
    st.metric(label="🌤️ Weather", value=latest_weather)

st.divider()

# --- TABLEAU DASHBOARD ---
st.subheader("📊 Live Analytics (Tableau)")

tableau_url = "https://prod-in-a.online.tableau.com/t/amaashvi-dd02ac07a9/authoring/final_dashboard/Sheet1#1" 

tableau_embed_code = f"""
<iframe src="{tableau_url}?:showVizHome=no&:embed=true" width="100%" height="600"></iframe>
"""
components.html(tableau_embed_code, height=600)

# --- AI CHAT ---
st.divider()
st.subheader("🤖 AI Executive Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about performance..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            ai_reply = get_ai_recommendation(latest_rev, latest_weather)
            st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})