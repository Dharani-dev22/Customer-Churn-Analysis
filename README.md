# Customer Churn Analysis: Identifying Drivers of Customer Attrition

📊 **[View the Interactive Tableau Dashboard Here](https://public.tableau.com/app/profile/pondharani.devendra/viz/CustomerChurnAnalysis_17825715777880/Dashboard1?publish=yes)**

![Tableau Dashboard Screenshot](dashboard_screenshot.png)

## 📝 Project Overview
Customer churn is one of the most critical metrics for subscription-based businesses. The objective of this project was to analyze a dataset of customer profiles to determine the overall churn rate and identify the primary financial and behavioral drivers causing customers to cancel their service. 

This project demonstrates an end-to-end data analysis pipeline, starting from raw data ingestion and Python-based data cleaning (handling missing values via imputation), to developing a highly interactive, executive-ready dashboard in Tableau.

## 🛠️ Tools & Technologies Used
* **Python (Pandas):** Data manipulation, deduplication, and handling missing variables (Mean/Median imputation to prevent Data Leakage).
* **Tableau Public:** Data visualization, interactive dashboard design, dual-axis charts, and dashboard filtering.
* **CSV:** Data storage and transfer.

## 💡 Key Business Insights
Through the visual analysis, three major trends were identified:
1. **Overall Churn Rate:** The customer base is currently experiencing a 50% churn rate.
2. **The Price Impact:** Customers who churned were paying a higher average monthly bill (**$71.78**) compared to loyal customers who were retained (**$68.57**). This indicates potential "sticker shock" or price sensitivity among a specific cohort.
3. **The Drop-Off Window:** Retained customers display high loyalty, staying for an average of **15 months**. However, churned customers are canceling their service rapidly—leaving after an average of just **4.6 months**.

**Actionable Recommendation:** The data suggests that new customers are sensitive to the current pricing model within their first half-year. Introducing a 6-month discounted onboarding tier could help push at-risk customers past the critical 4.6-month drop-off window, converting them into long-term users.

## 📂 Repository Structure
* `raw_customer_data.csv`: The initial dataset containing missing values and unstructured data.
* `clean_data.py`: The Python script used to clean the data, standardize variables, and impute missing financial/tenure records.
* `cleaned_customer_data.csv`: The final, analysis-ready dataset powering the Tableau visualizations.

## 🚀 How to Run this Project
1. Clone the repository: `git clone https://github.com/Dharani-dev22/Customer-Churn-Analysis.git`
2. Run the cleaning script in your terminal: `python clean_data.py`
3. View the generated output or click the Tableau link above to interact with the final dashboard.

---

## 📬 Let's Connect
If you have any questions about this project or want to discuss data analytics, feel free to reach out!

* **LinkedIn:** [Pondharani Devendra](https://www.linkedin.com/in/pondharani-devendra-a809b339b/)
* **Email:** [pondharani.devendra22@gmail.com](mailto:pondharani.devendra22@gmail.com)
