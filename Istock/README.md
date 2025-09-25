# Stock Analysis & Prediction Dashboard

A Streamlit web application for stock market analysis and price prediction using LSTM and ARIMA models.

## Features

- **Stock Data Visualization**: View historical stock prices with interactive candlestick charts
- **Technical Analysis**: Basic statistics and price movement analysis
- **Price Prediction**: Predict future stock prices using:
  - LSTM (Long Short-Term Memory) neural networks
  - ARIMA (AutoRegressive Integrated Moving Average) models
- **User-Friendly Interface**: Intuitive controls and visualizations

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd stock-analysis-prediction
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. In the sidebar:
   - Select a stock from the dropdown menu
   - Choose a date range for analysis
   - Select a prediction model (LSTM or ARIMA)
   - Adjust the number of days to predict

3. View the interactive visualizations and analysis in the main window

## Models

### LSTM (Long Short-Term Memory)
- Deep learning model for time series prediction
- Captures long-term dependencies in sequential data
- Ideal for capturing complex patterns in stock prices

### ARIMA (AutoRegressive Integrated Moving Average)
- Statistical model for time series forecasting
- Good for understanding and predicting future points in a series
- Parameters can be tuned for different stocks

## Dependencies

- Python 3.8+
- Streamlit
- yfinance
- pandas
- numpy
- plotly
- scikit-learn
- statsmodels
- tensorflow

## License

This project is licensed under the MIT License.

## Disclaimer

This application is for educational purposes only. The predictions should not be considered as financial advice. Always do your own research before making investment decisions.
