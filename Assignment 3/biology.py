#Program to determine the type of an animal by asking a series of questions to user
#Fulufhelo Mulaudzi
#04 March 2024

print('''Welcome to the Biology Expert
-----------------------------
Answer the following questions by selecting from among the options.''')

animal_type = ""

#Used nested if-statements to evaluate the type of animal using user input
#First if checks where the skeleton is found
skeleton = input("The skeleton is (internal/external)?\n")
if skeleton == "internal":
    egg_fertilization = input("The fertilisation of eggs occurs (within the body/outside the body)?\n")

    #The second if checks how egg fertilization takes place
    if egg_fertilization == "within the body":
        young_production = input("Young are produced by (waterproof eggs/live birth)?\n")

        #The third if how the young are produced
        if young_production == "waterproof eggs":
            skin_covering = input("The skin is covered by (scales/feathers)?\n")

            #The fourth if checks for the skin covering
            if skin_covering == "scales":
                animal_type = "Reptile"
            else:
                animal_type = "Bird"
        else:
            animal_type = "Mammal"

    #This else-statement serves to check where the animal lives only if eggs are fertilised outside the body
    else:
        where_it_lives = input("It lives (in water/near water)?\n")
        if where_it_lives == "in water":
            animal_type = "Fish"
        else:
            animal_type = "Amphibian"
else:
    animal_type = "Arthropod"

print(f"Type of animal: {animal_type}")
