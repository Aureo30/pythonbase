from statistics import mean
from random import shuffle
notes = [
    12, 13, 6,
    17, 4, 3,
    8, 13, 15
]
print(notes)
shuffle(notes)
print(notes)
result = mean(notes)
print("la moyenne de l'élève est de {}".format(result))