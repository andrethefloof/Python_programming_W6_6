LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def rot13(text):
    cipheredt = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            index = (LOWER_ALPHABETS.index(char) + 13) % 26
            cipheredt += LOWER_ALPHABETS[index]
        elif char in UPPER_ALPHABETS:
            index = (UPPER_ALPHABETS.index(char) + 13) % 26
            cipheredt += UPPER_ALPHABETS[index]
        else:
            cipheredt += char
    return cipheredt
def writeFile(filename, text):
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
writefile = writeFile
def shiftCharacter(char, alphabet):
    if char in alphabet:
        index = (alphabet.index(char) + 13) % 26
        return alphabet[index]
    return char
def askRows():
    fullt = ""
    print("Collecting plain text rows for ciphering.")
    while True:
        line = input("Insert row(empty stops): ")
        if line == "":
            break
        if fullt == "":
            fullt = line
        else:
            fullt += "\n" + line
    return fullt
def main():
    print()
    print("#### Ciphered text ####")
    fullt = askRows()
    cipheredt = rot13(fullt)
    print(cipheredt)
    print()
    print("### Ciphered text ###")
    filename = input("Insert filename to save: ")
    writefile(filename, cipheredt)
    print("Ciphered text saved!")
    print("Program ending.")
if __name__ == "__main__":
    main()