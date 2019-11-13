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
    alphabet_list_without_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # print('count(word_to_censor) :' + str(email_censored_list[-1].lower().count(word_to_censor)))

    email_censored_list = [email]
    word_to_censor_count = email_censored_list[0].lower().count(word_to_censor)
    for i in range(word_to_censor_count):
        # print('================================')
        # print('word_to_censor :' + word_to_censor)
        # print(' i :' + str(i))
        # print('email_censored_list[i].lower().find(word_to_censor) :' + str(email_censored_list[i].lower().find(word_to_censor)))
        if email_censored_list[i][email_censored_list[i].lower().find(word_to_censor) - 1] \
                in alphabet_list_without_s or\
                email_censored_list[i][email_censored_list[i].lower().find(word_to_censor) + len(word_to_censor)]\
                in alphabet_list_without_s:
            email_censored_list.append(email_censored_list[-1])
        else:
            email_censored_list.append('')
            email_censored_list[-1] += \
                email_censored_list[i][:email_censored_list[i].lower().find(word_to_censor)] + \
                "CENSORED" + \
                email_censored_list[i][email_censored_list[i].lower().find(word_to_censor)+len(word_to_censor):]
    return email_censored_list[-1]


# print(get_email_censored_word_or_phrase("She is pretty.\ntestshetest is pretty.", 'she'))
print(get_email_censored_word_or_phrase(email_one, 'learning algorithms'))


# Task 3


print('Task 3')


def get_censor_list_of_words_and_phrases(email, words_to_censor):
    email_censored_words_to_censor = [email]
    for index, word_to_censor in enumerate(words_to_censor):
        email_censored_words_to_censor.append(get_email_censored_word_or_phrase(email_censored_words_to_censor[index], word_to_censor))
        # print(get_email_censored_word_or_phrase(email_censored_words_to_censor, word_to_censor))
    return email_censored_words_to_censor[-1]


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
print(get_censor_list_of_words_and_phrases(email_two, proprietary_terms))
# print(get_censor_list_of_words_and_phrases(email_two, ["she", "personality matrix", "abcdefg"]))


# # Task 4
print('Task 4')


def get_censor_after_negative_words_twice(email, negative_words_to_censor):
    email_censored_after_negative_words_twice = ''
    email_censored = get_censor_list_of_words_and_phrases(email, proprietary_terms)
    negative_count = 0
    for email_index, email_word in enumerate(email_censored.split(' ')):
        word_to_add = ' '+email_word
        for word in negative_words:
            if word in email_word.lower():
                if negative_count == 2:
                    word_to_add = email_word.replace(word, " CENSORED")
                else:
                    negative_count += 1
        email_censored_after_negative_words_twice += word_to_add
    return email_censored_after_negative_words_twice


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                      "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                      "distressed", "concerning", "horrible", "horribly", "questionable"]
# print(get_censor_after_negative_words_twice(email_three, negative_words))


# # # Task 5
print('Task 5')


def get_censor_any_words_before_and_after_censored(email):
    email_censored = get_censor_list_of_words_and_phrases(email, proprietary_terms)
    email_censored = get_censor_list_of_words_and_phrases(email, negative_words)
    indices_to_censor = []
    for word_index, word in enumerate(email_censored.split(' ')):
        if 'CENSORED' in word:
            indices_to_censor.append(word_index - 1)
            indices_to_censor.append(word_index)
            indices_to_censor.append(word_index + 1)

    email_censored_any_words_before_and_after_censored = []
    for word_index, word in enumerate(email_censored.split(' ')):
        if word_index in indices_to_censor:
            word_to_add = 'CENSORED'
        else:
            word_to_add = word
        email_censored_any_words_before_and_after_censored.append(word_to_add)
    return ' '.join(email_censored_any_words_before_and_after_censored)


# print(get_censor_any_words_before_and_after_CENSORED(email_four))
