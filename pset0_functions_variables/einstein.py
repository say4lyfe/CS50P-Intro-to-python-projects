def main():
    x = int(input("what is the mass in kgs?"))
    print("the energy in joules is", eqn(x))

def eqn(m):
    return m * 300000000 * 300000000

main()
