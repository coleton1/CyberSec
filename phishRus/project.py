import shutil #this allows me to copy the orignal txt file and changed the copied file name and switch the file type to html


print(chr(27) + "[2J")         #this just clears the terminal when I start up the script 
def main(gmail, snapchat):
    print("What page would you like?")             #Menu that looks like trash but thats okay
    print("=============================")
    print("1.Gmail         2.Snapchat")
    spaceyboi()
    menu = input()
    
    file_path = None                               #this crap is not needed but fixed my issue of it trying to replace a second                                                     
    line_number_to_replace = None                  #link on a page that doesnt need a 2nd link changed so I shall keep this 
    new_text_to_insert = None
    line_linknumber_to_replace = None
    new_link_to_insert = None
    line_linknumber_to_replace2 = None

    if menu == "1":                                                  
        file_path = gmail                                        #What to do when you select gmail page
        line_number_to_replace = gmailnum()
        line_linknumber_to_replace = gmaillinknum()
        new_link_to_insert = input("Enter your phishing link here: ")
        new_text_to_insert = input("Enter Target's email here: ")

    elif menu == "2":                               
        file_path = snapchat                                     #what to do when you select snapchat page
        line_number_to_replace = snapchatnum()
        line_linknumber_to_replace = snapchatlinknum()
        line_linknumber_to_replace2 = snapchatlinknum2()
        new_link_to_insert = input("Enter your phishing link here: ")
        new_text_to_insert = input("Target's username: ")
                                                                                        #returning values that if statments changed 
    return file_path, line_number_to_replace, new_text_to_insert, line_linknumber_to_replace, new_link_to_insert, line_linknumber_to_replace2



#all these functions just return the number of the line that needs to be replaced 
def gmaillinknum():
    return 33

def snapchatlinknum():
    return 34

def snapchatlinknum2():
    return 43

def gmailnum():
    return 25

def snapchatnum():
    return 25
#spaceboi just exists to make spaces bc im lazy 
def spaceyboi():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

def filesave():
    fileinput = input("Enter your file name along with .html: ")
    shutil.copy(file_path, fileinput)
    print("Your new phishing page will be located in the 'phishRus' folder!")
    


#this is pretty self explanitory but it replaces the line with your text 
def replace_text_at_line(file_path, line_number, new_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = new_text + '\n'
    else:
        print("Error with line number")

    with open(file_path, 'w') as file:
        file.writelines(lines)

#does same thing but for link instead of text
def replace_link_at_line(file_path, line_number, new_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if line_number is not None and 1 <= line_number <= len(lines):     # "is not none and 1" is there due to it not being able to work if 
        lines[line_number - 1] = new_text + '\n'                        #the second link changer was set to none when using gmail page"
    
    with open(file_path, 'w') as file:
        file.writelines(lines)

gmail = "/home/coletonb/Desktop/phishRus/gmail.txt"    #Change these to the filepath of the txt files with html code in them
snapchat = "/home/coletonb/Desktop/phishRus/snapchat.txt" 
#assigning the values returned back into variables (i think)
file_path, line_number_to_replace, new_text_to_insert, line_linknumber_to_replace, new_link_to_insert, line_linknumber_to_replace2 = main(gmail, snapchat)
#calling the functions and having the magic happen
replace_text_at_line(file_path, line_number_to_replace, new_text_to_insert)
replace_link_at_line(file_path, line_linknumber_to_replace, new_link_to_insert)
replace_link_at_line(file_path, line_linknumber_to_replace2, new_link_to_insert)
filesave()


