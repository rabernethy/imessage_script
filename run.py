import sys, os

def message(phone, file_name):
    script = 'imessage -t text -c phone'
    to_be_sent = []
    print(phone)
    print(file_name)
    with open('text_files/'+file_name) as f:
        for line in f:
            to_be_sent.append(line)
    for line in to_be_sent:
        os.system('imessage -t text -c phone'.replace('text','"'+line+'"').replace('phone','"'+phone+'"'))

if __name__ == "__main__":
    if len(sys.argv)>1:
        message(sys.argv[1],sys.argv[2])