from matplotlib import pyplot as plt

languages = 'Python', 'Java', 'Go', "Ruby"
score = [35, 30, 25, 10]
explode = (0.1, 0, 0, 0) #this will explode the 1st slice

fig1, ax1 = plt.subplots()

ax1.pie(Score, explode=explode, labels=languages, autopct = '%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') #this ensures that the chart is drawn as a circle

plt.show()