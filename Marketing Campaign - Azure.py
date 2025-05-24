# Importing necessary libraries
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pyodbc as odbc
from credential import username, password, server, database    # Assuming credential.py contains your database credentials
# Load environment variables from .env file
load_dotenv('/Users/varrue/.cache/kagglehub/datasets/rodsaldanha/Marketing-campaign/versions/8/azure.env')
# Updated for GitHub push test

# --------------------------------------EXTRACT the dataset from CSV------------------------------------
# Read the CSV file
df = pd.read_csv('/Users/varrue/.cache/kagglehub/datasets/rodsaldanha/Marketing-campaign/versions/8/marketing_campaign.csv', delimiter=';')

# ---------------------------------------TRANSFORM the dataset------------------------------------

# Converts 'Dt_Customer' to datetime
# Calculates the age of the customer
from datetime import datetime
df['Age'] = datetime.now().year - df['Year_Birth']


# Creates age groups
# Note: Customers younger than 18 are excluded from the age groups.
df['Age_Group'] = pd.cut(df['Age'], bins=[18, 30, 45, 60, 100], labels=['18-30', '31-45', '46-60', '61+'])


# Creates a new total spend column - Sum of all spend columns
spend_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
df['Total_Spend'] = df[spend_columns].sum(axis=1)

# Creates Campaign response column - total sum of all response columns
campaign_columns = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']
df['Campaign_Response_Total'] = df[campaign_columns].sum(axis=1)

# Creates an Engagement score (based on interaction channels)
interaction_columns = ['NumWebVisitsMonth', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebPurchases']
df['Engagement_Score'] = df[interaction_columns].sum(axis=1)

# Renames the following columns for clarity and easy interpretation
df.rename(columns={
    'ID': 'Customer_ID',
    'Year_Birth': 'Birth_Year',
    'Income': 'Annual_Income',
    'Kidhome': 'Kids_at_Home',
    'Teenhome': 'Teens_at_Home',
    'Dt_Customer': 'Customer_Since',
    'Recency': 'Days_Since_Last_Purchase',
    'MntWines': 'Wine_Spend',
    'MntFruits': 'Fruit_Spend',
    'MntMeatProducts': 'Meat_Spend',
    'MntFishProducts': 'Fish_Spend',
    'MntSweetProducts': 'Sweet_Spend',
    'MntGoldProds': 'Gold_Spend',
    'NumDealsPurchases': 'Deals_Purchased',
    'NumWebPurchases': 'Web_Purchases',
    'NumCatalogPurchases': 'Catalog_Purchases',
    'NumStorePurchases': 'Store_Purchases',
    'NumWebVisitsMonth': 'Monthly_Web_Visits',
    'AcceptedCmp1': 'Campaign_1_Responded',
    'AcceptedCmp2': 'Campaign_2_Responded',
    'AcceptedCmp3': 'Campaign_3_Responded', 
    'AcceptedCmp4': 'Campaign_4_Responded',
    'AcceptedCmp5': 'Campaign_5_Responded',
    'Response': 'Last_Campaign_Response',
    'Complain': 'Customer_Complaint'
}, inplace=True)

# ---------------------------------------LOAD the dataset into Azure SQL DB------------------------------------
# Create a connection to the Azure SQL Database
server = 'marketing-server-1.database.windows.net'
database = 'marketing_campaign'
driver = '{ODBC Driver 18 for SQL Server}'
connection_string= (
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server={server},1433;"
    f"Database={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=60;"
)


print(f"Connecting to server: {server}, database: {database}")

try:
    conn = odbc.connect(connection_string)
    print("Connection successful!")

        # Define the SQLAlchemy engine for loading data
    engine_connection_string = (
        f"mssql+pyodbc://{username}:{password}@{server}:1433/{database}"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&Encrypt=yes"
        "&TrustServerCertificate=no"
        "&Connection+Timeout=60"
    )
    engine = create_engine(engine_connection_string)

    # Load data to the Azure SQL Database
    print("Loading data into Azure SQL Database...")
    df.to_sql(name='marketing_campaign', con=engine, if_exists='replace', index=False, chunksize=1000)
    print("Data successfully loaded into Azure SQL Database!")

except Exception as e:
    print("Connection failed or data load failed:")
    print(e)


# Load data to CSV saved locally
# Defines the directory for saving the file
output_directory = '/Users/varrue/Documents/Marketing Campaign Project' 
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist

# Save the file in the specified directory
output_file_path = os.path.join(output_directory, 'clean_marketing_data.csv')
df.to_csv(output_file_path, index=False)

# Print the absolute path of the saved file
print("File saved:", os.path.abspath(output_file_path))

print("ETL complete: Cleaned data loaded into Azure SQL table 'marketing_campaign'")
