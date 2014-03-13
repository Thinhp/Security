#author TanThinh s3357678
import enchant
import re

d = enchant.Dict("en_US")


def check_english_message(message):

    temp_mess = ' '.join(message.split())
    word_list = temp_mess.split()
    for x in word_list:
        if d.check(x) is True:
            return True
    return False