import pandas as pd

file_path = r"C:\Users\hijir\Documents\DE6\dibimbing-belajar-github\username.csv"
# Alternatively: file_path = "C:/Users/hijir/Documents/DE6/dibimbing-belajar-github/username.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Print the first few rows of the dataframe
print(df.head())

# Menampilkan informasi ringkas tentang DataFrame
df.info()