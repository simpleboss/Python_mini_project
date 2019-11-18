import string
print(string.ascii_lowercase)
email_one = open("email_one.txt", "r").read()


def get_(email, word_to_censor):
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
        if (left_character is None or left_character not in alphabets) and (right_character is None or left_character not in alphabets):
            email_censored = email_censored + 'CENSORED'
        else:
            email_censored = email_censored + word_to_censor

        remained_index = found_index + len(word_to_censor)
    email_censored = email_censored + email[remained_index:]
    return email_censored


t = get_("b", "a")
print(t)