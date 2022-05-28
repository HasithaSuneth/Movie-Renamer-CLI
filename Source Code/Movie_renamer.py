import sys
import os
import glob
import re
import string
from tkinter import filedialog, Tk, messagebox

def get_directory():
    dirname = filedialog.askdirectory(initialdir="/", title='Select Directory')
    print("Directory : {}".format(dirname))
    response1 = messagebox.askquestion("Question", "Confirm Directory")
    if response1 == "yes":
        return dirname
    else:
        response2 = messagebox.askquestion("Question", "Do you want to try again?")
        if response2 == "yes":
            get_directory()
        else:
            sys.exit()

def rename_options(path):
    usr_input = input("Select an Option : ")
    if usr_input == '1':
        movie_rename(path)
    elif usr_input == '2':
        clean_rename(path)
    elif usr_input == '3':
        user_sequence(path)   
    elif usr_input == '4':
        sys.exit()
    else:
        response3 = messagebox.askquestion("Question", "Invalide Input...\nDo you want to try again?")
        if response3 == "yes":
            rename_options()
        else:
            sys.exit()

def clean_rename(path):
    print("\nUser selection : Clean Name\n")
    org_names_list, cleaned_list = clean_name(path)
    preview(cleaned_list)
    response4 = messagebox.askquestion("Question", "Do you want to RENAME files/folder as preview?")
    if response4 == "yes":
        for i in range(len(org_names_list)):
            if os.path.exists(path+"\\"+org_names_list[i]):
                os.rename(path+"\\"+org_names_list[i], path+"\\"+cleaned_list[i])
        print("\n--- Rename Completed ---")
    else:
        response5 = messagebox.askquestion("Question", "Do you want to start from begining?")
        if response5 == "yes":
            main()
        else:
            sys.exit()

def movie_rename(path):
    print("\nUser selection : Movie Rename\n")
    org_names_list, cleaned_list = clean_name(path)
    movie_rename_list = []
    for i in cleaned_list:
        movie_temp1 = re.search("^([a-zA-Z0-9\'&! ]*) ([0-9]{4}) ", i)
        try:
            movie_temp2 = "{} ({})".format(string.capwords(movie_temp1[1]), movie_temp1[2])
            movie_rename_list.append(movie_temp2)
        except:
            try:
                movie_temp3 = re.search("^([a-zA-Z0-9\'&! ]*) ([0-9]{4})$", i)
                movie_rename_list.append("{} ({})".format(string.capwords(movie_temp3[1]), movie_temp3[2]))
            except:
                # print(i)
                movie_rename_list.append(i)
    preview(movie_rename_list)
    response6 = messagebox.askquestion("Question", "Do you want to RENAME files/folder as preview?")
    if response6 == "yes":
        for i in range(len(org_names_list)):
            if os.path.exists(path+"\\"+org_names_list[i]):
                os.rename(path+"\\"+org_names_list[i], path+"\\"+movie_rename_list[i])
        print("\n--- Rename Completed ---")
    else:
        response7 = messagebox.askquestion("Question", "Do you want to start from begining?")
        if response7 == "yes":
            main()
        else:
            sys.exit()

def user_sequence(path):
    print("\nUser selection : Customize\n")
    print("Select a Module...\n1. Sub Module\n2. Search Module\n3. Replace Module\n4. Exit")
    usr_input2 = input("Select an Option : ")
    if usr_input2 == '1':
        print("\n--- Sub Module ---\n")
        sub_list =[]
        sub_seq_src = input("Enter Sub Sequence SRC: ")
        sub_seq_dst = input("Enter Sub Sequence DST: ")
        org_names_list = [os.path.basename(t) for t in glob.glob(path + "/*")]
        for i in org_names_list:
            temp = re.sub(sub_seq_src, sub_seq_dst, i)
            sub_list.append(temp)
        preview(sub_list)
        response9 = messagebox.askquestion("Question", "Do you want to RENAME files/folder as preview?")
        if response9 == "yes":
            for i in range(len(org_names_list)):
                if os.path.exists(path+"\\"+org_names_list[i]):
                    os.rename(path+"\\"+org_names_list[i], path+"\\"+sub_list[i])
            print("\n--- Rename Completed ---")
        else:
            response10 = messagebox.askquestion("Question", "Do you want to try again?")
            if response10 == "yes":
                user_sequence(path)
            else:
                sys.exit()
        
    elif usr_input2 == '2':
        print("\n--- Search Module ---\n")
        sear_seq = input("Enter Search Sequence: ")
        search_list =[]
        org_names_list = [os.path.basename(t) for t in glob.glob(path + "/*")]
        for i in org_names_list:
            temp = re.search(sear_seq, i)
            try:
                search_list.append(temp[0])
            except:
                search_list.append(i)
        print("\nIf File/Folder names show same as before means... Fault Sequence.. Try again\n")
        preview(search_list)
        response13 = messagebox.askquestion("Question", "Do you want to RENAME files/folder as preview?")
        if response13 == "yes":
            for i in range(len(org_names_list)):
                if os.path.exists(path+"\\"+org_names_list[i]):
                    os.rename(path+"\\"+org_names_list[i], path+"\\"+search_list[i])
            print("\n--- Rename Completed ---")
        else:
            response14 = messagebox.askquestion("Question", "Do you want to try again?")
            if response14 == "yes":
                user_sequence(path)
            else:
                sys.exit()

    elif usr_input2 == '3':
        print("\n--- Replace Module ---\n")
        replace_list =[]
        rep_seq_src = input("Enter Replace Sequence to: ")
        rep_seq_dst = input("Enter Replace Sequence with: ")
        org_names_list = [os.path.basename(t) for t in glob.glob(path + "/*")]
        for i in org_names_list:
            temp = i.replace(rep_seq_src, rep_seq_dst)
            replace_list.append(temp)
        preview(replace_list)
        response11 = messagebox.askquestion("Question", "Do you want to RENAME files/folder as preview?")
        if response11 == "yes":
            for i in range(len(org_names_list)):
                if os.path.exists(path+"\\"+org_names_list[i]):
                    os.rename(path+"\\"+org_names_list[i], path+"\\"+replace_list[i])
            print("\n--- Rename Completed ---")
        else:
            response12 = messagebox.askquestion("Question", "Do you want to try again?")
            if response12 == "yes":
                user_sequence(path)
            else:
                sys.exit()
    elif usr_input2 == '4':
        sys.exit()
    else:
        response8 = messagebox.askquestion("Question", "Invalide Input...\nDo you want to try again?")
        if response8 == "yes":
            user_sequence(path)
        else:
            sys.exit()

def preview(in_list):
    print("Preview....\n")
    for i in in_list:
        print(i)

def clean_name(path):
    clean_name_list = []
    org_names_list = [os.path.basename(t) for t in glob.glob(path + "/*")]
    for i in org_names_list:
        temp = re.sub("[-.,\(\):_#\[\]]"," ", i).replace("  "," ").replace("  "," ")
        clean_name_list.append(temp)
    return org_names_list, clean_name_list

def main():
    root = Tk().withdraw()
    print("\n--------- Mass File Renamer ----------\n")
    direct = get_directory()

    print("\nSelect an option for continue....\n1. Movie Rename\n2. Clean Name\n3. Customize\n4. Exit")
    rename_options(direct)

main()