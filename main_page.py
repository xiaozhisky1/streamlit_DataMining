import streamlit as st


st.set_page_config(
    page_title="Hello",
    page_icon="🎈",
)

st.sidebar.markdown("# Hello 🎈")
# st.markdown("# 📉 Membership and division of labor", unsafe_allow_html=True, )

# col1,col2 = st.columns(2)
# with col1:
#     st.image("./images/1-1.png")
# with col2:
#     st.image("header.gif", width=330)
#     st.markdown("#### 林琰钧*、叶兴松*、李肖奕*、马骏驰*、刘凯*、吴林至*、贺禄元*")

st.image("images/0.png")
# st.divider()
# st.write("<h2><b>⚙️ <u>Configuration</b></h2>", unsafe_allow_html=True)
# uploaded_file = st.file_uploader("Choose a file")
#
# @st.cache_data
# def load_data(path: str):
#     df = pd.read_excel(path)
#     return df
#
# if uploaded_file is None:
#     default_path = "Financial Data Clean.xlsx"
#     df = load_data(default_path)
#     st.info("Using a random Sales Data for an example, Upload a file to use your own data 👇", icon="ℹ️")
# else:
#     df = load_data(uploaded_file)
#
# all_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#
# with st.expander("🔭 Data Preview", expanded=True): # 一个可展开和折叠的容器
#     st.dataframe(df, column_config={"Year": st.column_config.NumberColumn(format="%d")})

