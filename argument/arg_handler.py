import sys
from netaddr import IPAddress

def process_args():
    print("Processing Args")
    argumentList = sys.argv[1:]

    USAGE = f"Usage: python {sys.argv[0]} [--help] | ipv4\n"
    USAGE += f"       Requires valid ipv4 address."

    try:
        valid_ipv4(argumentList[0])
    except:
        raise SystemExit(USAGE)

    return argumentList[0]