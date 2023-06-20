import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Define paths
script_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(script_dir, '..', 'data')
output_dir = os.path.join(script_dir, '..', 'output')

# Read dataset
data = pd.read_csv(os.path.join(data_dir, 'train.csv'))

# Sales trends overtime
data['Order Date'] = pd.to_datetime(data['Order Date'], dayfirst=True)
sales_over_time = data.groupby(data['Order Date'].dt.to_period("M"))['Sales'].sum()

plt.figure(figsize=(10, 5))
sales_over_time.plot(kind='line')
plt.title('Sales Over Time')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'sales_trends.png'))
plt.show()

#Sales by states/cities
sales_by_state = data.groupby('State')['Sales'].sum()

plt.figure(figsize=(10, 5))
sales_by_state.sort_values(ascending=False).plot(kind='bar')
plt.title('Sales by State')
plt.xlabel('State')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'sales_states.png'))
plt.show()


# Best-Selling Categories and Sub-Categories
sales_by_category = data.groupby('Category')['Sales'].sum()

plt.figure(figsize=(10, 5))
sales_by_category.sort_values(ascending=False).plot(kind='bar')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'bestselling_categories.png'))
plt.show()


# Seasonality in Sales
data['Month'] = data['Order Date'].dt.month
sales_by_month = data.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10, 5))
sales_by_month.plot(kind='line')
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'seasonality.png'))
plt.show()


# Customer Distribution Across Segments
customers_by_segment = data['Segment'].value_counts()

plt.figure(figsize=(10, 5))
customers_by_segment.plot(kind='pie', autopct='%1.1f%%')
plt.title('Customer Distribution by Segment')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'customer_distribution.png'))
plt.show()


