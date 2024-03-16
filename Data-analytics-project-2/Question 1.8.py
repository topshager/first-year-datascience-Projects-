import pandas as pd
import matplotlib.pyplot as plt

# Read the data
data = pd.read_csv("#CSV location file path")

# Extract the columns data
rtn_2_day = data['Rtn..2.Day']
rtn_1_day_1 = data['Rtn..1.Day.1']

# Create the plot
plt.figure(figsize=(10, 6))

# Plot each column
plt.plot(data.index, rtn_2_day, label='Rtn..2.Day', color='blue')
plt.plot(data.index, rtn_1_day_1, label='Rtn..1.Day.1', color='orange')

# Set plot title and labels
plt.title('Share Values Over Time')
plt.xlabel('Record Index')
plt.ylabel('Value')
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
