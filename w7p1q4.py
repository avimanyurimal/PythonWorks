try:
    file_name= input('enter file name:')
    input_file=open(file_name,'r')
    print(input_file.read())
    input_file_close()
    input_file_opened=True
except:
    print('file not found')