import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 读取房价数据
df = pd.read_csv("housing.csv")

# 页面标题（lab要求，带上你的名字）
st.title("California Housing Data (1990) by Zeng Yating")

# 主页面滑块：最低房价
min_house_val = st.slider("Minimal Median House Value",
                          min_value=0,
                          max_value=500001,
                          value=200000)

filtered_df = df[df["median_house_value"] >= min_house_val]

# 子标题，lab强制要求
st.subheader("See more filters in the sidebar:")

# 侧边栏多选 ocean_proximity
location_options = filtered_df["ocean_proximity"].unique().tolist()
selected_locations = st.sidebar.multiselect(
    "Choose the location type",
    options=location_options,
    default=location_options
)
filtered_df = filtered_df[filtered_df["ocean_proximity"].isin(selected_locations)]

# 侧边栏单选收入等级 Low / Medium / High
income_level = st.sidebar.radio(
    "Choose income level",
    options=["Low", "Medium", "High"]
)

if income_level == "Low":
    filtered_df = filtered_df[filtered_df["median_income"] <= 2.5]
elif income_level == "Medium":
    filtered_df = filtered_df[(filtered_df["median_income"] > 2.5) & (filtered_df["median_income"] < 4.5)]
elif income_level == "High":
    filtered_df = filtered_df[filtered_df["median_income"] >= 4.5]

# 画地图
st.map(filtered_df)

# 房价直方图 bins=30
fig, ax = plt.subplots()
ax.hist(filtered_df["median_house_value"], bins=30)
st.pyplot(fig)