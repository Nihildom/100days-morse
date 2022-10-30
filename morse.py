morse_dict = {
    " ": " ",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}


print("Hello and Welcome to the Text-to-Morse Program!")
print("The Program is able to process Letters, Numbers and Spaces.") 
print("Please do not input any other characters.")
print("")



def morsing():
    running = True
    while running:
        phrase = input("Write your text to be morsed: ")
        text = phrase.lower()
        morse = []
        for element in text:
            morse.append(morse_dict[element])
        output = " ".join(morse)
        print(f"Your input in Morse: {output}")
        repeat = input("New Phrase? y/n: ")
        if repeat.lower() == "n":
            running = False
            print("See you later!")
morsing()






