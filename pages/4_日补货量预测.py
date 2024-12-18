import streamlit as st

st.markdown("# 日补货量预测 📈")
st.sidebar.markdown("# 日补货量预测 📈")

st.markdown("### LSTM时间序列预测")

st.image("./images/28.png")

st.markdown("#### 花叶类预测结果")
col1, col2 = st.columns((3,5))
with col1:
    st.markdown("##### 模型参数设置:")
with col2:
    st.image("./images/30.png")
st.markdown("- 回溯窗口设置: 根据时序分析的周规律结果设置回溯窗口大小为7的倍数，通过交叉验证评估最优效果")
st.markdown("- 隐藏层设置: 不同品类的波动幅度不同，调整隐藏层大小以调整模型表达能力")
st.markdown("- 自回归预测: 迭代地将预测的结果作为下一次的输入，以获得未来多个时间步的结果。")
st.image("./images/29.png")