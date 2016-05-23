'''
**********************************************
*  VBscript Simple Crypter                   *
* *************************                  *
*                                            *
* This is a simple VBscript Crypter,         *
* written in python.                         *
* The crypter generate random key and        *
* XOR the entire input script with this key. *
* The crypter create new script that XOR     *
* the encrypted data to decrpyt it           *
* and run the code in memory                 *
*                                            *
* Written by mitm @RealMitm                  *
**********************************************
'''

import random
import sys

BaseScript = """EncryptionKey = "{ENCRYPTION_KEY}"
EncryptedData = "{ENCRYPT_DATA}"
EncryptionKeySplited = Split(EncryptionKey,"|")
EncryptedDataSplited = Split(EncryptedData,"|")

Result = ""
KeyIndex = 0

for each Item in EncryptedDataSplited
	Result = Result & chr(Item Xor EncryptionKeySplited(KeyIndex))
	KeyIndex = KeyIndex + 1
	if (KeyIndex >= 5)then
		KeyIndex = 0
	end if
next

execute (Result)"""

def GenerateKey():
    arr = []
    for i in range(5):
        arr.append(random.randrange(1, 255))
    return arr

def GetArrAsString(arr, seperator):
    splits = 1
    result = ""
    for item in arr:
        result = result + str(item) + seperator
        if (len(result) > splits * 1000):
            result += "\"& _\n\""
            splits += 1
    return result[:-1]

def main():
    
    if len(sys.argv) < 2:
        print ("Usage: python VBSimpleCrypter.py <Input VBS File> [vbs|wsf]")
        sys.exit()

    InputFilePath = sys.argv[1]
    OriginalScript = ""

    with open(InputFilePath, 'r') as InputFile:
        OriginalScript = InputFile.read()
		
    Key = GenerateKey()

    Data = []
    index = 0
    for c in OriginalScript:
        Data.append(ord(c) ^ Key[index])
        index += 1
        if (index >= 5):
            index = 0

    ResultScript = BaseScript.replace("{ENCRYPTION_KEY}", GetArrAsString(Key, "|"))
    ResultScript = ResultScript.replace("{ENCRYPT_DATA}", GetArrAsString(Data, "|"))

    if len(sys.argv) > 2 and sys.argv[2] == "wsf":
        print ('<?XML version="1.0"?><job><script language="VBScript"><![CDATA[')

    print (ResultScript)

    if len(sys.argv) > 2 and sys.argv[2] == "wsf":
        print ("]]></script></job>")
    
    return 0

if __name__ == "__main__":
    sys.exit(int(main() or 0))