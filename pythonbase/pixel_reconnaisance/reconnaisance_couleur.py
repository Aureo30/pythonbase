from PIL import Image
img = Image.open("/var/www/html/ascii_art/joconde.jpeg")
largeur = 50
hauteur = 70
for y in range(hauteur):
    for x in range(largeur):
        r,v,b = img.getpixel((x, y))
        print("rouge :", r,", vert :", v,", bleu :", b)