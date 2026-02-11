def main():
    print("Amount Due: 50")
    remainder = 50
    while remainder.is_integer() :
        while True:
            x = int(input("Insert Coin: "))
            if x == 25 or x == 10 or x == 5:
                break
            else:
                print("Amount Due: 50")
        remainder = remainder - x
        if remainder > 0:
            print(f"Amount Due: {remainder}")
        elif remainder == 0:
            print("Change Owed: 0")
            break
        else:
            print(f"Change Owed: {abs(remainder)}")
            break
        
main()

