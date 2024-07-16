import numpy as np

## Problem 3.5

text = """NBPFR KISOQ NFRDB FKJFD XNOIN OJXIX NZXSI
DJXIJ NYENO ISDSA SOFBY REJRK IKSKI PFRAR 
DJZIJ RUSEE JXIZI KADFB JXIJK SODYI OGIOJ 
SEJIK ADSOG UESOJ JXIAI VKPWX IKIPF RARDJ 
ENIRU FOJXI GSNDN IDSOG GNDYF RKDIN OOFVI 
EUXKS DIDFB PFRKY FAUEN YSJIG DJSJI FBANO 
GJXIA ISONO ZGFID OJASJ JIKNB NJDFO EPNGE 
IYXSJ JIKFB SJKSO DYIOG IOJSE LNOGS OGIVK 
PFOIW NEEDS PSDPF RWSEL PFRKA PDJNY WSPNB 
JXNDP FROZA SOIQU KIDDI DXNAD IEBNO JIKAD 
JFFGI IUBFK AIWXP WXSJS VIKPD NOZRE SKEPG 
IIUPF ROZAS OJXND GIIUP FROZA SOARD JCICI 
IEFMR IOJNO UKSND IFBJX IVIKP GREEF EGGSP 
DWXNY XXSVI EFOZD NOYIU SDDIG SWSPS OGYFO 
VNOYI IANBP FRYSO JXSJJ XIKIN ZOFBZ FFGMR 
IIOSO OIWSD YREJR KIDUS EANID JGSPF BYFRK 
DIPFR WNEEU FFXUF FXWXS JIVIK DBKID XSOGO 
IWSOG GIYES KINJD YKRGI SOGAI SOBFK SKJDJ 
FUUIG DXFKJ NOJXI YREJN VSJIG YFRKJ FBJXI 
IAUKI DDHFD IUXNO ISOGI VKPFO IWNEE DSPSD 
PFRWS ELPFR KAPDJ NYWSP NBJXS JDOFJ ZFFGI 
OFRZX BFKXN AWXNY XNDZF FGIOF RZXBF KAIWX 
PWXSJ SVIKP YREJN VSJIG LNOGF BPFRJ XJXND 
LNOGF BPFRJ XARDJ CIJXI OSDIO JNAIO JSEUS 
DDNFO FBSVI ZIJSC EIBSD XNFOA RDJIQ YNJIP 
FRKES OZRNG DUEII OSOSJ JSYXA IOJSE SUESJ 
FBFKS CSDXB REPFR OZUFJ SJFFK SOFJJ FFBKI 
OYXBK IOYXC ISOJX FRZXJ XIUXN ENDJN OIDAS 
PHFDJ EIPFR WNEEK SOLSD SOSUF DJEIN OJXIX 
NZXSI DJXIJ NYCSO GNBPF RWSEL GFWOU NYYSG 
NEEPW NJXSU FUUPF KSENE PNOPF RKAIG NIVSE 
XSOGS OGIVK PFOIW NEEDS PSDPF RWSEL PFRKB 
EFWKP WSPNB XIDYF OJIOJ WNJXS VIZIJ SCEIE 
FVIWX NYXWF REGYI KJSNO EPOFJ DRNJA IWXPW 
XSJSA FDJUS KJNYR ESKEP URKIP FROZA SOJXN 
DURKI PFROZ ASOAR DJCI"""

# lettermap = {"A":"A","B":"B","C":"C","D":"D","E":"E",
#              "F":"F","G":"G","H":"H","I":"I","J":"J",
#              "K":"K","L":"L","M":"M","N":"N","O":"O",
#              "P":"P","Q":"Q","R":"R","S":"S","T":"T",
#              "U":"U","V":"V","W":"W","X":"X","Y":"Y",
#              "Z":"Z"}

# lettermap = {"A":"A","B":"B","C":"C","D":"D","E":"E",
#              "F":"F","G":"d","H":"H","I":"e","J":"t",
#              "K":"K","L":"L","M":"M","N":"N","O":"n",
#              "P":"P","Q":"Q","R":"R","S":"a","T":"T",
#              "U":"U","V":"V","W":"W","X":"h","Y":"Y",
#              "Z":"Z"}

lettermap = {"A":"A","B":"B","C":"C","D":"s","E":"E",
             "F":"i","G":"d","H":"H","I":"e","J":"t",
             "K":"K","L":"L","M":"M","N":"N","O":"n",
             "P":"P","Q":"Q","R":"n","S":"a","T":"T",
             "U":"U","V":"V","W":"W","X":"h","Y":"Y",
             "Z":"Z"}

def subcipher(lettermap,text):
     return "".join(lettermap.get(c," ") for c in text)

print(subcipher(lettermap, text))

def compute_Ngrams(msg,N=2):
    msg = msg.replace(" ","")
    msg = msg.replace("\n", "")
    counts = {}
    for i in range(len(msg) - 1):
        bigram = msg[i:i+N]
        if bigram in counts.keys():
            counts[bigram] += 1
        else:
            counts[bigram] = 1

    return counts

def calculate_order(Ngrams, N):
    Ngram_names = np.array(list(Ngrams.keys()))
    Ngram_counts = np.array([Ngrams[i] for i in Ngram_names])

    names, freqs = [], []
    total = sum(Ngram_counts)

    for _ in range(N):
        idx = np.argmax(Ngram_counts)
        names.append(str(Ngram_names[idx]))
        freqs.append(float(Ngram_counts[idx] / total))
        Ngram_counts[idx] = 0

    return names, freqs


letters = compute_Ngrams(text, N=1)
names, freqs = calculate_order(letters, 10)
print(names)
print(freqs)

bigrams = compute_Ngrams(text)
names, freqs = calculate_order(bigrams, 20)
print(names)
print(freqs)
trigrams = compute_Ngrams(text, N=3)
names, freqs = calculate_order(trigrams, 20)
print(names)
print(freqs)

qgrams = compute_Ngrams(text, N=4)
names, freqs = calculate_order(qgrams, 10)
print(names)
print(freqs)