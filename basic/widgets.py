import streamlit as st

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

import streamlit as st

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


# ----------复选框---------------

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['second column'])

'You selected: ', option