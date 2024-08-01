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

url1a = "https://flipsidecrypto.xyz/studio/queries/c293273a-67f3-42d2-98c4-679ae1aa8798"
@st.cache_data
def load_df1a():
    df1a = pd.read_csv('data/df1a.csv')
    return df1a


###################################
############ LOAD DATA ############
###################################

df1a = load_df1a()

###################################
########### PLOT CHARTS ###########
###################################


##################### DF1a #####################


########################################### FIG0
################ CHART START ###################

# Create two line charts
df1a_fig0_1 = px.line(df1a, x='DATE', y='VOLUME_USD')
df1a_fig0_2 = px.line(df1a, x='DATE', y='AVG_TXN_FEE_USD')

# Create a new figure with secondary y-axis
df1a_fig0 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
df1a_fig0.add_trace(
    go.Scatter(x=df1a_fig0_1.data[0].x, y=df1a_fig0_1.data[0].y, name="VOLUME_USD"),
    secondary_y=False,
)

df1a_fig0.add_trace(
    go.Scatter(x=df1a_fig0_1.data[0].x, y=df1a_fig0_2.data[0].y, name="AVG_TXN_FEE_USD"),
    secondary_y=True,
)

# Set x-axis title
df1a_fig0.update_xaxes(title_text="DATE")

# Set y-axes titles
df1a_fig0.update_yaxes(title_text="VOLUME_USD", secondary_y=False)

df1a_fig0.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

