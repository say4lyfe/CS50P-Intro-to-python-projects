Greet = input("Greeting: ").strip().lower()

if Greet.__contains__("hello"):
    print("$0")

elif Greet[0] == "h":
    print("$20")

else:
    print("$100")
