import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ========== 1. Title 标题（改成你自己名字）==========
st.title("California Housing Data (1990) by Wenbo Hu")

# 读取housing.csv
df = pd.read_csv("housing.csv")

# ========== 2. Slider：Minimal Median House Value ==========
house_value_slider = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000
)
# 筛选：只保留大于等于滑块值
df = df[df["median_house_value"] >= house_value_slider]

# ==========3. Subheader 子标题 ==========
st.subheader("See more filters in the sidebar:")

# ==========4. Sidebar multiselect 多选框 ocean_proximity ==========
location_options = df["ocean_proximity"].unique()
location_filter = st.sidebar.multiselect(
    "Choose the location type",
    options = location_options,
    default = location_options  # 默认全部选中
)
df = df[df["ocean_proximity"].isin(location_filter)]

# ==========5. Sidebar radio 单选框 Income Level ==========
income_choice = st.sidebar.radio(
    "Choose income level",
    options = ["Low", "Medium", "High"]
)
# if判断筛选
if income_choice == "Low":
    df = df[df["median_income"] <= 2.5]
elif income_choice == "Medium":
    df = df[(df["median_income"] > 2.5) & (df["median_income"] < 4.5)]
elif income_choice == "High":
    df = df[df["median_income"] >= 4.5]

# ==========6. 绘制筛选后地区地图 ==========
st.map(df)

# ==========7. 直方图 median_house_value，30 bins ==========
fig, ax = plt.subplots()
ax.hist(df["median_house_value"], bins=30)
ax.set_xlabel("Median House Value")
ax.set_ylabel("Count")
st.pyplot(fig)
