import pandas as pd

#loading dataset
data = pd.read_csv('/Users/joshuasingrew/Desktop/Data scince project /dataset_1.csv')

average_Hours = {}
average_hours_frequecy = data['Average hours spent studying on campus'].value_counts().sort_index()

i = 0  # Initialize index for iterating over frequency counts
for count in average_hours_frequecy:
    if i == 0:
        average_Hours['1-2'] = count
    elif i == 1:
        average_Hours['2-3'] =  count + count
        average_Hours['2-3'] =  count + count
    elif i == 3:
        average_Hours['2-3'] =  count + count
    elif i == 4:
        average_Hours['4-5'] = count + count
    elif i == 5:
        average_Hours['4-5'] =  count + count
        
    i += 1  # Increment index for the next iteration

print("\nFrequency Table for Average Hours Spent Studying on Campus:")
for key, value in average_Hours.items():
    print("------------------","\n|"+f"{key}" +"      |   "+ f"{value}"+" |","\n------------------")

        
#18 – 25, 25 – 35, 35 – 45, over 45 
print("\n")

age_groups = {'18-25': 0, '25-35': 0, '35-45': 0, 'over 45': 0}
age_frequencies = data['Student age'].value_counts().sort_index()

# Iterate over the ages and update the counts in the appropriate categories
for age, count in age_frequencies.items():
    if age >= 18 and age < 25:
        age_groups['18-25'] += count
    elif age >= 25 and age < 35:
        age_groups['25-35'] += count
    elif age >= 35 and age < 45:
        age_groups['35-45'] += count
    else:
        age_groups['over 45'] += count
print("------------------"+"\n"+"Student age")
# Display the counts for each age group
for group, count in age_groups.items():
    print("------------------","\n|"+f"{group}: {count}","\n"+"------------------")



# Define logical groupings for time taken on examination (minutes)
groupings = {
    '0-60': 0,
    '61-120': 0,
    '121-180': 0
}

# Iterate over the data and count occurrences in each grouping
for time in data['Time taken on examination (minutes)']:
    if time <= 60:
        groupings['0-60'] += 1
    elif 61 <= time <= 120:
        groupings['61-120'] += 1
    else:
        groupings['121-180'] += 1

# Display the frequency table
print("Frequency Table for Time taken on examination (minutes):")
for group, count in groupings.items():
    print("------------------"+"\n",f"{group}    :   {count}")

