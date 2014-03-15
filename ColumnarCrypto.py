#author TanThinh s3357678
import SpellCheckingEN

def get_factor(number):
    numberlist = []
    for x in range(2, number):
        if number % x == 0:
            numberlist.append(x)
    return numberlist

def decrypt_columnar(message):
    factor = get_factor(len(message))

    #There will be half combinations of the length but swapping around
    times = len(factor) / 2
    forward_index = 0
    backward_index = len(factor) - 1

    for x in range(0, times):

        #Create 2 lists that represent row and column,
        #first list has row(first index) and column(last index)
        #second list has row(last index) and column(first index)
        for y in range(0, 2):
            double_list = []
            message_position = 0
            if y == 0:
                for row in range(0, factor[forward_index]):
                    double_list.append([])
                    for column in range(0, factor[backward_index]):
                        double_list[row].append(message[message_position])
                        message_position += 1
            else:
                for row in range(0, factor[backward_index]):
                    double_list.append([])
                    for column in range(0, factor[forward_index]):
                        double_list[row].append(message[message_position])
                        message_position += 1

            decrypt_message = ""
            for k in range(0, len(double_list[0])):
                for z in range(0, len(double_list)):
                    decrypt_message += double_list[z][k]

            if SpellCheckingEN.check_english_message(decrypt_message.strip()) is True:
                if y is 0:
                    print "Column: " + str(factor[forward_index]) + " , Row: " + str(factor[backward_index])
                else:
                    print "Column: " + str(factor[backward_index]) + " , Row: " + str(factor[forward_index])
                print decrypt_message
                print "\n\n"

        forward_index += 1
        backward_index -= 1