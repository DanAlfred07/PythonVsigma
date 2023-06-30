import pandas as pd
import numpy as np

# Creating a DataFrame from a dictionary
data = {'SNO':[1,2,3],'Name': ['John', 'Emma', 'David'],
        'Age': [28, 32, 45],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

print(df)

# Create a Series from a list
s = pd.Series([1, 3, 5, 6, 8])
print(s)

# Create a DataFrame from a dictionary
data = {'Name': ['John', 'Emma', 'Tom'],
        'Age': [25, 28, 31],
        'City': ['New York', 'San Francisco', 'London']}
df = pd.DataFrame(data)
print(df)

# View the first 5 rows
print(df.head())

# View the last 3 rows
print(df.tail(3))

# Access the 'Name' column
print(df['Name'])

# Filter rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]
print(filtered_df)

# Add a new column 'Salary'
df['Salary'] = [50000, 60000, 70000]
print(df)

# Summary statistics
print(df.describe())

# Select a single column
print(df['Name'])

# Select multiple columns
print(df[['Name', 'Age']])

# Select a single row by index label
print(df.loc[0])

# Select multiple rows by index label range
print(df.loc[1:3])

# Select a single row by index position
print(df.iloc[0])

# Select multiple rows by index position range
print(df.iloc[1:3])

# Select rows where Age is greater than 25
print(df[df['Age'] > 25])

# Select rows where City is 'New York' and Age is greater than 25
print(df[(df['City'] == 'New York') & (df['Age'] > 25)])

# Check for missing values
print(df.isnull())

# Check for non-missing values
print(df.notnull())

# Drop rows with missing values
df.dropna()

# Drop columns with missing values
df.dropna(axis=1)

# Fill missing values with a specific value
df.fillna(0)


# Interpolate missing values using linear interpolation
df.interpolate()

# Group data by 'City' column and calculate the mean age
grouped_data = df.groupby('City')['Age'].mean()
print(grouped_data)

# Calculate the sum of salaries for each city
sum_salary = df.groupby('City')['Salary'].sum()
print(sum_salary)

# Apply custom aggregation functions
def custom_agg(x):
    return x.max() - x.min()

custom_result = df.groupby('City')['Age'].agg(custom_agg)
print(custom_result)

# Reshaping with pivot()
data = {'Name': ['John', 'Emma', 'Mike'],
        'Subject': ['Math', 'English', 'Science'],
        'Score': [85, 92, 78]}
df = pd.DataFrame(data)

df_pivot = df.pivot(index='Name', columns='Subject', values='Score')
print(df_pivot)

# Creating a pivot table with pivot_table()
df_pivot_table = df.pivot_table(index='Name', columns='Subject', values='Score', aggfunc='mean')
print(df_pivot_table)

# Unstacking with stack() and unstack()
df_stacked = df_pivot.stack()
print(df_stacked)

df_unstacked = df_stacked.unstack()
print(df_unstacked)

# Creating a DataFrame with DateTimeIndex
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales': [100, 150, 200, 175, 300, 250, 400, 375, 200, 150]}
df = pd.DataFrame(data, index=date_range)
print(df)

# Resampling to monthly frequency
df_monthly = df.resample('M').sum()
print(df_monthly)

# Shifting the data by 1 day
df_shifted = df.shift(1)
print(df_shifted)

# Rolling window calculation (moving average)
rolling_mean = df['Sales'].rolling(window=3).mean()
print(rolling_mean)

# Converting a column to categorical
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A']}
df = pd.DataFrame(data)

df['Category'] = df['Category'].astype('category')
print(df['Category'])

# Counting categorical values
value_counts = df['Category'].value_counts()
print(value_counts)

# Renaming and reordering categories
df['Category'] = df['Category'].cat.rename_categories({'A': 'High', 'B': 'Medium', 'C': 'Low'})
df['Category'] = df['Category'].cat.reorder_categories(['Low', 'Medium', 'High'], ordered=True)
print(df['Category'])


# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Mike', 'Emily', 'Daniel'],
        'Subject': ['Math', 'English', 'Math', 'Science', 'Science'],
        'Score': [85, 92, 78, 90, 88]}
df = pd.DataFrame(data)

# Group by 'Subject' and calculate the average score
group_by_subject = df.groupby('Subject')
avg_score = group_by_subject['Score'].mean()
print(avg_score)


# Create a DataFrame with DateTimeIndex
date_range = pd.date_range(start='2023-01-01', periods=5, freq='D')
data = {'Sales': [100, 150, 200, 175, 300]}
df = pd.DataFrame(data, index=date_range)

# Resample to monthly frequency
monthly_sales = df.resample('M').sum()
print(monthly_sales)


# Create two DataFrames
data1 = {'Name': ['John', 'Emma', 'Mike'],
         'Age': [25, 30, 28]}
df1 = pd.DataFrame(data1)

data2 = {'Name': ['Emma', 'Mike', 'Daniel'],
         'Salary': [5000, 6000, 7000]}
df2 = pd.DataFrame(data2)

# Inner join on 'Name'
merged_df = pd.merge(df1, df2, on='Name', how='inner')
print(merged_df)

# Create a DataFrame with missing values
data = {'Name': ['John', 'Emma', np.nan, 'Daniel'],
        'Age': [25, np.nan, 28, 32]}
