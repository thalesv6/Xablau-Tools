import os

def remove_desktop_ini_and_empty_folders(directory='.'):
    for root, dirs, files in os.walk(directory, topdown=False):
        for filename in files:
            if filename.lower() == 'desktop.ini':
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    print(f'Removed file: {file_path}')
                except Exception as e:
                    print(f'Error removing file {file_path}: {e}')
        

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                if not os.listdir(dir_path):  
                    os.rmdir(dir_path)
                    print(f'Removed empty folder: {dir_path}')
            except Exception as e:
                print(f'Error removing folder {dir_path}: {e}')


remove_desktop_ini_and_empty_folders()
