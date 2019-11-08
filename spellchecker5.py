import re
import time
from datetime import datetime
from difflib import SequenceMatcher

now = datetime.now() # fetches current date and time

time1 = time.process_time() # starts timer

file1 = "EnglishWords.txt"
with open(file1) as f:  # Opens text file
    text = f.read()  # Reads from text file
txt = text.split()  # splits the words in the text file
Exit = False
while Exit is False:  # While user hasn't decided to quit the program, it'll loop the code
    command = None
    try:
        print("\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
        print("\u2502        S P E L L  C H E C K E R         \u2502")
        print("\u2502                                         \u2502")
        print("\u2502     1. Check a file                     \u2502 \n\u2502     2. Check a sentence                 "
              "\u2502 \n\u2502""                                         \u2502\n\u2502     0. Quit                       "
              "      \u2502")
        print("\u2502                                         \u2502")
        print("\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518 ")
        command = input("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                       "\u2500\u2500\u2500\u2500 Enter a choice: ")     # user is asked for input
        if command != "1" and command != "2" and command != "0":        # if there's no valid option picked by the user, it will repeat the question and ask them again until a correct option is picked
            raise Exception("Invalid Option")
    except Exception as exc:
        print("Invalid Option")
        continue

    if command == "0":
        print("Program ended")
        break               # Program ends once the input is '0'

    if command == "1":
        print("\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
        print("\u2502         L O A D  F I L E                \u2502")
        print("\u2502                                         \u2502")
        print("\u2502     Enter the filename                  \u2502"
              "\n\u2502     then press [enter]                  \u2502")
        print("\u2502                                         \u2502")
        print("\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518 ")
        file2 = input("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                      "\u2500\u2500\u2500 filename: ")
        with open(file2) as f:   # Opens the users file which they input
            text2 = f.read()     # Reads the text file
            text2 = text2.lower()   # All words are made to be lowercase
            sentence = re.sub(r'[^a-zA-Z ]+', "", text2)  # ignores non-alphanumeric characters
            correct2 = 0
            incorrect2 = 0
            List = []
            ignored = 0
            marked = 0
            added = 0

            f = open("checkMe1.txt", "a")   # Opens new text
            for word1 in sentence.split():
                if word1 in text.split():
                    f.write(word1 + " ")
                    correct2 += 1
                elif word1 not in text.split():
                    incorrect2 += 1
                    word1 = word1.lower()
                    for x in range(0, 84094):
                        score1 = SequenceMatcher(None, word1, txt[x]).ratio()
                        if score1 >= 0.75:

                            print("\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                  "\u2500\u2500\u2500"
                                  "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                  "\u2500\u2500\u2500"
                                  "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
                            print("\u2502          W O R D  N O T  F O U N D      \u2502")
                            print("\u2502                                         \u2502")
                            print("\u2502     " + word1, (" " * (23 - len(word1))), "           \u2502")
                            print("\u2502     Did you mean:                       \u2502")
                            print("\u2502     " + txt[x], (" " * (23 - len(txt[x]))), "           \u2502")
                            print("\u2502                                         \u2502")
                            print(
                                "\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                "\u2500\u2500\u2500"
                                "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                "\u2500\u2500\u2500"
                                "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518 ")
                            alternative = input(
                                "\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                "\u2500\u2500"
                                "\u2500\u2500\u2500\u2500 enter [y] or [n]: ")
                            if alternative == "y" or alternative == "Y":
                                f.write(txt[x] + " ")
                                break
                            while alternative == "n" or alternative == "N":
                                user_input = None
                                try:

                                    print(
                                        "\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                        "\u2500"
                                        "\u2500\u2500\u2500"
                                        "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                        "\u2500"
                                        "\u2500\u2500\u2500"
                                        "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
                                    print("\u2502          W O R D  N O T  F O U N D      \u2502")
                                    print("\u2502                                         \u2502")
                                    print("\u2502     1. ignore word.                     \u2502")
                                    print("\u2502     2. Mark the word as incorrect       \u2502")
                                    print("\u2502     3. Add word to dictionary.          \u2502")
                                    print("\u2502                                         \u2502")
                                    print(
                                        "\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                        "\u2500"
                                        "\u2500\u2500\u2500"
                                        "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                        "\u2500"
                                        "\u2500\u2500\u2500"
                                        "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518")
                                    user_input = input(
                                        "\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                        "\u2500"
                                        "\u2500\u2500"
                                        "\u2500\u2500\u2500\u2500 enter choice: ")
                                    if user_input != "1" and user_input != "2" and user_input != "3":  # if there's no valid option picked by the user, it will repeat the question and ask them again until a correct option is picked
                                        raise Exception("Invalid Option")
                                except Exception as exc:
                                    print("Invalid Option")
                                    continue

                                if user_input == "1":
                                    f.write("!" + word1 + "! ")
                                    ignored += 1
                                    break
                                elif user_input == "2":
                                    f.write("?" + word1 + "? ")
                                    marked += 1
                                    break
                                elif user_input == "3":
                                    f.write("*" + word1 + "* ")
                                    added += 1
                                    with open("EnglishWords.txt", "a") as a:
                                        a.write("\n" + word1)
                                    List.append(word1)
                                    break
                                break

            filename = open("checkMe1.txt", "r+")
            readfile = filename.readlines()
            file_lines = (now.strftime(
                "%Y-%m-%d %H:%M:%S" + "\nNumber of words: " + str(len(List)) + "\nNumber of correct words: " + str(
                    correct2)) + "\nNumber of incorrect words: " + str(incorrect2) + "\n   Number ignored: " + str(
                ignored) + "\n   Number marked: " + str(marked) + "\n   Number added to dictionary: " + str(
                added) + "\n" + "" + "\n")
            print("\n" + file_lines)
            filename.seek(0)
            filename.write(file_lines)
            for line in readfile:
                filename.write("\n" + line)
            filename.close()

    elif command == "2":
        word = input("Enter sentence to spellcheck: ")  # Asks for user input
        word = word.lower()  # Turns all letters in each words into lowercase letters
        string = re.sub(r'[^a-zA-Z ]+', '', word)
        w = string.split()  # Splits sentence into list of words
        print(string, "\n")
        correct = 0
        incorrect = 0
        wordList = []

        for l in w:
            if l in text.split():
                print(l + " is spelt correctly")
                correct += 1
            else:
                print(l + " not found in dictionary")
                incorrect += 1
            wordList.append(l)

        print("\nNumber of words: ", str(len(wordList)))
        print("Number of correct words: ", correct)
        print("Number of incorrect words: ", incorrect)

        command = None
    user_input = input("\nPress q [enter] to quit or any other key [enter] to go again: ")
    if user_input == 'q' or user_input == 'Q':
        Exit = True
    else:
        Exit = False

time2 = time.process_time()
time = (time2 - time1)
print("\nTime elapsed: ", time * 1000000, " microseconds \n")
