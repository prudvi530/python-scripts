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

please check number_reverse_v2.py for advance version of the script


'''



def reverse(x):
    rev=0
    temp=0
    x_l=len(str(x))
    y=x
    if x < 0:
       str_x = str(x)
       str_n_x = str_x[1::]
       x_n_l=len(str(str_n_x))
       x = int(str_n_x)
       while x_n_l > 0:
           pop = x % 10
           x /= 10
           temp = (int(rev) * 10) + int(pop)
           rev = temp
           x_n_l -=1
    else:
        while x_l > 0:
            pop = x % 10
            x /= 10
            temp = (int(rev) * 10) + int(pop)
            rev = temp
            x_l -=1

    if temp > ( 2**31 - 1) or temp < (-2**31):
        return 0
    else:
        if y < 0:
            return -temp
        else:
            return temp



def main():
    x=1534236469 # sample value
    get_reverse_number=reverse(x)
    print(get_reverse_number)

if __name__ == '__main__':
    main()