def main():
    fname = input("Enter a filename: ")
    infile = open(fname, "r")
    data = infile.read()
    numbers = data.split()
    numbers = [int(num) for num in numbers]
    average = sum(numbers)/len(numbers)
    print(f"The average is: {average}")
    infile.close()

main()