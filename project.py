import random

class Word:
    def __init__(self, wordType):
        self.wordType = wordType
        self.word = input("Insert a/an " + wordType + " or press r to generate a word, then press enter : ")

        print("Fantastic!")

        if self.word == "r":
            self.randomWords()

        while True:
                if len(self.word) <= 0:
                    print("HEYY! Don't leave this part blank")
                    self.word = input("Insert a/an " + wordType + " or press r to generate a word, then press enter: ")
                    print("Fantastic!")
                    if self.word == "r":
                        self.randomWords()
                else:
                    break

    def randomWords(self):
        data = []
        file = open(self.wordType + ".txt", "r")
        for row in file:
            raw = row.replace("\n", "")
            data.append(raw)
        file.close()
        self.word = data[random.randint(0, len(data) - 1)]

    def getWord(self):
        return self.word



