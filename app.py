import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Personal AI Stock Analyst", layout="wide")
st.title("📈 Personal AI Stock Analyst")

st.sidebar.header("Stock Details")
stock = st.sidebar.text_input("Stock Name", "TCS")
price = st.sidebar.number_input("Current Price (Rs)", value=2000)
target = st.sidebar.number_input("Your Target Price (Rs)", value=2300)
qty = st.sidebar.number_input("Quantity", value=10)

if price < target:
    signal = "BUY 🟢"
    reason = f"{stock} ippo Rs {price} la irukku. Target Rs {target}. So up pogalam nu AI soludhu!"
elif price > target:
    signal = "SELL 🔴"
    reason = f"{stock} ippo Rs {price} la irukku. Target Rs {target} ah vida adhigam. So sell pannalam!"
else:
    signal = "HOLD 🟡"
    reason = "Price target kitta irukku, wait pannunga!"

col1, col2, col3 = st.columns(3)
col1.metric("Stock", stock)
col2.metric("Current Price", f"Rs {price}")
col3.metric("AI Signal", signal)

st.success(f"**AI Advice:** {reason}")
st.info(f"Total Investment: Rs {price * qty} | Expected Value: Rs {target * qty} | Profit: Rs {(target - price) * qty}")

# Fake chart
dates = pd.date_range("2026-10-01", periods=30)
prices = [price + random.randint(-50, 50) + i*5 for i in range(30)]
df = pd.DataFrame({"Date": dates, "Price": prices})
st.line_chart(df.set_index("Date"))

st.write("### Top Stocks Today")
data = {
    "Stock": ["TCS", "Infosys", "Reliance", "HDFC Bank", "Tata Motors"],
    "Price": [2000, 1500, 2600, 1600, 900],
    "Signal": ["BUY", "BUY", "HOLD", "SELL", "BUY"]
}
st.table(pd.DataFrame(data))
st.caption("Note: Idhu education ku mattum. Real money poda munna yosichu pannunga!")
