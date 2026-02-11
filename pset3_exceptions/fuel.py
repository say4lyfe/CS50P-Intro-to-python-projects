while True:
    try:
        fraction = input("Fraction: ")
        y , z = fraction.split("/")
        percentage = (int(y) / int(z)) * 100
        if 1 < percentage < 99:
            print(f"{percentage:.0f}%")
            break
        elif 0 <= percentage <= 1:
            print("E")
            break
        elif 99 <= percentage <= 100:
            print("F")
            break
        else:
            continue
        
    except (ValueError, ZeroDivisionError):    
        continue
