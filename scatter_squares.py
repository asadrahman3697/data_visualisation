import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]


# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=25)
# plt.scatter(x_values, y_values, c=(0.5, 1,  0.8), edgecolor='none', s=25)

# Apply a colormap - changing colours with values, increasing in intesity
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma,
    edgecolor='none', s=40)

plt.axis([0, 1100, 0, 1100000])
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

plt.tick_params(axis='both', which='minor', labelsize=14)

plt.show()

# Save to file - trim whitespaces from the plot
plt.savefig('squares_plot.png', bbox_inches='tight')
