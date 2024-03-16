import pandas as pd

# Load the dataset
data = pd.read_csv('/Users/joshuasingrew/Desktop/Data scince project /dataset_1.csv')

# Define study groupings
study_groups = {
    '1-2': data[(data['Average hours spent studying on campus'] >= 1) & (data['Average hours spent studying on campus'] <= 2)],
    '2-3': data[(data['Average hours spent studying on campus'] > 2) & (data['Average hours spent studying on campus'] <= 3)],
    '4-5': data[(data['Average hours spent studying on campus'] > 4) & (data['Average hours spent studying on campus'] <= 5)]
}

# Calculate the average mark achieved for each group
average_marks = {}
for group, df in study_groups.items():
    total_marks = df['Student mark achieved'].sum()
    count_students = df.shape[0]
    average_marks[group] = total_marks / count_students

# Print the average mark achieved for each study group
for group, average_mark in average_marks.items():
    print(f"Average mark achieved for {group} study group: {average_mark}")
