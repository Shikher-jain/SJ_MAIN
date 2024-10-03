def countValidCombination(row):
    n = len(row)
    count = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (row[i] != row[j]) and (row[j] != row[k]):
                    count += 1
    return count

def winner(row1, row2):
    if not all(c in 'ML' for c in row1) or not all(c in 'ML' for c in row2):
        return "Invalid input"
    count1 = countValidCombination(row1)
    count2 = countValidCombination(row2)
    if count1 > count2:
        return "Ashok"
    elif count2 > count1:
        return "Anand"
    else:
        return "Draw"

row1 = "MMLMLLM"  # Ashok's row
row2 = "LMLLLMLM"   # Anand's row

row1 = "MLLM"  # Ashok's row
row2 = "LMLL"   # Anand's row

result =winner(row1, row2)
print(result)