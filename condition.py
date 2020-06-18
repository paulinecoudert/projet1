user_age = input("Quel est votre age? ")
user_age= int(user_age)

if user_age < 18:
    print ( "Désolé vous êtes trop jeune" )
elif user_age > 130:
    print ( "Désolé vous êtes hors limite d'age")
else: 
    print(" Vous êtes le bienvenue ")

print ("--FIN--")