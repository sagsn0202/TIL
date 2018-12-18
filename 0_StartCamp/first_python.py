def popular_words(text: str, words: list) -> dict:
    
    text_list = text.split()
    lower_text_list = list(map(lambda x: x.lower(), text_list))
    
    count_word_dict = {}
    for word in words:
        count_word_dict[word] = lower_text_list.count(word)

    return count_word_dict

print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))