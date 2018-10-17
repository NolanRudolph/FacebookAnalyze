
import sys

def main():
    # CLI Argument Reading
    global toRead
    global grandDick
    try:
        if sys.argv[1]:
            toRead = sys.argv[1]
    except:
        print("You gave no file to read.")

def parseArg():
    file = open(toRead, "r")
    









if __name__ == '__main__':
    main()