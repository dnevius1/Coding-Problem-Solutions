def circular_array_loop(nums):  
    size = len(nums)

    # Iterate through each element in array
    for i in range(size):
        slow = fast = i
        # Positive values indicate forward 
        # direction. Negative for reverse.
        forward = nums[i] > 0

        while True:
            slow = next_step(slow, nums[slow], size)
            if is_not_cycle(nums, forward, slow):
                break
            
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break

            if slow == fast:
                return True

    return False

# Function to calculate the next step. Returns
# an integer representing the next index.
def next_step(pointer, value, size):
    # Calculate next index
    result = (pointer + value) % size
    if result < 0:
        result += size
    return result

# Function to decide if a cycle exists. 
def is_not_cycle(nums, prev_direction, pointer):
    curr_direction = nums[pointer] >= 0
    # If directions are different or next index
    # is the same index, there is no cycle.
    if (prev_direction != curr_direction) or (abs(nums[pointer] % len(nums)) == 0):
        return True
    else:
        return False
