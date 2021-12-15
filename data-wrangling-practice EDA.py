# Firstly, we import Numpy and pandas library and then read the dataset.
import numpy as np
import pandas as pd

df=pd.read_csv('Mobile_Food_Facility_Permit.csv')

# df.head( ): By default, it returns the first 5 rows of the Dataframe. To change the default, you may insert a value between the parenthesis to change the number of rows returned.
print(df.head())

# df.tail( ): By default, it returns the last 5 rows of the Dataframe. This function is used to get the last n rows. This function returns the last n rows from the object based on position.
print(df.tail())

# df.info( ): It helps in getting a quick overview of the dataset. This function is used to get a brief summary of the dataframe. This method prints information about a DataFrame including the index dtype and column dtypes, non-null values, and memory usage.
print(df.info())

# df.shape: It shows the number of dimensions as well as the size in each dimension. Since data frames are two-dimensional, what shape returns is the number of rows and columns.
# print(df.shape())

# df.size: Return an int representing the number of elements in this object. Return the number of rows if Series, otherwise returns the number of rows times the number of columns if DataFrame.
# print(df.size())

# df.ndim: Returns dimension of dataframe/series. 1 for one dimension (series), 2 for two dimensions (dataframe).
# print(df.ndim())

# df.describe( ): Return a statistical summary for numerical columns present in the dataset. This method calculates some statistical measures like percentile, mean and standard deviation of the numerical values of the Series or DataFrame.
print(df.describe())

# df.sample( ): Used to generate a sample randomly either row or column. It allows you to select values randomly from a Series or DataFrame. It is useful when we want to select a random sample from a distribution.
print(df.sample())

# df.isnull( ).sum( ): Return the number of missing values in each column.
print(df.isnull().sum())

# df.nunique( ): Return number of unique elements in the object. It counts the number of unique entries over columns or rows. It is very useful in categorical features especially in cases where we do not know the number of categories beforehand.
print(df.nunique())

# df.index: This function searches for a given element from the start of the list and returns the lowest index where the element appears.
print(df.index)

# df.columns: Return the column labels of the dataframe.
print(df.columns)

# df.memory_usage( ): Returns how much memory each column uses in bytes. It is useful especially when we work with large data frames.
print(df.memory_usage())

# df.dropna( ): This function is used to remove a row or a column from a dataframe that has a NaN or missing values in it.
print(df.dropna())

# df.nlargest( ): Returns the first n rows ordered by columns in descending order.
print(df.nlargest(20, 'locationid'))

# df.isna( ): This function returns a dataframe filled with boolean values with true indicating missing values.
print(df.isna())

# df.duplicated( ):  Returns a boolean Series denoting duplicate rows.
print(df.duplicated())

# value_counts( ): This function is used to get a Series containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently occurring element. It excludes missing values by default. This function comes in handy when we want to check the problem of class imbalance for a categorical variable.
print(df['Approved'].value_counts())

# df.corr( ): This function is used to find the pairwise correlation of all columns in the dataframe. Any missing values are automatically excluded. For any non-numeric data type columns in the dataframe, it is ignored. This function comes in handy while we doing the Feature Selection by observing the correlation between features and target variable or between variables.
print(df.corr())

# df.dtypes: This function shows the data type of each column.
print(df.dtypes)

print(df['locationid'].plot)
print(df['locationid'].plot.hist)