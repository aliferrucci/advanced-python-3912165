# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> prints out args
    Parameters:
    arg1: the first argument. Can be anything.
    arg2: the second argument. Defaults to none. Optional
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
