import face_recognition
import cv2
import os
from PIL import Image
def crop(path):

    cropped_imgs = list()

    try:
        image = face_recognition.load_image_file(path)
        face_locations = face_recognition.face_locations(image)
        print("I found {} face(s) in this photograph.".format(len(face_locations)))
        for face_location in face_locations:

            # Print the location of each face in this image
            top, right, bottom, left = face_location
            print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

            # You can access the actual face itself like this:
            face_image = image[top-15:bottom+15, left-15:right+15]
            pil_image = Image.fromarray(face_image)
            cropped_imgs.append(pil_image)
    except:
        print("no faces found or can't open image")

    return cropped_imgs

dir_base = '/Users/chen.tingyuan/Desktop/PJS/python/crawler/beauty_dataset_test/'
dir_des = '/Users/chen.tingyuan/Desktop/PJS/python/crawler/beauty_dataset_crop/'
dirs = os.listdir(dir_base)
count = 0
for repo in dirs:
    if repo =='.DS_Store':
        continue
    repo_des = dir_des + repo
    try:
        os.mkdir(repo_des)
    except:
        print("create repo failed")
    repo_path = dir_base + repo 
    images = os.listdir(repo_path)
    for image in images:
        image_path = repo_path + '/'+image
        croppeds = crop(image_path)
        for i,img in enumerate(croppeds):
            img.save(repo_des+'/'+str(i)+image)
        count = count +1 
        print(count)