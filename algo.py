# beginning_number = input("Enter beginning number: ")
# ending_number = input("Enter ending number: ")


# def is_palindrome(input_string):
#     split_str = list(input_string)
#
#     if "" in split_str:
#         print("Space")
#     if split_str[0] == split_str[-1] and split_str[1] == split_str[-2]:
#         print("palindrome!")
#     else:
#         print("Not palindrome")
#
#
# is_palindrome(raw_input("Enter test word: "))

def fib(n):
    if n == 1 or n == 2:
        return 1
    if n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))
