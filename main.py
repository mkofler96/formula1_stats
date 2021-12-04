import pandas
import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
import seaborn as sns
from backend import *

year = 2021
circuit = "qatar"

#setup()
#fp1, fp2, fp3 = load_summary(year, circuit)
#laps_fp1, laps_fp2, laps_fp3 = load_laps(year, circuit, fp1, fp2, fp3)

# layout
#st.set_page_config(layout="wide")
#null, col_left_fp1, col_right_fp1, null2 = st.columns([0.5, 1, 2.5, 0.5])
#null, col_left_fp2, col_right_fp2, null2 = st.columns([0.5, 1, 2.5, 0.5])
#null, col_left_fp3, col_right_fp3, null2 = st.columns([0.5, 1, 2.5, 0.5])
#col_left_fp1.dataframe(data = fp1, width=1024, height=768)
#col_left_fp2.dataframe(data = fp2, width=1024, height=768)
#col_left_fp3.dataframe(data = fp3, width=1024, height=768)

#set background
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
#plt.grid(visible=None)

#sns.heatmap(laps_fp1.transpose(), vmin=laps_fp1.min().min(), vmax=laps_fp1.min().max(), fmt="f", linewidths=.5, ax=ax, mask=laps_fp1.transpose().isnull())
#col_right_fp1.pyplot(f)

f2, ax2 = plt.subplots()

#sns.heatmap(laps_fp2.transpose(), vmin=laps_fp2.min().min(), vmax=laps_fp2.min().max(), fmt="f", linewidths=.5, ax=ax2, mask=laps_fp2.transpose().isnull())
#col_right_fp2.pyplot(f2)

f3, ax3 = plt.subplots()
#sns.heatmap(laps_fp3.transpose(), vmin=laps_fp3.min().min(), vmax=laps_fp3.min().max(), fmt="f", linewidths=.5, ax=ax3, mask=laps_fp3.transpose().isnull())
#col_right_fp3.pyplot(f3)
def SIR(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

N = 1000
beta = 1.0
D = 4.0
gamma = 1.0 / D

S0, I0, R0 = 999, 1, 0

t = np.linspace(0, 49, 50)
S, I, R = t, t, t

def plotsir(t, S, I, R):
  f, ax = plt.subplots(1,1,figsize=(10,4))
  ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
  ax.plot(t, I, 'y', alpha=0.7, linewidth=2, label='Infected')
  ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')

  ax.set_xlabel('Time (days)')

  ax.yaxis.set_tick_params(length=0)
  ax.xaxis.set_tick_params(length=0)
  ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
  legend = ax.legend()
  legend.get_frame().set_alpha(0.5)
  for spine in ('top', 'right', 'bottom', 'left'):
      ax.spines[spine].set_visible(False)
      #st.pyplot(f)
      plt.show()

plotsir(t, S, I, R)