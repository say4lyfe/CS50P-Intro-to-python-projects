def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s.isalnum():

        if  2 <= len(s) <= 6:

            x = s[0:2]
            if x.isalpha():

                for char in s:
                    if char.isdigit():
                        if char == "0":
                            y , z = s.split("0")
                            if y.isalpha():
                                return False

                        elif char != "0":
                            a = s.index(char)
                            b = s[a:6]
                            if b.isdigit():
                                return True
                            else:
                                return False

                if s.isalpha():
                    return True
                
            else:
                return False 
              
        else:
            return False    
         
    else:
        return False



if __name__ == "__main__":
    main()