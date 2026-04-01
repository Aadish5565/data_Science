import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [10,15,25,30,50]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

students = ['John', 'Jane', 'Alice', 'Bob']
marks = [75, 85, 60, 90]

dec_COLORS = ['blue', 'orange', 'green', 'red']

plt.bar(students, marks, color=dec_COLORS)
plt.title("Student Marks")
plt.show()

regions = ['North America', 'Europe', 'Asia', 'Others']
revenue = [45, 25, 20, 10]

plt.pie(revenue, labels=regions, autopct='%1.1f%%', colors=dec_COLORS)
plt.title("Revenue Distribution")
plt.show()

hist_data = np.random.randint(1, 100, size=100)
plt.hist(hist_data, bins=10, color='purple', edgecolor='black')
plt.title("Histogram of Random Data")
plt.show()
