
import getopt, sys, os

def process_args(argumentList):
    print("Processing Args")

    # Options
    options = "hmeo:"

    # Long options
    long_options = ["Help", "My_file"]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--Help"):
                print ("ex. python main.py 192.168.1.1")

            elif currentArgument in ("-m", "--My_file"):
                print ("Displaying file_name:", sys.argv[0])

            elif currentArgument in ("-e"):
                print (f"There is no spoon, see? {currentValue}")

    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))

    try:
        arg_ipv4 = argumentList[0]
    except IndexError as err:
        print (f"Your error my good sir: {(str(err))}")
        os._exit(1)
        raise err

    return arg_ipv4