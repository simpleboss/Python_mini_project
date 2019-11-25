import string
print(string.ascii_lowercase)
# These are the emails you will be censoring.
# The open() function is opening the text file that the emails are contained in
# and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# Task 1
# Complete

# Task 2
print('Task 2')


def get_email_censored_word_or_phrase(email, word_to_censor):
    alphabets = string.ascii_lowercase

    email_lower = email.lower()
    email_not_censored = email
    email_censored = ''
    remained_index = 0
    how_many_word_to_censor = email_lower.count(word_to_censor)
    for _ in range(how_many_word_to_censor):
        found_index = remained_index + email_lower[remained_index:].find(word_to_censor)
        email_censored = email_censored + email[remained_index:found_index]

        left_character = email[found_index - 1] if found_index > 0 else None
        right_character = email[found_index + len(word_to_censor)] if found_index + len(word_to_censor) < len(email) else None
        if (left_character is None or left_character not in alphabets) and (right_character is None or right_character not in alphabets):
            email_censored = email_censored + 'CENSORED'
        else:
            email_censored = email_censored + word_to_censor
        remained_index = found_index + len(word_to_censor)

    email_censored = email_censored + email[remained_index:]
    return email_censored


# print(get_email_censored_word_or_phrase(email_one, 'learning algorithms'))
# Test Case
test_case = [["b", "a"],
             ["a", "a"],
             ["a a a a a", "a"],
             ["A", "a"],
             ["a!", "a"],
             ["a.", "a"],
             ["ab", "a"],
             ["aab", "a"],
             ["ba", "a"],
             ["baa", "a"],
             ["ead", "a"],
             ["baaab", "a"],
             ["ab a", "a"],
             ["a ab", "a"],
             ["baab eaae", "a"]]
# for case in test_case:
#     print(case)
#     print(get_email_censored_word_or_phrase(case[0], case[1]))


# Task 3
print('Task 3')
# 3.
# Write a function that can censor not just a specific word or phrase from a body of text,
# but a whole list of words and phrases, and then return the text.
# Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two.
# proprietary_terms =
# ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]


def get_censor_list_of_words_and_phrases(email, words_to_censor):
    email_censored = email
    for word_to_censor in words_to_censor:
        email_censored = get_email_censored_word_or_phrase(email_censored, word_to_censor)
    return email_censored


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]

assert get_censor_list_of_words_and_phrases('This is my test', []) == 'This is my test', 'wrong'
assert get_censor_list_of_words_and_phrases('This is my test', ['is']) == 'This CENSORED my test', 'wrong'
assert get_censor_list_of_words_and_phrases('This is my test', ['is', 'test']) == 'This CENSORED my CENSORED', 'wrong'
assert get_censor_list_of_words_and_phrases('This is my test', ['android']) == 'This is my test', 'wrong'
# print(get_censor_list_of_words_and_phrases(email_two, proprietary_terms))


# Task 4
print('Task 4')
word_boundary_list = [' ', '.', ',', '!', '?', ':', ';', '(', ')', '[', ']', '{', '}', '\'', '\"', '-', '+', '*',
                      '\%', '=', '`', '~', '|']


def get_censor_after_negative_words_twice(email, negative_words_to_censor):
    alphabet_list_without_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               't', 'u', 'v', 'w', 'x', 'y', 'z']
    email = get_censor_list_of_words_and_phrases(email, proprietary_terms)
    negative_words_indices = []
    for word_to_censor in negative_words_to_censor:
        word_to_censor_count = email.lower().count(word_to_censor)
        word_to_censor_indices = [0]
        for i in range(word_to_censor_count):
            word_to_censored_index = email[word_to_censor_indices[-1]:].lower().find(word_to_censor)
            if email.lower()[word_to_censored_index - 1] not in alphabet_list_without_s and \
                    email.lower()[word_to_censored_index + len(word_to_censor)] not in alphabet_list_without_s:
                word_to_censor_indices.append(word_to_censored_index)
            else:
                break
        word_to_censor_indices.pop(0)
        negative_words_indices.extend(word_to_censor_indices)
    begin_index_to_censor = sorted(negative_words_indices)[1]
    email_censored = email[:begin_index_to_censor + 1] + get_censor_list_of_words_and_phrases(email[begin_index_to_censor + 1:], negative_words_to_censor)
    return email_censored


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]
# print(get_censor_after_negative_words_twice(email_three, negative_words))

# # # Task 5
print('Task 5')


def get_censor_any_words_before_and_after_censored(email):
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    email_censored = get_censor_list_of_words_and_phrases(email, proprietary_terms)
    email_censored = get_censor_list_of_words_and_phrases(email_censored, negative_words)
    print(email_censored)
    indices_of_censor = []
    for word_index, word in enumerate(email_censored.split(' ')):
        if 'CENSORED' in word:
            indices_of_censor.append(word_index)

    indices_of_previous_and_next_word_of_censor = []
    for censor_index in indices_of_censor:
        for letter_index, letter in enumerate(email_censored[censor_index+len('CENSORED'):]):
            for boundary in word_boundary_list:
                if boundary == letter:
                    continue
                else:
                    indices_of_previous_and_next_word_of_censor.append()
    email_censored_any_words_before_and_after_censored = []
    print(indices_of_censor)
    for word_index, word in enumerate(email_censored.split(' ')):
        print('=============')
        print(word)
        print(word_index)
        if word_index in indices_of_censor:
            for boundary in word_boundary_list:
                if boundary in word:
                    word_to_add += boundary
            word_to_add = word + 'CENSORED'
        else:
            word_to_add = word
        email_censored_any_words_before_and_after_censored.append(word_to_add)
    return ' '.join(email_censored_any_words_before_and_after_censored)


# print(get_censor_any_words_before_and_after_censored(email_four))
