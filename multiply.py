import sys

if __name__ == "__main__":
    args = [float(arg) for arg in sys.argv[1:]]
    (a, b) = args
    print(a*b)
