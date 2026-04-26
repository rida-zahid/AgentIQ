import json
import pandas as pd

# Load JSON
with open('data/News_Category_Dataset_v3.json', 'r') as f:
    data = [json.loads(line) for line in f]

# Convert to DataFrame
df = pd.DataFrame(data)

# Keep only useful columns
df = df[['headline', 'category', 'short_description']]

# Remove empty rows
df = df.dropna()

# Take 2000 rows
df = df.head(2000)

# Save as CSV
df.to_csv('data/news_2000.csv', index=False)

print("Done! Shape:", df.shape)
print(df.head(3))