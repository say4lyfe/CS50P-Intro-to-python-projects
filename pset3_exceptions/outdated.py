months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            a ,b ,c = date.split("/")
            a = int(a)
            b = int(b)
            if 1 <= a <= 12 and 1 <= b <= 31:
                print(f"{c}-{a:02}-{b:02}")
                break
            else:
                continue
        elif "," in date:
            x , y , z = date.split(" ")
            x = months.index(x) + 1
            y = y.replace("," , "")
            y = int(y)
            if 1 <= y <= 31:
                print(f"{z}-{x:02}-{y:02}")
                break
            else:
                continue
    except(ValueError):
        continue