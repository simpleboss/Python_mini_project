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
email_one_list_by_sentence = email_one.split('\n')
email_one_censored_all_instances_of_the_phrase_learning_algorithms = []
for email_one_sentence in email_one_list_by_sentence:
    if 'learning algorithms' in email_one_sentence.lower():
        email_one_sentence_list_by_word = email_one_sentence.split(' ')
        email_one_sentence_censored = []
        i = 0
        while i < len(email_one_sentence_list_by_word):
            if 'learning' == email_one_sentence_list_by_word[i].lower():
                email_one_sentence_censored.append('CENSORED')
                i += 2
            else:
                email_one_sentence_censored.append(email_one_sentence_list_by_word[i])
                i += 1
        email_one_censored_all_instances_of_the_phrase_learning_algorithms.append(' '.join(email_one_sentence_censored))
    else:
        email_one_censored_all_instances_of_the_phrase_learning_algorithms.append(email_one_sentence)
print(' '.join(email_one_censored_all_instances_of_the_phrase_learning_algorithms))


# Task 3
print('Task 3')


def getting_censor_list_of_words_and_phrases(email, proprietary_terms):
    email_list_by_sentence = email.split('\n')
    censored_email_list = []
    for email_sentence in email_list_by_sentence:
        for proprietary_term in proprietary_terms:
            if proprietary_term not in email_sentence.lower() and email_sentence not in censored_email_list:
                censored_email_list.append(email_sentence)
            else:
                break
    return '\n'.join(censored_email_list)


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
print(getting_censor_list_of_words_and_phrases(email_two, proprietary_terms))


# Task 4
print('Task 4')


def getting_censor_negative_words_twice(email, negative_words):
    email_censored = getting_censor_list_of_words_and_phrases(email, proprietary_terms)
    email_censored_list_by_sentence = email_censored.split('\n')
    count = 0
    email_censored_and_removed_negative_words_list = []
    for email_sentence in email_censored_list_by_sentence:
        for negative_word in negative_words:
            if negative_word in email_sentence:
                count += 1
                if count >= 3:
                    break
                elif email_sentence not in email_censored_and_removed_negative_words_list:
                    email_censored_and_removed_negative_words_list.append(email_sentence)
    return '\n'.join(email_censored_and_removed_negative_words_list)


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
print(getting_censor_negative_words_twice(email_three, negative_words))


# Task 5
print('Task 5')

