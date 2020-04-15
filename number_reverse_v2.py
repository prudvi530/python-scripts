'''
leet code Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

please check number_reverse_v1.py for basic version of the script

'''

'''
abs() function will give you the absolute value of a number 
example : 
abs(321) is 321 and abs(-321) will be 321 
so we can use abs function and avoid multiple loops , one for postive numbers , one for negative numbers as we did in version 1

now we need to iterate the value and perform required actions to get the reverse number as per the requirement 
'''


def reverse(x):
    temp = 0
    original_value = x
    while int(abs(x)) > 0:
        x = abs(int(x))
        temp = int(temp*10) + int(x % 10)
        x /= 10
    if temp > 2**31 - 1 or temp < -2**31:
        return 0
    elif original_value < 0:
        return -temp
    else:
        return temp

def main():
    x=-120 # sample value , replace it to test more use cases
    get_reverse_number = reverse(x)
    print(get_reverse_number)


if __name__ == '__main__':
    main()