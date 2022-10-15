import cezar


OriginalFile = open("Testowy.jpg", "rb")
EncryptedFile = open("EncryptedTestowy.jpg", "w")
while (byte := OriginalFile.read(1)):
    LengthOfByte = len(str(byte)) - 1
    EncryptedByte = cezar.enc_ceasar(5, str(byte)[2:LengthOfByte])
    EncryptedByte = EncryptedByte + "\n"
    EncryptedFile.write(EncryptedByte)

OriginalFile.close()
EncryptedFile.close()

File2Decrypt = open("EncryptedTestowy.jpg", "r")
DecryptedFile = open("WynikTestowy.jpg", "wb")

while (line := File2Decrypt.readline()):
    LengthOfByte = len(str(line)) - 1
    DecryptedByte = cezar.dec_ceasar(5, str(line))
    if DecryptedByte[LengthOfByte].encode("UTF-8") == b'\x05':
        DecryptedByte = DecryptedByte[:LengthOfByte]
    if len(DecryptedByte) == 3:
        ToWrite = DecryptedByte.encode()
    else:
        ToWrite = DecryptedByte.encode().decode('unicode_escape').encode("raw_unicode_escape")
    DecryptedFile.write(ToWrite)