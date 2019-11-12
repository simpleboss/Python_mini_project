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
    email_list_by_word = email.split(' ')
    email_censored = []
    i = 0
    while i < len(email_list_by_word):
        is_censored = False
        j = 0
        while word_to_censor.split()[j] in email_list_by_word[i + j].lower():
            if j == len(word_to_censor.split()) - 1:
                is_censored = True
                email_list_by_word_to_scan = email_list_by_word[i + j].lower()
                email_list_by_word_to_scan_censored = email_list_by_word_to_scan.replace(word_to_censor.split()[j], 'CENSORED')
                email_censored.append(email_list_by_word_to_scan_censored)
                i += j + 1
                break
            else:
                j += 1
        if not is_censored:
            email_censored.append(email_list_by_word[i])
            i += 1
    return ' '.join(email_censored)


print(get_email_censored_word_or_phrase(email_one, 'learning algorithms'))


# Task 3


print('Task 3')


def get_censor_list_of_words_and_phrases(email, words_to_censor):
    email_list_by_word = email.split(' ')
    email_censored = []
    i = 0
    while i < len(email_list_by_word):
        is_censored = False
        for word_to_censor in words_to_censor:
            j = 0
            while word_to_censor.split()[j] in email_list_by_word[i + j].lower():
                if j == len(word_to_censor.split()) - 1:
                    is_censored = True
                    email_list_by_word_to_scan = email_list_by_word[i + j].lower()
                    email_list_by_word_to_scan_censored = email_list_by_word_to_scan.replace(word_to_censor.split()[j], 'CENSORED')
                    email_censored.append(email_list_by_word_to_scan_censored)
                    i += j + 1
                    break
                else:
                    j += 1
        if not is_censored:
            email_censored.append(email_list_by_word[i])
            i += 1
    return ' '.join(email_censored)


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
print(get_censor_list_of_words_and_phrases(email_two, proprietary_terms))


# Task 4
print('Task 4')


def get_censor_after_negative_words_twice(email, words_to_censor):
    pass


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                      "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                      "distressed", "concerning", "horrible", "horribly", "questionable"]
print(get_censor_after_negative_words_twice(email_three, negative_words))
# # Task 5
# print('Task 5')
