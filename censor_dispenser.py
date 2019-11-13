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
    if len(email) < len(word_to_censor):
        return email
    email_censored = ''
    pass_count = 0
    alphabet_list_without_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for email_index, email_letter in enumerate(email):
        if email_index < pass_count:
            continue
        equal_count = 0
        letter_to_add = ''
        for word_index, word_letter in enumerate(word_to_censor):
            pass_count = email_index + word_index + 1
            letter_to_add += email[email_index + word_index]
            if email[email_index + word_index].lower() == word_letter.lower():
                equal_count += 1
            else:
                email_censored += letter_to_add
                break

            if equal_count == len(word_to_censor):
                if email[email_index + word_index + 1] in alphabet_list_without_s:
                    email_censored += email[email_index: email_index + len(word_to_censor) + 1]
                else:
                    email_censored += 'CENSORED'
    return email_censored

# for loop with range(len(email))
    # i = 0
    # for j in range(len(email)):
    #     if word_to_censor[i].lower() == email[j].lower():
    #         equal_count += 1
    #         i += 1
    #     else:
    #         email_censored += email[j-i:j+1]
    #         i = 0
    #         equal_count = 0
    #         continue
    #
    #     if i == len(word_to_censor):
    #         # print('found')
    #         # print(i)
    #         # print(equal_count)
    #         # print(len(word_to_censor)+1)
    #         # print(email[j+1].lower())
    #         if equal_count == len(word_to_censor) and email[j+1].lower() not in alphabet_list:
    #             word_to_add = 'CENSORED'
    #         else:
    #             word_to_add = email[j-len(word_to_censor):j+1]
    #         equal_count = 0
    #         i = 0
    #         email_censored += word_to_add
    # return email_censored


# print(get_email_censored_word_or_phrase(email_one, 'learning algorithms'))


# Task 3


print('Task 3')


def get_censor_list_of_words_and_phrases(email, words_to_censor):
    email_censored = email
    for word_to_censor in words_to_censor:
        email_censored = get_email_censored_word_or_phrase(email_censored, word_to_censor)
    return email_censored


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
# print(get_censor_list_of_words_and_phrases(email_two, proprietary_terms))


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
#print(get_censor_after_negative_words_twice(email_three, negative_words))

# # # Task 5
print('Task 5')


def get_censor_any_words_before_and_after_CENSORED(email):
    email_censored = get_censor_list_of_words_and_phrases(email, proprietary_terms)
    email_censored = get_censor_list_of_words_and_phrases(email, negative_words)
    indices_to_censor = []
    for word_index, word in enumerate(email_censored.split(' ')):
        if 'CENSORED' in word:
            indices_to_censor.append(word_index - 1)
            indices_to_censor.append(word_index)
            indices_to_censor.append(word_index + 1)

    email_censored_any_words_before_and_after_CENSORED = []
    for word_index, word in enumerate(email_censored.split(' ')):
        if word_index in indices_to_censor:
            word_to_add = 'CENSORED'
        else:
            word_to_add = word
        email_censored_any_words_before_and_after_CENSORED.append(word_to_add)
    return ' '.join(email_censored_any_words_before_and_after_CENSORED)


print(get_censor_any_words_before_and_after_CENSORED(email_four))
