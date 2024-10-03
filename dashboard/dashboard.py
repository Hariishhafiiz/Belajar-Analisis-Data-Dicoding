import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def get_total_count_by_hour_df(hour_df):
    hour_count_df = hour_df.groupby(by="hour").agg({"total_users": ["sum"]})
    return hour_count_df

def count_by_day_clean(day_clean):
    day_clean_count_2011 = day_clean.query('date >= "2011-01-01" and date < "2012-12-31"')
    return day_clean_count_2011

def total_registered_users_df(day_clean):
    reg_df = day_clean.groupby(by="date").agg({
        "registered_users": "sum"
    })
    reg_df = reg_df.reset_index()
    reg_df.rename(columns={
        "registered_users": "register_sum"
    }, inplace=True)
    return reg_df

def total_casual_users_df(day_clean):
    cas_df = day_clean.groupby(by="date").agg({
        "casual_users": ["sum"]
    })
    cas_df = cas_df.reset_index()
    cas_df.rename(columns={
        "casual_users": "casual_users_sum"
    }, inplace=True)
    return cas_df

def sum_order(hour_df):
    sum_order_items_df = hour_df.groupby("hour").total_users.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_df

def macem_season(day_clean): 
    season_df = day_clean.groupby(by="season").total_users.sum().reset_index() 
    return season_df

# Load data
days_df = pd.read_csv("dashboard/day_clean.csv")
hour_df = pd.read_csv("dashboard/hour_clean.csv")

# Prepare data
datetime_columns = ["date"]
days_df.sort_values(by="date", inplace=True)
days_df.reset_index(inplace=True)

hour_df.sort_values(by="date", inplace=True)
hour_df.reset_index(inplace=True)

for column in datetime_columns:
    days_df[column] = pd.to_datetime(days_df[column])
    hour_df[column] = pd.to_datetime(hour_df[column])

# Get date range
min_date_days = days_df["date"].min()
max_date_days = days_df["date"].max()
min_date_hour = hour_df["date"].min()
max_date_hour = hour_df["date"].max()

# Sidebar with date input
with st.sidebar:
    st.image("dashboard/bike_bg.jpg")
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days]
    )
  
# Filter data by date range
main_df_days = days_df[(days_df["date"] >= str(start_date)) & 
                       (days_df["date"] <= str(end_date))]

main_df_hour = hour_df[(hour_df["date"] >= str(start_date)) & 
                        (hour_df["date"] <= str(end_date))]

# Process data
hour_count_df = get_total_count_by_hour_df(main_df_hour)
day_clean_count_2011 = count_by_day_clean(main_df_days)
reg_df = total_registered_users_df(main_df_days)
cas_df = total_casual_users_df(main_df_days)
sum_order_items_df = sum_order(main_df_hour)
season_df = macem_season(main_df_hour)

# Dashboard Header
st.header('🚲 Bike Rent 🚲')

st.subheader('Daily Bike Rent')
col1, col2, col3 = st.columns(3)

with col1:
    total_orders = day_clean_count_2011.total_users.sum()
    st.metric("Total Sharing Bike", value=total_orders)

with col2:
    total_sum = reg_df.register_sum.sum()
    st.metric("Total Registered Users", value=total_sum)

with col3:
    total_sum = cas_df.casual_users_sum.sum()
    st.metric("Total Casual Users", value=total_sum)

st.subheader("Kinerja Penyewaan Sepeda Selama Beberapa Tahun Terakhir")

plt.figure(figsize=(24, 5))
monthly_counts = main_df_days['total_users'].groupby(main_df_days['date']).max()

plt.scatter(monthly_counts.index, monthly_counts.values, c="#90CAF9", s=10, marker='o')
plt.plot(monthly_counts.index, monthly_counts.values)
plt.xlabel('Bulan')
plt.ylabel('Jumlah')
plt.title('Grafik Jumlah Penyewa Sepeda per Bulan dari 2011 - 2012', loc="center", fontsize=35)

st.pyplot(plt)

st.subheader("Jumlah Penyewa Sepeda berdasarkan Cuaca")
weather_usage = main_df_days.groupby(by="weather_condition").total_users.sum().reset_index()
weather_usage.rename(columns={"total_users": "total_users_count"}, inplace=True)
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3"]

plt.figure(figsize=(10, 5))
sns.barplot(
    x="weather_condition", 
    y="total_users_count", 
    data=weather_usage.sort_values(by="total_users_count", ascending=False),
    palette=colors
)

plt.title("Jumlah Penyewa Sepeda Terhadap Cuaca", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)

st.pyplot(plt)



# Season Analysis
# Season Analysis
st.subheader("Jumlah Penyewa Sepeda Terhadap Musim")
season_usage = days_df.groupby(by="season").total_users.sum().reset_index()
season_usage.rename(columns={"total_users": "total_users_count"}, inplace=True)
season_usage_sorted = season_usage.sort_values(by="total_users_count", ascending=False)
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

plt.figure(figsize=(10, 5))

sns.barplot(
    x="season", 
    y="total_users_count", 
    data=season_usage_sorted,
    palette=colors,
    order=season_usage_sorted['season']
)

plt.title("Jumlah Penyewa Sepeda Terhadap Musim", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)

st.pyplot(plt)  # Menggunakan st.pyplot untuk menampilkan plot di Streamlit

# Comparison of User Types
# Comparison of User Types
st.subheader("Jumlah Penyewa Sepeda Casual dan Registered Terhadap Musim")
season_usage = days_df.groupby(by="season")[['casual_users', 'registered_users']].sum().reset_index()
season_usage.rename(columns={"casual_users": "casual_users_count", "registered_users": "registered_users_count"}, inplace=True)
casual_sorted = season_usage.sort_values(by="casual_users_count", ascending=False)
registered_sorted = season_usage.sort_values(by="registered_users_count", ascending=False)
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

fig, ax = plt.subplots(1, 2, figsize=(15, 6))

sns.barplot(
    x="season", 
    y="casual_users_count", 
    data=season_usage,
    palette=colors,
    order=casual_sorted['season'],
    ax=ax[0]
)
ax[0].set_title("Jumlah Casual Users Terhadap Musim", loc="center", fontsize=28)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(axis='x', labelsize=12)

sns.barplot(
    x="season", 
    y="registered_users_count", 
    data=season_usage,
    palette=colors,
    order=registered_sorted['season'],
    ax=ax[1]
)
ax[1].set_title("Jumlah Registered Users Terhadap Musim", loc="center", fontsize=28)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].tick_params(axis='x', labelsize=12)

plt.tight_layout()
st.pyplot(fig)  # Menggunakan st.pyplot untuk menampilkan plot di Streamlit

# Comparison of Weekend and Weekday Users
st.subheader("Jumlah Penyewa Sepeda Saat Weekend dan Weekday")
category_usage = days_df.groupby(by="category_days")['total_users'].sum().reset_index()
category_usage.rename(columns={"total_users": "total_users_count"}, inplace=True)

plt.figure(figsize=(10, 6))

colors = ["#72BCD4", "#D3D3D3"]

sns.barplot(x="category_days", y="total_users_count", data=category_usage.sort_values(by="total_users_count", ascending=False), palette=colors)

plt.title("Jumlah Penyewa Sepeda Terhadap Category Days", loc="center", fontsize=18)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)

st.pyplot(plt)  # Menggunakan st.pyplot untuk menampilkan plot di Streamlit