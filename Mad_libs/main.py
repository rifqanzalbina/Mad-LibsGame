from ast import FloorDiv
from random import randint
import copy

print("Welcome to Madlib Games")

play = input("Lets we Play, shall we ? \n")

if play.lower() == "yes":
    print("Okey lets play The game : \n")

    noun1 = input("Enter your name : ")
    noun2 = input("Enter your friend Name : ")
    noun3 = input("Enter another Your Friend Name's : ")
    place = input("Enter a place name : ")
    adjective1 = input("Enter an Adjective : ")
    adjective2 = input("Enter another Adjective : ")
    adjective3 = input("Enter one more Adjective : ")
    adverb1 = input("Enter an Adverb : ") 
    adverb2 = input("Enter another Adverb : ")
    Exclamation = input("Enter an Emotion : ")

    # The Story About 

    print(
        "One day\n"+ noun1 + " went to " + place + " . "
        " He felt very Lonely , even though the view was " + adjective1 + " . "
        " He decided to call his two best friend " + noun2 + noun3 + " . "
        " When They came, they told\t " + noun1 + " something " + adjective2 + " had happened. "
        + noun1 + " went there very " + adverb1 + ""
        " When he came he found out that his other Friend was falling off a cliff "
        + noun1 + " said " + Exclamation + " Inside he was feeling " + adjective3 + " ."
        + noun1 + " Managed to save him " 
        " After that they had a " + adverb2 + " celebration "
        " They all Laughed"
    )
else:
    quit()