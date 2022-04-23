from wsgiref.validate import InputWrapper


message = input('ENter the message:')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 5
encrypt =''
decrypt = ''
for i in message:
    position = alphabet.find(i)
    newposition = (position+key)%26
    encrypt += alphabet[newposition]

print(encrypt)
      
for i in encrypt:
    pos = alphabet.find(i)
    newpos = (pos-key)%26
    decrypt += alphabet[newpos]

print(decrypt)
 
print(input("Enter a name: "))

