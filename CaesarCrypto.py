#author TanThinh s3357678
import SpellCheckingEN
import Alphabet


#Use to create the cipher table based on how many number shifting
def cipher_table(number):

    initial = 0
    table_bottom = []
    while initial < Alphabet.table_length:
        index = initial + number
        if index >= Alphabet.table_length:
            index -= Alphabet.table_length
        table_bottom.append(Alphabet.tablefinal[index])
        initial += 1
    return table_bottom


#Use to decrype message and print out to screen possible answers if boolean is False
# Only print English checking if boolean is True
def decrypt_caesar(message, boolean):
    length = len(message)

    for x in range(1, len(Alphabet.alphabet)):
        temp_message = caesar_message(message, x, length)
        # print possible answers if boolean is True
        if SpellCheckingEN.check_english_message(temp_message.strip()) is True and boolean is True \
                or boolean is False:
            print "Shifting number: " + str(x)
            print temp_message
            print "\n\n"


def decrypt_caesar_with_key(message, key, boolean):
    count = key
    change_direction = 0

    for x in range(0, 2):
        temp_message = caesar_message(message, count, len(message))
        if SpellCheckingEN.check_english_message(temp_message.strip()) is True and boolean is True\
                or boolean is False:
            if change_direction == 0:
                print "Shifting number right: " + str(key)
            else:
                print "Shifting number left: " + str(key)
            print temp_message
            print "\n\n"
        count = len(Alphabet.alphabet) - count
        change_direction = 1


#Support method for decrypt_caesar method
def caesar_message(message, times, length):
    temp_message = ""

    #The table after shifting
    temp_cipher_table = cipher_table(times)
    count = 0
    while count < length:
        index = 0
        while index < len(temp_cipher_table):
            if message[count] == Alphabet.tablefinal[index]:
                temp_index = Alphabet.tablefinal.index(Alphabet.tablefinal[index])
                temp_message += str(temp_cipher_table[temp_index])
            index += 1
        count += 1

    return temp_message
