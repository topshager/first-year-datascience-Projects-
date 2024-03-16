import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Function to generate random marks within the given range
def generate_marks():
    return np.random.randint(78, 131, size=150)  # Generating marks from 60% to 100% of 130

# Function to generate random time taken on examination
def generate_exam_time():
    return np.random.randint(60, 181, size=150)  # Generating time from 60 to 180 minutes

# Generate student numbers and ages
student_numbers = range(10001, 10151)
student_age = np.random.randint(18, 61, size=150)  # Generating ages between 18 and 60

# Generate Average hours spent studying on campus for both datasets
average_hours = np.random.choice([1, 2, 3, 4, 5], size=150)

# Dataset 1
dataset_1 = pd.DataFrame({
    'Student number': student_numbers,
    'Student age': student_age,
    'Average hours spent studying on campus': average_hours,
    'Student mark achieved': generate_marks(),
    'Time taken on examination (minutes)': generate_exam_time()
})

# Dataset 2
dataset_2 = pd.DataFrame({
    'Student number': student_numbers,
    'Student age': student_age,
    'Average hours spent studying on campus': average_hours,
    'Student mark achieved': generate_marks(),
    'Time taken on examination (minutes)': generate_exam_time()
})

# Saving datasets to CSV files
dataset_1.to_csv('dataset_1.csv', index=False)
dataset_2.to_csv('dataset_2.csv', index=False)
