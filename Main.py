#author TanThinh s3357678
import Message1
import Message2
import enchant

cipher_message1 = "P)P,?;STYR'?Z('-LY;PO';Z'VYZ-'LMZ(;';SP':PN(,T;?4QZN(:PO'MWLNV SZYPAML,NPWZYL\n" + \
                "': LTYASP,P'L;'XZMTWP'-Z,WO'NZYR,P::\n" + \
                "':TWPY;'NT,NWP'LYO'RPPV: SZYP'SL)P'U(:;'LYYZ(YNPO'XZ,P'OP;LTW:'ZY';SP'MWLNV SZYP\n" + \
                "'L' SZYP'QZN(:PO'ZY':PN(,T;?'LYO' ,T)LN?\"'9MWLNV SZYP9':PPX:';Z'MP'MZ;S'L' ,ZO(N;'LYO'L'NZX LY?\n" + \
                "'L:'TY';SP'NZX LY?'MWLNV SZYP'-TWW' ,Z)TOP'( OL;P:'LYO':(  Z,;'QZ,';SP' ,ZO(N;'MWLNV SZYP\"'SL)TYR'MPPY'NZQZ(YOPO'M?' STW'$TXXP,XLY\n" + \
                "';SP'N,PL;Z,'ZQ' R 'P4XLTW'PYN,? ;TZY\n" + \
                "';SP'NZX LY?'SL:';ZY:'ZQ':PN(,T;?';LWPY;\"'MWLNV SZYP'-L:'LYYZ(YNPO'LMZ(;'L'XZY;S'LRZ\n" + \
                "'M(;';ST:'T:';SP'QT,:;';TXP'-P8,P'RP;;TYR'OP;LTW:'ZY'U(:;'-SL;';SP'MWLNV SZYP'T:'LYO'SZ-'T;'-Z,V:\""

cipher_message2 = "NFEEPO IE OOPPPSSTE.ELSST KNASONPL ETO  WA  ICEGRAFC ESNR S  WDSBOY,CY-EI'TTORE I EULVL H\n" + \
                  "OPNSO KER OMVSEEORE\n" + \
                  "FT  RKEMV SAIC RGERP- AAEESOE  KCETTGSSRCAPP Y TR "

# Message1.decrypt_caesar(cipher_message1)
Message2.decrypt_columnar(cipher_message2)