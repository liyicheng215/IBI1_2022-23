# import matplotlib
# make a list of olympic costs by []
# make a list of country and year
# print sorted list of costs
# make bar plot by plt.bar using list name and costs
# adjust the rotation and font size

import matplotlib.pyplot as plt
costs = [1, 8, 15, 7, 5, 14, 43, 40]
name = ['Los Angeles 1984', 'Seoul1988', 'Barcelona 1992', 'Atlanta 1996',
        'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012']
print(sorted(costs))
plt.bar(name, costs)
plt.xticks(rotation=20, fontsize=8)
plt.show()
