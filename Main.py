#author TanThinh s3357678
import CaesarCrypto
import ColumnarCrypto
import RandomCrypto
import enchant

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

#Message 7 ---- Unknown ; key : unknown
f = open('msg7.enc', 'r')
cipher_message7 = f.read()
f.close()


#Decrypting part !!!

# Decrypt 1
# CaesarCrypto.decrypt_caesar(cipher_message1, True)

# Decrypt 2
# ColumnarCrypto.decrypt_columnar(cipher_message2)

# Decrypt 3
# print RandomCrypto.get_letter_frequency(cipher_message3)

# Decrypt 4
# CaesarCrypto.decrypt_caesar_with_key(cipher_message4, 12, False)

# Decrypt 7
print RandomCrypto.get_letter_frequency(cipher_message7)

# d = enchant.Dict("en_US")
# print d.check("J")