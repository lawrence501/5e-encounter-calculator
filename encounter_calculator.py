import csv
import math
import re

def getInt(promptStr):
    while True:
        try:
            i = int(input("%s: " % promptStr))
            break
        except ValueError:
            print("Must be an integer.\n")
    return i

def getDifficulty(promptStr):
    while True:
        try:
            d = input("%s: " % promptStr)
            assert d in {"easy", "medium", "hard", "deadly"}
            break
        except AssertionError:
            print("Must be easy, medium, hard, or deadly.\n")
    return d

def getEncounterCr():
    while True:
        try:
            ecr = 0
            s = input("Monster sets: ")
            sets = s.split(", ")
            for set in sets:
                setSplit = set.split("x ")
                assert len(setSplit) == 2
                ecr += int(setSplit[0]) * float(setSplit[1])
            break
        except AssertionError:
            print("Please enter the correct monster set format\n")
        except ValueError:
            print("Monster count must be an integer and CR must be a number\n")
    return ecr

def calculateDifficulty(tcl, ecr):
    if ecr < tcl // 3:
        return "easy"
    if ecr < tcl // 2:
        return "medium"
    if ecr < (2 * tcl) // 3:
        return "hard"
    return "deadly"

if __name__ == "__main__":
    while True:
        charCounter = getInt("Enter the number of characters to balance for")
        tcl = charCounter * getInt("Enter the party level")

        print("\nYou can now enter monster sets and see what difficulty they would be for this group configuration.\n\t"
              " For example, for 3x CR 1s and 2x CR 2s, you would enter: 3x 1, 2x 2\n\t")
        while True:
            ecr = getEncounterCr()
            print("Difficulty: %s\n" % calculateDifficulty(tcl, ecr))
