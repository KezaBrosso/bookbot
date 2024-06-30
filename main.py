def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_text(path_to_file)
    word_list = file_contents.split()
    word_count = count_words(word_list)
    character_count = get_char_count(file_contents)
    sorted_list = to_be_sorted(character_count)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_list:
        print(f"The {item['char']} character was found {item['num']} times")
    
    print("--- End Report ---")


def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text)

def get_char_count(text):
    my_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict

def sort_on(dict):
    return dict["num"]

def to_be_sorted(unsorted_dict):
    new_list = []
    for item in unsorted_dict:
        if item.isalpha() == True:
            new_list.append({"char": item, "num":unsorted_dict[item]})
        else:
            pass
    new_list.sort(reverse=True, key=sort_on)
    return new_list

main()