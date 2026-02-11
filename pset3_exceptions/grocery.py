grocery_list = {}

while True:
    try:
        grocery = input().upper()
        if grocery in grocery_list:
            grocery_list[grocery] = grocery_list[grocery] + 1
        else:
            grocery_list[grocery] = 1

    except (EOFError):
        for grocery in sorted(grocery_list):
            print(f"{grocery_list[grocery]} {grocery}")
        break