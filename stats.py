def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)
    

def character_count(text):
    words = text.lower()
    chars = {}
    for char in words:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(d):
    return d["num"]

def character_sorting(characters):
    sorted_list = []
    for ch in characters:
        sorted_list.append({"char": ch, "num": characters[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

