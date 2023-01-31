import os

file="tester.txt"
target_file="target.txt"
target_folder="/root/FizzBuzz_Mohaseenkhan"

def leet_code(text):
    text = text.replace("a", "4")
    text = text.replace("e", "3")
    text = text.replace("i", "1")
    text = text.replace("o", "0")
    text = text.replace("s", "5")
    text = text.replace("t", "7")
    return text

def copy_pages(file, start_page, end_page, target_file, target_folder=None):
    if target_folder:
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        target_file = os.path.join(target_folder, target_file)
    
    with open(file, "r") as f:
        lines = f.readlines()
    
    start_line = (start_page - 1) * 25
    end_line = end_page * 25
    pages = lines[start_line:end_line]
    
    with open(target_file, "w") as f:
        for page in pages:
            f.write(leet_code(page))

def menu():

#    file_name = input("Enter the file name: ")
#    file_name = os.path.expanduser(file_name)
    start_page = int(input("Enter the starting page: "))
    end_page = int(input("Enter the ending page: "))
#    target_file = input("Enter the target file name: ")
#    target_folder = input("Enter the target folder (optional): ")
    copy_pages(file, start_page, end_page, target_file, target_folder)



if __name__ == "__main__":
    menu()

