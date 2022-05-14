import os
import time

days = 15        # Maximum age of file to stay, older will be deleted
folders = [
            'D:/Di/Musor/musor1',
            'D:/Di/Musor/musor2',
            'D:/Di/Musor/musor3'
            ]
total_deleted_size = 0                      # Total deleted size of all files
total_deleted_file = 0                      # Total deleted files
total_deleted_dirs = 0                      # Total deleted empty folders
now_time = time.time()                      # Get Current time in seconds
age_time = now_time - 60*60*20*days         # Minus days in seconds

def delete_old_files(folder):
    """Delete files older then X days"""
    global total_deleted_file
    global total_deleted_size
    for path, dirs, files in os.walk(folder):
        for file in files:
            file_name = os.path.join(path, file)   # Get Full PATH to file
            file_time = os.path.getmtime(file_name)
            if file_time < age_time:
                size_file = os.path.getsize(file_name)
                total_deleted_size += size_file         # Count sum of size
                total_deleted_file += 1
                print('Deleting File: ' + str(file_name))
                os.remove(file_name)                    #delete file

def delete_empty_dir(folder):
    global total_deleted_dirs
    empty_folders_in_this_run = 0                       # Delete parents folders
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            total_deleted_dirs += 1
            empty_folders_in_this_run += 1
            print('Deleting Empty Dir: ' + str(path))
            os.rmdir(path)
    if empty_folders_in_this_run > 0:
        delete_empty_dir(folder)
#===========================MAIN==================================
start_time = time.asctime()
for folder in folders:
    delete_old_files(folder)    # Delete old files
    delete_empty_dir(folder)    # Delete empty folders
finish_time = time.asctime()
print('-----------START---------------')
print('Start Time: ' + str(start_time))
print('Total Deleted Size: ' + str(int(total_deleted_size/1024/1024)) + 'MB')
print('Total Deleted Files: ' + str(total_deleted_file))
print('Total Deleted Empty Folders: ' + str(total_deleted_dirs))
print('Finish Time: ' + str(finish_time))
print('---------END OF FUNCTION--------')

