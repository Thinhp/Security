#author TanThinh s3357678
import SpellCheckingEN

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'\"\n0123456789"

tablefinal = list(alphabet)

table_length = len(tablefinal)
    
def cipher_table(number):

    initial = 0
    table_bottom = []
    while initial < table_length:
        index = initial + number
        if index >= table_length:
            index -= table_length
        table_bottom.append(tablefinal[index])
        initial += 1
    return table_bottom

def decrype_caesar(message):
    length = len(message)


    for x in range(0, len(alphabet)):

        temp_message = ""
        #The table after shifting
        temp_cipher_table = cipher_table(x)
        count = 0
        while count < length:
            index = 0
            while index < len(temp_cipher_table):
                if message[count] == tablefinal[index]:
                    temp_index = tablefinal.index(tablefinal[index])
                    temp_message += str(temp_cipher_table[temp_index])
                index += 1
            count += 1
        # print temp_message
        if SpellCheckingEN.check_english_message(temp_message.strip()) is True:
            print "Shifting number: " + str(x)
            print temp_message
            print "\n\n"