PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as letter_file:
    names = letter_file.readlines()

for name in names:
    # remove the new line
    name = name.strip()

    with open("Input/Letters/starting_letter.txt") as letter_file:
        letter = letter_file.read()
        letter = letter.replace(PLACEHOLDER, name)
        with open(f"Output/letter_for_{name}.txt", mode="w") as output_file:
            output_file.write(letter)

