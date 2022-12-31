from datetime import date
from datetime import datetime
from datetime import timedelta
import os
import shutil
#from sys import argv
import sys


def get_date_on_period_as_folder(arg_date, arg_count_days):
    day_count = timedelta(arg_count_days)
    f_date1 = arg_date - day_count
#    f_day1 = f_date1.day
    f_month1 = f_date1.month
    f_year1 = f_date1.year
    name_folder1 = str(f_year1)+'_'+str(f_month1)
    return name_folder1


def save_print_string_to_file(name_file, string1):
    print(string1)
    with open(name_file, "a") as file:
        file.write("\n"+str(datetime.now())+' : '+string1)
        
        

def delete_catalog_not_empty(arg_catalog, arg_day):
    del_path = arg_catalog
    del_path_90 = get_date_on_period_as_folder(date.today(), arg_day)
    del_path_full = del_path+del_path_90
    name_file_log = arg_catalog+'cs7_del_log.txt';
    save_print_string_to_file(name_file_log, 'Start search catalog in '+del_path)
    try:
        list_of_catalog = os.listdir(del_path)
        del_catalog = ''
        for entry in list_of_catalog:
            if entry == del_path_90:
                #print(entry+' - it is for deleting')
                save_print_string_to_file(name_file_log, entry+' - it is for deleting')
                del_catalog = entry
            else:
                #print(entry+' - skip...')
                save_print_string_to_file(name_file_log, entry+' - skip...')
        if del_catalog == '':
            #print(del_path_90+' - not found!')
            save_print_string_to_file(name_file_log, del_path_90+' - not found!')
        else:
            #print(del_path_full+' - start deleting...')
            save_print_string_to_file(name_file_log, del_path_full+' - start deleting...')
            shutil.rmtree(del_path_full)
            #print(del_path_full+' - was deleted!')
            save_print_string_to_file(name_file_log, del_path_full+' - was deleted!')

    except FileNotFoundError:
        #print('Catalog not found!')
        save_print_string_to_file(name_file_log, 'Catalog not found!')


def main():
    folder_name_finally = ''
    letter_disk_finally = 'C'
    folder_name = 'CINC'
    letter_disk = 'C'
    #script, folder_name, letter_disk = argv
#   'C:\\DataBase\\1C_Backups\\     C
    #for param in sys.argv:
    i = 1
    for param in sys.argv:
        print(param)
        if i == 1:
           script = param
        elif i == 2:
           folder_name = param
        elif i == 3:
           letter_disk = param
        i += 1
    if script == '':
        print('What is it?')
    letter_disk_finally = letter_disk
    folder_name_finally = str(letter_disk_finally)+':\\DataBase\\1C_Backups\\'+folder_name+'\\'
    delete_catalog_not_empty(folder_name_finally, 90)
    delete_catalog_not_empty(folder_name_finally, 60)
        

main()

