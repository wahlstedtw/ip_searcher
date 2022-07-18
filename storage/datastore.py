
def store(url_data):
    print("Storing ipv4 only")
# Intentionally has no processing. Leaves open the possibility of doing
#  something different with the data like saving it in a file.
    return url_data['data']['resources']['ipv4']
