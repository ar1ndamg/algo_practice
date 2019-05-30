import os
import re
from math import sqrt



def main(corpus_file_name, test_sets_file, commonwords_file_name=None):
    start_time = os.times()
    # read commonwords file
    try:
        common = open(commonwords_file_name)
        common_words = common.read().splitlines()

    except:
        print("Warning: common words file was not found. Hence, ignoring it. ")
        common_words = []
    # read corpus file
    try:
        s = open(corpus_file_name)
        # replace unnecessary \n with spaces
        text = s.read().replace('\n', ' ').lower()
        if not text.strip():
            print("[error] Empty corpus file!")
            return
        # split lines
        lines = re.split(r'\?|!|\.', text)
        #print("[debug] Line spliting completed.")
    except:
        print("[error] Corpus file was not found!")
        return
    # read target sets file
    try:
        test_sets_file = open(test_sets_file)
        test = test_sets_file.read().strip()
        if not test:
            print("[error] Empty tests set file!")
            return
        target_dict = {}
        test_lines = test.splitlines()
        for index in range(len(test_lines)):
            if index == 0 or (test_lines[index].strip() and not test_lines[index-1].strip()):
                target = test_lines[index].strip().lower()
                target_dict[target] = []
            else:
                if test_lines[index].strip():
                    target_dict[target].append(
                        test_lines[index].strip().lower())
    except:
        print("[error] Test sets file was not found!")
        return
    words_count_dict = {}  # counts distinct words in the corpus file
    words_word_count_dict = {}  # keeps track of associated words frequencies
    # make words list with frequency
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # using regex to get words from a line
        words = re.split(r'\?|\"|!|;|\-{2}|:|\[|\]|\(|\)|\.|,|\s', line)
        # print("[debug]Line:", line)
        # print("[debug]Words:", words)
        for word in words:
            if word in common_words or not word.strip():
                continue
            # if it the first time we see the word add it to word_count_dict and create a new dictonary under words_word_count_dict to keep track of associated words frequencies
            # otherwise increase the word count
            if word in words_count_dict:
                words_count_dict[word] += 1
            else:
                words_count_dict[word] = 1
                words_word_count_dict[word] = {}
            # iterate through other words in the line to crate the associated frequency count
            for other_words in words:
                if other_words in common_words or word == other_words or not other_words.strip():
                    continue
                if other_words in words_word_count_dict[word]:
                    words_word_count_dict[word][other_words] += 1
                else:
                    words_word_count_dict[word][other_words] = 1

    # Printing the data structures
    # temp = sorted(words_count_dict, key=words_count_dict.get, reverse=True)
    # print("[debug] printing the words_word_count_dict:")
    # for word in temp:
    #     print(word, words_count_dict[word], '\t')
    #     for other_word in sorted(words_word_count_dict[word].keys()):
    #         print('\t', other_word, words_word_count_dict[word][other_word])

    # Cosine similarity scoring
    cosine_metric = {}
    for target in target_dict:
        cosine_metric[target] = {}
        try:
            target_profile = set(words_word_count_dict[target].keys())
        except:
            print(
                "[error] target_word {} was not present in corpus file!".format(target))
            continue
        for test_word in target_dict[target]:
            try:
                test_profile = set(words_word_count_dict[test_word].keys())
            except:
                print(
                    "[error] test_word {} was not present in corpus file!".format(test_word))
                continue
            matches = target_profile.intersection(test_profile)
            # casually printing the matches for debugging perpose
            # print("[debug]", "target_word:", target,
            #       'test_word:', test_word, ", matches found:", matches)
            numerator = 0
            sum1 = 0
            sum2 = 0

            for word in matches:
                numerator += words_word_count_dict[target][word] * \
                    words_word_count_dict[test_word][word]
            for word in target_profile:
                sum1 += words_word_count_dict[target][word]**2
            for word in test_profile:
                sum2 += words_word_count_dict[test_word][word]**2

            denominator = sqrt(sum1*sum2)
            if denominator:
                score = float(numerator)/denominator
            else:
                score = 0.0
            cosine_metric[target][test_word] = score

    # printing cosine metrics and synonym
    for target in cosine_metric:
        print("[debug] target_word:", target)
        temp = sorted(cosine_metric[target],
                      key=cosine_metric[target].get, reverse=True)
        for test in temp:
            print('\t', test, cosine_metric[target][test])
        # you can set any threshold here and use a for loop for multiple synonyms
        if temp and cosine_metric[target][test] > 0.0:
            print(">>Synnonym of {} is {}.".format(target, temp[0]))
        else:
            print(">>Synonym for {} not found!".format(target))

    # Execution time
    finish_time = os.times()
    print("\n[debug] Execution Times - User: {0:0.2f} Sys: {1:0.2f}".format(finish_time[0] - start_time[0], finish_time[1] - start_time[1]))


if __name__ == '__main__':   
    main('lifeOnMississippi.txt', 'test.txt', 'common.txt')
    
