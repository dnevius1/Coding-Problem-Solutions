# Uses fast and slow pointers. Takes in a number and determines whether or not summing
# the squared-digits of the number eventually results in 1 or creates a cycle (ends up 
# back at the original number). If 1, returns True. If fast == slow, returns False. 
def sum_of_squared_digits(number): # Helper function that calculates the sum of squared digits.
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum

def is_happy_number(n):
    slow = n
    fast = sum_of_squared_digits(n)
    while fast != 1 and fast != slow:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))
        if fast == 1:
            return True
        if fast == slow:
            return False
    return True
