#author TanThinh s3357678
import CaesarCrypto
import ColumnarCrypto
import RandomCrypto
import enchant

#Caesar crypto; key:unknown
cipher_message1 = "P)P,?;STYR'?Z('-LY;PO';Z'VYZ-'LMZ(;';SP':PN(,T;?4QZN(:PO'MWLNV SZYPAML,NPWZYL\n" + \
                "': LTYASP,P'L;'XZMTWP'-Z,WO'NZYR,P::\n" + \
                "':TWPY;'NT,NWP'LYO'RPPV: SZYP'SL)P'U(:;'LYYZ(YNPO'XZ,P'OP;LTW:'ZY';SP'MWLNV SZYP\n" + \
                "'L' SZYP'QZN(:PO'ZY':PN(,T;?'LYO' ,T)LN?\"'9MWLNV SZYP9':PPX:';Z'MP'MZ;S'L' ,ZO(N;'LYO'L'NZX LY?\n" + \
                "'L:'TY';SP'NZX LY?'MWLNV SZYP'-TWW' ,Z)TOP'( OL;P:'LYO':(  Z,;'QZ,';SP' ,ZO(N;'MWLNV SZYP\"'SL)TYR'MPPY'NZQZ(YOPO'M?' STW'$TXXP,XLY\n" + \
                "';SP'N,PL;Z,'ZQ' R 'P4XLTW'PYN,? ;TZY\n" + \
                "';SP'NZX LY?'SL:';ZY:'ZQ':PN(,T;?';LWPY;\"'MWLNV SZYP'-L:'LYYZ(YNPO'LMZ(;'L'XZY;S'LRZ\n" + \
                "'M(;';ST:'T:';SP'QT,:;';TXP'-P8,P'RP;;TYR'OP;LTW:'ZY'U(:;'-SL;';SP'MWLNV SZYP'T:'LYO'SZ-'T;'-Z,V:\""

#Columnar crypto; key:unknown
cipher_message2 = "NFEEPO IE OOPPPSSTE.ELSST KNASONPL ETO  WA  ICEGRAFC ESNR S  WDSBOY,CY-EI'TTORE I EULVL H\n" + \
                  "OPNSO KER OMVSEEORE\n" + \
                  "FT  RKEMV SAIC RGERP- AAEESOE  KCETTGSSRCAPP Y TR "

#Random substitution; key:unknown
cipher_message3 = "I\" L'0N 0QVWI0\"880WI3XX0'\",'! 606X\"3'90 XQ0I\"3LQ\"3X0LNX' 4W0:VT0'N:WQ\"3X$EXWWX30'N:WQ\"3X0QN!8" + \
                  "L0I\"BX0IX81XL0WIX0,N'WJ0E!W0WIX0'N:WQ\"3X0I\"' 4W07I\" 6XL0,!7IR$$E\"37X8N \"J0'1\"V $QIV8X0WIX06\"8\"TF0" + \
                  "'H0Q\"'0X\"'V8F0WIX0,N'W0V,1N3W\" W0WIV 60\"  N! 7XL0\"W0'\",'! 64'0,NEV8X0QN38L07N 63X''013X''0XBX " + \
                  "WJ0WIX07N,1\" F0\"8'N0'INQXL0N::0WI3XX0 XQ0',\"3W0Q\"W7IX'R0'\",'! 60LX,NXL0WIX06X\"30)J0WIX06X\"30)0 " + \
                  "XNJ0\" L0WIX06X\"30:VWR0WIX0(6\"8\"TF(0E3\" LV 60V'06N X0EX7\"!'X0WIX0Q\"W7IX'0 N08N 6X303! 0\" " + \
                  "L3NVLDWIXF4BX0'QVW7IXL0WN0'\",'! 64'0WV2X 0N'R"

# Unknown ; key = 12
cipher_message4 = "$ )\"TM-Q\"( \";T !\"$ ):\"! :W\"R :\"Q-Q:$\",)Q;(U Z" + \
                  "UR\"$ )\"; X-Q\"(TQ\".: NXQY\"BAN$\"TMZPA0\"$ )\"TM-Q\"( \"Q?.XMUZ\"T !\"$ )\"; X-QP\"(TQ\".: NXQY" + \
                  "UR\"$ )\"!: (QBM\".: S:MY\"( \"; X-Q\"(TQ\".: NXQY0\"$ )\"TM-Q\"( \";)NYU(\"$ ):\"; ):OQ\"O PQ\"!U(TBMZ\"Q?.XMZM(U Z\" R\"T !\"$ )\");QP\"U(\"( \"; X-Q\"(TQ\".: NXQY" + \
                  "$ )\"Y);(\"!:U(Q\"B$ ):\" !Z\".: S:MY;1\"$ )\"OMZZ (\"P !ZX MP\"; R(!M:Q\"R: Y\"(TQ\"UZ(Q:ZQ(\" :\"BAN :: !A\"; ):OQ\"O PQ\"R: Y\" (TQ:\";()PQZ(;" + \
                  ".XMSUM:U;Y\":)XQ;\"!UXX\"NQ\"M..XUQPB-Q:$\";(:UO(X$\"UZ\"(TQ\"YM:WUZS\" R\"(TU;\"M;;USZYQZ("

#Decrypting part !!!
# Decrypt 1
# CaesarCrypto.decrypt_caesar(cipher_message1)
CaesarCrypto.decrypt_caesar(cipher_message1, True)

# Decrypt 2
# ColumnarCrypto.decrypt_columnar(cipher_message2)

# Decrypt 3
# print RandomCrypto.get_letter_frequency(cipher_message3)

# Decrypt 4
# CaesarCrypto.decrypt_caesar_with_key(cipher_message4, 12, False)

# d = enchant.Dict("en_US")
# print d.check("J")