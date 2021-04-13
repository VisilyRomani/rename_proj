import os
import pathlib
import sys
import time


def rename():
    print("1 - rename with letter and number")
    print("2 - rename with number")
    print("0 - close")

    while True:
        try:
            sel = int(input("enter your selection:"))
            break
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")

    if sel == 1:
        letter = input("what letter? ")
        i = input("what number? ")
        path = pathlib.Path(__file__).parent.absolute()
        for files in os.listdir(path):
            if files[0:3] == "DSC":
                fileDest = letter + str(i) + ".jpg"
                fileSource = path / files
                fileDest = path / fileDest
                os.rename(fileSource, fileDest)
                i = int(i) + 1
    elif sel == 2:
        i = input("what number? ")
        path = pathlib.Path(__file__).parent.absolute()
        for files in os.listdir(path):
            if files[0:3] == "DSC":
                fileDest = str(i) + ".jpg"
                fileSource = path / files
                fileDest = path / fileDest
                os.rename(fileSource, fileDest)
                i = int(i) + 1
    elif sel == 0:
        return


if __name__ == '__main__':
    rename()
    print("Done")
    time.sleep(10)
