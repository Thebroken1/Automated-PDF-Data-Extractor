from TextExtractor import text_extractor as tee
from TableExtractor import table_extractor as tae
from Ocr import image_extractor as ie

while(True):
    user_option = int(input(f"\n1.Create Text File \n2.Create CSV file \n3.Create Image File \n4.Create All \n5.Exit \nInput: "))
    if user_option == 5:
        break
    else:
        user_path = input("\nEnter File Name:")
        user_path += ".pdf"
        
        if user_option == 1:
            if tee(user_path):
                print(f"Text file of {user_path} Created")
            else:
                print(f"Failed to Create File")
        elif user_option == 2:
            if tae(user_path):
                print(f"CSV file of {user_path} Created")
            else:
                print(f"Failed to Create File")
        elif user_option == 3:
            if ie(user_path):
                print(f"Image file of {user_path} Created")
            else:
                print(f"Failed to Create File")

        elif user_option ==4:
            
            if tae(user_path):
                print(f"CSV file of {user_path} Created")
            else:
                print(f"Failed to Create File")
            if tee(user_path):
                print(f"Text file of {user_path} Created")
            else:
                print(f"Failed to Create File")
            if ie(user_path):
                print(f"Image file of {user_path} Created")
            else:
                print(f"Failed to Create File")
       
        elif user_option == 5:
            break
        
        else:
            print("Incorrect Input")