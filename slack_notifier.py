import requests
import json
from config import SLACK_WEBHOOK_URL

def send_slack_alert(ai_insight, revenue, weather):
    """
    Sends a nice looking text alert to Slack.
    """
    if not SLACK_WEBHOOK_URL:
        print("❌ Slack Webhook URL missing.")
        return

    # ROI Calculation
    marketing_spend = revenue * 0.05 
    roi = round((revenue - marketing_spend) / marketing_spend, 2)

    payload = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🚀 RevenueAI Daily Report",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*💰 Revenue:*\n₹{revenue:,}"},
                    {"type": "mrkdwn", "text": f"*🌤 Weather:*\n{weather}"},
                    {"type": "mrkdwn", "text": f"*📢 ROI:*\n{roi}x"},
                    {"type": "mrkdwn", "text": "*📅 Status:*\nData Synced"}
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*🤖 AI Copilot Insight:*\n>{ai_insight}"
                }
            }
        ]
    }

    try:
        response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            print("✅ Slack Alert Sent Successfully.")
        else:
            print(f"❌ Failed to send Slack Alert: {response.text}")
    except Exception as e:
        print(f"❌ Slack Connection Error: {e}")