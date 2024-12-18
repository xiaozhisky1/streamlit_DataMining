import streamlit as st
import time
import numpy as np
import pandas as pd

# st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# 成本定价模型 📈")
st.sidebar.header("成本定价模型 📈")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("##### 价格随时间变化")
    st.image("./images/17.png")
with col2:
    st.markdown("##### 销量随时间变化")
    st.image("./images/18.png")
with col3:
    st.markdown("###### 花叶类销量与价格变化")
    st.image("./images/19.png")

st.markdown("### 数据汇总")
st.image("./images/20.png")

st.markdown("### 用不同模型拟合销量与定价的关系")
# ---复选框---
df = pd.DataFrame({
    'column': ["决策树模型", "线性模型", "集成模型", "神经网络模型", "KNN模型"],
    })

option = st.selectbox(
    "选择模型",
     df['column']
)

if option == "决策树模型":
    st.image("./images/23.png")
elif option == "线性模型":
    st.image("./images/24.png")
elif option == "集成模型":
    st.image("./images/25.png")
elif option == "神经网络模型":
    st.image("./images/26.png")
elif option == "KNN模型":
    st.image("./images/27.png")


st.markdown("### 各蔬菜品类销售总量与成本加成定价的关系")
col4,col5 = st.columns((1,2))
with col4:
    st.image("./images/21.png")
with col5:
    st.image("./images/22.png")