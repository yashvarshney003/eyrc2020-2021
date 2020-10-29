# uncompyle6 version 3.6.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version has problems handling the Python 3 byte type in contants properly.

# Embedded file name: /home/erts-09/Documents/GitHub/Maze-Bot/Tasks/Task_1/Task_1B/task_1b_cardinal.py
# Size of source mod 2**32: 13394 bytes
"""
*****************************************************************************************
*
*        =================================================
*             Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        =================================================
*
*  This script is intended to check the output of Task 1B
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
import os, sys, platform, csv, cv2, numpy as np, string, random, base64
from datetime import datetime
format_check_flag = True
maze_array_score = 0
maze00_ideal = [
 [
  7, 3, 10, 10, 6, 3, 10, 6, 3, 6], [1, 12, 3, 10, 12, 5, 7, 9, 12, 5],
 [
  1, 14, 9, 6, 7, 5, 9, 10, 6, 5], [5, 3, 6, 5, 5, 9, 6, 3, 12, 5],
 [
  5, 5, 9, 12, 1, 14, 9, 4, 3, 4], [5, 9, 6, 7, 1, 10, 10, 12, 5, 13],
 [
  9, 6, 5, 1, 8, 10, 10, 14, 9, 6], [7, 5, 5, 9, 6, 3, 6, 3, 6, 5],
 [
  5, 5, 9, 14, 13, 5, 9, 12, 5, 5], [9, 8, 10, 10, 10, 12, 11, 10, 8, 12]]
maze01_ideal = [
 [
  7, 11, 2, 2, 6, 7, 3, 14, 7, 7], [9, 10, 4, 13, 13, 9, 0, 10, 0, 4],
 [
  3, 14, 1, 2, 14, 11, 0, 14, 13, 13], [1, 2, 12, 13, 11, 2, 12, 7, 7, 7],
 [
  5, 1, 14, 7, 3, 8, 10, 8, 8, 4], [5, 13, 7, 1, 12, 3, 10, 14, 11, 12],
 [
  5, 7, 1, 8, 2, 8, 2, 14, 7, 7], [9, 8, 4, 7, 13, 7, 13, 7, 1, 12],
 [
  11, 6, 1, 8, 10, 0, 2, 0, 8, 14], [11, 8, 8, 10, 14, 13, 13, 9, 10, 14]]
maze02_ideal = [
 [
  7, 7, 11, 6, 3, 10, 6, 7, 3, 14], [5, 5, 11, 8, 0, 14, 9, 8, 0, 14],
 [
  1, 0, 10, 14, 13, 11, 6, 3, 8, 14], [13, 5, 11, 2, 14, 3, 8, 0, 10, 6],
 [
  3, 0, 2, 8, 2, 12, 11, 0, 14, 13], [5, 5, 5, 11, 8, 14, 11, 4, 3, 14],
 [
  5, 5, 5, 11, 10, 2, 2, 8, 8, 6], [5, 13, 1, 6, 11, 12, 1, 6, 3, 12],
 [
  1, 6, 13, 5, 3, 10, 4, 5, 1, 6], [13, 9, 14, 13, 13, 11, 12, 13, 13, 13]]
maze03_ideal = [
 [
  7, 11, 2, 14, 3, 14, 3, 2, 2, 6], [5, 11, 0, 2, 8, 2, 4, 13, 13, 5],
 [
  1, 10, 12, 13, 11, 12, 9, 2, 14, 5], [13, 11, 6, 3, 2, 10, 10, 0, 14, 5],
 [
  3, 10, 8, 4, 13, 3, 10, 0, 14, 5], [13, 11, 10, 4, 3, 12, 11, 0, 14, 5],
 [
  11, 10, 2, 4, 5, 7, 7, 1, 6, 13], [3, 2, 4, 13, 13, 1, 0, 4, 9, 6],
 [
  13, 5, 13, 11, 10, 12, 5, 5, 11, 4], [11, 12, 11, 10, 10, 10, 12, 13, 11, 12]]
maze04_ideal = [
 [
  7, 11, 2, 10, 10, 10, 6, 3, 14, 7], [5, 7, 13, 7, 7, 11, 0, 4, 3, 12],
 [
  1, 12, 7, 9, 4, 7, 13, 5, 1, 14], [1, 14, 1, 6, 1, 4, 7, 5, 5, 7],
 [
  1, 14, 13, 5, 13, 9, 0, 8, 8, 12], [9, 10, 6, 9, 10, 2, 8, 2, 10, 14],
 [
  7, 3, 4, 7, 11, 12, 7, 1, 10, 14], [9, 4, 13, 9, 10, 2, 8, 0, 2, 14],
 [
  3, 0, 10, 6, 11, 4, 11, 12, 1, 14], [13, 13, 11, 8, 10, 8, 10, 14, 9, 14]]
maze05_ideal = [
 [
  7, 3, 10, 14, 3, 2, 10, 14, 11, 6], [5, 1, 14, 11, 4, 9, 6, 11, 10, 4],
 [
  1, 0, 2, 14, 13, 11, 0, 14, 3, 12], [5, 13, 9, 2, 10, 10, 4, 7, 5, 7],
 [
  9, 14, 11, 12, 3, 10, 8, 0, 8, 12], [11, 6, 11, 10, 12, 7, 11, 4, 3, 14],
 [
  11, 0, 10, 10, 6, 1, 2, 0, 0, 14], [11, 12, 11, 2, 0, 4, 5, 13, 9, 6],
 [
  11, 10, 2, 4, 13, 5, 1, 2, 6, 5], [11, 10, 12, 13, 11, 12, 13, 13, 13, 13]]
maze06_ideal = [
 [
  7, 3, 6, 3, 6, 3, 10, 2, 10, 6], [1, 12, 9, 12, 9, 12, 3, 12, 7, 5],
 [
  9, 10, 10, 6, 7, 3, 12, 11, 4, 5], [3, 6, 3, 12, 5, 9, 10, 6, 5, 5],
 [
  5, 9, 8, 14, 1, 2, 14, 5, 1, 12], [5, 11, 2, 2, 12, 5, 3, 12, 5, 7],
 [
  9, 6, 5, 5, 11, 4, 9, 6, 9, 4], [3, 12, 13, 9, 6, 9, 6, 5, 7, 5],
 [
  5, 3, 10, 6, 5, 11, 12, 5, 5, 5], [9, 12, 11, 8, 12, 11, 10, 12, 9, 12]]






maze07_ideal = [
 [
  3, 14, 3, 10, 10, 10, 10, 2, 10, 6], [5, 3, 12, 11, 6, 3, 6, 13, 3, 4],
 [
  5, 9, 2, 10, 12, 5, 9, 6, 5, 13], [1, 14, 5, 3, 6, 9, 6, 5, 9, 6],
 [
  9, 10, 12, 5, 9, 10, 12, 5, 3, 12], [3, 10, 6, 5, 7, 3, 10, 12, 9, 6],
 [
  5, 11, 8, 12, 5, 5, 3, 6, 3, 12], [5, 7, 3, 10, 4, 5, 5, 5, 9, 6],
 [
  5, 5, 9, 6, 5, 9, 12, 9, 6, 5], [9, 12, 11, 12, 9, 10, 10, 10, 8, 12]
  ]





maze08_ideal = [
 [
  3, 2, 10, 10, 10, 10, 6, 11, 2, 6], [5, 5, 3, 10, 10, 6, 9, 6, 13, 5],
 [
  5, 9, 8, 10, 14, 5, 3, 8, 10, 4], [5, 3, 6, 3, 10, 12, 13, 3, 6, 13],
 [
  9, 12, 5, 9, 10, 10, 10, 12, 9, 6], [3, 14, 9, 10, 10, 10, 2, 14, 3, 12],
 [
  1, 6, 3, 10, 2, 14, 5, 3, 12, 7], [5, 9, 12, 7, 9, 10, 12, 13, 3, 4],
 [
  9, 6, 3, 4, 3, 10, 10, 6, 13, 5], [11, 8, 12, 9, 12, 11, 10, 8, 10, 12]]


  
maze09_ideal = [
 [
  3, 2, 10, 14, 3, 10, 10, 6, 11, 6], [5, 5, 11, 10, 12, 3, 14, 9, 10, 4],
 [
  5, 9, 6, 3, 10, 8, 10, 10, 10, 12], [5, 3, 4, 9, 6, 3, 2, 10, 10, 14],
 [
  5, 5, 5, 3, 12, 5, 13, 3, 10, 6], [5, 5, 5, 5, 7, 1, 6, 5, 3, 4],
 [
  5, 5, 13, 5, 9, 12, 5, 5, 5, 5], [5, 9, 6, 9, 6, 3, 12, 5, 5, 5],
 [
  5, 7, 9, 6, 5, 9, 10, 12, 5, 5], [9, 8, 14, 9, 8, 10, 10, 10, 12, 13]]



  
local_vars = locals()

def random_string(length=10, char=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation):
    return ''.join((random.choice(char) for x in range(length)))


def encode_with_random_string(str_input):
    str_input = random_string(7) + str_input + random_string(7)
    str_output = base64.b64encode(str_input.encode('utf-8')).decode('utf-8')
    return str_output


def check_format(maze_array):
    global format_check_flag
    if isinstance(maze_array, list) and len(maze_array) == 10:
        for maze_row in range(0, len(maze_array)):
            if isinstance(maze_array[maze_row], list) and len(maze_array[maze_row]) == 10:
                for row_cell in range(0, len(maze_array[maze_row])):
                    if isinstance(maze_array[maze_row][row_cell], int):
                        format_check_flag = format_check_flag and True
                    else:
                        format_check_flag = format_check_flag and False
                        print('\n[ERROR] Encoded values in Maze Array are not integers. Check your script to generate task_1b_output.csv.')
                        break

            else:
                format_check_flag = format_check_flag and False
                print('\n[ERROR] The encoded maze array is not a list of list OR a nested list. Check your script to generate task_1b_output.csv.')
                break

    else:
        format_check_flag = format_check_flag and False
        print('\n[ERROR] The encoded maze array is not a list. Check your script to generate task_1b_output.csv.')
    if format_check_flag == True:
        print('\nEncoded Maze Array = %s' % maze_array)
    return format_check_flag


def compare_maze_arrays(maze_array_generated, maze_array_ideal):
    global maze_array_score
    maze_array_score = 0
    if abs(len(maze_array_generated) - len(maze_array_ideal)) == 0:
        for maze_row in range(0, len(maze_array_ideal)):
            for row_cell in range(0, len(maze_array_ideal[maze_row])):
                if maze_array_generated[maze_row][row_cell] == maze_array_ideal[maze_row][row_cell]:
                    maze_array_score = maze_array_score + 1
                else:
                    maze_array_score = maze_array_score - 1

    else:
        maze_array_score = 0
    return maze_array_score


def main():
    try:
        team_id = int(input('\nEnter your Team ID (for e.g.: "1234" or "321"): '))
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
            output_csv_file_name = 'task_1b_output.csv'
            if os.path.exists(output_csv_file_name):
                os.remove(output_csv_file_name)
            try:
                import task_1b
            except ImportError:
                print('\n[ERROR] task_1b.py file is not present in this folder. Make sure task_1b.py is present in current directory.\n')
                sys.exit()
            else:
                img_dir_path = 'test_cases/'
                for file_num in range(0, 10):
                    img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'
                    print('\n============================================')
                    print('\nFor maze0' + str(file_num) + '.jpg')
                    input_img = cv2.imread(img_file_path)
                    warped_img = task_1b.applyPerspectiveTransform(input_img)
                    if type(warped_img) is np.ndarray:
                        maze_array = task_1b.detectMaze(warped_img)
                        format_check_flag = check_format(maze_array)
                        if format_check_flag:
                            if file_num == 0:
                                output_csv_file_obj = open(output_csv_file_name, 'w', newline='')
                                csv_writer_obj = csv.writer(output_csv_file_obj)
                                team_id_platform_csv_row = [
                                 encode_with_random_string('Team ID'), encode_with_random_string(str(team_id)),
                                 encode_with_random_string('OS'), encode_with_random_string(platform_uname)]
                                csv_writer_obj.writerow(team_id_platform_csv_row)
                            else:
                                maze_array_ideal_name = 'maze0' + str(file_num) + '_ideal'
                                maze_array_score = compare_maze_arrays(maze_array, local_vars[maze_array_ideal_name])
                                if maze_array_score == 100:
                                    print('\nYour code successfully passed the test case maze0' + str(file_num) + ' image.')
                                else:
                                    print('\n[WARNING] Your code failed for the test case maze0' + str(file_num) + ' image. Check your code.')
                            maze_img_score_csv_row = [encode_with_random_string('For maze0' + str(file_num) + '.jpg'), encode_with_random_string(str(maze_array_score))]
                            csv_writer_obj.writerow(maze_img_score_csv_row)
                            for maze_row in range(0, len(maze_array)):
                                maze_array_data_csv_row = []
                                for row_cell in range(0, len(maze_array[maze_row])):
                                    maze_array_data_csv_row.append(encode_with_random_string(str(maze_array[maze_row][row_cell])))

                                csv_writer_obj.writerow(maze_array_data_csv_row)

                            print('\n============================================')
                        else:
                            print('\n[ERROR] maze_array returned by detectMaze function is incomplete OR not in expected format! Check the function in code.\n')
                            exit()
                    else:
                        print('\n[ERROR] applyPerspectiveTransform function is not returning the warped maze image in expected format! Check the function in code.\n')
                        exit()

                current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                current_time_csv_row = [encode_with_random_string('Date and Time of execution'), encode_with_random_string(current_time)]
                csv_writer_obj.writerow(current_time_csv_row)


if __name__ == '__main__':
    main()