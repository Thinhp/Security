#author TanThinh s3357678
import Alphabet

#Put the alphabet letter to the corresponding number
letter_dictionary = {}
count = 0
for x in Alphabet.tablefinal:
    letter_dictionary[x] = count
    count += 1


def decrypt_vernam(message, key, boolean):
    print "-----------BEGIN VERNAM----------"
    message_list = list(message)
    key_list = list(key)
    to_return = ""

    #Get whichever has shorter length
    total_length = len(message_list) if len(message_list) < len(key_list) else len(key_list)

    for times in range(0, total_length):

        message_number = 0
        key_number = 0
        final_letter = ''

        for letter in letter_dictionary:
            if letter == message_list[times]:
                message_number = letter_dictionary[letter]
            if letter == key_list[times]:
                key_number = letter_dictionary[letter]

        letter_minus = message_number - key_number
        if letter_minus < 0:
            letter_minus += len(letter_dictionary)
        # print "Mes_num: " + str(message_number)
        # print "Key_num: " + str(key_number)
        # print "Minus: " + str(letter_minus)

        for letter in letter_dictionary:
            if letter_minus == letter_dictionary[letter]:
                final_letter = letter
        # print "Return letter: " + str(final_letter)

        to_return += str(final_letter)

    print to_return
    return to_return