# Update layout
df1a_fig0.update_layout(
    title_text="Daily Volume USD vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df1a_fig0.update_layout(hovermode="x unified")

# Customize colors
df1a_fig0.update_traces(line=dict(color="blue"), secondary_y=False)
df1a_fig0.update_traces(line=dict(color="red"), secondary_y=True)
df1a_fig0.update_traces(line=dict(width=0.9))

################### CHART END ##################

########################################### FIG1
################ CHART START ###################

# Create two line charts
df1a_fig1_1 = px.line(df1a, x='DATE', y='TOTAL_ACTIVE_USERS')
df1a_fig1_2 = px.line(df1a, x='DATE', y='AVG_TXN_FEE_USD')

# Create a new figure with secondary y-axis
df1a_fig1= make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
df1a_fig1.add_trace(
    go.Scatter(x=df1a_fig1_1.data[0].x, y=df1a_fig1_1.data[0].y, name="ACTIVE_USERS"),
    secondary_y=False,
)

df1a_fig1.add_trace(
    go.Scatter(x=df1a_fig1_1.data[0].x, y=df1a_fig1_2.data[0].y, name="AVG_TXN_FEE_USD"),
    secondary_y=True,
)

# Set x-axis title
df1a_fig1.update_xaxes(title_text="DATE")

# Set y-axes titles
df1a_fig1.update_yaxes(title_text="ACTIVE_USERS", secondary_y=False)
df1a_fig1.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

# Update layout
df1a_fig1.update_layout(
    title_text="Daily Active Users vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df1a_fig1.update_layout(hovermode="x unified")

# Customize colors
df1a_fig1.update_traces(line=dict(color="blue"), secondary_y=False)
df1a_fig1.update_traces(line=dict(color="red"), secondary_y=True)

df1a_fig1.update_traces(line=dict(width=0.9))

################### CHART END ##################


########################################### FIG2
################ CHART START ###################

# Create two line charts
df1a_fig2_1 = px.line(df1a, x='DATE', y='SWAP_TXNS')
df1a_fig2_2 = px.line(df1a, x='DATE', y='AVG_TXN_FEE_USD')

# Create a new figure with secondary y-axis
df1a_fig2 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
df1a_fig2.add_trace(
    go.Scatter(x=df1a_fig2_1.data[0].x, y=df1a_fig2_1.data[0].y, name="SWAP_TXNS"),
    secondary_y=False,
)

df1a_fig2.add_trace(
    go.Scatter(x=df1a_fig2_1.data[0].x, y=df1a_fig2_2.data[0].y, name="AVG_TXN_FEE_USD"),
    secondary_y=True,
)

# Set x-axis title
df1a_fig2.update_xaxes(title_text="DATE")

# Set y-axes titles
df1a_fig2.update_yaxes(title_text="SWAP_TXNS", secondary_y=False)
df1a_fig2.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

# Update layout
df1a_fig2.update_layout(
    title_text="Daily Swap Transactions vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df1a_fig2.update_layout(hovermode="x unified")

# Customize colors
df1a_fig2.update_traces(line=dict(color="blue"), secondary_y=False)
df1a_fig2.update_traces(line=dict(color="red"), secondary_y=True)
df1a_fig2.update_traces(line=dict(width=0.9))
################### CHART END ##################

########################################### FIG3
################ CHART START ###################

# Create two line charts
df1a_fig3_1 = px.line(df1a, x='DATE', y='TOTAL_ACTIVE_POOLS')
df1a_fig3_2 = px.line(df1a, x='DATE', y='AVG_TXN_FEE_USD')

# Create a new figure with secondary y-axis
df1a_fig3 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
df1a_fig3.add_trace(
    go.Scatter(x=df1a_fig3_1.data[0].x, y=df1a_fig3_1.data[0].y, name="ACTIVE_POOLS"),
    secondary_y=False,
)

df1a_fig3.add_trace(
    go.Scatter(x=df1a_fig3_1.data[0].x, y=df1a_fig3_2.data[0].y, name="AVG_TXN_FEE_USD"),
    secondary_y=True,
)

# Set x-axis title
df1a_fig3.update_xaxes(title_text="DATE")

# Set y-axes titles
df1a_fig3.update_yaxes(title_text="ACTIVE_POOLS", secondary_y=False)

df1a_fig3.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

# Update layout
df1a_fig3.update_layout(
    title_text="Daily Active Pools vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df1a_fig3.update_layout(hovermode="x unified")

# Customize colors
df1a_fig3.update_traces(line=dict(color="blue"), secondary_y=False)
df1a_fig3.update_traces(line=dict(color="red"), secondary_y=True)
df1a_fig3.update_traces(line=dict(width=0.9))

################### CHART END ##################

########################################### FIG4
################ CHART START ###################

# Create two line charts
df1a_fig4_1 = px.line(df1a, x='DATE', y='PROTOCOL_FEES_USD')
df1a_fig4_2 = px.line(df1a, x='DATE', y='AVG_TXN_FEE_USD')

# Create a new figure with secondary y-axis
df1a_fig4 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
df1a_fig4.add_trace(
    go.Scatter(x=df1a_fig4_1.data[0].x, y=df1a_fig4_1.data[0].y, name="PROTOCOL_FEES_USD"),
    secondary_y=False,
)

df1a_fig4.add_trace(
    go.Scatter(x=df1a_fig4_1.data[0].x, y=df1a_fig4_2.data[0].y, name="AVG_TXN_FEE_USD"),
    secondary_y=True,
)

# Set x-axis title
df1a_fig4.update_xaxes(title_text="DATE")

# Set y-axes titles
df1a_fig4.update_yaxes(title_text="PROTOCOL_FEES_USD", secondary_y=False)
df1a_fig4.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

# Update layout
df1a_fig4.update_layout(
    title_text="Daily Protocol Fees USD vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df1a_fig4.update_layout(hovermode="x unified")

# Customize colors
df1a_fig4.update_traces(line=dict(color="blue"), secondary_y=False)
df1a_fig4.update_traces(line=dict(color="red"), secondary_y=True)
df1a_fig4.update_traces(line=dict(width=0.9))

################### CHART END ##################

########################################### FIG5
################ CHART START ###################

# Create two line charts
df1a_fig5_1 = px.line(df1a, x='DATE', y='MINT_LIQUIDITY_TXNS')
df1a_fig5_2 = px.line(df1a, x='DATE', y='BURN_LIQUIDITY_TXNS')
df1a_fig5_3 = px.line(df1a, x='DATE', y='AVG_TXN_FEE_USD')

# Create a new figure with secondary y-axis
df1a_fig5 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
df1a_fig5.add_trace(
    go.Scatter(x=df1a_fig5_1.data[0].x, y=df1a_fig5_1.data[0].y, name="MINT_LIQUIDITY_TXNS"),
    secondary_y=False,
)

df1a_fig5.add_trace(
    go.Scatter(x=df1a_fig5_2.data[0].x, y=df1a_fig5_2.data[0].y, name="BURN_LIQUIDITY_TXNS"),
    secondary_y=False,
)

df1a_fig5.add_trace(
    go.Scatter(x=df1a_fig5_3.data[0].x, y=df1a_fig5_3.data[0].y, name="AVG_TXN_FEE_USD"),
    secondary_y=True,
)

# Set x-axis title
df1a_fig5.update_xaxes(title_text="DATE")

# Set y-axes titles
df1a_fig5.update_yaxes(title_text="MINT_LIQUIDITY_TXNS, BURN_LIQUIDITY_TXNS", secondary_y=False)
df1a_fig5.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

# Update layout
df1a_fig5.update_layout(
    title_text="Daily Mint & Burn Liquidity Transactions vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df1a_fig5.update_layout(hovermode="x unified")

# Customize colors
df1a_fig5.update_traces(line=dict(color="blue"), secondary_y=False, selector=dict(name="MINT_LIQUIDITY_TXNS"))
df1a_fig5.update_traces(line=dict(color="green"), secondary_y=False, selector=dict(name="BURN_LIQUIDITY_TXNS"))
df1a_fig5.update_traces(line=dict(color="red"), secondary_y=True, selector=dict(name="AVG_TXN_FEE_USD"))
df1a_fig5.update_traces(line=dict(width=0.9))
################### CHART END ##################

########################################### FIG6
################ CHART START ###################

# Create two line charts
df1a_fig6_1 = px.line(df1a, x='DATE', y='INCREASE_LIQUIDITY_TXNS')
df1a_fig6_2 = px.line(df1a, x='DATE', y='DECREASE_LIQUIDITY_TXNS')
df1a_fig6_3 = px.line(df1a, x='DATE', y='AVG_TXN_FEE_USD')

# Create a new figure with secondary y-axis
df1a_fig6 = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
df1a_fig6.add_trace(
    go.Scatter(x=df1a_fig6_1.data[0].x, y=df1a_fig6_1.data[0].y, name="INCREASE_LIQUIDITY_TXNS"),
    secondary_y=False,
)

df1a_fig6.add_trace(
    go.Scatter(x=df1a_fig6_2.data[0].x, y=df1a_fig6_2.data[0].y, name="DECREASE_LIQUIDITY_TXNS"),
    secondary_y=False,
)

df1a_fig6.add_trace(
    go.Scatter(x=df1a_fig6_3.data[0].x, y=df1a_fig6_3.data[0].y, name="AVG_TXN_FEE_USD"),
    secondary_y=True,
)

# Set x-axis title
df1a_fig6.update_xaxes(title_text="DATE")

# Set y-axes titles
df1a_fig6.update_yaxes(title_text="INCREASE_LIQUIDITY_TXNS, DECREASE_LIQUIDITY_TXNS", secondary_y=False)
df1a_fig6.update_yaxes(title_text="AVG_TXN_FEE_USD", secondary_y=True)

# Update layout
df1a_fig6.update_layout(
    title_text="Daily Increase & Decrease Liquidity Transactions vs Daily Avg Txn Fee USD",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
df1a_fig6.update_layout(hovermode="x unified")

# Customize colors
df1a_fig6.update_traces(line=dict(color="blue"), secondary_y=False, selector=dict(name="INCREASE_LIQUIDITY_TXNS"))
df1a_fig6.update_traces(line=dict(color="green"), secondary_y=False, selector=dict(name="DECREASE_LIQUIDITY_TXNS"))
df1a_fig6.update_traces(line=dict(color="red"), secondary_y=True, selector=dict(name="AVG_TXN_FEE_USD"))
df1a_fig6.update_traces(line=dict(width=0.9))
################### CHART END ##################

###################################
############# LAYOUT ##############
###################################

text_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">This analysis aims to delve deep into the effects of gas subsidies on Uniswap\'s ecosystem, with a particular focus on L2 networks: Arbitrum, Base and Optimism in particular, where the majority of retail user activity occurs. Our objective is to provide actionable insights that can guide Uniswap\'s strategy in optimizing gas subsidies to enhance user engagement and ultimately boost protocol revenue.</p>'

text_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">Key areas of focus include:</p>'

text_3 = '<ul style="font-family:sans-serif; color:#4d372c; font-size: 20px;"><li>Assessing the direct impact of gas subsidies on transaction volumes across different types of activities (swaps, liquidity additions, and removals).</li><li>Examining changes in liquidity provider (LP) behavior in response to reduced transaction costs.</li><li>Conducting a comparative analysis of gas subsidy effects across various liquidity pool types.</li><li>Investigating user responses to high gas periods on L2s and identifying potential targeted subsidy strategies.</li></ul>'

text_4 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">We\'ll explore not just how different user groups respond to gas price fluctuations, but also why these responses make compelling arguments for or against specific subsidy approaches.</p>'

text_5 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 20px;">We analyzed data from these 3 L2s: Arbitrum, Base, and Optimism, provided by <a href="https://flipsidecrypto.xyz/">Flipside Crypto</a>. You can click on the <b>View SQL</b> button under each chart to view the underlying SQL query.</p>'

st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Uniswap Gas Subsidy On L2s"}</h1>', unsafe_allow_html=True)

st.markdown(text_1, unsafe_allow_html=True)
st.markdown(text_2, unsafe_allow_html=True)
st.markdown(text_3, unsafe_allow_html=True)
st.markdown(text_4, unsafe_allow_html=True)
st.markdown(text_5, unsafe_allow_html=True)

st.subheader('Methodology')
st.markdown(
    '''
    **Our analysis focuses on Uniswap activity across three Layer 2 (L2) networks: Arbitrum, Base, and Optimism, starting from January 1, 2023.**
    
    1. **Swap Transactions:**
       - We collect detailed swap transaction data from the `crosschain.defi.ez_dex_swaps` table.
       - For each swap, we record timestamp, transaction hash, pool information, trader address, and token details (including amounts and USD values).
    
    2. **Transaction Fees:**
       - We join swap data with transaction fee information from each L2's `core.fact_transactions` table.
       - We convert ETH-denominated fees to USD using hourly price data from `ethereum.price.ez_prices_hourly`.
    
    3. **Volume Data:**
       - Daily volume in USD is aggregated from `external.defillama.fact_dex_volume` for Uniswap v1, v2, and v3 on the three L2s.
    
    4. **Protocol Fees:**
       - We collect daily protocol fees in USD from `external.defillama.fact_protocol_fees_revenue` for Uniswap across all versions on the L2s.
    
    5. **Liquidity Provider (LP) Actions:**
       - We analyze LP activities by counting distinct transactions for minting, burning, increasing, and decreasing liquidity.
       - This data is gathered from `ez_decoded_event_logs` on each L2, focusing on Uniswap-related contracts.
    
    6. **Data Aggregation:**
       - We combine all these data sources to create a daily summary of Uniswap activity across the L2s.
       - Key metrics include:
         * Total active users and swap transactions
         * LP action counts (mints, burns, increases, decreases)
         * Total active pools
         * Transaction fees (total and average, in both ETH and USD)
         * Volume in USD
         * Protocol fees in USD
    '''
)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"General Overview"}</h1>', unsafe_allow_html=True)
st.info("This page encapsulates the essential takeaways from our analysis.", icon="ℹ️")
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

st.plotly_chart(df1a_fig0, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url1a}")

col_1a, col_1b = st.columns(2)
with col_1a:
    st.plotly_chart(df1a_fig1, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url1a}")
with col_1b:
    st.plotly_chart(df1a_fig2, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url1a}")

col_2a, col_2b = st.columns(2)
with col_2a:
    st.plotly_chart(df1a_fig3, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url1a}")
with col_2b:
    st.plotly_chart(df1a_fig4, theme="streamlit", use_container_width=True)
    st.link_button("View SQL", f"{url1a}")

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insight_1 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;"></p>'
st.markdown(insight_1, unsafe_allow_html=True)

insight_2 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;"></p>'
st.markdown(insight_2, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Liquidity Provider Actions"}</h1>', unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

st.plotly_chart(df1a_fig5, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url1a}")

st.plotly_chart(df1a_fig6, theme="streamlit", use_container_width=True)
st.link_button("View SQL", f"{url1a}")

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insight_3 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;"></p>'
st.markdown(insight_3, unsafe_allow_html=True)

insight_4 = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;"></p>'
st.markdown(insight_4, unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)
