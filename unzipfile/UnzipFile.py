# Create a ZipFile Object and load sample.zip in it
import os
import zipfile
import logging


class UnzipFilesInCurrentDirectory:

    @staticmethod
    # List all files in a directory using scandir()
    def extract_zip_file(filename):
        try:
            with zipfile.ZipFile(filename, 'r') as zipObj:
                # Extract all the contents of zip file in current directory
                zipObj.extractall()
        except zipfile.LargeZipFile:
            print("This zip file '{}' is very large".format(filename))
            log.warning("This zip file '{}' is very large".format(filename))
            with zipfile.ZipFile(filename, 'r', allowZip64=True) as zipObj:
                # Extract all the contents of zip file in current directory
                zipObj.extractall()
        except zipfile.BadZipFile:
            print("'{}'is a bad zip file".format(filename))
            log.error("'{}'is a bad zip file".format(filename))


def delete_file_if_exists(filepath=""):
    if filepath != "":
        try:
            if os.path.exists(filepath):
                log.info("Old log file exists.")
                print("Log file Exists")
                os.remove(filepath)
                log.info("Old log file has been deleted.")
                print("old log file has been deleted")
            else:
                log.warning("Old log file does not exists.")
                print("Old Log file does not exist.")
                return
        except:
            log.error("Could not delete the old log file. Please verify. Close old log file if it is opened.")
            print("Could not delete the old log file. Please verify.")


# creating logger object
log = logging.getLogger("Unzip")
log.setLevel(logging.DEBUG) # setting the level
delete_file_if_exists("log.log") # deleting the old log file, if exists.
# setting the basic log configuration
logging.basicConfig(filename="log.log",  #this is the file path
                    format = '%(asctime)s : %(name)s : %(levelname)s : %(message)s',
                    #format = '%(asctime)s : %(levelname)s : %(message)s',
                    datefmt= '%d/%m/%Y %I:%M:%S %p',
                )
# current Directory
currentDir = './'

with os.scandir(currentDir) as entries:
    num_of_zip_files = 0
    for entry in entries:
        if entry.name.endswith('.zip'):
            num_of_zip_files+=1
            try:
                print("Extracting '{}' file to same directory as zipfile's name".format(entry.name))
                log.info("Extracting '{}' file to same directory as zipfile's name".format(entry.name))
                UnzipFilesInCurrentDirectory.extract_zip_file(entry.name)
            except:
                print("Could not extract '{}' zip file.".format(entry.name))
                log.error("Could not extract '{}' zip file.".format(entry.name))
        elif num_of_zip_files == 0:
            print("No zip files are available in this directory.\nThanks for using.")
            log.info("No zip files are available in this directory.\nThanks for using.")
        else:
            print("All available zip files have been extracted successfully.\nThanks for using.")
            log.info("All available zip files have been extracted successfully.\nThanks for using.")