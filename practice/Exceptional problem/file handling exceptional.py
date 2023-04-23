try:
    with open("datafile.txt","r")as file:
     data =file.read()
     print (data)
except FileNotFoundError:
   print ("file not found")
except PermissionError:
   print("file acced denide") 
except Exception as e:
   print(f"An error occured:{e}")         