def v(s):
    return all(c in '01' for c in s)

def c(s, a, b):
    cost = 0
    for i in range(len(s) - 1):
        if s[i:i+2] == "01":
            cost += a
        elif s[i:i+2] == "10":
            cost += b
    return cost

def h(s1, s2):
    return sum(1 for x, y in zip(s1, s2) if x != y)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        s = data[2 * i - 1]
        a, b = map(int, data[2 * i].split())
        
        if not v(s):
            results.append("INVALID")
            continue
        
        count_0 = s.count('0')
        count_1 = len(s) - count_0
        
        all_ones_first = '1' * count_1 + '0' * count_0
        all_zeros_first = '0' * count_0 + '1' * count_1
        
        cost_ones_first = c(all_ones_first, a, b)
        cost_zeros_first = c(all_zeros_first, a, b)
        
        if cost_ones_first < cost_zeros_first:
            best_rearranged = all_ones_first
            min_cost = cost_ones_first
            min_hamming = h(s, best_rearranged)
        elif cost_zeros_first < cost_ones_first:
            best_rearranged = all_zeros_first
            min_cost = cost_zeros_first
            min_hamming = h(s, best_rearranged)
        else:
            hamming_ones_first = h(s, all_ones_first)
            hamming_zeros_first = h(s, all_zeros_first)
            if hamming_ones_first < hamming_zeros_first:
                best_rearranged = all_ones_first
                min_cost = cost_ones_first
                min_hamming = hamming_ones_first
            else:
                best_rearranged = all_zeros_first
                min_cost = cost_zeros_first
                min_hamming = hamming_zeros_first
        
        results.append(str(min_hamming))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
