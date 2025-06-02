def count_words(text):
    text_list = list(text)
    return(len(text_list))
print(count_words("hgjdfkl"))


def average_word_length(text):
    text_list1 = list(text.split(" "))
    x = []
    for word in text_list1:
        leng = len(word)
        x.append(leng)

    av = sum(x)/len(x)
    return av
print(average_word_length("hhdk fkfjfjfj jff"))

    