import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
from statsmodels.tsa.arima.model import ARIMA
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Page Config
st.set_page_config(page_title="Stock Analysis & Prediction", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main {padding: 2rem;}
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("📈 Stock Analysis & Prediction Dashboard")

# Sidebar
st.sidebar.header('Stock Selection')
stock_options = {
    'NVIDIA Corporation': 'NVDA',
    'Microsoft (OpenAI)': 'MSFT',
    'Tesla': 'TSLA'
}

selected_stock = st.sidebar.selectbox('Select Stock', list(stock_options.keys()))
ticker = stock_options[selected_stock]

# Date Range
default_end = datetime.now()
default_start = default_end - timedelta(days=365)
start_date = st.sidebar.date_input('Start Date', default_start)
end_date = st.sidebar.date_input('End Date', default_end)

# Get Stock Data
@st.cache_data
def get_stock_data(ticker, start_date, end_date):
    try:
        df = yf.download(ticker, start=start_date, end=end_date)
        return df
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

df = get_stock_data(ticker, start_date, end_date)

if df is not None and not df.empty:
    # Display Raw Data
    st.subheader(f"{selected_stock} Stock Data")
    st.dataframe(df.tail())

    # Basic Statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Plot Closing Price
    st.subheader("Stock Price")
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                name='Market Data'))
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)

    # Model Selection
    st.sidebar.subheader("Prediction Model")
    model_choice = st.sidebar.selectbox(
        'Select Model',
        ['LSTM', 'ARIMA']
    )
    
    n_days = st.sidebar.slider('Days to Predict', 1, 60, 30)

    if model_choice == 'LSTM':
        st.subheader("LSTM Model Prediction")
        # LSTM implementation would go here
        st.info("LSTM model will be implemented here")
        
    elif model_choice == 'ARIMA':
        st.subheader("ARIMA Model Prediction")
        # ARIMA implementation would go here
        st.info("ARIMA model will be implemented here")

else:
    st.warning("No data available for the selected stock and date range.")
