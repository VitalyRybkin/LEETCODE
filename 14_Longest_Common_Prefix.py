"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

strs = ["flower", "flow", "flight"]


def longestCommonPrefix(strs: list[str]) -> str:
    res = ""
    first = strs[0]
    prefs_dict = {}
    for i in range(len(min(strs))):
        prefs_dict[first[0 : i + 1]] = i
        for j in range(len(strs)):
            if strs[j][0 : i + 1] in prefs_dict.keys():
                if j == len(strs) - 1:
                    res = first[0 : i + 1]
            else:
                return res
    return res


print(longestCommonPrefix(strs))
