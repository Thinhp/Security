#author TanThinh s3357678
import SpellCheckingEN

def get_factor(number):
    numberlist = []
    for x in range(2, number):
        if number % x == 0:
            numberlist.append(x)
    return numberlist


def decrypt_columnar(message, boolean):
    factor = get_factor(len(message))
    to_return = []
    count = 1

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

            if SpellCheckingEN.check_english_message(decrypt_message.strip()) is True and boolean is True \
                    or boolean is False:
                if y is 0:
                    print "Column: " + str(factor[forward_index]) + " , Row: " + str(factor[backward_index])
                else:
                    print "Column: " + str(factor[backward_index]) + " , Row: " + str(factor[forward_index])
                print "Message number: " + str(count)
                count += 1
                print decrypt_message
                to_return.append(decrypt_message)
                print "\n\n"

        forward_index += 1
        backward_index -= 1
    return to_return


def decrypt_columnar_multiple_times(message, times):
    message_list = [message]

    for count in range(0, times):
        temp_list = []

        print "---------Times: " + str(count + 1) + " -----------"
        for x in range(0, len(message_list)):
            temp_decrypt = decrypt_columnar(message_list.pop(), False)
            for y in temp_decrypt:
                temp_list.append(y)
        message_list = temp_list