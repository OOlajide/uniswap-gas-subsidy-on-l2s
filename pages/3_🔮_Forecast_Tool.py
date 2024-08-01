import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit_extras.colored_header import colored_header

st.cache_data.clear()

st.set_page_config(
    page_title="Uniswap Gas Subsidy On L2s",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/sageOlamide",
        "About": None
    }
)

###################################
############ CACHE DATA ###########
###################################

url = "https://flipsidecrypto.xyz/studio/queries/c293273a-67f3-42d2-98c4-679ae1aa8798"
@st.cache_data
def load_df():
    df = pd.read_csv('data/df1a.csv')
    return df


###################################
############ LOAD DATA ############
###################################

df = load_df()

st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Forecast Tool"}</h1>', unsafe_allow_html=True)

# Forecasting Impact of Gas Subsidy

# Create a slider for selecting subsidy percentage
subsidy_percentage = st.slider('Select % Subsidy', min_value=10, max_value=100, step=5, value=20)

# Create a dropdown for selecting the metric to forecast
forecast_metric = st.selectbox('Select metric to forecast', ['SWAP_TXNS', 'VOLUME_USD', 'TOTAL_ACTIVE_USERS', 'PROTOCOL_FEES_USD'])

# Function to forecast impact
@st.cache_data
def forecast_impact(df, subsidy_percentage, forecast_metric):
    future_dates = pd.date_range(start='2024-08-01', end=df['DATE'].max())
    df_future = pd.DataFrame({'DATE': future_dates})
    df_combined = pd.concat([df, df_future], ignore_index=True)

    # Apply subsidy to TOTAL_TXN_FEE_USD
    df_combined['TOTAL_TXN_FEE_USD'] = df['TOTAL_TXN_FEE_USD'] * (1 - subsidy_percentage / 100.0)

    # Simple forecast: assume linear relation with TOTAL_TXN_FEE_USD
    df_combined['FORECAST_' + forecast_metric] = df[forecast_metric] * (1 + subsidy_percentage / 100.0)

    return df_combined

df_forecast = forecast_impact(df, subsidy_percentage, forecast_metric)

# Plotting
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['DATE'], y=df[forecast_metric], mode='lines', name='Actual'))
fig.add_trace(go.Scatter(x=df_forecast['DATE'], y=df_forecast['FORECAST_' + forecast_metric], mode='lines', name='Forecast'))
fig.update_layout(title='Forecast of {} with {}% Subsidy'.format(forecast_metric, subsidy_percentage), xaxis_title='Date', yaxis_title=forecast_metric)
st.plotly_chart(fig)

# Display methodology
methodology_text = '''
### Methodology

We applied the subsidy to the total transaction fees for each day and then projected its impact proportionally to other metrics, under the assumption of a linear relationship. Specifically, the methodology involves applying the selected subsidy percentage to calculate the new forecasted metric for each day in the unified date range. The forecast also assumes a linear relationship, meaning that a change in transaction fees will result in a proportional change in the selected metric.

This approach allows us to estimate how different levels of subsidies might influence user behavior and protocol performance over time, providing a simplified yet insightful view of potential outcomes.
'''
st.markdown(methodology_text)
