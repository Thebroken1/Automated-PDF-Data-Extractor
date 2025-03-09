from TextExtractorV import text_extractor as tee
from TableExtractorV import table_extractor as tae

while(True):
    user_option = int(input(f"\n1.Create Text File \n2.Create CSV file \n3.Create Both \n4.Exit \nInput: "))
    if user_option == 4:
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
        elif user_option ==3:
            if tae(user_path):
                print(f"CSV file of {user_path} Created")
            else:
                print(f"Failed to Create File")
            if tee(user_path):
                print(f"Text file of {user_path} Created")
            else:
                print(f"Failed to Create File")
        elif user_option == 4:
            break
        else:
            print("Incorrect Imput")