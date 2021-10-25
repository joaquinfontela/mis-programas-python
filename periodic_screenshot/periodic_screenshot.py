from time import sleep, gmtime
import datetime
import os
import sys
from PeriodError import PeriodError
screenshots_folder_name = 'screenshots'
explicit = True

try:
    import pyautogui
except ModuleNotFoundError:
    raise Exception(
        "Install 'pyautogui' module to be able to run this program. Recommended command: 'pip install pyautogui'.")


def process_argv(argv):
    """
    Processes the arguments from the second to the end and defines the values of the corresponding variables.
    """
    argv = argv[2:]
    for arg in argv:
        if arg[0] != '-':
            raise Exception(
                f"Can't process argument: {arg}. Try typing it starting with '-'.")

        arg = arg[1:]
        splitted = arg.split('=')

        if len(splitted) != 2:
            raise Exception(f"Can't process argument: {arg}")

        if splitted[0] == 'explicit':
            if splitted[1] not in ['yes', 'no']:
                raise Exception(
                    f"Can't process argument 'explicit' with value: '{splitted[1]}'")
            global explicit
            explicit = (splitted[1] == 'yes')

        elif splitted[0] == 'dest_folder':
            if splitted[1] == '':
                raise Exception(
                    f"You must define a non-empty string value for argument 'dest_folder'.")
            global screenshots_folder_name
            screenshots_folder_name = splitted[1]

        else:
            raise Exception(f"Unknown argument {splitted[0]}")


def create_screenshots_directory():
    """
    Checks if it exists a directory to save the screenshots taken during the execution of the program.
    If it doesn't, it creates one with name SCREENSHOTS_FOLDER_NAME.
    """
    cur_dir = os.getcwd()
    file_list = os.listdir(cur_dir)
    if not screenshots_folder_name in file_list:
        os.mkdir(screenshots_folder_name)


def periodic_screenshot():
    """
    This program recieves a positive integer 'period' as the first argument.
    It will execute an infinite loop taking a screenshot every 'period' seconds.
    Each screenshot will be saved into SCREENSHOTS_FOLDER_NAME
    with a name referring to the datetime it was taken.
    Optional arguments:
    '-explicit': prints extra information about each screenshot. Possible values: ['yes', 'no'].
    '-dest_folder': lets the user change the name of the screenshots folder. Must be a non-null value.
    """
    if len(sys.argv) == 1:
        raise PeriodError("You didn't specify screenshot period.")
    period = sys.argv[1]
    if not period.isdigit():
        raise PeriodError(
            "Period value error: not a positive whole number.")
    process_argv(sys.argv)
    create_screenshots_directory()
    period = int(period)
    print(
        f'From now on, this program will start screenshooting every {period} seconds.\n')
    n_screenshots = 0

    while not sleep(period):
        shot = pyautogui.screenshot()
        n_screenshots += 1
        print(
            f'Took screenshot number {n_screenshots} at datetime {datetime.datetime.now()}.') if explicit else None
        cur_time = gmtime()
        shot_name = str(cur_time.tm_year) + str(cur_time.tm_mon) + str(cur_time.tm_mday) +\
            str(cur_time.tm_hour) + str(cur_time.tm_min) + str(cur_time.tm_sec)
        shot.save(f'./{screenshots_folder_name}/{shot_name}.png')
        print(f'Saved screenshot {shot_name}.') if explicit else None


if __name__ == '__main__':
    periodic_screenshot()
