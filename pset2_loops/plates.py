def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ## no special characters
    if s.isalnum():
    ## at least 2 letters, at most 6 characters
        if  2 <= len(s) <= 6 :
    ## first 2 are letters
            x = s[0:2]
            if x.isalpha():
    ## numbers do not start with 0
                for char in s:
                    if char.isdigit():
                        if char == "0":
                            y , z = s.split("0")
                            if y.isalpha():
                                return False
    ## numbers are at the end
                        elif char != "0":
                            a = s.index(char)
                            b = s[a:5]
                            if b.isdigit():
                                return True
    ## all are letters
                if s.isalpha():
                    return True

main()
