# uncompyle6 version 3.6.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version has problems handling the Python 3 byte type in contants properly.

# Embedded file name: /home/erts-09/Documents/GitHub/Maze-Bot/Tasks/Task_1/Task_1A/Solution/Task_1A_Part1/test.py
# Size of source mod 2**32: 5165 bytes
"""
*****************************************************************************************
*
*        =================================================
*             Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        =================================================
*
*  This script is intended to check the output of Task 1A - Part 1
*  of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:                    task_1b_cardinal.py
*  Created:                             11/10/2020
*  Last Modified:               12/10/2020
*  Author:                              e-Yantra Team
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
"""
import string, random, base64, os, sys, platform
from datetime import datetime
import cv2, numpy as np

def random_string(length=10, char=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation):
    return ''.join((random.choice(char) for x in range(length)))


def encode_with_random_string(str_input):
    
    str_input = random_string(7) + str_input + random_string(7)
    str_output = base64.b64encode(str_input.encode('utf-8')).decode('utf-8')
    return str_output


if __name__ == '__main__':
    try:
        team_id = 2139
        print("hello")
    except ValueError:
        print('\n[ERROR] Enter your Team ID which is an integer!\n')
        sys.exit()
    else:
        platform_uname = platform.uname().system
        conda_env_name = os.environ['CONDA_DEFAULT_ENV']
        expected_conda_env_name = 'NB_' + str(team_id)
        if conda_env_name == expected_conda_env_name:
            conda_env_name_flag = 1
        else:
            conda_env_name_flag = 0
            print('\n[WARNING] Conda environment name is not found as expected: NB_%s. Run this file with correct conda environment.\n' % str(team_id))
            sys.exit()
    if conda_env_name_flag == 1:
        output_txt_file_name = 'task_1a_part1_output.txt'
        if os.path.exists(output_txt_file_name):
            os.remove(output_txt_file_name)
        output_txt_file_obj = open(output_txt_file_name, 'w')
        output_txt_file_obj.write(encode_with_random_string('Team ID') + encode_with_random_string(str(team_id)) + '\n')
        output_txt_file_obj.write(encode_with_random_string('OS') + encode_with_random_string(platform_uname) + '\n')
        try:
            import task_1a_part1
        except ImportError:
            print('\n[ERROR] task_1a_part1.py file is not present in this folder. Make sure task_1a_part1.py is present in current directory.\n')
            sys.exit()
        else:
            curr_dir_path = os.getcwd()
            print('\nCurrently working in ' + curr_dir_path)
            img_dir_path = curr_dir_path + '/Samples/'
            file_count = 3
            for file_num in range(file_count):
                img_file_path = img_dir_path + 'Sample' + str(file_num + 1) + '.png'
                print('\n============================================')
                print('\nLooking for Test' + str(file_num + 1) + '.png')
                if os.path.exists('Test_Images/Test' + str(file_num + 1) + '.png'):
                    print('\nFound Test' + str(file_num + 1) + '.png')
                else:
                    print('\n[ERROR] Test' + str(file_num + 1) + '.png not found. Make sure "Test_Images" folder has the selected file.')
                    exit()
                print('\n============================================')
                try:
                    print('\nRunning scan_image function with ' + img_file_path + ' as an argument')
                    shapes = task_1a_part1.scan_image(img_file_path)
                    if type(shapes) is dict:
                        print(shapes)
                        print('\n')
                        output_txt_file_obj.write(encode_with_random_string('For Test' + str(file_num + 1) + '.png image') + '\n')
                        output_txt_file_obj.write(encode_with_random_string(str(shapes)) + '\n')
                    else:
                        print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.\n')
                        exit()
                except Exception:
                    print('\n[ERROR] scan_image function is throwing an error. Please debug scan_image function')
                    exit()
                else:
                    print('\n============================================')

            current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            output_txt_file_obj.write(encode_with_random_string('Date and Time of execution') + encode_with_random_string(current_time) + '\n')
            output_txt_file_obj.close()
            print('\n' + output_txt_file_name + ' generated!')