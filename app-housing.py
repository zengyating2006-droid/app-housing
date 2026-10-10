import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 读取完整原始数据
df = pd.read_csv("housing.csv")

# 1. 标题
st.title("California Housing Data (1990) by Zeng Yating")

# 2. 房价滑块
min_house_val = st.slider(
    label="Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000
)
# 第一步筛选：房价
filtered_df = df[df["median_house_value"] >= min_house_val]

# 3. 子标题
st.subheader("See more filters in the sidebar:")

# =========【修复重点】location选项从原始df拿，不是filtered_df！=====
location_list = df["ocean_proximity"].unique().tolist()
selected_loc = st.sidebar.multiselect(
    label="Choose the location type",
    options=location_list,
    default=location_list
)
filtered_df = filtered_df[filtered_df["ocean_proximity"].isin(selected_loc)]

# 4. 收入单选
income_choice = st.sidebar.radio(
    label="Choose income level",
    options=["Low", "Medium", "High"]
)

if income_choice == "Low":
    filtered_df = filtered_df[filtered_df["median_income"] <= 2.5]
elif income_choice == "Medium":
    filtered_df = filtered_df[(filtered_df["median_income"] > 2.5) & (filtered_df["median_income"] < 4.5)]
elif income_choice == "High":
    filtered_df = filtered_df[filtered_df["median_income"] >= 4.5]

# 调试：显示剩余数据行数
st.write("Remaining districts count:", len(filtered_df))

# 地图
if filtered_df.empty:
    st.write("No districts match your filters.")
else:
    st.map(filtered_df)

# 直方图
if not filtered_df.empty:
    fig, ax = plt.subplots()
    ax.hist(filtered_df["median_house_value"], bins=30)
    st.pyplot(fig)
