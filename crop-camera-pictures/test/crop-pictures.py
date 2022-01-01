import os
from PIL import Image


def crop_current_directory():
    if 'crop' not in os.listdir('.'):
        raise Exception(
            "Create a 'crop' folder in the current directory before running the script.")
    files = [f for f in os.listdir('.') if os.path.isfile(
        f) and f.endswith('.png')]
    already_cropped = os.listdir('./crop')
    for idx, f in enumerate(files):
        if (str(f)[:-4] + '-cropped.png') in already_cropped:
            continue
        n = len(files)
        print(f'Cropping image {str(f)} ({idx}/{n}).')
        im = Image.open(str(f))
        width, height = im.size
        # cropped = im.crop((239, 90, width - 32, height - 61))
        cropped = im.crop((239, 169, width - 32, height - 119))
        file_name = str(f)
        file_name = file_name[:-4]
        cropped.save('crop/' + file_name + '-cropped.png')


if __name__ == "__main__":
    crop_current_directory()
