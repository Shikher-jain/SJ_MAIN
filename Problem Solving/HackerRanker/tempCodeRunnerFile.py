import re
import os
import math
import random
import sys
def reverse_words_order_and_swap_cases(sentence):
    word_list = sentence.split()
    print(word_list)
    reversed_list = word_list[:: -1]
    reversed_sentence = " ".join(reversed_list)
    return reversed_sentence.swapcase()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    sentence = raw_input()
    result = reverse_words_order_and_swap_cases(sentence)
    fptr.write(result + '\n')
    fptr.close()