import re
import sys


def main():
    # CLI Argument Reading
    global grandDic
    grandDic = {}
    to_read = ""
    try:
        if sys.argv[1]:
            to_read = sys.argv[1]
    except:
        print("You gave no file to read.")

    config_arg(set_parse_var(to_read))
    print_dic()
    return


def set_parse_var(read_me):
    file = open(read_me, "r")
    HUGETEXT = ""
    for line in file:
        for char in line:
            HUGETEXT += char

    return_text = HUGETEXT.split("_3ji8")
    return return_text


def config_arg(read_me):
    to_match = "Invited"

    for line in read_me:
        is_match = re.search(to_match, line)
        if is_match:
            i = 0
            counter = 0
            for char in line:
                if char == to_match[i] and to_match[i] == "d":
                    j = counter + 5
                    temp_name = ""
                    while line[j] != "<":
                        temp_name += line[j]
                        j += 1

                    if temp_name in grandDic:
                        grandDic[temp_name] += 1
                    else:
                        grandDic[temp_name] = 1
                    break
                elif char == to_match[i]:
                    i += 1
                elif char != to_match[i]:
                    i = 0
                counter += 1
    return


def print_dic():
    for item in grandDic:
        print("{} invited {} people(s).".format(item, grandDic[item]))
    return


if __name__ == '__main__':
    main()
