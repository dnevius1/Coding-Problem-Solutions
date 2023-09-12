#Left and right pointer traverses string to tell if string can be a palindrome by removing at most one character.
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    right_mismatch = 0
    left_mismatch = 0
    mismatch = 0
    while left <= right:
        if mismatch > 1:
            return False
        if s[left] == s[right]:
            left = left + 1
            right = right - 1
            print("main if")
        else:
            # skip right index
            mismatch += 1
            SR_right = right - 1
            SR_left = left
            print("main else ")
            while SR_left <= SR_right:
                print("SR")
                if s[SR_left] == s[SR_right]:
                    SR_left = SR_left + 1
                    SR_right = SR_right - 1
                else:
                    SR_left = SR_left + 1
                    SR_right = SR_right - 1
                    right_mismatch += 1
            # skip left index
            SL_right = right
            SL_left = left + 1
            while SL_left <= SL_right:
                print("SL")
                if s[SL_left] == s[SL_right]:
                    SL_left = SL_left + 1
                    SL_right = SL_right - 1
                else:
                    SL_left = SL_left + 1
                    SL_right = SL_right - 1
                    left_mismatch += 1
            left = left + 1
            right = right - 1
            if right_mismatch and left_mismatch != 0:
                return False
            else:
                return True
    return False


s = "madame"
ispala = is_palindrome(s)
print(ispala)
