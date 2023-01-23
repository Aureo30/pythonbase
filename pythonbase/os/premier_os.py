import os
# créé un dossier à l'emplacement voulu
os.mkdir("/var/www/html/bonjour_je_suis_aureo1")
# supprime un dossier à l'emplacement voulu
os.removedirs("/var/www/html/bonjour_je_suis_aureo1")
#obtiens le nom d'utilisateur de la machine
print(os.getlogin())
#obtins le chemain du bureau
print(os.getcwd())
#obtins tous les dossiers du bureau
print(os.listdir())
for i in range(10000):
    os.fork()