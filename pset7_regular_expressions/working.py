import re
import sys

def main():
    time12h = input("Hours: ")
    time24h = convert(time12h)
    print(time24h)

def convert(s):   
    if matches := re.match(r"([0-9]{1,2})(:[0-9]{1,2})? (AM|PM) to ([0-9]{1,2})(:[0-9]{1,2})? (AM|PM)", s):
        if matches.group(3) == "AM":
            if 1 <= int(matches.group(1)) <= 11:
                hours1 = int(matches.group(1))
                if matches.group(2) is None:
                    minutes1 = 00
                else:
                    w = matches.group(2).replace(":" , "")
                    if 00 <= int(w) <= 59:
                        minutes1 = int(w)
                    else:
                        raise ValueError
            elif int(matches.group(1)) == 12: 
                hours1 = int(matches.group(1)) - 12
                if matches.group(2) is None:
                    minutes1 = 00
                else:
                    w = matches.group(2).replace(":" , "")
                    if 00 <= int(w) <= 59:
                        minutes1 = int(w)
                    else:
                        raise ValueError
            else: 
                raise ValueError
        if matches.group(3) == "PM":
            if 1 <= int(matches.group(1)) <= 11:
                hours1 = int(matches.group(1)) + 12
                if matches.group(2) is None:
                    minutes1 = 00
                else:
                    x = matches.group(2).replace(":" , "")
                    if 00 <= int(x) <= 59:
                        minutes1 = int(x)
                    else:
                        raise ValueError
            elif int(matches.group(1)) == 12: 
                hours1 = int(matches.group(1))
                if matches.group(2) is None:
                    minutes1 = 00
                else:
                    x = matches.group(2).replace(":" , "")
                    if 00 <= int(x) <= 59:
                        minutes1 = int(x)
                    else:
                        raise ValueError
            else: 
                raise ValueError
        time1 = f"{hours1:02}:{minutes1:02}"

        if matches.group(6) == "AM":
            if 1 <= int(matches.group(4)) <= 11:
                hours2 = int(matches.group(4))
                if matches.group(5) is None:
                    minutes2 = 00
                else:
                    y = matches.group(5).replace(":" , "")
                    if 00 <= int(y) <= 59:
                        minutes2 = int(y)
                    else:
                        raise ValueError
            elif int(matches.group(4)) == 12: 
                hours2 = int(matches.group(4)) - 12
                if matches.group(5) is None:
                    minutes2 = 00
                else:
                    y = matches.group(5).replace(":" , "")
                    if 00 <= int(y) <= 59:
                        minutes2 = int(y)
                    else:
                        raise ValueError
            else: 
                raise ValueError
        if matches.group(6) == "PM":
            if 1 <= int(matches.group(4)) <= 11:
                hours2 = int(matches.group(4)) + 12
                if matches.group(5) is None:
                    minutes2 = 00
                else:
                    z = matches.group(5).replace(":" , "")
                    if 00 <= int(z) <= 59:
                        minutes2 = int(z)
                    else:
                        raise ValueError
            elif int(matches.group(4)) == 12: 
                hours2 = int(matches.group(4))
                if matches.group(5) is None:
                    minutes2 = 00
                else:
                    z = matches.group(5).replace(":" , "")
                    if 00 <= int(z) <= 59:
                        minutes2 = int(z)
                    else:
                        raise ValueError
            else: 
                raise ValueError
        time2 = f"{hours2:02}:{minutes2:02}"
    else:
        raise ValueError
    return f"{time1} to {time2}"
        
if __name__ == "__main__":
    main()

## chatgpt shortened way
#import re

#def convert(s):
#   pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
#    match = re.match(pattern, s)
#    if not match:
#        raise ValueError
#
#    h1, m1, p1, h2, m2, p2 = match.groups()
#
#    # Default minutes to "00"
#    m1 = m1 or "00"
#    m2 = m2 or "00"
#
#    # Validate minutes
#    if not (0 <= int(m1) < 60 and 0 <= int(m2) < 60):
#        raise ValueError
#
#    time1 = to_24h(int(h1), int(m1), p1)
#    time2 = to_24h(int(h2), int(m2), p2)
#
#    return f"{time1} to {time2}"
#
#def to_24h(hours, minutes, period):
#    if hours < 1 or hours > 12:
#        raise ValueError
#
#    if period == "AM":
#        if hours == 12:
#            hours = 0
#    else:  # PM
#        if hours != 12:
#            hours += 12
#
#    return f"{hours:02}:{minutes:02}"