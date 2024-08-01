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

url4a = "https://flipsidecrypto.xyz/studio/queries/8fbe8306-d3f8-48df-af8a-db5ec2232f88"
@st.cache_data
def load_df4a():
    df4a = pd.read_csv('data/df4a.csv')
    return df4a

url5a = "https://flipsidecrypto.xyz/studio/queries/6010b2ac-7cb1-4fa7-aa99-02b5bcb56d76"
@st.cache_data
def load_df5a():
    df5a = pd.read_csv('data/df5a.csv')
    return df5a

###################################
############ LOAD DATA ############
###################################

df4a = load_df4a()
df5a = load_df5a()

###################################
########### PLOT CHARTS ###########
###################################


##################### DF4a #####################


################### CHART START ##################
# Create separate line charts for each category
very_high = df4a[df4a['CATEGORY'] == 'Very High: > $10B']
high = df4a[df4a['CATEGORY'] == 'High: $1B - $10B']
medium = df4a[df4a['CATEGORY'] == 'Medium: $100M - $999M']
low = df4a[df4a['CATEGORY'] == 'Low: <$100M']

df4a_fig1_1 = px.line(very_high, x='DATE', y='TOTAL_ACTIVE_USERS', title='Very High: > $10B - ACTIVE_USERS', labels={'TOTAL_ACTIVE_USERS': 'Total Active Users'})
df4a_fig1_2 = px.line(high, x='DATE', y='TOTAL_ACTIVE_USERS', title='High: $1B - $10B - ACTIVE_USERS', labels={'TOTAL_ACTIVE_USERS': 'Total Active Users'})
df4a_fig1_3 = px.line(medium, x='DATE', y='TOTAL_ACTIVE_USERS', title='Medium: $100M - $999M - ACTIVE_USERS', labels={'TOTAL_ACTIVE_USERS': 'Total Active Users'})
df4a_fig1_4 = px.line(low, x='DATE', y='TOTAL_ACTIVE_USERS', title='Low: <$100M - ACTIVE_USERS', labels={'TOTAL_ACTIVE_USERS': 'Total Active Users'})
df4a_fig1_5 = px.line(df4a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis
df4a_fig1 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for each category
for trace in df4a_fig1_1.data:
    trace.update(name='Very High: > $10B - ACTIVE_USERS', hovertemplate='%{y}')
    df4a_fig1.add_trace(trace, secondary_y=False)

for trace in df4a_fig1_2.data:
    trace.update(name='High: $1B - $10B - ACTIVE_USERS', hovertemplate='%{y}')
    df4a_fig1.add_trace(trace, secondary_y=False)

for trace in df4a_fig1_3.data:
    trace.update(name='Medium: $100M - $999M - ACTIVE_USERS', hovertemplate='%{y}')
    df4a_fig1.add_trace(trace, secondary_y=False)

for trace in df4a_fig1_4.data:
    trace.update(name='Low: <$100M - ACTIVE_USERS', hovertemplate='%{y}')
    df4a_fig1.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df4a_fig1_5.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df4a_fig1.add_trace(trace, secondary_y=True)

# Set x-axis title
df4a_fig1.update_xaxes(title_text="DATE")

# Set y-axes titles
df4a_fig1.update_yaxes(title_text="ACTIVE_USERS", secondary_y=False)
df4a_fig1.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df4a_fig1.update_layout(
    title_text="Total Active Users per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

df4a_fig1.update_layout(hovermode="x unified")
df4a_fig1.update_traces(line=dict(width=0.9))

# Update trace colors
df4a_fig1.update_traces(selector=dict(name='Very High: > $10B - ACTIVE_USERS'), line=dict(color="blue"), showlegend=True)
df4a_fig1.update_traces(selector=dict(name='High: $1B - $10B - ACTIVE_USERS'), line=dict(color="green"), showlegend=True)
df4a_fig1.update_traces(selector=dict(name='Medium: $100M - $999M - ACTIVE_USERS'), line=dict(color="purple"), showlegend=True)
df4a_fig1.update_traces(selector=dict(name='Low: <$100M - ACTIVE_USERS'), line=dict(color="orange"), showlegend=True)
df4a_fig1.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)
################### CHART END ##################

################### CHART START ##################
# Create separate line charts for each category
very_high_swap = df4a[df4a['CATEGORY'] == 'Very High: > $10B']
high_swap = df4a[df4a['CATEGORY'] == 'High: $1B - $10B']
medium_swap = df4a[df4a['CATEGORY'] == 'Medium: $100M - $999M']
low_swap = df4a[df4a['CATEGORY'] == 'Low: <$100M']

df4a_fig2_1 = px.line(very_high_swap, x='DATE', y='SWAP_TXNS', title='Very High: > $10B - SWAP_TXNS', labels={'SWAP_TXNS': 'Swap Transactions'})
df4a_fig2_2 = px.line(high_swap, x='DATE', y='SWAP_TXNS', title='High: $1B - $10B - SWAP_TXNS', labels={'SWAP_TXNS': 'Swap Transactions'})
df4a_fig2_3 = px.line(medium_swap, x='DATE', y='SWAP_TXNS', title='Medium: $100M - $999M - SWAP_TXNS', labels={'SWAP_TXNS': 'Swap Transactions'})
df4a_fig2_4 = px.line(low_swap, x='DATE', y='SWAP_TXNS', title='Low: <$100M - SWAP_TXNS', labels={'SWAP_TXNS': 'Swap Transactions'})
df4a_fig2_5 = px.line(df4a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis
df4a_fig2 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for each category
for trace in df4a_fig2_1.data:
    trace.update(name='Very High: > $10B - SWAP_TXNS', hovertemplate='%{y}')
    df4a_fig2.add_trace(trace, secondary_y=False)

for trace in df4a_fig2_2.data:
    trace.update(name='High: $1B - $10B - SWAP_TXNS', hovertemplate='%{y}')
    df4a_fig2.add_trace(trace, secondary_y=False)

for trace in df4a_fig2_3.data:
    trace.update(name='Medium: $100M - $999M - SWAP_TXNS', hovertemplate='%{y}')
    df4a_fig2.add_trace(trace, secondary_y=False)

for trace in df4a_fig2_4.data:
    trace.update(name='Low: <$100M - SWAP_TXNS', hovertemplate='%{y}')
    df4a_fig2.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df4a_fig2_5.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df4a_fig2.add_trace(trace, secondary_y=True)

# Set x-axis title
df4a_fig2.update_xaxes(title_text="DATE")

# Set y-axes titles
df4a_fig2.update_yaxes(title_text="SWAP_TXNS", secondary_y=False)
df4a_fig2.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df4a_fig2.update_layout(
    title_text="Swap Transactions per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

df4a_fig2.update_layout(hovermode="x unified")
df4a_fig2.update_traces(line=dict(width=0.9))

# Update trace colors
df4a_fig2.update_traces(selector=dict(name='Very High: > $10B - SWAP_TXNS'), line=dict(color="blue"), showlegend=True)
df4a_fig2.update_traces(selector=dict(name='High: $1B - $10B - SWAP_TXNS'), line=dict(color="green"), showlegend=True)
df4a_fig2.update_traces(selector=dict(name='Medium: $100M - $999M - SWAP_TXNS'), line=dict(color="purple"), showlegend=True)
df4a_fig2.update_traces(selector=dict(name='Low: <$100M - SWAP_TXNS'), line=dict(color="orange"), showlegend=True)
df4a_fig2.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)
################### CHART END ##################


##################### DF5a #####################

# Create separate line charts for each category in df5a
greater_than_year = df5a[df5a['CATEGORY'] == 'Older than 1 year']
less_than_year = df5a[df5a['CATEGORY'] == 'Not Older than 1 year']

df5a_fig1_1 = px.line(greater_than_year, x='DATE', y='TOTAL_ACTIVE_USERS', title='Older than 1 year - ACTIVE_USERS', labels={'TOTAL_ACTIVE_USERS': 'Total Active Users'})
df5a_fig1_2 = px.line(less_than_year, x='DATE', y='TOTAL_ACTIVE_USERS', title='Not Older than 1 year - ACTIVE_USERS', labels={'TOTAL_ACTIVE_USERS': 'Total Active Users'})
df5a_fig1_3 = px.line(df5a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis
df5a_fig1 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for each category
for trace in df5a_fig1_1.data:
    trace.update(name='Older than 1 year - ACTIVE_USERS', hovertemplate='%{y}')
    df5a_fig1.add_trace(trace, secondary_y=False)

for trace in df5a_fig1_2.data:
    trace.update(name='Not Older than 1 year - ACTIVE_USERS', hovertemplate='%{y}')
    df5a_fig1.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df5a_fig1_3.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df5a_fig1.add_trace(trace, secondary_y=True)

# Set x-axis title
df5a_fig1.update_xaxes(title_text="DATE")

# Set y-axes titles
df5a_fig1.update_yaxes(title_text="ACTIVE_USERS", secondary_y=False)
df5a_fig1.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df5a_fig1.update_layout(
    title_text="Total Active Users per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

df5a_fig1.update_layout(hovermode="x unified")
df5a_fig1.update_traces(line=dict(width=0.9))

# Update trace colors
df5a_fig1.update_traces(selector=dict(name='Older than 1 year - ACTIVE_USERS'), line=dict(color="blue"), showlegend=True)
df5a_fig1.update_traces(selector=dict(name='Not Older than 1 year - ACTIVE_USERS'), line=dict(color="green"), showlegend=True)
df5a_fig1.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)

# Create separate line charts for each category in df5a
greater_than_year_swap = df5a[df5a['CATEGORY'] == 'Older than 1 year']
less_than_year_swap = df5a[df5a['CATEGORY'] == 'Not Older than 1 year']

df5a_fig2_1 = px.line(greater_than_year_swap, x='DATE', y='SWAP_TXNS', title='Older than 1 year - SWAP_TXNS', labels={'SWAP_TXNS': 'Swap Transactions'})
df5a_fig2_2 = px.line(less_than_year_swap, x='DATE', y='SWAP_TXNS', title='Not Older than 1 year - SWAP_TXNS', labels={'SWAP_TXNS': 'Swap Transactions'})
df5a_fig2_3 = px.line(df5a, x='DATE', y='AVG_TXN_FEE_USD', title='Category - AVG_TXN_FEE_USD', labels={'AVG_TXN_FEE_USD': 'Avg Txn Fee USD'})

# Create a new figure with secondary y-axis
df5a_fig2 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces for each category
for trace in df5a_fig2_1.data:
    trace.update(name='Older than 1 year - SWAP_TXNS', hovertemplate='%{y}')
    df5a_fig2.add_trace(trace, secondary_y=False)

for trace in df5a_fig2_2.data:
    trace.update(name='Not Older than 1 year - SWAP_TXNS', hovertemplate='%{y}')
    df5a_fig2.add_trace(trace, secondary_y=False)

# Add single AVG_TXN_FEE_USD trace
for trace in df5a_fig2_3.data:
    trace.update(name='Avg Txn Fee USD', hovertemplate='%{y}', line=dict(color='red'))
    df5a_fig2.add_trace(trace, secondary_y=True)

# Set x-axis title
df5a_fig2.update_xaxes(title_text="DATE")

# Set y-axes titles
df5a_fig2.update_yaxes(title_text="SWAP_TXNS", secondary_y=False)
df5a_fig2.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

df5a_fig2.update_layout(
    title_text="Swap Transactions per Category vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

df5a_fig2.update_layout(hovermode="x unified")
df5a_fig2.update_traces(line=dict(width=0.9))

# Update trace colors
df5a_fig2.update_traces(selector=dict(name='Older than 1 year - SWAP_TXNS'), line=dict(color="blue"), showlegend=True)
df5a_fig2.update_traces(selector=dict(name='Not Older than 1 year - SWAP_TXNS'), line=dict(color="green"), showlegend=True)
df5a_fig2.update_traces(selector=dict(name='Avg Txn Fee USD'), line=dict(color="red"), showlegend=True)

###################################
############# LAYOUT ##############
###################################

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Pool Volume"}</h1>', unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

st.plotly_chart(df4a_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url4a}")

st.plotly_chart(df4a_fig2, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url4a}")


colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Pool Age"}</h1>', unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

st.plotly_chart(df5a_fig1, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url5a}")

st.plotly_chart(df5a_fig2, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url5a}")
