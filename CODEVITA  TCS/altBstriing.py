def alternatingString(Bstring, Corrlist):
    n = len(Bstring)  
    pattern1 = ''.join('1' if i % 2 == 0 else '0' for i in range(n))
    pattern2 = ''.join('0' if i % 2 == 0 else '1' for i in range(n))
    cost_pattern1 = sum(Corrlist[i] for i in range(n) if Bstring[i] != pattern1[i])
    cost_pattern2 = sum(Corrlist[i] for i in range(n) if Bstring[i] != pattern2[i])
    return min(cost_pattern1, cost_pattern2),pattern1,pattern2

Bstring = "100101110110"
Corrlist = [5, 19, 8, 7, 6, 15, 4, 3, 2, 1, 10, 8]

# Bstring  = input()
# Corrlist = map(int,input().split())

result = alternatingString(Bstring, Corrlist)
print(result)  # Output: 16

# # def max_worth_removal(binary_string, worth_list):
# #     n = len(binary_string)
# #     # if binary_string[0]=='1':
# #     pattern1 = ''.join('1' if i % 2 == 0 else '0' for i in range(n))
# #     cost_pattern1 = sum(worth_list[i] for i in range(n) if binary_string[i] != pattern1[i])
# #         # return cost_pattern1
# #     # if binary_string[0]=='0':
# #     pattern2 = ''.join('0' if i % 2 == 0 else '1' for i in range(n))
# #     cost_pattern2 = sum(worth_list[i] for i in range(n) if binary_string[i] != pattern2[i])
# #         # return cost_pattern2
    
# #     return cost_pattern1, cost_pattern2,pattern1, pattern2


# # binary_string = input().strip()
# # worth_list = list(map(int, input().strip().split()))


# # result = max_worth_removal(binary_string, worth_list)
# # print(result)

# def max_worth_removal(binary_string, worth_list):
#     n = len(binary_string)
#     total_worth = sum(worth_list)
#     max_kept_worth = 0
    
#     for start_char in ('0', '1'):  # Try starting with '0' and '1'
#         kept_worth = 0
#         prev_char = None
        
#         for i in range(n):
#             if prev_char is None or binary_string[i] != prev_char:
    
#                 kept_worth += worth_list[i]
#                 prev_char = binary_string[i]
        
    
#         max_kept_worth = max(max_kept_worth, kept_worth)
    
#     removal_cost = total_worth - max_kept_worth
#     return removal_cost

# # Input
# binary_string = input().strip()
# worth_list = list(map(int, input().strip().split()))

# # Output
# result = max_worth_removal(binary_string, worth_list)
# print(result)

#   ---------------------------------------


s=input()
arr=list(map(int,input().split()))
res=0
n=len(s)
last_digit_s=int(s[0])
last_digit_arr=arr[0]

for i in range(1,n):
  if int(s[i]) - 0 == last_digit_s :
    res += min(arr[i],last_digit_arr)
    last_digit_arr = max(arr[i],last_digit_arr)
  else:
    last_digit_s =int(s[i]) - 0
    last_digit_arr =arr[i]
print(res)
