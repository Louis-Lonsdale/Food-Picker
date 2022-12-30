import random
class weeklyPlanner:

    def __init__(self, foodList = None):
        if foodList is None:
            foodList = []
        else:
            self.foodList = foodList

    def makeWeeklyPlan(self, foodList):
        i = 0
        finalList = []
        while i <= 6:
            x = random.randint(0, len(foodList))
            finalList.append(foodList[x])
            foodList.remove[x]

        return finalList