#method to move .jpg files from directory
import shutil, glob

def moveJpg():
    #move files jpg from directory "Desktop" to "Images"
    
    src = r"/Users/anubis/Desktop/"
    despictures = "/Users/anubis/Pictures/"
    destxt = "/Users/anubis/Documents/"
    

    for x_file in glob.glob(src+"\\*.jpg"):
        shutil.move(x_file,despictures)
  
    for x_file in glob.glob(src+"\\*.txt"):
        shutil.move(x_file,destxt)
    
    for x_file in glob.glob(src+"\\*.JPEG"):
        shutil.move(x_file,destxt)

    
    print("pictures moved succesfully")

moveJpg()