import argparse


class Caesar:
    def __init__(self):
        pass
    
    def CaesarShift(self, begin, end, number, key):
        '''number from [begin; end] should be changed by += key'''
        number -= begin
        number += key
        number %= (end - begin + 1)
        if number < 0:
            number += (end - begin + 1)
        return begin + number

    def CaesarEncryptChar(self, char, key = 0):
        if ord('a') <= ord(char) and ord(char) <= ord('z'):
            char = chr(self.CaesarShift(ord('a'), ord('z'), ord(char), key))
        elif ord('A') <= ord(char) and ord(char) <= ord('Z'):
            char = chr(self.CaesarShift(ord('A'), ord('Z'), ord(char), key))
        else:
            pass

        return char

    def CaesarEncryptLine(self, string, key = 0):
        ret_str = ''
        for i in range(len(string)):
            ret_str += self.CaesarEncryptChar(string[i], key)
        return ret_str

    def CaesarEncryptText(text, key = 0):
        # text is a list of strings
        for i in range(len(text)):
            text[i] = CaesarEncrypt(text[i], key)
        return text

    def CaesarEncryptFile(self, in_path = "input.txt", out_path = "output.txt", key = 0):
        with open(in_path, 'a') : pass
        text = []
        
        with open(in_path, 'r') as in_file:
            for line in in_file:
                text.append(line)
        in_file.close()

        with open(out_path, 'w') as out_file:
            for line in text:
                out_file.write(self.CaesarEncryptLine(line, key))
        out_file.close()

    def CaesarDecryptFile(self, in_path, out_path, key = 0, automatic = True):
        if not automatic:
            CaesarEncrypyptFile(in_path, out_path, - key)
        else:
            #Method is based on the most frequent char of English alphabet
            
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
            
            self.CaesarEncryptFile(in_path, out_path, ord('e') - ord(the_most_frequent_letter))

class Text:
    def __init__(self, in_path = "input.txt",
                 out_path = "output.txt", key_path = "key.txt"):
        self.in_path = in_path
        self.out_path = out_path
        self.key_path = key_path

    def Encrypt(self, encryptor = "Caesar"):
        if encryptor == "Caesar":
            caesar = Caesar()
            with open(self.key_path, 'r') as key_file:
                key = int(key_file.read())
            caesar.CaesarEncryptFile(self.in_path, self.out_path, key)
        else:
            print("Sorry, no such encryptor.")
            pass

    def Decrypt(self, decryptor = "Caesar", automatic = False):
        if decryptor == "Caesar":
            caesar = Caesar()
            with open(self.key_path, 'r') as key_file:
                key = int(key_file.read())
                key_file.close()
            caesar.CaesarDecryptFile(self.in_path, self.out_path, key, automatic)
        else:
            print("Sorry, no such encryptor.")
            pass

print("It is a cryptography programm")
#CaesarEncryptFile(key = 2)
#CaesarDecryptFile(in_path = "output.txt", out_path = "output2.txt")

informer = argparse.ArgumentParser(description='Information for encryption.')

informer.add_argument('--action', type=str)
informer.add_argument('--in_path', type=str)
informer.add_argument('--out_path', type=str)
informer.add_argument('--cipher_name', type=str)
informer.add_argument('--key_path', type=str)

info = informer.parse_args()
print("checkpoint 1")
print(info.in_path, info.out_path, info.key_path, info.cipher_name, info.action)
text = Text(info.in_path, info.out_path, info.key_path)

if info.action == "Encrypt":
    text.Encrypt(info.cipher_name)
elif info.action == "Decrypt":
    text.Decrypt(info.cipher_name, automatic = True)
else:
    print("Action can be recognised.")

