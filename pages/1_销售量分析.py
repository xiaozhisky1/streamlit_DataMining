import streamlit as st


st.markdown("# 销售量分析 📈")
st.sidebar.markdown("# 销售量分析 📈")

st.markdown("## 分析1：销售总量 ")
with st.expander("🔭 分析1：销售总量", expanded=False):
    # 设置标题
    st.markdown("#### 总销售量按年月的变化趋势 ")
    st.image("./images/1.png")

    col1,col2 = st.columns(2)
    with col1:
        st.markdown("#### 年规律")
        st.image("./images/2.png", width=600)
    with col2:
        st.markdown("#### 周规律")
        st.image("./images/5.png", width=600)

    col3,col4 = st.columns(2)
    with col3:
        st.markdown("#### 年规律时间序列分解")
        st.image("./images/3.png",width=600)
    with col4:
        st.markdown("#### 周规律时间序列分解")
        st.image("./images/6.png",width=600)

    st.markdown("#### 每月的蔬菜总销售量热力图")
    st.image("./images/4.png")



st.markdown("## 分析2：品类（年规律） ")
with st.expander("🔭 分析2：品类（年规律）", expanded=False):
    st.markdown("#### 品类")
    st.image("./images/7.png")

    st.markdown("#### 年规律")
    st.image("./images/8.png")

    st.markdown("#### 每月总销售量变化曲线")
    col1, col2 = st.columns(2)
    with col1:
        st.image("./images/9.png")
    with col2:
        st.image("./images/10.png")

    st.markdown("#### “水生根茎类”时间序列分解")
    st.image("./images/10-1.png")