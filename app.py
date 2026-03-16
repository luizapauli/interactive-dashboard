import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Salary Dashboard in the Data Field",
    page_icon=":bar_chart:",
    layout="wide",
)

df = pd.read_csv("https://raw.githubusercontent.com/luizapauli/interactive-dashboard/refs/heads/main/salaries_cleaned_eng.csv")

st.title("💲 Salary Analisys Dashboard in the Data Field")
st.markdown("Explore the salary data in the data field over the past years. Use the filters below to refine your analysis.")

col1, col2, col3, col4, col5, col6 = st.columns([1, 0.65, 1.2, 1.4, 1.6, 4], gap="xsmall", vertical_alignment="top")

with col1:
    # st.write("🔍 Filters")
    # st.title("# 🔍 Filters")
    st.markdown("#### 🔍 Filters")

with col2:
    f1 = st.popover("Year")
    with f1:
        available_years = sorted(df['Year'].unique())
        selected_years = st.multiselect("Select Year(s):", options=available_years, default=available_years)

with col3:
    f1 = st.popover("Seniority Level")
    with f1:
        available_seriorities = sorted(df['Seniority'].unique())
        selected_seriorities = st.multiselect("Select Seniority Level(s):", options=available_seriorities, default=available_seriorities)

with col4:
    f1 = st.popover("Employment Type")
    with f1:
        available_contracts = sorted(df['Contract'].unique())
        selected_contracts = st.multiselect("Select Employment Type(s):", options=available_contracts, default=available_contracts)

with col5:
    f1 = st.popover("Size of the Company")
    with f1:
        available_sizes = sorted(df['Size_Enterprise'].unique())
        selected_sizes = st.multiselect("Select Size of the Company(s):", options=available_sizes, default=available_sizes)

df_filtered = df[
    (df['Year'].isin(selected_years)) &
    (df['Seniority'].isin(selected_seriorities)) &
    (df['Contract'].isin(selected_contracts)) &
    (df['Size_Enterprise'].isin(selected_sizes))
]

st.subheader("📊 Overall Metrics")

if not df_filtered.empty:
    avg_salary = df_filtered['USD'].mean()
    max_salary = df_filtered['USD'].max()
    total_entries = df_filtered.shape[0]
    most_common_role = df_filtered['Role'].mode()[0]
else:
    avg_salary, max_salary, total_entries, most_common_role = 0,0,0,"N/A"

col1, col2, col3, col4 = st.columns(4, gap="small")
col1.metric("Average Salary", f"${avg_salary:,.2f}")
col2.metric("Max Salary", f"${max_salary:,.2f}")
col3.metric("Total Entries", f"{total_entries}")
col4.metric("Most Common Role", most_common_role)

st.markdown("---")

col_graph1, col_graph2 = st.columns(2, gap="medium")

with col_graph1:
    if not df_filtered.empty:
        top_roles = df_filtered.groupby('Role')['USD'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        graph_roles = px.bar(
            top_roles,
            x = 'USD',
            y = 'Role',
            orientation='h',
            title="Top 10 Roles by Average Salary",
            labels={"USD": "Annual Average Salary (USD)", "Role": "Job Role"},
            color_discrete_sequence=['#29B09D']
        )
        st.plotly_chart(graph_roles, use_container_width=True)
    else:
        st.info("No data available for the selected filters.")

with col_graph2:
    if not df_filtered.empty:
        salary_distribution = px.histogram(
            df_filtered,
            x='USD',
            nbins=30,
            title="Annual Salary Distribution",
            labels={"USD": "Annual Salary (USD)", 'count': ''},
            color_discrete_sequence=["#57CDBD"]
        )
        salary_distribution.update_layout(title_x=0.1)
        st.plotly_chart(salary_distribution, use_container_width=True)
    else:
        st.info("No data available for the selected filters.")

col_graph3, col_graph4 = st.columns(2, gap="medium")

with col_graph3:
    if not df_filtered.empty:
        remote_count = df_filtered['Remote'].value_counts().reset_index()
        remote_count.columns = ['index', 'Remote']
        graph_remote = px.pie(
            remote_count,
            names='index',
            values='Remote',
            title="Remote vs On-site Work Distribution",
            labels={"index": "Work Type", "Remote": "Count"},
            color_discrete_sequence=['#29B09D', "#2FB8BF", '#83C9FF']
        )
        graph_remote.update_traces(textposition='inside', textinfo='percent+label')
        graph_remote.update_layout(title_x=0.1)
        st.plotly_chart(graph_remote, use_container_width=True)
    else:
        st.info("No data available for the selected filters.")

with col_graph4:
    if not df_filtered.empty:
        df_ds = df_filtered[df_filtered['Role'] == 'Data Scientist']
        medium_ds_country = df_ds.groupby('Country_ISO3')['USD'].mean().reset_index()
        graph_countries = px.choropleth(
            medium_ds_country,
            locations= 'Country_ISO3',
            color= 'USD',
            color_continuous_scale= 'viridis',
            title="Average Salary for Data Scientists by Country",
            labels={"USD": "Average Salary (USD)", "Country_ISO3": "Country"}
        )
        graph_countries.update_layout(title_x=0.1)
        st.plotly_chart(graph_countries, use_container_width=True)
    else:
        st.info("No data available for the selected filters.")

st.divider()
    
st.subheader("Detailed Data View")
st.dataframe(df_filtered)