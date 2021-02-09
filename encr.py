from cryptography.fernet import Fernet

# This file is used to access all the encrypted passwords and usernames
# Read https://cryptography.io/en/latest/fernet.html on how to create a key and encrypt your text



with open(r'D:\PyCharm Projects\timetablesel\test\file3.bin', 'rb') as file_object:
    for line in file_object:
        key = line

cipher_suite = Fernet(key)

with open(r'D:\PyCharm Projects\timetablesel\test\file2.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line

with open(r'D:\PyCharm Projects\timetablesel\test\file1.bin', 'rb') as file_object:
    for line in file_object:
        encryptedusr = line

with open(r'D:\PyCharm Projects\timetablesel\test\file4e.bin', 'rb') as file_object:
    for line in file_object:
        encryptedusraca = line

with open(r'D:\PyCharm Projects\timetablesel\test\file4p.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwdaca = line

password_b = cipher_suite.decrypt(encryptedpwd)
username_b = cipher_suite.decrypt(encryptedusr)
usraca = cipher_suite.decrypt(encryptedusraca)
pwdaca = cipher_suite.decrypt(encryptedpwdaca)

usrne = bytes(username_b).decode("utf-8")
paswrd = bytes(password_b).decode("utf-8")
usrnaca = bytes(usraca).decode("utf-8")
paswrdaca = bytes(pwdaca).decode("utf-8")


def username_aca_plain():
    return usrnaca


def password_aca_plain():
    return paswrdaca


def username_plain():
    return usrne


def password_plain():
    return paswrd
