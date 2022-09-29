import re,os,sys,logging,time,datetime,getopt,numpy
def usage():
    print('''
    #-------------------------------------------------------------------------------
    #Author:Guoxiang Xie(zgtl15@foxmail.com)
    #Time:  2022/09/29
    #Version: 1.0
    ###this scipt is used to count CDS info from gtf 
    Useage: python script.py [option] [parameter]
    -i/--input           input  CDS length  list
    -o/--out             output result file
    -h/--help            show possible options''')

'''
before use this script, do "sed 's/"/\t/g' gtf_file |awk '($3=="CDS")'| awk '{print$10"\t"$5-$4}' > CDS_length.txt " to get the CDS length txt 
'''
opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["help","input=","output=",])
for op, value in opts:
    if op == "-i" or op == "---input":
        infile1 = value
    elif op == "-o" or op == "--out":
        out = value
    elif op == "-h" or op == "--help":
        usage()
        sys.exit(1)
if len(sys.argv) < 5:
    usage()
    sys.exit(1)

###infile
'''
ENSBTAG00000006648      122
ENSBTAG00000006648      322
ENSBTAG00000006648      174
ENSBTAG00000006648      239
ENSBTAG00000006648      34
ENSBTAG00000006648      287
ENSBTAG00000006648      174
ENSBTAG00000006648      239
ENSBTAG00000054829      115
ENSBTAG00000054829      174
ENSBTAG00000054829      117
ENSBTAG00000054829      292
ENSBTAG00000001753      1280
ENSBTAG00000001753      109
ENSBTAG00000001753      125
ENSBTAG00000001753      106

'''
def genedic(infile1):
    f1=open(infile1)
    genedic={}
    for xgx in f1 : 
        xgx_spl = xgx.split()
        key = xgx_spl[0]
        value = xgx_spl
        if key in genedic :
            genedic[key].append(value)
        else :
             genedic[key] = []
             genedic[key].append(value)
    f1.close()
    return genedic

genedic = genedic(infile1)
f2 = open(out,'w')
for key,value in genedic.items():
    CDS_len = []
    for aaa in value:
        CDS_len.append(eval(aaa[1]))
    f2.write(f'{key}	{sum(CDS_len)}\n')



f2.close()
