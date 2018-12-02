import os
import cv2

def convert_rgb_to_greyscale(input_dir: str,  output_dir: str):
    """
    :param int input_dir: input_directory of images.
    :param str output_dir: output_directory of images.
    """

    input_dir = os.fsencode(input_dir)
    for input_file in os.listdir(input_dir):
        input_filename = os.fsdecode(input_file)

        img = cv2.imread(input_filename , cv2.IMREAD_GRAYSCALE)

        output_filename = output_dir + '/' + input_filename
        cv2.imwrite(output_filename, img)

    return
