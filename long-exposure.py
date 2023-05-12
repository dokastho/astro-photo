#!/usr/bin/python3

from gphoto2 import logging
import gphoto2 as gp
import os
import subprocess
import sys

def capture_image(count: int):
    logging.basicConfig(
        format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    callback_obj = gp.check_result(gp.use_python_logging())
    camera = gp.Camera()
    camera.init()
    print('Capturing image')
    file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
    img_path = os.getcwd() + "/Pictures"
    if len(sys.argv) > 2:
        img_path += "/"
        img_path += str(sys.argv[2])
        pass
        
    print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
    fname = str(count) +"-" + file_path.name
    target = os.path.join(img_path, fname)
    print('Copying image to', target)
    camera_file = camera.file_get(
        file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
    camera_file.save(target)
    subprocess.call(['xdg-open', target])
    camera.exit()
    pass

def main():
    if len(sys.argv) < 2:
        print("Missing required parameters")
        exit(1)
    
    for i in range(int(sys.argv[1])):
        capture_image(i)
        pass
    
    return 0

if __name__ == "__main__":
    main()