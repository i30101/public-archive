import random
import requests

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--.."
}

ALPHABET = list(MORSE.keys())

FRACTIONATED = list({
    "A": "...", "B": "..-", "C": "..x", "D": ".-.", "E": ".--", "F": ".-x", "G": ".x.",
    "H": ".x-", "I": ".xx", "J": "-..", "K": "-.-", "L": "-.x", "M": "--.", "N": "---",
    "O": "--x", "P": "-x.", "Q": "-x-", "R": "-xx", "S": "x..", "T": "x.-", "U": "x.x",
    "V": "x-.", "W": "x--", "x": "x-x", "Y": "xx.", "Z": "xx-"
}.values())

KEY = open("key/key.txt").read()


# translates text to morse
def to_morse(plain):
    plaintext = plain.upper()
    morse_text = ""
    for i, char in enumerate(plaintext):
        if char == " ":
            morse_text += "x"
        else:
            morse_text += MORSE[char]
            if i != len(plaintext) - 1:
                morse_text += "x"
    return morse_text


# translates to list of numbers
def to_numbers(plain):
    plaintext = plain.upper().replace(" ", "")
    return [ALPHABET.index(char) for char in plaintext]


# get random word from internet
def random_word():
    api_url = "https://api.api-ninjas.com/v1/randomword"
    while True:
        response = requests.get(api_url, headers={"X-Api-Key": KEY})
        if response.status_code == requests.codes.ok:
            response = response.text.replace("{\"word\": \"", "").replace("\"}", "")
            if 4 < len(response) < 8 and [response.count(letter) for letter in response] == [1 for n in response]:
                return response
        else:
            print("Error:", response.status_code, response.text)


# get random quote from internet
def random_quote() -> dict:
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    while True:
        response = requests.get(api_url, headers={'X-Api-Key': KEY})
        if response.status_code == requests.codes.ok:
            response = response.text.split(":")
            quote = response[1].replace(" \"", "").replace("\", \"author\"", "").replace("\'", "")

            # check if quote meets cipher constraints
            if not (any([x in quote for x in ["?", ";", "-"]]) and not any(char.isdigit() for char in quote)) and "." in quote:
                # process quote and author
                quote = quote[: quote.index(".")].replace(", ", "")
                author = response[2].replace(" \"", "").replace("\",category\"", "")

                # create output dictionary
                output = {"quote": quote, "author": author}

                return output
        else:
            print("Error:", response.status_code, response.text)


# outputs random letter-number assignment questions
def letter_number():
    print("Letter-Number Assignments")
    for i in range(5):
        print(':\t'.join(random.sample(ALPHABET, k=4)) + ":")


# outputs pollux question
def pollux(plain, author):
    # translate letters to morse
    morse_text = to_morse(plain)

    # bank of numbers
    numbers = [str(num) for num in list(range(10))]

    # chooses random number from number bank
    def choose(l):
        chosen = random.sample(numbers, k=random.randint(3, 4))
        l = [num for num in l if num not in chosen]
        return chosen

    dot_numbers = choose(numbers)
    numbers = [num for num in numbers if num not in dot_numbers]
    dash_numbers = choose(numbers)
    numbers = [num for num in numbers if num not in dash_numbers]
    x_numbers = numbers

    # chooses random numbers given in question
    def sample(l):
        return ", ".join(random.sample(l, k=int(len(l) / 2)))

    question = f"Solve this Pollux quote by {author} where"
    question += f"{sample(dot_numbers)} = ., "
    question += f"{sample(dash_numbers)} = -, "
    question += f"and {sample(x_numbers)} = x"
    print(question)

    # ciphertext (morse tranlsated to numbers)
    ciphertext = ""
    for char in morse_text:
        match char:
            case ".": ciphertext += random.choice(dot_numbers)
            case "-": ciphertext += random.choice(dash_numbers)
            case _: ciphertext += random.choice(x_numbers)
    print(" ".join(ciphertext))


# outputs morbit question
def morbit(plain, author):
    # translate letters to  morse
    morse_text = to_morse(plain)

    # bank of numbers
    numbers = [str(num) for num in list(range(10))]

    # dot-dash-x combinations
    combinations = ["..", "--", ".-", "-.", "x.", "x-", ".x", "-x", "xx"]

    # number to combinatination assignments
    assignments = random.sample(numbers, k=9)

    # create question
    question = f"Solve this Morbit quote by {author} where "
    random_combinations = random.sample(combinations, k=random.randint(3, 5))
    random_numbers = [assignments[combinations.index(c)] for c in random_combinations]
    for i, combination in enumerate(random_combinations):
        question += f"{random_numbers[i]} = {combination}"
        if i != len(random_combinations) - 1:
            question += ", "
    print(question)

    # translate every morse combintation in to numbers
    ciphertext = ""
    if len(morse_text) % 2 == 1:
        morse_text += "x"
    for i in range(0, len(morse_text), 2):
        ciphertext += assignments[combinations.index(morse_text[i: (i + 2)])]
    print(" ".join(ciphertext))


# outputs fractionated morse question
def fractionated(plain, author):
    # translate plaintext to ciphertext
    morse_text = to_morse(plain)

    # print(len(morseText))

    # adjust length for transcription
    if int(len(morse_text)) % 3 != 0:
        morse_text += "".join(["x" for i in range(3 - (len(morse_text) % 3))])

    # get random word
    rand = random_word().upper()

    # ciphertext alphabet
    cipher_alphabet = rand + "".join([l for l in ALPHABET if l not in rand])

    # create ciphertext
    cipher_text = ""
    for i in range(0, len(morse_text), 3):
        triplet = morse_text[i: i + 3]
        # print(triplet)
        letter = cipher_alphabet[FRACTIONATED.index(triplet)]
        cipher_text += letter

    print(
        f"Solve this Fractionated Morse cipher by {author} that ends with the word {plain[plain.rindex(' '):].upper()}\n")
    print("  ".join(cipher_text))


# outputs porta question
def porta(plain, author):
    # get keyword
    keyword = random_word().upper()
    
    # split alphabet
    first_half = ALPHABET[:13]
    second_half = ALPHABET[13:]
    
    rows = [second_half[i:] + second_half[:i] for i in range(13)]
    
    # print question
    print(f"Solve this Porta cipher by {author} with the keyword {keyword}.")

    ciphertext = ""
    for i, plainLetter in enumerate(plain):
        row_index = int(ALPHABET.index(keyword[i % len(keyword)]) / 2)
        if plainLetter in first_half:
            ciphertext += rows[row_index][first_half.index(plainLetter)]
        else:
            ciphertext +=ALPHABET[rows[row_index].index(plainLetter)]
    
    print(ciphertext)


# demo of all ciphers ()
def demo(num_each_cipher):

    ciphers = [pollux, morbit, fractionated]

    letter_number()
    print("\n\n\n")

    for cipher in ciphers:
        for i in range(num_each_cipher):
            quote = random_quote()
            cipher(quote["quote"], quote["author"])
            print("\n\n\n")


if __name__ == "__main__":
    # quote_dict = random_quote()
    # quote = quote_dict["quote"]
    # author = quote_dict["author"]

    # print(quote)
    # print(author)
    # print(random_word())

    # print(to_numbers("bell"))

    # print(random_quote())    
    pollux()