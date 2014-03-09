#author TanThinh s3357678

def get_letter_frequency(message):
    letter_list = {}

    # put all the characters into the dictionary with its frequency
    for x in message:
        if x in letter_list.keys():
            letter_list[x] += 1
        else:
            letter_list[x] = 1

    #Because the dictionary is unorder, I convert to 2D list to store
    #each character with their frequency for easily access
    temp_data_key = sorted(letter_list, key=letter_list.get)
    temp_data_value = []
    temp_data = []
    count = 0
    for id in temp_data_key:
        temp_data_value.append(letter_list[id])
    for x in range(0, len(temp_data_value)):
        temp_data.append([])
        temp_data[count].append(temp_data_key[x])
        temp_data[count].append(temp_data_value[x])
        count += 1

    return temp_data

def print_out_messages(line, letter_list):

    for x in line:
        if x in letter_list:
            print x,
        else:
            print " ",
    print ""
    for x in line:
        print x,

# This will print out
def manual_substitution(message, letter, replace):
    whole_message = ""
    for x in message:
        trigger = 0
        for y in range(0, len(letter)):
            if x == letter[y]:
                whole_message += str(replace[y])
                trigger = 1
        if trigger == 0:
            whole_message += str(x)
    return whole_message


# message: the original message
# number: how many most common letters in English we want to replace.
def replace_most_common_letters(message, number):
    the_list = get_letter_frequency(message)
    most_common_letters = []
    original_common_letter = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'U']

    #Store most 5 common letters to the list
    for index in range(0, number):
        most_common_letters.append(the_list.pop())

    # Loop and print out the most 5 common replacements
    # The most common letters in English are E, T, A, O, I, N , S, H, R, D, L, U
    letter_number = 0
    remember_list = []
    whole_message = message
    final_message = ""
    for letter in most_common_letters:
        print "Common letter number " + str(letter_number + 1) + ": " + letter[0]
        print "Converted to: " + original_common_letter[letter_number]
        print "Frequency: " + str(letter[1])

        temp_sentence = ""
        for character in whole_message:
            if character == letter[0]:
                cha = ''
                for times in range(0, number):
                    if letter_number == times:
                        cha = original_common_letter[times]
                        remember_list.append(cha)
                temp_sentence += str(cha)
            else:
                temp_sentence += str(character)
        print_out_messages(temp_sentence, remember_list)
        whole_message = temp_sentence
        final_message = temp_sentence
        print "\n"
        letter_number += 1

    #Manual substitution
    print "\n"
    letter = ['R']
    replace = ['.']
    final_message = manual_substitution(final_message, letter, replace)
    for x in replace:
        remember_list.append(x)
    print_out_messages(final_message,remember_list)

cipher_message3 = "I\" L'0N 0QVWI0\"880WI3XX0'\",'! 606X\"3'90 XQ0I\"3LQ\"3X0LNX' 4W0:VT0'N:WQ\"3X$EXWWX30'N:WQ\"3X0QN!8" + \
                  "L0I\"BX0IX81XL0WIX0,N'WJ0E!W0WIX0'N:WQ\"3X0I\"' 4W07I\" 6XL0,!7IR$$E\"37X8N \"J0'1\"V $QIV8X0WIX06\"8\"TF0" + \
                  "'H0Q\"'0X\"'V8F0WIX0,N'W0V,1N3W\" W0WIV 60\"  N! 7XL0\"W0'\",'! 64'0,NEV8X0QN38L07N 63X''013X''0XBX " + \
                  "WJ0WIX07N,1\" F0\"8'N0'INQXL0N::0WI3XX0 XQ0',\"3W0Q\"W7IX'R0'\",'! 60LX,NXL0WIX06X\"30)J0WIX06X\"30)0 " + \
                  "XNJ0\" L0WIX06X\"30:VWR0WIX0(6\"8\"TF(0E3\" LV 60V'06N X0EX7\"!'X0WIX0Q\"W7IX'0 N08N 6X303! 0\" " + \
                  "L3NVLDWIXF4BX0'QVW7IXL0WN0'\",'! 64'0WV2X 0N'R"

replace_most_common_letters(cipher_message3, 2)