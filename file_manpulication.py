import string
def count_words_in_file(file_path):
    word_count = {}
    file = open(file_path, 'r')
    text = file.read()
    file.close()
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_word_count = sorted(word_count.items())
    for word, count in sorted_word_count:
        print(f"{word}: {count}")
file_path = input("Enter the path to the text file: ")
count_words_in_file(file_path="file.py ")
