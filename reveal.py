from stegano import lsb
secret_message=lsb.reveal('secret.png')
print(secret_message)