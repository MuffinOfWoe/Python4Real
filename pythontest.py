class Cards():
    name = "z"
    wins = "zzz"
    currentCharacter = ""

class NativeIslander(Cards):
    def __init__(self):
        self.name = "NativeIslander"
        self.team = "Bad"

someList = []
someList.append(NativeIslander)
print(someList[0].name)