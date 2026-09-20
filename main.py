import socket
from urllib.parse import urlparse

print("-" * 40)
print("         DNS Enumeration Tool")
print("-" * 40)

def clean_domain(domain):

    domain = domain.strip()

    if not domain.startswith(("http://", "https://")):
        domain = "https://" + domain

    parsed = urlparse(domain)

    return parsed.hostname


def dns_lookup(domain):
    print(f"\nDNS Enumeration: {domain}")
    print("-" * 40)

    results = {
        "domain": domain,
        "ipv4": [],
        "ipv6": [],
        "subdomains": {}
    }

    # IPv4 Lookup
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(domain)

        results["ipv4"] = addresses

        print("--> IPv4 addresses:")
        for ip in addresses:
            print(f"    {ip}")

    except socket.gaierror:
        print("--> Could not resolve IPv4 address")

    print("=" * 40)

    # IPv6 Lookup
    try:
        ipv6_addresses = set()

        address_info = socket.getaddrinfo(domain,None,socket.AF_INET6)
        for info in address_info:
            ipv6_addresses.add(info[4][0])

        results["ipv6"] = list(ipv6_addresses)

        print("--> IPv6 addresses:")
        for ip in results["ipv6"]:
            print(f"    {ip}")

    except socket.gaierror:
        print("--> Could not resolve IPv6 address")

    print("=" * 40)

    # Subdomain Enumeration
    with open("subdomains.txt", "r") as file:
        subdomains = [line.strip() for line in file]

    print("Checking subdomains...")
    print("~" * 25)

    for sub in subdomains:

        hostname = f"{sub}.{domain}"

        try:
            ip = socket.gethostbyname(hostname)

            results["subdomains"][hostname] = ip

            print(f"(+) {hostname} -> {ip}")

        except socket.gaierror:
            pass

    return results


def main():

    domain = input("Enter domain (example.com): ")

    domain = clean_domain(domain)

    if not domain:
        print("[!] Invalid domain")
        return

    dns_lookup(domain)

    print("-" * 40)

main()