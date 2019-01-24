import itertools

def LFSR():
    tempInput = input("Type in the LSFR that you want to analyze:")         #user input
    lfsr = []
    for digit in tempInput:
        lfsr.append(int(digit))                     #convert digits into array format
    allSequences = []
    for item in itertools.product([0, 1], repeat=len(lfsr)):
        allSequences.append(list(item))                 #finds all possible sequences
    subSequencesLength = []
    while len(allSequences) != 0:                       #there are still sequences to be found
        currentSequence = allSequences[0]
        History = []
        lengthOfSubsequence = 0
        while(currentSequence not in History):
            result = 0
            History.append(currentSequence)
            for i in range(0,len(lfsr)):
                result =  (result + (currentSequence[i]*lfsr[i])) % 2
            newSequence = currentSequence[1:]
            newSequence.append(result)
            currentSequence = newSequence
            lengthOfSubsequence+=1
        print(History, "length: %d"  % (lengthOfSubsequence))
        subSequencesLength.append(lengthOfSubsequence)
        for i in range(0, len(History)):
            allSequences.remove(History[i])
    print("Lenghts of subsequences: %s " %(subSequencesLength))
LFSR()
