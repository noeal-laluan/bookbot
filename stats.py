def count_words(text):
    indv_words = text.split()
    return len(indv_words)

def count_chars(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    counts_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    counts_list.sort(key=lambda x: x["num"], reverse = True)

    return counts_list