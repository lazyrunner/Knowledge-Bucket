#  Tutorial for various palindrome ideas 

"""
Tutorial 1 : Check if a string is a palindrome

The logic here is simple: The reverse of a string == string 
"""

def check_palindrome(s):
    """
    Visualise the solution as two pointers (begin and end) pointing to the    two ends of the string. 
    For every iteration till it both reached the middle, begin pointer takes a step ahead towards the middle and end pointer takes a step back towards the middle. At each step, s[begin] == s[end] for it to be palindrome.
    """

    # one pointer starts from beginning
    begin= 0
    # end pointer starts from end
    end = len(s)-1

    while begin <= end:
        if s[begin] != s[end]:
            return False

        begin +=1
        end -= 1

    return True


"""
Tutorai 2 : https://leetcode.com/problems/palindromic-substrings/

Here, we find palindromic contiguous substrings.

"""

# Solution 1 

test_str1 = "abba"
test_str2 = "abc"

def get_all_palindrome_type1(s):

    # outer loop which will go through each element
    palindrome = []
    for i in range(len(s)):
       str1 = s[i]
       rev = s[i]

       # every single letter is a palindrome
       palindrome.append(s[i])

       # inner loop goes from i+1 to end of string and for each 
       # letter we add it to str1 which is the straight forward 
       # substring and rev which reverses the string
       for j in range(i+1,len(s)):
           str1 += s[j]
           rev = s[j] + rev

           if str1 == rev:
               palindrome.append(str1)

    print(palindrome)
    # The time complexity of this brute force is O(n^2)


"""
 The second method is the main method that I properly understood

 We know there are two types of palindromic string - even (which has even number of characters) and odd (odd number of characters). 

 For odd case, let us consider each character in the string to be in the middle of a palindrome. 
 We will introduce two pointer left and right each pointing to the current character, the left pointer goes left by a single step and the right pointer goes right by a single step for each iteration. If the string is a palindrom s[left] = s[right].
 Otherwise, it is not a palindrome.
 For even case, left can point to current and right will point to current+1 (as we consider two characters to be the middle of a even palindromic string).
 Just like in odd, in even we again change the left and right and check if character are equal (to make it a palindrom) otherwise not.
"""
def get_all_palindrome_type2(s):

    palindrome = []

    for i in range(len(s)):

        # for odd palindrome
        left = i
        right = i

        while left >=0 and right < len(s) and s[left] == s[right]:
            if left == right:
                palindrome.append(s[left])
            else:
                palindrome.append(s[left:right+1])
            left -=1
            right +=1

        # for even palindrome
        left = i
        right = i+1

        while left >=0 and right< len(s) and s[left] == s[right]:

            palindrome.append(s[left:right+1])
            left -=1
            right +=1

    print(palindrome)
    # The time complexity is O(n^2)



if __name__ == "__main__":
    str1 = "abc"
    print(f"{str1} is a palindrome {check_palindrome(str1)}")
    str2 = "abba"
    print(f"{str2} is a palindrome {check_palindrome(str2)}")
    print(f"The string is {test_str1}")
    print("The palindromes are: ")
    get_all_palindrome_type2(test_str1)
    print(f"The string is {test_str2}")
    print("The palindromes are: ")
    get_all_palindrome_type2(test_str2)






