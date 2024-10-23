def getInt(promptStr):
    while True:
        try:
            i = int(input("%s: " % promptStr))
            break
        except ValueError:
            print("Must be an integer.\n")
    return i

def getEncounterCr(partyLvl):
    while True:
        try:
            ecr = 0
            s = input("Monster sets: ")
            sets = s.split(", ")
            for set in sets:
                setSplit = set.split("x ")
                assert len(setSplit) == 2
                cr = float(setSplit[1])
                if partyLvl < 5 and cr < 1:
                    cr = 0.125 if cr == float(0) else cr * 2
                ecr += int(setSplit[0]) * cr
            break
        except AssertionError:
            print("Please enter the correct monster set format\n")
        except ValueError:
            print("Monster count must be an integer and CR must be a number\n")
    return ecr

def calculateDifficulty(tcl, ecr):
    if ecr < round(tcl / 6):
        return "trivial"
    if ecr < round(tcl / 3):
        return "easy"
    if ecr < round(tcl / 2):
        return "medium"
    if ecr < round((2 * tcl) / 3):
        return "hard"
    return "deadly"

if __name__ == "__main__":
    while True:
        charCounter = getInt("Enter the number of characters to balance for")
        partyLvl = getInt("Enter the party level")
        tcl = charCounter * partyLvl

        print("\nYou can now enter monster sets and see what difficulty they would be for this group configuration.\n\t"
              " For example, for 3x CR 1s and 2x CR 2s, you would enter: 3x 1, 2x 2\n\t")
        while True:
            ecr = getEncounterCr(partyLvl)
            print("Difficulty: %s\n" % calculateDifficulty(tcl, ecr))
