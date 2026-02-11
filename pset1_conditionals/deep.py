ans = input("what is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

match ans:
    case "42" | "forty two" | "forty-two":
        print("yes")
    case _:
        print("no")