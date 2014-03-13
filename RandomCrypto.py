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