from cryptography.fernet import Fernet
## 1.Generate the key and print
key = Fernet.generate_key()

print(key)

## 2.Create a cipher with the key and encrypt the message
cipher = Fernet(key)

encrypted_text = cipher.encrypt(b'this is my secret message')

print(encrypted_text)
## Decrypt
original_text = cipher.decrypt(encrypted_text)

print(original_text.decode())

## 3.Encrypt files
## open a file and write a constant key to a file
key = Fernet.generate_key()
fkey = open("file_key.txt",'wb')
fkey.write(key)

## 4.read the key from the file and encrypt the excel
fkey = open("file_key.txt",'rb')
key = fkey.read()
cipher = Fernet(key)
filename = 'my_secret_excel.xlsx'
with open( filename,'rb')as f:
    e_file = f.read()

encrypted_file = cipher.encrypt(e_file)

with open( filename + "encrypted", 'wb') as ef:
    ef.write(encrypted_file)

# 5.Decrypt the file
fkey = open("file_key.txt",'rb')
key = fkey.read()
cipher = Fernet(key)

with open('my_secret_excel.xlsxencrypted','rb')as df:
    encrypted_data = df.read()


decrypted_file = cipher.decrypt(encrypted_data)

with open('my_secret_excel decrypted.xlsx','wb') as df:
    df.write(decrypted_file)

