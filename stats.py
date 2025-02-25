def count_words(text):
    return len(text.split())

def count_characters(text):
    count_dict = {}
    for character in text.lower():
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1
    return count_dict

def sort_on(dict):
    key = list(dict.keys())[0]
    return dict[key]

def get_sorted_count_characters(count_characters):
    my_list = [{key: value} for key, value in count_characters.items()]
    my_list.sort(reverse=True, key=sort_on)
    return my_list
