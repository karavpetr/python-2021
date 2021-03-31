import argparse


class Cipher:
    def __init__(self):
        pass

    def CharShift(self, begin, end, number, key):
        '''number from [begin; end] should be changed by += key'''
        number -= begin
        number += next(key)
        number %= (end - begin + 1)
        if number < 0:
            number += (end - begin + 1)
        return begin + number

    def EncryptChar(self, char, key):
        if ord('a') <= ord(char) and ord(char) <= ord('z'):
            char = chr(self.CharShift(ord('a'), ord('z'), ord(char), key))
        elif ord('A') <= ord(char) and ord(char) <= ord('Z'):
            char = chr(self.CharShift(ord('A'), ord('Z'), ord(char), key))
        else:
            next(key)
        return char

    def EncryptLine(self, string, key):
        ret_str = ''
        for i in range(len(string)):
            ret_str += self.EncryptChar(string[i], key)
        return ret_str

    def EncryptFile(self, in_path, out_path, key):
        with open(in_path, 'a'):
            pass
        text = []
        
        with open(in_path, 'r') as in_file:
            for line in in_file:
                text.append(line)
        in_file.close()

        with open(out_path, 'w') as out_file:
            for line in text:
                out_file.write(self.EncryptLine(line, key))
        out_file.close()
    

class Caesar(Cipher):
    def __init__(self):
        pass

    def AutoDecrypt(self, in_path, out_path, key_number):
        #Method is based on the most frequent char of an English alphabet
        
        with open(in_path, 'a') : pass
        frequencies = {}
        
        with open(in_path, 'r') as in_file:
            for line in in_file:
                for char in line:
                    try:
                        frequencies[char] += 1
                    except:
                        frequencies.update({char : 1})
        in_file.close()

        the_most_frequent_letter = 'e'
        the_largest_frequence = 0
        for char in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
            try:
                if frequencies[char] > the_largest_frequence:
                    the_largest_frequence = frequencies[char]
                    the_most_frequent_letter = char
            except:
                pass

        def key():
            while True:
                yield ord('e') - ord(the_most_frequent_letter)
        self.EncryptFile(in_path, out_path, key())

    def DecryptFile(self, in_path, out_path, key_number):
        def key():
            while True:
                yield key_number * (-1)
        self.EncryptFile(in_path, out_path, key())

    def Decrypt(self, in_path, out_path, key_path):
        with open(key_path, 'r') as key_file:
            key_number = int(key_file.read())
        key_file.close()
        self.DecryptFile(in_path, out_path, key_number)

    def Encrypt(self, in_path, out_path, key_path):
        with open(key_path, 'r') as key_file:
            key_number = int(key_file.read())
        key_file.close()
        def key():
            while True:
                yield key_number
        self.EncryptFile(in_path, out_path, key())

class Vigenere(Cipher):
    def __init__(self):
        pass

    def Encrypt(self, in_path, out_path, key_path):
        with open(key_path, 'r') as key_file:
            key_word = str(key_file.read())
        key_file.close()

        def key():
            while True:
                for char in key_word.lower():
                    yield ord(char) - ord('a')
        
        self.EncryptFile(in_path, out_path, key())

    def Decrypt(self, in_path, out_path, key_path):
        with open(key_path, 'r') as key_file:
            key_word = str(key_file.read())
        key_file.close()

        def key():
            while True:
                for char in key_word.lower():
                    yield ord('a') - ord(char)
        
        self.EncryptFile(in_path, out_path, key())

class Vernam(Cipher):
    def __init__(seld):
        pass

    def CharShift(self, begin, end, number, key):
        '''number from [begin; end] should be changed by += key'''
        number -= begin
        number ^= next(key)
        number += begin
        return number

    def EncryptChar(self, char, key):
        if ord('a') <= ord(char) and ord(char) <= ord('a') + 31:
            char = chr(self.CharShift(ord('a'), ord('a') + 31, ord(char), key))
        elif ord('A') <= ord(char) and ord(char) <= ord('A') + 31:
            char = chr(self.CharShift(ord('A'), ord('A') + 31, ord(char), key))
        else:
            next(key)
        return char
    
    def Encrypt(self, in_path, out_path, key_path):
        with open(key_path, 'r') as key_file:
            key_word = str(key_file.read())
        key_file.close()

        def key():
            key_file = open(key_path, 'r')
            for line in key_file:
                for char in line:
                    yield min(max(ord(char.lower()) - ord('a'), 0), ord('z'))
            key_file.close()
        
        self.EncryptFile(in_path, out_path, key())

    def Decrypt(self, in_path, out_path, key_path):
        self.Encrypt(in_path, out_path, key_path)

class Text:
    def __init__(self, in_path = "input.txt",
                 out_path = "output.txt", key_path = "key.txt"):
        self.in_path = in_path
        self.out_path = out_path
        self.key_path = key_path

    def Encrypt(self, cipher_name):
        if cipher_name == "Caesar":
            caesar = Caesar()
            caesar.Encrypt(self.in_path, self.out_path, self.key_path)
        elif cipher_name == "Vigenere":
            vigenere = Vigenere()
            vigenere.Encrypt(self.in_path, self.out_path, self.key_path)
        elif cipher_name == "Vernam":
            vernam = Vernam()
            vernam.Encrypt(self.in_path, self.out_path, self.key_path)
        else:
            print("Sorry, no such encryptor.")
            pass

    def Decrypt(self, cipher_name):
        if cipher_name == "Caesar":
            caesar = Caesar()
            caesar.Decrypt(self.in_path, self.out_path, self.key_path)
        elif cipher_name == "Vigenere":
            vigenere = Vigenere()
            vigenere.Decrypt(self.in_path, self.out_path, self.key_path)
        elif cipher_name == "Vernam":
            vernam = Vernam()
            vernam.Decrypt(self.in_path, self.out_path, self.key_path)
        else:
            print("Sorry, no such decryptor.")
            pass

    def AutoDecrypt(self, decryptor = "Caesar", automatic = True):
        if decryptor == "Caesar":
            caesar = Caesar()
            caesar.AutoDecrypt(self.in_path, self.out_path, self.key_path)
        else:
            print("Sorry, no such encryptor.")
            pass


informer = argparse.ArgumentParser(description='Information for encryption.')

informer.add_argument('--action', type=str)
informer.add_argument('--in_path', type=str)
informer.add_argument('--out_path', type=str)
informer.add_argument('--cipher_name', type=str)
informer.add_argument('--key_path', type=str)

info = informer.parse_args()
text = Text(info.in_path, info.out_path, info.key_path)

if info.action == "Encrypt":
    text.Encrypt(info.cipher_name)
elif info.action == "Decrypt":
    text.Decrypt(info.cipher_name)
elif info.action == "AutoDecrypt":
    text.AutoDecrypt(info.cipher_name)
else:
    print("Action can not be recognised.")

print("Finish")

#python3 cryptography.py --action=Encrypt --in_path=test/test.txt --out_path=test/output.txt --cipher_name=Vernam --key_path=test/key.txt
#python3 cryptography.py --action=Decrypt --in_path=test/output.txt --out_path=test/output2.txt --cipher_name=Vernam --key_path=test/key.txt
