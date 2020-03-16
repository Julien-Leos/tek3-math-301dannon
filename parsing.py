import sys

def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def check_usage(arg):
    if arg == "-h" or arg == "--help":
        print("USAGE\n\t./301dannon file\nDESCRIPTION\n\tfile\tfile that contains the numbers to be sorted, seperated by spaces\n")
        sys.exit(0)

def parse(args):
    if len(args) != 1:
        print("Invalid number of arguments. Try ./301dannon -h for usage")
        sys.exit(84)
    check_usage(args[0])
    content = open(args[0], 'r').read()
    new = ""
    for x in content:
        if (is_number(x) == False and x != '.' and x != '-'):
            if (new[-1] != ' '):
                new += " "
        else:
            new += x
    array = new.split(' ') 
    return list(map(float, array))