from string import punctuation

s = "Việc học tập là rất quan trọng, cho nên, cần học, học nữa, học mãi"

def get_most_frequent_word(s):
    result = []
    used_words = []
    max = 0
    for i in s :
        if i in punctuation:
            s = s.replace(i,"")
    s = s.lower().split(" ")
    for i in s:
        if i in used_words:
            pass
        else:
            if s.count(i) > max:
                result = [[i,s.count(i)]]
                max = s.count(i)
            elif s.count(i) == max:
                result.append([i,s.count(i)])
            used_words.append(i)
    for i in result:
        print(f"Từ xuất hiện nhiền nhất là \"{i[0]}\" với tần suất là {i[1]} ")
    return result

def get_words_length(s):
    result = []
    for i in punctuation:
            s = s.replace(i," ")
    s = s.split(" ")
    for i in s:
        result.append([i, len(i)])
    print(result)
    return result


def find_words (s, dictionary):
    result = []
    dictionary = " ".join(dictionary)
    print(dictionary)
    for i in punctuation:
        s = s.replace(i, " ")
    s = s.split(" ")
    dictionary = dictionary.split(" ")
    for i in dictionary:
        if i in s:
            if i not in result:
                result.append(i)
    print(result)


task_1 = get_most_frequent_word(s)
get_words_length(s)

dic = {"học", "nữa", "học sinh", "học bạ", "mãi", "học tập"}
find_words(s,dic)


