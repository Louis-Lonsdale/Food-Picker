
from imports.TextReader import fileReader
from imports.weeklyMaker import weeklyPlanner


fileLocation = "/home/louislonsdale/Projects/foodapp/Food-Picker/list.txt"
x = fileReader()
list = x.getList(fileLocation)
y = weeklyPlanner()
finalList = y.makeWeeklyPlan(x)

for i in finalList:
    print(finalList[i])

