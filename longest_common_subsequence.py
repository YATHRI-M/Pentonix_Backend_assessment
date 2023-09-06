def longest_substring(s):
    substring_len = 0 #stores the length of the longest substring without repetation 
    substring_set = set() # an empty set used to keep track of the current characters without repetation
    curr_substring = '' # a variable to build substring
    start = 0 #a variable whic is used to keep track of the index of the 1st un repeated character

    for ch in s: #Iterates to the length of the string
        if ch not in substring_set:
            curr_substring += ch
            substring_set.add(ch)
            substring_len = max(substring_len, len(curr_substring))
            """The above if condition is used to build the substring, for each character it checks if that character is present in set,
            if it is not present it will add the character to the set and stores the length of the set"""
        else:
            while s[start] != ch:
                substring_set.remove(s[start])
                start += 1
            start += 1
            """if the character is present in the set, it will remove the first character from the set and set the index variable 
            i.e, start to the next character"""
    return substring_len

if __name__ == '__main__':
    s = 'abcabcbb' #passing the predefined string to the function
    """print('Enter the string')
    s = input()
    we can even accept the string from the user"""
    print(longest_substring(s))
