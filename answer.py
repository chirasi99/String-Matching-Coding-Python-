
# opening and reading the file
fptr = open("modules.txt", "r")


# creating a function to compute the LPS table
def FindLPS(p, m, LongestPrefixSuffix):
    len = 0  # length of the previous longest prefix and suffix

    LongestPrefixSuffix[0]  # LongestPrefixSuffix[0] is 0
    i = 1

    # Calculating the LongestPrefixSuffix[i] for i = 1 to m-1 using while loop
    while i < m:
        if p[i] == p[len]:
            len += 1
            LongestPrefixSuffix[i] = len
            i += 1
        else:
            if len != 0:
                len = LongestPrefixSuffix[len-1]
            else:
                LongestPrefixSuffix[i] = 0
                i += 1


# Python program for KMP string searching algorithm
def kmpSearcher(p, t):
    m = len(p)  # getting the length of the pattern
    n = len(t)  # getting the length of the text

    # create LongestPrefixSuffix[] that will hold the longest prefix and suffix values of the pattern
    LongestPrefixSuffix = [0]*m
    indexP = 0  # index for p[]
    sub_count = 0  # calculating numbers of pattern

    # Preprocess the pattern (calculate LongestPrefixSuffix[] array)
    FindLPS(p, m, LongestPrefixSuffix)

    indexT = 0  # index for t[]
    while indexT < n:
        if p[indexP] == t[indexT]:
            indexT += 1
            indexP += 1

        if indexP == m:
            sub_count += 1
            indexP = LongestPrefixSuffix[indexP-1]

        # mismatch after j matches
        elif indexT < n and p[indexP] != t[indexT]:
            if indexP != 0:
                indexP = LongestPrefixSuffix[indexP-1]
            else:
                indexT += 1
    return sub_count  # returning the how many matches are include in the text


# getting the user input as the pattern that would to be searched
string = input("\n\tEnter the Pattern : ")
pattern = string.lower()  # considering case insensitivity.

# reading file content, each line by line.
lines = fptr.readlines()

total_count = 0
# creating a new list
result_list = []
index = 0

# looping content of the file each line by line
for line in lines:
    text = line
    # getting no of matches including the relevant text
    output = kmpSearcher(pattern, text.lower())

    #  checking the no of matches are greater than 0 (if the pattern has include into the text),and then add that line into newly created list
    if output > 0:
        result_list.insert(index, line)
        total_count += output  # updating total_count variable
        # Incrementing index value
        index += 1


# closing file after reading
fptr.close()


# if the length of result_list is 0 (empty list) that means there is a no matching pattern with the texts included in the file print that pattern is not found.
if len(result_list) == 0:
    print("\n" + string + " pattern is not found in the file\n")

else:
    # displaying the lines containing given pattern
    linelenght = len(result_list)
    print("\n")
    # creating a for loop and displaying pattern included texts in the newly created list
    for i in range(linelenght):
        print(end=result_list[i])

    # printing the number of matching texts including the file with the relevant pattern
    print("\tNumber of matches : ", total_count, "\n")
