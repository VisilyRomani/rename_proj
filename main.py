import os
import pathlib
import sys
import time


def numberCheck():
    print("1 - rename with letter and number")
    print("2 - rename with number")
    print("0 - close")

    while True:
        try:
            sel = int(input("enter your selection:"))
            break
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")

    if sel == 0:
        return

    if sel == 1:
        letter = input("what letter? ")
    i = input("what number? ")
    path = pathlib.Path(__file__).parent.absolute()
    for files in os.listdir(path):
        if files[0:3] == "DSC":
            if sel == 1:
                file_destination = letter + str(i) + ".jpg"
            else:
                file_destination = str(i) + ".jpg"
            file_source = path / files
            file_destination = path / file_destination
            os.rename(file_source, file_destination)
            i = int(i) + 1


if __name__ == '__main__':
    numberCheck()
    print("Done")
    time.sleep(5)
