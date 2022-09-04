from email.mime import image
from os import access
import cv2
from cv2 import VideoCapture
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    #starting cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while result:
       #read the frames while camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() used for saving image to any storage device.
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
    return image_name
    print("snapshotTaken")
    #Releases the camera
    videoCaptureObject.release()
    #closes all the windows
    cv2.destroyAllWindows()
take_snapshot()

#uploading files to dropbox
def upload_files(image_name):
    access_token = "sl.BORPCpQd2CN-hzWxQDerNNGJ5-MOscDcItQmQlbWvnYpU2P8WJg8AeIOzYO1muQeMPNboH3iq_agmsUr3MlmLNMLagCc49tNhdS8bjG9pgW3E8zDhqZm9HME4scFIKk_ITWej50"
    file = image_name
    file_from = file
    file_to = "/Pro-102Automation#1" + (image_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb')as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while (True):
        if((time.time()-start_time)>=300):
            name = take_snapshot()
            upload_files(name)
main()