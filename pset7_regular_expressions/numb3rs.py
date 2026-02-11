import re
import sys


def main():
    ip_address = input("IPv4 Address: ")
    check = validate(ip_address)
    print(check)


def validate(ip):
    if matches := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        groups = [matches.group(1),matches.group(2),matches.group(3),matches.group(4)]
        for group in groups:
            if (0 <= int(group) <= 255) and (group.startswith("0") == False or group == "0"):
                pass
            else:
                return False
            
        return True  
        
    else:
        return False

if __name__ == "__main__":
    main()