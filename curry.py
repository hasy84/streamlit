import streamlit as st
from random import choice
import pandas as pd
import numpy as np
import altair as alt

html = """
<h1>今日の料理</h1>
<h2>カレーライス</h2>
<h3>材料</h3>
<ul>
    <li>
        じゃがいも
    </li>
    <li>肉</li>
    <li>人参</li>
</ul>
<h3>作り方</h3>
"""

st.markdown(html, unsafe_allow_html=True)
