import os
import shutil
import time


# To get the path for the directory to clean up(For Windows), right click the directory folder and select properties
# Copy the path to the right of the Location label, FOR THIS DIRECTORY ONLY add the name of the folder at the end
# Of the path making sure to seperate the name with a \ symbol.
directory = input("Enter the path for the directory you want to clean up: ")
files = os.listdir(directory)

# To enter the path for each of the below(For Windows), open file explorer, right click and select properties
# Copy the path to the right of the Location label.
documents = input("Enter the path for Documents here: ")
documents = os.path.join(documents, 'Documents')

downloads = input("Enter the path for Downloads here: ")
downloads = os.path.join(downloads, 'Downloads')

music = input("Enter the path for Music here: ")
music = os.path.join(music, 'Music')

pics = input("Enter the path for Pictures here: ")
pics = os.path.join(pics, 'Pictures')

videos = input("Enter the path for Videos files here: ")
videos = os.path.join(videos, 'Videos')


for file in files:
    if file.lower().endswith('.mov') or file.lower().endswith('.mp4') or file.lower().endswith('.wmv'):
        shutil.copy(file, videos)
        os.remove(file)
    elif file.lower().endswith('.jpg') or file.lower().endswith('.gif') or file.lower().endswith('.png'):
        shutil.copy(file, pics)
        os.remove(file)
    elif file.lower().endswith('mp3') or file.lower().endswith('.wav') or file.lower().endswith('.wma'):
        shutil.copy(file, music)
        os.remove(file)
    elif file.lower().endswith('.exe') or file.lower().endswith('.msi') or file.lower().endswith('.iso'):
        shutil.copy(file, downloads)
        os.remove(file)
    elif file.lower().endswith('.docx') or file.endswith('.doc') or file.lower().endswith('.txt'):
        shutil.copy(file, documents)
        os.remove(file)
    time.sleep(1)
    print("Working on {}".format(file))
