#author TanThinh s3357678
import enchant

d = enchant.Dict("en_US")

def check_english_message(message):

    word_list = message.split(" ", 2)
    for x in word_list:
        if d.check(x) is True:
            return True
    return False