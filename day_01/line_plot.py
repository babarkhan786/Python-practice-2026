# Line Plot Example in Python
# Matplotlib is the most common library for making plots

import matplotlib.pyplot as plt

# Example data: x and y values
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 1, 5, 3, 6]

# Create the line plot
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='My Data')

# Add labels and title
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Simple Line Plot')
plt.legend()  # Shows the label

# Add a grid (optional)
plt.grid(True)

# Display the plot
plt.show()

# To save the plot to a file instead of showing it:
# plt.savefig('line_plot.png')
# plt.close()
