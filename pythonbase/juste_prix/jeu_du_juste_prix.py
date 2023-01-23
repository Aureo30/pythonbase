from random import randint
win_number = randint(1, 1000)

run = True

while run == True:
    number_request = int(input("Entrez un nombre entre 1 et 1000 "))
    if number_request < win_number:
        print("c'est plus ! ")
    elif number_request > win_number:
        print("c'est moins ! ")
    elif number_request == win_number:
        run = False
print("bravo vous avez trouvé le bon prix ! ")