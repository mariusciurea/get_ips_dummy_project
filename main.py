"""main module for the git session"""


def get_ip_addresses() -> list:
    """dummy function"""

    return ["10.111.122.68", "10.111.122.69"]


if __name__ == "__main__":
    ips = get_ip_addresses()
    print(ips)