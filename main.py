import pandas
import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
import seaborn as sns
from backend import *


season, race_names, next_race, current_weekend_title = get_current_weekends()
year = season
circuit = next_race

setup()
fp1, fp2, fp3 = load_summary(year, circuit)
laps_fp1, laps_fp2, laps_fp3 = load_laps(year, circuit, fp1, fp2, fp3)

# layout
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>"+current_weekend_title+"</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'> In-Depth Analysis by Michael Kofler</h3>", unsafe_allow_html=True)
st.markdown("""---""")
null, col_left_fp1, col_right_fp1, null2 = st.columns([0.5, 1, 2.5, 0.5])
st.markdown("""---""")
null, col_left_fp2, col_right_fp2, null2 = st.columns([0.5, 1, 2.5, 0.5])
st.markdown("""---""")
null, col_left_fp3, col_right_fp3, null2 = st.columns([0.5, 1, 2.5, 0.5])
st.markdown("""---""")
col_left_fp1.subheader("FP1")
col_left_fp2.subheader("FP2")
col_left_fp3.subheader("FP3")
col_left_fp1.dataframe(data = fp1, width=1024, height=768)
col_left_fp2.dataframe(data = fp2, width=1024, height=768)
col_left_fp3.dataframe(data = fp3, width=1024, height=768)

#st.markdown(
#    """
#    <style>
#    .reportview-container {
#        background: url("https://images5.alphacoders.com/317/thumb-1920-317664.jpg")
#    }
#    </style>
#    """,
#    unsafe_allow_html=True
#)

#sns.set_style('white')
# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots()
plt.grid(visible=None)

sns.heatmap(laps_fp1.transpose(), vmin=laps_fp1.min().min(), vmax=laps_fp1.min().max(), fmt="f", linewidths=.5, ax=ax, mask=laps_fp1.transpose().isnull(), cmap = "spring")
col_right_fp1.pyplot(f)

f2, ax2 = plt.subplots()

sns.heatmap(laps_fp2.transpose(), vmin=laps_fp2.min().min(), vmax=laps_fp2.min().max(), fmt="f", linewidths=.5, ax=ax2, mask=laps_fp2.transpose().isnull(), cmap = "spring")
col_right_fp2.pyplot(f2)

f3, ax3 = plt.subplots()
sns.heatmap(laps_fp3.transpose(), vmin=laps_fp3.min().min(), vmax=laps_fp3.min().max(), fmt="f", linewidths=.5, ax=ax3, mask=laps_fp3.transpose().isnull(), cmap = "spring")
col_right_fp3.pyplot(f3)
