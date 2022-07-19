# Challenge 2 - Functions, Arrays and Files
import random

totaldicenum = []

# calculate average


def calculateAverage(array):
    return (round(sum(array) / len(array)))

# display num to user


def displayNumb(array):
    return '|'.join(map(str, array))

# write the numbers into a text file


def writeNumbersToFile(numbers):
    with open("yournumbers.txt", 'w') as numberoutput:
        display = displayNumb(numbers)
        numberoutput.write(display)

# Read file


def readFile():
    with open("yournumbers.txt", "r") as readingoutput:
        print(f"3. Your numbers were: {readingoutput.readline()}")

# Roll the dice program


def rollDice():
    while True:
        try:
            dicenumbers = []
            numofdice = int(input("How many dices you want to roll: "))
            if numofdice > 0:
                for x in range(numofdice):
                    rolldice = random.randint(1, 6)
                    dicenumbers.append(rolldice)
                    totaldicenum.append(rolldice)
                print(dicenumbers)

                askuser = input(
                    "Do you want to roll the dice again? (yes/no): ")
                if askuser == 'no':
                    writeNumbersToFile(totaldicenum)
                    print(
                        f"1. Your average is {calculateAverage(totaldicenum)}")
                    print(f"2. Total rolls {len(totaldicenum)}")
                    readFile()
                    print("--------------")
                    print("See you later")
                    break
                elif askuser != 'no' and askuser != 'yes':
                    print("No valid option")
                    break

        except ValueError:
            print("No valid option. Try again!")


rollDice()
