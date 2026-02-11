from validator_collection import validators, errors

email = input("What is your email address? ")

try:
    validate = validators.email(email, allow_empty= False)   
    print("valid")
except(errors.InvalidEmailError):
    print("invalid")
except(ValueError):
    print("invalid")