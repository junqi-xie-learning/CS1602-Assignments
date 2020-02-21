# File: chaos.py
	# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function\n")
    x1 = float(input("Enter the first float number between 0 and 1:"))
    x2 = float(input("Enter the second float number between 0 and 1:"))
    # the input value is 0.25 & 0.26.
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("{}\t{:.17f}\t{:.17f}".format(i + 1, x1, x2))


main()
