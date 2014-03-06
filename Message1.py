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

#Use to decrype message and print out to screen possible answers
def decrypt_caesar(message):
    length = len(message)

    for x in range(1, len(Alphabet.alphabet)):
        temp_message = ""

        #The table after shifting
        temp_cipher_table = cipher_table(x)
        count = 0
        while count < length:
            index = 0
            while index < len(temp_cipher_table):
                if message[count] == Alphabet.tablefinal[index]:
                    temp_index = Alphabet.tablefinal.index(Alphabet.tablefinal[index])
                    temp_message += str(temp_cipher_table[temp_index])
                index += 1
            count += 1

        # print possible answers
        if SpellCheckingEN.check_english_message(temp_message.strip()) is True:
            print "Shifting number: " + str(x)
            print temp_message
            print "\n\n"