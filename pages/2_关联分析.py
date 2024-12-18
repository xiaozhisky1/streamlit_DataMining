import streamlit as st

st.markdown("# 关联分析 📈")
st.sidebar.markdown("# 关联分析 📈")

st.markdown("## FP-Growth算法")
with st.expander("🔭 FP-Growth算法", expanded=False):

    st.markdown("### Step 1 数据存储优化")
    st.image("./images/11.png")

    st.markdown("### Step 2 购物篮分析")
    st.image("./images/12.png")

    st.markdown("### Step 3 FP-Growth计算频繁项集与关联规则")
    st.write("min_support_count设为1000，要求某个项集几乎每天都出现")
    st.write("min_confidence根据规则数动态选择，权衡可靠性与数量")
    st.image("./images/13.png")

    col1, col2 = st.columns(2)
    with col1:
        st.image("./images/14.png")
    with col2:
        st.image("./images/16.png")


st.markdown("## K-means算法")
with st.expander("🔭 K-means算法", expanded=False):
    st.markdown("### 相关性热力图 ")
    st.image("./images/15-1.png")

    st.markdown("### 层次聚类树状图 ")
    st.image("./images/15-2.png")