from collections import defaultdict
from string import punctuation
from math import sqrt, acos

translation_table = str.maketrans(
    punctuation+"ABCDEFGHIJKLMNOPQRSTUVWXYZ", " "*len(punctuation)+"abcdefghijklmnopqrstuvwxyz")


def document_distance(file1: str, file2: str):
    """ Returns the distance between two documents or text files. the lower the distance the more similar they are """
    file1_text = process_file(file1)
    file2_text = process_file(file2)
    file1_words = get_words_from_text_list(file1_text)
    file2_words = get_words_from_text_list(file2_text)
    file1_word_freq = get_freq_count_from_words_dict(file1_words)
    file2_word_freq = get_freq_count_from_words_dict(file2_words)
    distance = vector_angle(file1_word_freq, file2_word_freq)
    print(distance)


def process_file(file_name: str):
    """ Returns the text content of a file """
    with open(file_name) as f:
        return f.read()


def get_words_from_text_list(text: str):
    """Returns a list of words from a text"""
    words_list = []
    translated_line = text.translate(translation_table)
    words_list = translated_line.split()
    return words_list


def get_freq_count_from_words_dict(words_list: list):
    """ Takes a list of words and returns the frequency of each word from a list"""
    word_freq_dict = defaultdict(int)
    for word in words_list:
        word_freq_dict[word] += 1
    return word_freq_dict


def vector_angle(l1: dict, l2: dict):
    ''' Takes two dictonaries l1 and l2, and returns the angle between two vectors i.e., (l1.l2)/|l1||l2|'''
    numerator = inner_product(l1, l2)
    denominator = sqrt(inner_product(l1, l1)*inner_product(l2, l2))
    print(numerator/denominator)
    return acos(numerator/denominator)


def inner_product(D1: dict, D2: dict):
    """ Takes two dictonaries D1 and D2, and retuens the inner or dot product of the vectors """
    sum = 0.0
    for key in D1:
        if key in D2:
            sum += D1[key] * D2[key]
    return sum


def main():
    print("Starting")
    document_distance('./files/document_distance/dism.log',
                      './files/document_distance/CBS.log')
    print("End")


if __name__ == '__main__':
    import cProfile
    cProfile.runctx("main()", None, locals())
