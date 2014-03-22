#author TanThinh s3357678


def get_words(text, length):
    temp_mess = ' '.join(text.split())
    word_list = temp_mess.split()

    return_list = []
    for x in word_list:
        if len(x) == length:
            if len(return_list) == 0:
                return_list.append(x)
            else:
                check = False
                for y in return_list:
                    if y == x:
                        check = True
                        break
                if check is False:
                    return_list.append(x)

    return return_list


def decrypt_grille(message, word_list):

    message_list = list(message)
    return_list = []

    for x in word_list:
        words = list(x)
        count = 0
        for letter in message_list:
            word_letter = words[count]
            # print "Letter: " + str(letter)
            # print "Word letter: " + str(word_letter)
            if letter == word_letter.upper():
                max_range = len(words) - 1
                if count == max_range:
                    return_list.append(x)
                    break
                else:
                    count += 1
            # print count
    print return_list