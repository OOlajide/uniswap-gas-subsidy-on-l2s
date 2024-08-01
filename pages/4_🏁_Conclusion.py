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


colored_header(
    label="",
    description="",
    color_name="gray-70",
)
st.markdown(f'<h1 style="color:#434346;font-size:40px;text-align:center;">{"Conclusion & Recommendation"}</h1>', unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

insights = '<p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The Dencun upgrade in mid-March 2024 had a significant impact on Uniswap\'s ecosystem, particularly on L2 networks. The upgrade, which reduced transaction fees, led to an increase in volume, active users, number of swaps, and active pools. This suggests that reduced transaction fees can indeed stimulate activity across the platform. However, it\'s crucial to note that despite this increased activity, protocol fee revenue didn\'t see a proportional increase, highlighting a complex relationship between transaction volume and actual revenue generation.</p><p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Among the L2 networks, Base emerged as the primary beneficiary of the upgrade, largely due to the "Base memecoin meta." This phenomenon indicates that reduced fees may have a more pronounced effect in speculative or trend-driven markets, which is an important consideration when evaluating the potential impact of fee subsidies.</p><p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Looking at transaction types, we observed that mint and burn liquidity transactions saw a rapid increase following the upgrade, while increase and decrease liquidity transactions also rose, albeit with a short-lived trend. This suggests that lower fees particularly encourage liquidity provision and removal, but the effect may be temporary. Such behavior could be leveraged to boost liquidity in specific pools or during particular periods.</p><p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The impact of reduced fees varied significantly across different pool types. Full stablecoin pairs were largely unaffected, indicating that these trades are less sensitive to fee changes. In contrast, partial stablecoin pairs saw increased activity, suggesting that pairs with one volatile asset are more responsive to fee reductions. Governance pairs showed minimal reaction, with only a slight increase in swap numbers for partial governance pairs. This differentiation in response across pool types suggests that a targeted approach to fee subsidies might be more effective than a blanket policy.</p><p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Pool size and age also played a role in the response to reduced fees. Pools with less than $100M total volume were most reactive, showing the largest increase in activity. Both older and younger pools saw an increase in the number of swaps, but younger pools (less than 1 year old) experienced a more significant increase in active users. This indicates that newer, smaller pools might benefit most from fee subsidies, potentially helping to bootstrap liquidity and user engagement in emerging markets or for new token pairs.</p><p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">Given these insights, there\'s a case for selectively subsidizing transaction fees, but with important considerations. A targeted approach focusing on emerging L2s with potential for speculative activity, smaller and newer pools, and pairs involving at least one volatile asset could be most effective. However, the limited impact on protocol revenue suggests that subsidies should be viewed primarily as a user acquisition and engagement tool rather than a direct revenue driver.</p><p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">The temporary nature of some of the observed increases, particularly in liquidity transactions, indicates that periodic promotions might be more effective than constant subsidies. This approach could help maintain user interest and engagement without committing to long-term fee reductions that might not be sustainable.</p><p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">While the memecoin effect on Base demonstrated high responsiveness to fee reductions, relying on such volatile markets may not be a sustainable long-term strategy. Uniswap should carefully balance the potential for short-term growth against the risks of encouraging unsustainable speculative behavior.</p><p style="font-family:sans-serif; color:#4d372c; font-size: 18px;">In conclusion, a nuanced and targeted subsidy strategy could benefit Uniswap, focusing on specific areas of the ecosystem where the impact is likely to be most significant. This could involve temporary, targeted subsidy programs to boost user engagement and liquidity in L2s, smaller pools, and for liquidity provision activities.</p>'
st.markdown(insights, unsafe_allow_html=True)
