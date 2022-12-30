class fileReader:
    def __init__(self, fileLocation=None):
        if fileLocation is None:
            fileLocation = ""
        else:
            self.fileLocation = fileLocation

    def getList(self, fileLocation):
        textFile = open(fileLocation, "r")
        foodList = []
        for line in textFile:
            cleanValue = line.strip()
            foodList.append(cleanValue)

        return foodList
        
