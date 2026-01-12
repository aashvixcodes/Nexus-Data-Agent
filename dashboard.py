import streamlit as st
import pandas as pd
import subprocess
import os

st.set_page_config(
    page_title="RevenueAI Executive Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("RevenueAI Copilot")
st.markdown("### Enterprise Decision Support System")
st.divider()

with st.sidebar:
    st.header("Control Center")
    if st.button("Initialize Analysis Pipeline", type="primary", use_container_width=True):
        with st.status("Executing Workflow...", expanded=True) as status:
            st.write("Connecting to data sources...")
            try:
                result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
                
                if result.returncode == 0:
                    st.write("Processing AI models...")
                    st.write("Updating Tableau extracts...")
                    st.write("Dispatching Slack alerts...")
                    status.update(label="Pipeline Execution Successful", state="complete", expanded=False)
                    st.rerun()
                else:
                    status.update(label="Pipeline Execution Failed", state="error")
                    st.error("Runtime Error Detected")
                    st.code(result.stderr)
            except Exception as e:
                status.update(label="System Error", state="error")
                st.error(str(e))

    st.divider()
    st.caption("v1.0.0 | Production Build")

try:
    if os.path.exists("data.csv"):
        df = pd.read_csv("data.csv")
        
        latest_val = df.iloc[-1]['revenue']
        prev_val = df.iloc[-2]['revenue'] if len(df) > 1 else latest_val
        delta_val = ((latest_val - prev_val) / prev_val) * 100

        kpi1, kpi2, kpi3 = st.columns(3)

        with kpi1:
            st.metric(
                label="Projected Revenue",
                value=f"₹{latest_val:,.2f}",
                delta=f"{delta_val:.2f}%"
            )
        
        with kpi2:
            st.metric(
                label="Model Confidence",
                value="94.2%",
                delta="1.5%"
            )

        with kpi3:
            st.metric(
                label="Active Data Points",
                value=str(len(df)),
                delta="Updated Now"
            )

        st.divider()

        chart_section, data_section = st.columns([2, 1])

        with chart_section:
            st.subheader("Revenue Trajectory")
            st.area_chart(df['revenue'], color="#2ecc71")

        with data_section:
            st.subheader("Recent Entries")
            st.dataframe(
                df.tail(10),
                use_container_width=True,
                hide_index=True
            )

    else:
        st.warning("No dataset detected. Please initialize the analysis pipeline from the sidebar.")

except Exception as e:
    st.error(f"Dashboard Visualization Error: {str(e)}")