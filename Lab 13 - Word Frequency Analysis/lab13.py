def main():
    fileName = "numbers.txt"
    infile = open(fileName, "r")
    line1 = infile.readline()
    print (line1)
    infile.close()
    

main()