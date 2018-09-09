print("Welcome to the kitchen.")  # prindin tervitava lause
name = input("What is your name?")  # salvestan nime, mille kasutaja kirjutab pärast küsimust muutujasse "name"
print(f"Hi there, {name}!")  # kasutan f stringi ja kirjutan muutuja "name" koos lausega
drink = input("What do you like for a drink?")  # salvestan kasutaja poolt antud vastuse muutujasse "drink"
if drink == "tea":  # kontrollin, kas kasutaja antud vastus oli "tea"
    print(f"Have a nice {drink}!")  # ja prindin selle, kui oli tea
elif drink == "coffee":  # kas vastus oli "coffee"?
    print("Feeling tired?")  # ja kui oli, siis prindin selle
else:  # muudel juhtudel, kui ei ole ei "tea" ega "coffee"
    print("We only serve water.")  # prindin muu versioon
