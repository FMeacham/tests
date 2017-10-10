import sys

if __name__ == "__main__":
    args = [float(arg) for arg in sys.argv[1:]]
    (a, b) = args
    print('The product of {0} and {1} is'.format(a, b), a*b)
    print('Hello new branch!')
