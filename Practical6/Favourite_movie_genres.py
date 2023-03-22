# import matplotlib
# make a dictionary of favourite movie genres by {}
# make the pie chart  by plt.pie and data is x = value of dictionary and labels = key of dictionary
# print dictionary and a specific input (choose 'comedy here')
import matplotlib.pyplot as plt

Dic = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18,
       'Documentary': 12, 'History': 8, 'War': 7}
plt.pie(x=Dic.values(),
        labels=Dic.keys(),
        autopct='%.1f%%')
plt.show()
print(Dic)
print(Dic['Comedy'])  # input key 'Comedy' and print the output :the value of people like comedy best
