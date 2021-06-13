def buildSequence(commonSubseq, original):
    sequence = []
    rowIdx, colIdx = len(commonSubseq)-1, len(commonSubseq[0])-1

    while rowIdx > 0 and colIdx > 0:
        currentValue, refRow, refCol = commonSubseq[rowIdx][colIdx]
        refValue, _, _ = commonSubseq[refRow][refCol]
        if refValue != currentValue:
            sequence.append(original[colIdx-1])
        rowIdx = refRow
        colIdx = refCol

    return sequence

def findLongestCommonSubsequence(first: str, second: str):
    commonSubseq = [[[0, 0, 0] for _ in range(len(first)+1)] for _ in range(len(second)+1)]

    for rowIdx in range(1, len(second)+1):
        secondChar = second[rowIdx-1]
        for colIdx in range(1, len(first)+1):
            firstChar = first[colIdx-1]
            columnBeforeCount = commonSubseq[rowIdx][colIdx-1][0]
            rowBeforeCount = commonSubseq[rowIdx-1][colIdx][0]
            rowColumnBeforeCount = commonSubseq[rowIdx-1][colIdx-1][0]        

            if secondChar == firstChar and commonSubseq[rowIdx][colIdx][0] < (rowColumnBeforeCount + 1):
                commonSubseq[rowIdx][colIdx] = [rowColumnBeforeCount + 1, rowIdx-1, colIdx-1]

            if commonSubseq[rowIdx][colIdx][0] < columnBeforeCount:
                commonSubseq[rowIdx][colIdx] = [columnBeforeCount, rowIdx, colIdx-1]

            if commonSubseq[rowIdx][colIdx][0] < rowBeforeCount:
                commonSubseq[rowIdx][colIdx] = [rowBeforeCount, rowIdx-1, colIdx]


    return ' '.join(reversed(list(map(str, buildSequence(commonSubseq, first)))))

length = input() # no need to process
firstArr = list(map(int, input().split()))
secondArr = list(map(int, input().split()))
    
subseq = findLongestCommonSubsequence(firstArr, secondArr)
print(subseq)