
alphabet="abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter):
    letter=letter.lower()
    return(alphabet.index(letter))


def rotate_character(char, rot):
    if char.isalpha():
        #rot=int(rot)
        if "a"<=char<="z":
            return chr(97+(alphabet_position(char)+rot)%26)
        elif "A"<=char<="Z":
            return chr(97+(alphabet_position(char)+rot)%26).upper()
    return char

def encrypt(text,rot):
    encrypted_text=""
    for char in range(len(text)):
        encrypted_text+=rotate_character(text[char],int(rot))
    return encrypted_text