#author TanThinh s3357678
import CaesarCrypto
import ColumnarCrypto
import RandomCrypto
import enchant
import VernamCrypto
import GrilleCrypto

#Message 1 ---- Caesar crypto; key:unknown
f = open('msg1.enc', 'r')
cipher_message1 = f.read()
f.close()

#Message 2 ---- Columnar crypto; key:unknown
f = open('msg2.enc', 'r')
cipher_message2 = f.read()
f.close()

#Message 3 ---- Random substitution; key:unknown
f = open('msg3.enc', 'r')
cipher_message3 = f.read()
f.close()

#Message 4 ---- Unknown ; key = 12
f = open('msg4.enc', 'r')
cipher_message4 = f.read()
f.close()

#Message 5 ---- Vernam(addition) ; key: unknown
f = open('msg5.enc', 'r')
cipher_message5 = f.read()
f.close()

#Message 7 ---- Unknown ; key : unknown
f = open('msg7.enc', 'r')
cipher_message7 = f.read()
f.close()

#Message 8 ---- Columnar ; key: unknown
f = open('msg8.enc', 'r')
cipher_message8 = f.read()
cipher_message8 += " "
f.close()

#Message 9 ---- Unknown (not Vernam) ; key: unknown
f = open('msg9.enc', 'r')
cipher_message9 = f.read()
f.close()

#Message 10 ---- Vernam(addition) ; key: unknown
f = open('msg10.enc', 'r')
cipher_message10 = f.read()
f.close()

#Message 6 ---- Unknown ; key:unknown
f = open('msg6.enc', 'r')
cipher_message6 = f.read()
f.close()

#Message 11 + 12 ---- Caesar ; key: same with each other
f = open('msg11.enc', 'r')
temp_cipher11 = f.read()
f.close()
f = open('msg12.enc', 'r')
temp_cipher12 = f.read()
f.close()

#------- Decrypting part !!! --------
# Please uncomment each of these to run the program

#======== Decrypt 1 ========#
# - Result at shifting number 39

# CaesarCrypto.decrypt_caesar(cipher_message1, True)


#======== Decrypt 2 ========#
# - Result at:
#   Message number 7
#   Column: 8, Row: 20

# ColumnarCrypto.decrypt_columnar(cipher_message2, True)


#======== Decrypt 3 ========#
# - Only print the frequency of letters
# - I worked this out by using by hand

# print RandomCrypto.get_letter_frequency(cipher_message3)


#======== Decrypt 4 ========#
# CaesarCrypto.decrypt_caesar_with_key(cipher_message4, 12, False)

# Decrypt 7
# - Same as message 3, only print the frequency of letters, worked out by hand

# print RandomCrypto.get_letter_frequency(cipher_message7)


#======== Decrypt 8 and 5 ========#
# - Decrypt and get all possible results of message 8 using Columnar Tranposition
# - For each result use Vernam cryptography with offset 100

# decrypted_msg8 = ColumnarCrypto.decrypt_columnar(cipher_message8, False)
# count = 1
# for msg in decrypted_msg8:
#     print "\nVernam number: " + str(count)
#     VernamCrypto.decrypt_vernam(cipher_message5, msg[100:], False)
#     count += 1

#======== Decrypt 9 ========#
# -Use Caesar to decrypt message 9 and get hint for messaage 6

# CaesarCrypto.decrypt_caesar(cipher_message9, True)

#======== Decrypt 10 ========#
# -Copy key of message 5 and put to a file call Key5
# -Loop through the key and get the substring with the length equal to the message
# -If reach the end, exit
# -Answer is at Vernam number: 540

# f = open('Key5', 'r')
# key_msg8 = f.read()
# f.close()
# extra_range = 0
# for mark in range(len(key_msg8)):
#     print "Vernam number: " + str(mark)
#     if extra_range + len(cipher_message10) >= len(key_msg8)-1:
#         break
#     VernamCrypto.decrypt_vernam(cipher_message10, key_msg8[mark:(len(cipher_message10) + extra_range)], True)
#     extra_range += 1

#======== Decrypt 6 ========#
# -Copy words in the assignment description and put in the file 'assignment_description'
# -Read from it and put in a variable
# -Use method get_words from Grille class to get all the word that has 7 characters
# -Use method decrypt_grille to get the words in the word_list

# f = open('assignment_description', 'r')
# assignment_description = f.read()
# f.close()
# length_word = 7
# word_list = GrilleCrypto.get_words(assignment_description, length_word)
# print "Words that has " + str(length_word) + " characters in the description:"
# print word_list
# print "\nWords that are in the Grille message:"
# GrilleCrypto.decrypt_grille(cipher_message6, word_list)

#======== Decrypt 11 + 12 ========#
#Combine the two message - Getting each of character in both of them and
#added to the new variables in interleave order

# cipher_message_11_12 = ""
# for x in range(len(temp_cipher11)):
#     cipher_message_11_12 += temp_cipher11[x]
#     cipher_message_11_12 += temp_cipher12[x]
# CaesarCrypto.decrypt_caesar(cipher_message_11_12, True)