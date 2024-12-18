import streamlit as st

st.markdown("# 日定价策略 📈")
st.sidebar.markdown("# 日定价策略 📈")

st.image("images/31.png")

st.markdown("### 以最大化利润为目标进行定价(线性规划)")
st.markdown("- 最大化目标： 利润  P=(售价×销量)−(批发价×进货量)")
st.markdown("- 决策变量：售价、进货量")
st.markdown("- 约束条件：批发价，销量")

st.image("images/32.png",width=300)