df = pd.DataFrame(data)

# Drop rows with missing values
df_dropped = df.dropna()
print(df_dropped)

# Fill missing values with a specific value
df_filled = df.fillna('Unknown')
print(df_filled)

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Mike'],
        'Age': [25, 30, 28]}
df = pd.DataFrame(data)

# Select rows where age is greater than 28
selected_rows = df[df['Age'] > 28]
print(selected_rows)

# Create a DataFrame with MultiIndex
data = {'Subject': ['Math', 'Math', 'Science', 'Science'],
        'Name': ['John', 'Emma', 'John', 'Emma'],
        'Score': [85, 92, 78, 88]}
df = pd.DataFrame(data)

# Set MultiIndex on Subject and Name columns
df.set_index(['Subject', 'Name'], inplace=True)
print(df)

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Mike'],
        'Subject': ['Math', 'English', 'Science'],
        'Score': [85, 92, 78]}
df = pd.DataFrame(data)

# Pivot the DataFrame
pivot_df = df.pivot(index='Name', columns='Subject', values='Score')
print(pivot_df)

# Create a DataFrame with DateTimeIndex
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales': [100, 150, 200, 175, 300, 250, 400, 375, 200, 150]}
df = pd.DataFrame(data, index=date_range)

# Resample to monthly frequency and calculate the sum
monthly_sales = df.resample('M').sum()
print(monthly_sales)

# Create a DataFrame with missing values
data = {'Name': ['John', 'Emma', np.nan, 'Daniel'],
        'Age': [25, np.nan, 28, 32]}
df = pd.DataFrame(data)

# Fill missing values with the mean age
mean_age = df['Age'].mean()
df_filled = df.fillna(mean_age)
print(df_filled)

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Mike', 'John'],
        'Subject': ['Math', 'English', 'Science', 'Math'],
        'Score': [85, 92, 78, 90]}
df = pd.DataFrame(data)

# Group by Name and calculate the mean score
group_means = df.groupby('Name')['Score'].mean()
print(group_means)

# Create two DataFrames
df1 = pd.DataFrame({'Name': ['John', 'Emma'],
                    'Age': [25, 30]})
df2 = pd.DataFrame({'Name': ['Mike', 'Daniel'],
                    'Age': [28, 32]})

# Merge the DataFrames based on the Name column
merged_df = pd.merge(df1, df2, on='Name')
print(merged_df)

# Create a DataFrame with a categorical column
data = {'Name': ['John', 'Emma', 'Mike'],
        'Grade': ['A', 'B', 'A']}
df = pd.DataFrame(data)

# Convert the Grade column to categorical
df['Grade'] = pd.Categorical(df['Grade'], categories=['A', 'B', 'C'], ordered=True)
print(df['Grade'])

# Create a DataFrame with a text column
data = {'Name': ['John Smith', 'Emma Johnson', 'Mike Davis']}
df = pd.DataFrame(data)

# Extract first names
df['First Name'] = df['Name'].str.split().str[0]
print(df)

# Create a DataFrame
data = {'Scores': [85, 92, 78, 90, 250]}
df = pd.DataFrame(data)

# Calculate Tukey's fences
q1 = df['Scores'].quantile(0.25)
q3 = df['Scores'].quantile(0.75)
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

# Identify outliers
outliers = df[(df['Scores'] < lower_fence) | (df['Scores'] > upper_fence)]
print(outliers)

# Create a DataFrame
data = {'Scores': [85, 92, 78, 90, 250]}
df = pd.DataFrame(data)

# Calculate Tukey's fences
q1 = df['Scores'].quantile(0.25)
q3 = df['Scores'].quantile(0.75)
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

# Identify outliers
outliers = df[(df['Scores'] < lower_fence) | (df['Scores'] > upper_fence)]
print(outliers)

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3],
                    'B': ['a', 'b', 'c']})
df2 = pd.DataFrame({'A': [4, 5, 6],
                    'B': ['d', 'e', 'f']})

# Concatenate the DataFrames vertically
result = pd.concat([df1, df2], ignore_index=True)
print(result)

# Create a DataFrame with duplicate rows
data = {'A': [1, 2, 3, 2],
        'B': ['a', 'b', 'c', 'b']}
df = pd.DataFrame(data)

# Remove duplicate rows
df_unique = df.drop_duplicates()
print(df_unique)

# Create a DataFrame
data = {'ID': [1, 2, 3],
        'Math': [85, 92, 78],
        'Science': [90, 88, 95]}
df = pd.DataFrame(data)

# Melt the DataFrame
df_melted = pd.melt(df, id_vars='ID', var_name='Subject', value_name='Score')
print(df_melted)

# Create a DataFrame with a categorical column
data = {'Category': ['A', 'B', 'A', 'C']}
df = pd.DataFrame(data)

# Convert the Category column to categorical
df['Category'] = pd.Categorical(df['Category'], categories=['A', 'B', 'C'], ordered=True)
print(df['Category'])

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Mike', 'John'],
        'Subject': ['Math', 'English', 'Science', 'Math'],
        'Score': [85, 92, 78, 90]}
df = pd.DataFrame(data)

# Group by Name and calculate multiple aggregate statistics
group_stats = df.groupby('Name')['Score'].agg(['mean', 'min', 'max'])
print(group_stats) 