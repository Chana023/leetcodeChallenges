# https://leetcode.com/problems/ransom-note/description/

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    ransomNote_dict = {}
    magazine_dict = {}
    checker = True
    for i in range(0, len(ransomNote), 1):
        if ransomNote[i] not in ransomNote_dict:
            ransomNote_dict[ransomNote[i]] = 1
        elif ransomNote[i] in ransomNote_dict:
            ransomNote_dict[ransomNote[i]] = ransomNote_dict[ransomNote[i]] + 1

    for i in range(0, len(magazine), 1):
        if magazine[i] not in magazine_dict:
            magazine_dict[magazine[i]] = 1
        elif magazine[i] in ransomNote_dict:
            magazine_dict[magazine[i]] = magazine_dict[magazine[i]] + 1


    if len(magazine_dict) < len(ransomNote_dict):
        print('False')
        return False    
    else:
        for key, value in ransomNote_dict.items():
            if key in magazine_dict:
                if magazine_dict[key] < ransomNote_dict[key]:
                    print("False")
                    return False
            else:
                print("False")
                return False
    
    print("True")
    return True


word1 = 'a'
word2 = 'a'

canConstruct(word1, word2)



