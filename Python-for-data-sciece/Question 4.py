
import csv
import numpy as np
import matplotlib.pyplot as plt

# 4.1
# a. Read the percent-bachelors-degrees-women-usa.csv file as a list of lists.
with open("/Users/joshuasingrew/Library/Mobile Documents/com~apple~CloudDocs/data science /percent-bachelors-degrees-women-usa.csv", "r") as file:
    BDW = list(csv.reader(file))

# b. Assign the result to the variable BDW.
# (Already done in part a)

# c. Display the first five rows of BDW separately on different lines.
for i in range(5):
    print(BDW[i])

# d. Remove the header row (column names) of the dataset and assign the rest of the dataset to BDW1.
BDW1 = BDW[1:]

# e. Using slicing, display the first, second, and third row of BDW1.
print(BDW1[0])
print(BDW1[1])
print(BDW1[2])

# 4.2
# a. Create a dictionary called "Indexcount_year".
Indexcount_year = {}
for row in BDW1:
    year = int(row[0])
    Indexcount_year[year] = Indexcount_year.get(year, 0) + 1

# b. Create a dictionary called "Indexpercent_year".
Indexpercent_year = {}
for i, row in enumerate(BDW1):
    year = int(row[0])
    Indexpercent_year[year] = i

# 4.3
# a. Read the percentages of women who earned a degree per year in the following majors.
Maths_Stats = [float(row[3]) for row in BDW1]
Physic_Sc = [float(row[9]) for row in BDW1]
Engine = [float(row[15]) for row in BDW1]
Computer_Sci = [float(row[18]) for row in BDW1]

# Extracting the years
Year = [int(row[0]) for row in BDW1]

# 4.4
# a. Create a Numpy array called "Selected4Majors".
Selected4Majors = np.array([Maths_Stats, Physic_Sc, Engine, Computer_Sci], dtype=float)

# b. Create a dictionary called "Majors".
Majors = {"Maths_Stats": 0, "Physic_Sc": 1, "Engine": 2, "Computer_Sci": 3}

# 4.5
# Write a Python function:
def plot_selected_degrees(data, majorlist):
    for major in majorlist:
        plt.plot(Year, Selected4Majors[Majors[major]], label=major)

    plt.legend(loc='upper left')
    plt.title("Percentage of Selected4Degrees Awarded per Year")
    plt.xlabel("Year")
    plt.ylabel("Selected4Degrees")
    plt.show()

# Example usage
plot_selected_degrees(Year, ["Maths_Stats", "Physic_Sc", "Engine", "Computer_Sci"])
