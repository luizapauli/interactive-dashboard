# 📊 Data Science Salaries Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

## 🔎 Project Overview
This project was developed during **Class 4** of the **Alura Data Immersion 2025**. The goal was to build an interactive web dashboard to analyze global salaries in the Data Science field.

Using **Streamlit**, this application allows users to explore salary trends based on seniority, company size, and contract type, providing visual insights into the data market.

## ✨ Features
* **Interactive Filters:** Popover filters for Year, Seniority Level, Contract Type, and Company Size.
* **Key Performance Indicators (KPIs):** Real-time calculation of Average Salary, Max Salary, and Most Frequent Job Title.
* **Visualizations:**
    * 📊 **Top 10 Jobs:** Bar chart showing the highest-paying roles.
    * 📈 **Salary Distribution:** Histogram of annual salaries (USD).
    * 🥧 **Work Models:** Pie chart comparing Remote vs. On-site roles.
    * 🌍 **Global Heatmap:** Choropleth map displaying Data Scientist salaries by country.

## 📂 Dataset
The dashboard consumes data directly from the following raw CSV file:
* **URL:** `https://raw.githubusercontent.com/luizapauli/interactive-dashboard/refs/heads/main/salaries_cleaned_eng.csv`
* **Columns:** 'Year', 'Seniority', 'Contract', 'Role', 'Salary', 'Coin', 'USD', 'Country', 'Remote', 'Enterprise', 'Size_Enterprise', 'Country_ISO3'

## 🛠️ Technologies
* **[Streamlit](https://streamlit.io/):** For building the web application interface.
* **[Pandas](https://pandas.pydata.org/):** For data manipulation and filtering.
* **[Plotly Express](https://plotly.com/python/plotly-express/):** For creating interactive charts.

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install the requirements:**
    ```bash
    pip install streamlit pandas plotly
    ```

3.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
    *(Note: Replace `app.py` with the filename you saved the code as).*

4.  **Access the Dashboard:**
    The app will open automatically in your browser at `http://localhost:8501`.

## 📝 Author
Developed by **Luiza Pauli** during the Alura Imersão Dados 2025.

---
*This project is for educational purposes.*
