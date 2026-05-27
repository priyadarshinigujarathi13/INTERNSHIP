# import matplotlib
# import numpy
# import pandas
# import seaborn

# print("All Libraries Installed Successfully")
# =========================================
# 1. LINE CHART
# =========================================

import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

plt.plot(x, y)

plt.title("Line Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.show()

# =========================================
# 2. BAR CHART
# =========================================

import matplotlib.pyplot as plt

x = ['Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190]

plt.bar(x, y)

plt.title("Bar Chart")
plt.xlabel("Day")
plt.ylabel("Total Bill")

plt.show()

# =========================================
# 3. HISTOGRAM
# =========================================

import matplotlib.pyplot as plt

x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14,
     14, 15, 16, 16, 17, 18, 18, 19, 20,
     20, 21, 22, 23, 24, 25, 25, 26, 28,
     30, 32, 35, 36, 38, 40, 42, 44, 48, 50]

plt.hist(x, bins=10, color='steelblue')

plt.title("Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")

plt.show()

# =========================================
# 4. SCATTER PLOT
# =========================================

import matplotlib.pyplot as plt

x = [ 'Fri', 'Sat', 'Sun',
      'Fri', 'Sat', 'Sun']

y = [120, 250, 190,
     160, 130,200]

plt.scatter(x, y)

plt.title("Scatter Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")

plt.show()

# =========================================
# 5. PIE CHART
# =========================================

import matplotlib.pyplot as plt

cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR']

data = [23, 10, 35, 15, 12]

plt.pie(data, labels=cars)

plt.title("Pie Chart")

plt.show()

# =========================================
# 6. BOX PLOT
# =========================================

import matplotlib.pyplot as plt

data = [
    [10, 12, 14, 15, 18, 20, 22],
    [8, 9, 11, 13, 17, 19, 14,21],
    [14, 16, 18, 20, 23, 25, 27]
]

plt.boxplot(data)

plt.xlabel("Groups")
plt.ylabel("Values")
plt.title("Box Plot")

plt.show()

# =========================================
# 7. HEATMAP
# =========================================

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

data = np.random.rand(10, 10)

plt.imshow(data, cmap='viridis',
           interpolation='nearest')

plt.colorbar()

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title('Heatmap')

plt.show()
