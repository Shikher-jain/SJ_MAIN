from typing import List

def find_subsets(N: int, R: int, strings: str) -> List[str]:
    subsets = [""]  # Rank 1: Empty set

    # Split input strings into a list
    strings_list = strings.split(",")
    
    # Add individual strings as subsets with ranks 2 to N + 1
    subsets.extend(strings_list)

    # Generate subsets with combinations of strings
    for i in range(N):
        for j in range(i + 1, N):
            subset = strings_list[i] + "," + strings_list[j]
            
            # Check if this subset is legal
            legal = True
            for k in range(j + 1, N):
                pos1 = subset.find(strings_list[k])
                pos2 = subset.find(",", pos1)
                
                # Adjust legality based on your specific requirements
                if pos1 != -1 and pos2 == -1:
                    legal = False
                    break
            
            # If legal, add it to the subsets
            if legal:
                subsets.append(subset)

    # Sort subsets based on size and order of appearance
    subsets.sort(key=lambda x: (len(x), strings_list.index(x.split(",")[0])))

    # Check if R is within valid bounds
    result = []
    if 1 <= R <= len(subsets):
        result.append(subsets[R - 1])
    else:
        result.append("Invalid rank")  # Handle invalid R
    
    return result

N = int(input("Enter number of strings: "))
R = int(input("Enter rank (R): "))
strings = input("Enter comma-separated strings: ")

# Find the R-th subset
result = find_subsets(N, R, strings)

# Output the R-th subset
print(result[0])

