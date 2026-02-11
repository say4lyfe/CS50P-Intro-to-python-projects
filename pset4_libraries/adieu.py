import inflect

name_list = []
p = inflect.engine()

while True:
    try:
        name = input("name: ")
        name_list.append(name)
    except(EOFError):
        print("\nAdieu, adieu, to" , p.join(name_list))
        break