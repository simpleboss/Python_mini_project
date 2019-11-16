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
    alphabet_list_without_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               't', 'u', 'v', 'w', 'x', 'y', 'z']
    email_censored = email
    word_to_censor_count = email.lower().count(word_to_censor)
    for i in range(word_to_censor_count):
        word_to_censored_index = email_censored.lower().find(word_to_censor)
        if email_censored[word_to_censored_index - 1] not in alphabet_list_without_s and email_censored[word_to_censored_index + len(word_to_censor)] not in alphabet_list_without_s:
            email_censored = email_censored[:word_to_censored_index] + "CENSORED" + email_censored[word_to_censored_index + len(word_to_censor):]
    return email_censored


print(get_email_censored_word_or_phrase(email_one, 'learning algorithms'))


# Task 3
print('Task 3')


def get_censor_list_of_words_and_phrases(email, words_to_censor):
    email_censored_words_to_censor = [email]
    for index, word_to_censor in enumerate(words_to_censor):
        email_censored_words_to_censor.append(
            get_email_censored_word_or_phrase(email_censored_words_to_censor[index], word_to_censor))
        # print(get_email_censored_word_or_phrase(email_censored_words_to_censor, word_to_censor))
    return email_censored_words_to_censor[-1]


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]
# print(get_censor_list_of_words_and_phrases(email_two, proprietary_terms))


# # Task 4
print('Task 4')

word_boundary_list = [' ', '.', ',', '!', '?', ':', ';', '(', ')', '[', ']', '{', '}', '\'', '\"', '-', '+', '*',
                      '\%', '=', '`', '~', '|']
def get_censor_after_negative_words_twice(email, negative_words_to_censor):
    email_censored_from_task3_function = get_censor_list_of_words_and_phrases(email, proprietary_terms)
    negative_words_indices_list = []
    for negative_word in negative_words_to_censor:
        last_found_index = len(email_censored_from_task3_function) - 1
        for current_word_index in range(0, len(email_censored_from_task3_function), last_found_index):
            if email_censored_from_task3_function[
                email_censored_from_task3_function.find(negative_word, current_word_index) - 1] in word_boundary_list and \
                    email_censored_from_task3_function[
                        email_censored_from_task3_function.find(negative_word, current_word_index) + len(negative_word)] \
                    in word_boundary_list:
                negative_words_indices_list.append(email_censored_from_task3_function.find(negative_word))
                last_found_index = email_censored_from_task3_function.find(negative_word, current_word_index)
            else:
                break
    print('negative_words_indices_list :' + str(negative_words_indices_list))
    print('sort()' + str(sorted(negative_words_indices_list)))
    email_censored_after_negative_words_twice = \
        email_censored_from_task3_function[:sorted(negative_words_indices_list)[1]+1] + \
        get_censor_list_of_words_and_phrases\
            (email_censored_from_task3_function[sorted(negative_words_indices_list)[1]+1:], negative_words)
    return email_censored_after_negative_words_twice


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
