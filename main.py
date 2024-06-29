def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    dict = count_characters(file_contents)
    chars_sorted = chars_to_sort(dict)
    print_report(word_count, chars_sorted)

def count_words(words):
    total_words = words.split()
    return len(total_words)
    
def count_characters(text):
    lowered_text = text.lower()
    new_dict = {}
    for char in lowered_text:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    return(new_dict)

def chars_to_sort(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict_item):
    return dict_item["num"]

def print_report(words, sorted_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(words) + " words found in document")
    print("")

    for char in sorted_dict:
        if not char["char"].isalpha():
            continue
        print(f"the '{char['char']}' character was found {char['num']} times")

    print("--- End report ---")

main()