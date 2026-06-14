
"""
Created on Sun Jun 14 21:20:35 2026

@author: DISHA
"""

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 140, 180, 170]

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()




students = ["A", "B", "B", "C", "D"]
marks = [80, 65, 90, 75, 85]

plt.bar(students, marks)
plt.title("Student Marks")
plt.show()




ages = [22, 23, 24, 25, 26, 28, 29, 30, 31]

plt.hist(ages, bins=5)
plt.title("Age Distribution")
plt.show()


hours = [2, 3, 4, 5, 6, 7]
marks = [40, 50, 55, 70, 76, 90]

plt.scatter(hours, marks)
plt.xlabel("Study hours")
plt.ylabel("Marks")
plt.show()


companies = ["A", "B", "C"]
share = [40, 35, 25]

plt.pie(share, labels=companies, autopct="%1.1f%%")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.histplot(tips["total_bill"], kde=True)
plt.show()





