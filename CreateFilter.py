

from Commons import *


import csv


class CreateFilter:

    def __init__(self):

        self.templateBase = None

        self.templateEntry = None

        self.loadTemplates()

        self.targetLabeling = None

        self.targetMarkAsRead = None

        self.loadTargetLists()

        self.entryTextList = None

        self.loadEntryList()

    def loadTemplates(self):

        with open("template/base.xml", mode="r", encoding="utf-8")as f:

            self.templateBase = f.read()

        with open("template/entry.xml", mode="r", encoding="utf-8")as f:

            self.templateEntry = f.read()

    def createEntry(self, email, label, markAsRead, archive):

        entryText = self.templateEntry.format(
            title=email,

            id=email+"_"+label+"_"+str(markAsRead),
            email=email,

            label=label,

            markAsRead=markAsRead,

            archive=archive
        )

        return entryText

    def loadTargetLists(self):

        with open("data/labelingList.csv", mode="r", encoding="utf-8", newline="")as f:

            reader = csv.reader(f)

            self.targetLabeling = [row for row in reader][1:]

        with open("data/markAsReadList.csv", mode="r", encoding="utf-8", newline="")as f:

            reader = csv.reader(f)

            self.targetMarkAsRead = [row for row in reader][1:]

    def loadEntryList(self):

        self.entryTextList = []

        for target in self.targetLabeling:

            text = self.createEntry(target[0], target[1], "false", "true")

            self.entryTextList.append(text)

        for target in self.targetMarkAsRead:

            text = self.createEntry(target[0], target[1], "true", "true")

            self.entryTextList.append(text)

    def printXml(self):

        entrysText = ""

        for entryText in self.entryTextList:

            entrysText += entryText+"\n"

        xmlText = self.templateBase.format(entrysText=entrysText)

        with open("output/filters.xml", mode="w", encoding="utf-8")as f:

            f.write(xmlText)


if __name__ == "__main__":

    cf = CreateFilter()

    cf.printXml()
    print("ret")
