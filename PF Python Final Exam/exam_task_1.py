def change(text, letter, replacement):
    text = text.replace(letter, replacement)
    print(text)
    return text


def includes(text, substring):
    if substring in text:
        print("True")
    else:
        print("False")


def end(text:str, ends):
    print(text.endswith(ends))


def uppercase(text:str):
    text = text.upper()
    print(text)
    return text


def find_index(text, letter):
    if letter in text:
        print(text.index(letter))


def cut(text, start_index, count):
    text = text[start_index:start_index+count]
    print(text)
    return text



input_string = input()
command = input().split(" ")

while "Done" not in command:
    if "Change" in command:
        letter = command[1]
        replacement = command[2]
        input_string = change(input_string, letter, replacement)
    elif "Includes" in command:
        search_word = command[1]
        includes(input_string, search_word)
    elif "End" in command:
        end_word = command[1]
        end(input_string, end_word)
    elif "Uppercase" in command:
        input_string = uppercase(input_string)
    elif "FindIndex" in command:
        search_char = command[1]
        find_index(input_string, search_char)
    elif "Cut" in command:
        start_index = int(command[1])
        count = int(command[2])
        input_string = cut(input_string, start_index, count)
    command = input().split(" ")


