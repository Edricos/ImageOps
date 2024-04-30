import matplotlib.pyplot as plt
import numpy as np



# Generate the same data sets with log-normal distribution for distinct peaks
data1 = np.random.lognormal(mean=1.6, sigma=0.9, size=10000)
data2 = np.random.lognormal(mean=3.9, sigma=0.3, size=15000)
data3 = np.random.lognormal(mean=4.5, sigma=0.18, size=12000)


# Define bins along a log space
bins = np.linspace(0,
                   120, 20)

# Plotting the histogram with a linear scale on the y-axis
# Set alpha to less than 1 for transparency
plt.hist(data1, bins=bins, alpha=0.5, label='Depth prior 1', color='red')
plt.hist(data2, bins=bins, alpha=0.5, label='Depth prior 2', color='green')
plt.hist(data3, bins=bins, alpha=0.5, label='Depth prior 3', color='blue')

plt.xscale('linear')
plt.yscale('linear')  # Change to linear scale

# Set axis labels and legend
plt.xlabel('Distans')
plt.ylabel('Frequency')
plt.legend()

# Save and show the plot
plt_path = 'histogram_linear_scale_transparent.png'
plt.savefig(plt_path)
plt.show()
