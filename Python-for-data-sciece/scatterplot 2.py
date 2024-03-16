import pandas as pd
import matplotlib.pyplot as plt

# Load both datasets
data1 = pd.read_csv('/Users/joshuasingrew/Desktop/Data scince project /dataset_1.csv')
data2 = pd.read_csv('/Users/joshuasingrew/Desktop/Data scince project /dataset_2.csv')

merged_data = pd.concat([data1, data2])
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['Student age'], merged_data['Average hours spent studying on campus'])
plt.title('Relationship between Age and Time Spent on Campus')
plt.xlabel('Student age')
plt.ylabel('Average hours spent studying on campus')
plt.grid(True)
plt.show()
