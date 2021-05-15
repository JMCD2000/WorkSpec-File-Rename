"""
This copies, and renames PDF ship specs
"""
import shutil
import os
import re

myShip = input('Enter the Ship Class and Hull Number: ')
myAvail = input('Enter the Ship Availibility spec was written for: ')
curWD = input('Enter file path of folder: ')
#curWD = 'C:\Users\jon\Dropbox\Spec Parser\lpd 25 work items\LPD 25 FOA'

fileName_Spec_Regex = re.compile(r'\d{3}[-]\d{2}[-]\d{3}') #170-11-003
fileName_SpecMod_Regex = re.compile(r'.MOD.\d{2}') #MOD 01 or MOD_01 or _MOD_01
fileName_postDelivery_DocNumber_Regex = re.compile(r'._\w{2,3}-\d{4}_') #AWI-1199
fileName_postDelivery_DocNumberPSA_Regex = re.compile(r'._\w{2,3}-\d{4}\w_') #AWI-1199P
fileName_postDelivery_DocNumberParts_Regex = re.compile(r'._\w{2,3}-\d{4}\W\w\W_') #AWI-1199(Y)
fileName_DateIssued_Regex = re.compile(r'Issued \d+_\d+_\d\d\d\d') #Issued 10_19_2017

for fileName_HII in os.listdir(curWD):
    newFileName = ''
    print(fileName_HII)

    curFileName_spec = fileName_Spec_Regex.search(fileName_HII)
    print(str(curFileName_spec))
    curFileName_SpecMod = fileName_SpecMod_Regex.search(fileName_HII)
    print(str(curFileName_SpecMod))

    if curFileName_spec is not None:
        newFileName = curFileName_spec

    elif curFileName_SpecMod is not None:
        newFileName = curFileName_spec + ' MOD ' + curFileName_SpecMod[-2:]

    else:
        print('File read error on Spec Regex')
        print(fileName_HII)
        continue

    print(newFileName)
    
    curFileName_postDelivery_DocNumber = fileName_postDelivery_DocNumber_Regex.search(fileName_HII)
    print(str(curFileName_postDelivery_DocNumber))
    curFileName_postDelivery_DocNumberPSA = fileName_postDelivery_DocNumberPSA_Regex.search(fileName_HII)
    print(str(curFileName_postDelivery_DocNumberPSA))
    curFileName_postDelivery_DocNumberParts = fileName_postDelivery_DocNumberParts_Regex.search(fileName_HII)
    print(str(curFileName_postDelivery_DocNumberParts))

    if curFileName_postDelivery_DocNumber is not None:
        newFileName = newFileName + ' ' + str(curFileName_postDelivery_DocNumber)

    elif curFileName_postDelivery_DocNumberPSA is not None:
        newFileName = newFileName + ' ' + curFileName_postDelivery_DocNumberPSA

    elif curFileName_postDelivery_DocNumberParts is not None:
        newFileName = newFileName + ' ' + curFileName_postDelivery_DocNumberParts

    else:
        print('File read error on Doc Number Regex')
        print(fileName_HII)
        continue

    curFileName_DateIssued = fileName_DateIssued_Regex.search(fileName_HII)
    print(str(curFileName_DateIssued))

    if curFileName_DateIssued is not None:
        newFileName = curFileName_spec + ' ' + curFileName_DateIssued

    else:
        print('File read error on Spec Regex')
        print(fileName_HII)
        continue
    
    print(newFileName)
