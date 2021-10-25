from time import sleep, gmtime
import os
import sys
SCREENSHOTS_FOLDER_NAME = 'screenshots'

try:
    import pyautogui
except ModuleNotFoundError:
    raise Exception(
        "Run 'pip install pyautogui' to install the corresponding dependency.")


def create_screenshots_directory():
    """
    Checks if it exists a directory to save the screenshots taken during the execution of the program.
    If it doesn't, it creates one with name SCREENSHOTS_FOLDER_NAME.
    """
    cur_dir = os.getcwd()
    file_list = os.listdir(cur_dir)
    if not SCREENSHOTS_FOLDER_NAME in file_list:
        os.mkdir(SCREENSHOTS_FOLDER_NAME)


def periodic_screenshot():
    """
    This program recieves a positive integer 'period' as an unique argument.
    It will execute an infinite loop taking a screenshot every 'period' seconds.
    Each screenshot will be saved into SCREENSHOTS_FOLDER_NAME
    with a name referring to the datetime it was taken.
    """
    if len(sys.argv) == 1:
        raise Exception("You didn't specify screenshot period.")
    period = sys.argv[1]
    if not period.isdigit():
        raise Exception("Period value error: not a positive whole number.")
    create_screenshots_directory()
    period = int(period)
    print(
        f'From now on, this program will start screenshooting every {period} seconds.\n')

    while not sleep(period):
        shot = pyautogui.screenshot()
        cur_time = gmtime()
        shot_name = str(cur_time.tm_year) + str(cur_time.tm_mon) + str(cur_time.tm_mday) +\
            str(cur_time.tm_hour) + str(cur_time.tm_min) + str(cur_time.tm_sec)
        shot.save(f'./{SCREENSHOTS_FOLDER_NAME}/{shot_name}.png')
        print(f'Saved screenshot {shot_name}.')


if __name__ == '__main__':
    periodic_screenshot()
