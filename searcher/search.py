from netaddr import IPNetwork, IPAddress

def for_ipv4(url_data, ip_arg):
    print(f"Searching for : {ip_arg}")

    for cidr in url_data:
        if IPAddress(ip_arg) in IPNetwork(cidr):
            print(f"Found It! {cidr}")
            return True
    return False
