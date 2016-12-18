import matplotlib.pyplot as plt

#input_values = [0, 1, 2, 3, 4, 5]
#squares = [0, 1, 4, 9, 16, 25]



input_values =[i for i in range(0,100)]
squares = [i*i for i in range(0,100)]


plt.plot(input_values, squares, linewidth=5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.show()
