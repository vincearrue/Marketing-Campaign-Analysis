# Marketing-Campaign-Analysis
Analysis of marketing campaign effectiveness and customer segmentation

## Overview
This project explores the effectiveness of multiple marketing campaigns through data analysis, using Python for data cleaning and preprocessing, Azure SQL Database for querying and storing the data, and Tableau for data visualization. The goal is to understand the performance of marketing campaigns, segment customers based on their demographics and engagement, and identify actionable insights to optimize future campaigns.

## Tools
**Python:**

Data cleaning and preprocessing using libraries like pandas.

Feature engineering, such as calculating customer age and segmenting based on demographics.

**Azure SQL Database:**

Cloud-based database for storing, querying, and managing large datasets.

Used to store the cleaned and processed marketing data for further analysis.

**Azure Data Studio:**

A cross-platform tool to query Azure SQL Database.

Used for advanced data exploration and analysis before importing the data into Tableau.

**Tableau:**
Data visualization tool used for creating dashboards that display campaign performance, customer segmentation, and funnel conversion rates.

**Git:**

Version control for tracking changes, collaboration, and maintaining project history.



## How to Run
**Prerequisites**
Before running the project, make sure you have the following installed:
**Python (version 3.x)**

**Azure SQL Database (for storing and querying data)**

**Azure Data Studio (for querying the database)**

**Tableau (for data visualization)**

1. Clone the repository, save the raw marketing_campaign.csv file and update the file paths in the code
   
   git clone https://github.com/vincearrue/Marketing-Campaign-Analysis.git
    cd Marketing-Campaign-Analysis
   
3. Set Up Python Environment
   
     python -m venv venv
   
5. Activate the virtual environment:

    On macOS/Linux:
    source venv/bin/activate

    On Windows:
    .\venv\Scripts\activate
   
6. Install the required dependencies by running the following command:

    pip install -r requirements.txt
   
7. Run the Python Script for Data Preprocessing
   
The Python script Marketing Campaign - Azure.py cleans and preprocesses the raw marketing campaign data. Run the following command to execute it:

    python Marketing_Campaign_Azure.py

This will generate the cleaned dataset and save it as cleaned_campaign_data.csv.


6. Import the cleaned data into Tableau for further analysis and visualization.

## Files
- `Marketing Campaign - Azure.py`: Python script for data preprocessing.
- `cleaned_campaign_data.csv`: Cleaned and processed campaign data.
- 'marketing_campaign.csv': Raw Data file
- Screenshots of Tableau dashboards showcasing the analysis.

**  NOTE: Your IP will need to be whitelisted on the Azure SQL Server to successfully connect to the database.**
