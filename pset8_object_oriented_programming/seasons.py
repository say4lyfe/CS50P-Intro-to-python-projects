from datetime import date
import sys
import inflect

p = inflect.engine()

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def get(cls):
        birth_day = input("Date of birth: ")
        try:
            d = date.fromisoformat(birth_day)
            year = d.year
            month = d.month
            day = d.day
            return cls(year, month, day)
        except(ValueError):
            sys.exit("invalid date")
    
    def __sub__(self, other):
        self = date(self.year, self.month, self.day)
        return other - self
    
    def __str__(self):
        return f"{self.year}, {self.month}, {self.day}"

def main():
    bday_date = Date.get()
    tdy_date  = date.today()
    delta = bday_date - tdy_date
    minutes = delta.total_seconds()/60
    words = p.number_to_words(int(minutes), andword= " ").capitalize()
    print(f"{words} minutes")
    
if __name__ == "__main__":
    main()