def count_ACT(dnaString):
    dnaStringUpper = dnaString.upper()
    
    countA = 0
    countC = 0
    countT = 0
    
    for i in dnaStringUpper:
        if i == 'A':
            countA += 1
        elif i == 'C':
            countC += 1
        elif i == 'T':
            countT += 1

    total_count = countA + countC + countT
    return total_count

def contains_sequence(dnaString):
    dnaStringUpper = dnaString.upper()
    return "ATGATCAAG" in dnaStringUpper

def countATGATCAAG(dnaSequence):
    dnaSequence.count('ATGATCAAG')
    return dnaSequence

def secondStringOccurs(dnaSequence2):
    dnaStringUpper = dnaSequence2.upper()
    return dnaSequence2 in dnaStringUpper

def main():
    dnaSequence = "ATGATCAAGATGATCAAGATGATCAAG"
    dnaSequence2 = "ATGATCAAG"
    
    print("Count of A, C, and T in the DNA sequence:", count_ACT(dnaSequence))

    countATGATCAAG = dnaSequence.count('ATGATCAAG')

    contains_atgatcaag = contains_sequence(dnaSequence)
    if contains_atgatcaag:
        print("The DNA sequence contains the sequence ATGATCAAG")
    else:
        print("The DNA sequence does not contain the sequence ATGATCAAG")

    print (f"The DNA sequence 'ATGATCAAG' is repeated: {countATGATCAAG}")
    
    contains_atgatcaag2 = secondStringOccurs(dnaSequence2)
    if contains_atgatcaag2:
        print(f"The DNA sequence two is repeated in DNA sequence one about: {countATGATCAAG}")
    else:
        print("The DNA sequence two does not repeat")

main()
