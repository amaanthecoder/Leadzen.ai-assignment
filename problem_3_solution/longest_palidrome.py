def LongestPalindromicString(string):
    if len(string) < 2:
        return string

    if len(string) == 2:
        if string == string[::-1]:
            return string
        return string[0]

    output = ""
    for i in range(len(string)):
        for j in range(len(string) - 1, i, -1):
            if string[i: j + 1] == string[i: j + 1][::-1]:
                if len(output) < len(string[i: j + 1]):
                    output = string[i: j + 1]

    if not output:
        return string[1]

    return output


string = input("Enter string: ")
print(f"Longest Palindromic String: {LongestPalindromicString(string)}")
