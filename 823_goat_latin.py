#  https://leetcode.com/problems/goat-latin/description/

def toGoatLatin(sentence):

    sentence_str = str(sentence)
    sentence_list = list(sentence_str.split(' '))
    result = []

    for i in range(0, len(sentence_list), 1):
        temp_str = ''
        if sentence_list[i][0] in ['a','e','i','o','u','A','E','I','O','U']:
            temp_str = sentence_list[i] + 'ma'
        elif sentence_list[i][0] not in ['a','e','i','o','u','A','E','I','O','U']:
            temp_str = sentence_list[i][1:] + sentence_list[i][0] + 'ma'
            
        temp_str = temp_str + (i+1) * 'a'
        
        result.append(temp_str)

    result = ' '.join(result)

    print(result)
    return result


toGoatLatin("I speak Goat Latin")