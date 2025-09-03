def count_words(text):
    return len(text.split())

def count_chars(text):
    dict = {}
    for c in text:
        current_c = c.lower()
        if (current_c in dict):
            dict[current_c] += 1
        else:
            dict[current_c] = 1
    return dict

def sort_on(items):
    return items["num"]

def sort_chars(dict): 
    chars_list = []
    for char in dict:
        current_char = {}
        if (char.isalpha()):
            current_char["char"] = char
            current_char["num"] = dict[char]
            chars_list.append(current_char)
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

