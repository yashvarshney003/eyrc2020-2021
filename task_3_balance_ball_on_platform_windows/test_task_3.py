# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: test_task_3.py
# Compiled at: 2020-10-13 11:41:31
# Size of source mod 2**32: 5165 bytes
"""
*****************************************************************************************
*
*        =================================================
*             Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        =================================================
*
*  This script is used to auto-evaluate Task 3 of
*  Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:                    test_task_3.py
*  Created:                             20/11/2020
*  Last Modified:               20/11/2020
*  Author:                              e-Yantra Team
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD (now MOE) project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
"""
import time, cv2, csv, numpy as np, os, sys, traceback, base64, string, random, datetime
if hasattr(sys, 'frozen'):
    sys.path.append(os.path.dirname(sys.executable))
try:
    student_code_task_3 = __import__('task_3')
except ImportError:
    print('\n[ERROR] task_3.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_3.py is present in this current directory.\n')
    sys.exit()
except Exception:
    print('\n[ERROR] Your task_3.py throwed an Exception, kindly debug your code!\n')
    traceback.print_exc(file=(sys.stdout))
    sys.exit()

try:
    student_code_task_2a = __import__('task_2a')
except ImportError:
    print('\n[ERROR] task_2a.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_2a.py is present in this current directory.\n')
    sys.exit()
except Exception:
    print('\n[ERROR] Your task_2a.py throwed an Exception, kindly debug your code!\n')
    traceback.print_exc(file=(sys.stdout))
    sys.exit()

try:
    student_code_task_1b = __import__('task_1b')
except ImportError:
    print('\n[ERROR] task_1b.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_1b.py is present in this current directory.\n')
    sys.exit()
except Exception:
    print('\n[ERROR] Your task_1b.py throwed an Exception, kindly debug your code!\n')
    traceback.print_exc(file=(sys.stdout))
    sys.exit()

try:
    student_code_task_1a_part_1 = __import__('task_1a_part1')
except ImportError:
    print('\n[ERROR] task_1a_part1.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure task_1a_part1.py is present in this current directory.\n')
    sys.exit()
except Exception:
    print('\n[ERROR] Your task_1a_part1.py throwed an Exception, kindly debug your code!\n')
    traceback.print_exc(file=(sys.stdout))
    sys.exit()
else:
    try:
        sim = __import__('sim')
    except Exception:
        print('\n[ERROR] It seems the sim.py OR simConst.py files are not found!\n')
        print('Your current directory is: ', os.getcwd())
        print('[WARNING] Make sure to have following files in the current directory:')
        print('sim.py, simConst.py and appropriate library - remoteApi.dll (if on Windows), remoteApi.so (if on Linux) or remoteApi.dylib (if on Mac).\n')
        sys.exit()
    else:
        green_ball_1 = 0
        vision_sensor_1 = 0
        concatenated_image = np.empty((1024, 1024, 3))
        list_of_setpoints = [
         [
          640, 640], [217, 217], [1063, 217], [217, 1063], [1063, 1063]]
        result_dict = {}

        def evaluate_student_code():
            global client_id
            global result_dict
            global vision_sensor_1
            try:
                student_code_task_3.init_setup(client_id)
            except Exception:
                print('\n[ERROR] Your init_setup() function throwed an Exception. Kindly debug your code!')
                print('Stop the CoppeliaSim simulation manually if started.\n')
                traceback.print_exc(file=(sys.stdout))
                print()
                sys.exit()
            else:
                center_x = 1063
                center_y = 1063
                for setpoint_count, setpoint in enumerate(list_of_setpoints):
                    print('\n====================================')
                    print('Setpoint ', setpoint_count, ':')
                    three_second_hold_time_flag = 0
                    reached_setpoint_flag = 0
                    duration = 0
                    drift_count = 0
                    if setpoint[0] != 640:
                        setpoint[0] = setpoint[0] - 17
                        setpoint[1] = setpoint[1] - 17
                    return_code_error_ring = sim.simxSetObjectPosition(client_id, error_ring_respondable_1, -1, [(setpoint[1] - 640) / 1280, (setpoint[0] - 640) / 1280, pos_top_plate_respondable_1[2] + 0.03], sim.simx_opmode_oneshot)
                    student_code_task_3.change_setpoint(setpoint)
                    init_simulation_time = 0
                    curr_simulation_time = 0
                    return_code_signal, init_simulation_time_string = sim.simxGetStringSignal(client_id, 'time', sim.simx_opmode_streaming)
                    if return_code_signal == 0:
                        init_simulation_time = float(init_simulation_time_string)
                    if curr_simulation_time - init_simulation_time <= 15:
                        return_code_signal, curr_simulation_time_string = sim.simxGetStringSignal(client_id, 'time', sim.simx_opmode_buffer)
                        if return_code_signal == 0:
                            curr_simulation_time = float(curr_simulation_time_string)
                        try:
                            vision_sensor_image, image_resolution, return_code = student_code_task_2a.get_vision_sensor_image(vision_sensor_1)
                            if return_code == sim.simx_return_ok:
                                if len(image_resolution) == 2:
                                    if len(vision_sensor_image) > 0:
                                        try:
                                            transformed_image = student_code_task_2a.transform_vision_sensor_image(vision_sensor_image, image_resolution)
                                            if type(transformed_image) is np.ndarray:
                                                try:
                                                    warped_img = student_code_task_1b.applyPerspectiveTransform(transformed_image)
                                                    if type(warped_img) is np.ndarray:
                                                        try:
                                                            shapes = student_code_task_1a_part_1.scan_image(warped_img)
                                                            if type(shapes) is dict and shapes != {}:
                                                                center_x = shapes['Circle'][1]
                                                                center_y = shapes['Circle'][2]
                                                            else:
                                                                if type(shapes) is not dict:
                                                                    print('\n[ERROR] scan_image function returned a ' + str(type(shapes)) + ' instead of a dictionary.')
                                                                    print('Stop the CoppeliaSim simulation manually.')
                                                                    print()
                                                                    sys.exit()
                                                        except Exception:
                                                            print('\n[ERROR] Your scan_image function in task_1a_part1.py throwed an Exception. Kindly debug your code!')
                                                            print('Stop the CoppeliaSim simulation manually.\n')
                                                            traceback.print_exc(file=(sys.stdout))
                                                            print()
                                                            sys.exit()

                                                    else:
                                                        print('\n[ERROR] applyPerspectiveTransform function did not return image in NumPy array and hence not configured correctly, check the code.')
                                                        print('Stop the CoppeliaSim simulation manually.')
                                                        print()
                                                except Exception:
                                                    print('\n[ERROR] Your applyPerspectiveTransform function in task_1b.py throwed an Exception. Kindly debug your code!')
                                                    print('Stop the CoppeliaSim simulation manually.\n')
                                                    traceback.print_exc(file=(sys.stdout))
                                                    print()
                                                    sys.exit()

                                            else:
                                                print('\n[ERROR] transform_vision_sensor_image function in task_2a.py did not return image in NumPy array and hence not configured correctly, check the code.')
                                                print('Stop the CoppeliaSim simulation manually.')
                                                print()
                                        except Exception:
                                            print('\n[ERROR] Your transform_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
                                            print('Stop the CoppeliaSim simulation manually.\n')
                                            traceback.print_exc(file=(sys.stdout))
                                            print()
                                            sys.exit()

                            try:
                                student_code_task_3.control_logic(center_x, center_y)
                                if abs(setpoint[0] - center_x) <= 50 and abs(setpoint[1] - center_y) <= 50:
                                    if reached_setpoint_flag == 0:
                                        three_second_init = curr_simulation_time
                                        duration = round(curr_simulation_time - init_simulation_time, 2)
                                        print('\nSetpoint hold initiated')
                                        reached_setpoint_flag = 1
                                elif three_second_hold_time_flag == 0:
                                    sys.stdout.write('\r')
                                    sys.stdout.write('{} seconds elapsed '.format(round(curr_simulation_time - three_second_init, 2)))
                                    sys.stdout.flush()
                                elif curr_simulation_time - three_second_init >= 3:
                                    three_second_hold_time_flag = 1
                                else:
                                    duration = round(curr_simulation_time - init_simulation_time, 2)
                                    three_second_init = curr_simulation_time
                                    if three_second_hold_time_flag == 1:
                                        drift_count += 1
                                        print('\nThe ball has drifted from setpoint ', setpoint_count)
                                    reached_setpoint_flag = 0
                                    three_second_hold_time_flag = 0
                            except:
                                print('\n[ERROR] Your control_logic function throwed an Exception. Kindly debug your code!')
                                print('Stop the CoppeliaSim simulation manually.\n')
                                traceback.print_exc(file=(sys.stdout))
                                print()
                                sys.exit()

                        except Exception:
                            print('\n[ERROR] Your get_vision_sensor_image function in task_2a.py throwed an Exception. Kindly debug your code!')
                            print('Stop the CoppeliaSim simulation manually.\n')
                            traceback.print_exc(file=(sys.stdout))
                            print()
                            sys.exit()

                    else:
                        if reached_setpoint_flag == 0:
                            print('\nUh oh. The ball was unable to reach the desired setpoint.')
                        elif three_second_hold_time_flag == 1:
                            print('\n\nSetpoint ', setpoint_count, ' hold complete')
                        else:
                            print('\nSetpoint ', setpoint_count, ' hold incomplete. Try tuning your control logic.')
                        result_dict.setdefault(str(setpoint), [duration, reached_setpoint_flag, three_second_hold_time_flag, drift_count])
                else:
                    print('\n====================================')


        def end_program():
            try:
                return_code = student_code_task_2a.stop_simulation()
                if return_code == sim.simx_return_novalue_flag:
                    print('\nSimulation stopped correctly.')
                    try:
                        student_code_task_2a.exit_remote_api_server()
                        if student_code_task_2a.start_simulation() == sim.simx_return_initialize_error_flag:
                            print('\nDisconnected successfully from Remote API Server in CoppeliaSim!')
                        else:
                            print('\n[ERROR] Failed disconnecting from Remote API server!')
                            print('[ERROR] exit_remote_api_server function in task_2a.py is not configured correctly, check the code!')
                    except Exception:
                        print('\n[ERROR] Your exit_remote_api_server function in task_2a.py throwed an Exception. Kindly debug your code!')
                        print('Stop the CoppeliaSim simulation manually.\n')
                        traceback.print_exc(file=(sys.stdout))
                        print()
                        sys.exit()

                else:
                    print('\n[ERROR] Failed stopping the simulation in CoppeliaSim server!')
                    print('[ERROR] stop_simulation function in task_2a.py is not configured correctly, check the code!')
                    print('Stop the CoppeliaSim simulation manually.')
                print()
                sys.exit()
            except Exception:
                print('\n[ERROR] Your stop_simulation function in task_2a.py throwed an Exception. Kindly debug your code!')
                print('Stop the CoppeliaSim simulation manually.\n')
                traceback.print_exc(file=(sys.stdout))
                print()
                sys.exit()


        def encode_and_delete_image(duration_of_code, teamID):
            date_time = str(datetime.datetime.now()) + '$$##@@'
            teamID = teamID + '$$##@@'
            duration_of_code = str(duration_of_code) + '$$##@@'
            student_answer_result = str(result_dict) + '\n' + '$$##@@'
            try:
                result_for_encoding = bytes(''.join(random.choices((string.ascii_uppercase + string.digits), k=119)), 'utf-8') + bytes(date_time, 'utf-8') + bytes(teamID, 'utf-8') + bytes(duration_of_code, 'utf-8') + bytes(student_answer_result, 'utf-8') + bytes(''.join(random.choices((string.ascii_uppercase + string.digits), k=285)), 'utf-8')
                img_encoded = base64.b64encode(result_for_encoding)
                output_file = open('task_3_output.txt', 'wb')
                output_file.write(img_encoded)
                output_file.close()
                print("\n'task_3_output.txt' file written successfully. Please check the file in the same directory in which you are running the code.")
            except KeyboardInterrupt:
                print('Program interrupted')
                end_program()
            except Exception:
                print('Unknown error occurred')
                traceback.print_exc(file=(sys.stdout))


        def check_scene():
            global error_ring_respondable_1
            global green_ball_1
            global pos_top_plate_respondable_1
            global vision_sensor_1
            try:
                return_code, green_ball_1 = sim.simxGetObjectHandle(client_id, 'green_ball_1', sim.simx_opmode_blocking)
                if return_code != 0:
                    print("\n[ERROR] Unable to locate 'green_ball_1' in the scene hierarchy. Undo the new changes or download the task_3.ttt scene file again.")
                    sys.exit()
            except:
                end_program()
                sys.exit()
            else:
                try:
                    return_code, error_ring_respondable_1 = sim.simxGetObjectHandle(client_id, 'error_ring_respondable_1', sim.simx_opmode_blocking)
                    if return_code != 0:
                        print("\n[ERROR] Unable to locate 'error_ring_respondable_1' in the scene hierarchy. Undo the new changes or download the task_3.ttt scene file again.")
                        sys.exit()
                except:
                    end_program()
                    sys.exit()
                else:
                    try:
                        return_code, error_ring_visual_1 = sim.simxGetObjectHandle(client_id, 'error_ring_visual_1', sim.simx_opmode_blocking)
                        if return_code != 0:
                            print("\n[ERROR] Unable to locate 'error_ring_visual_1' in the scene hierarchy. Undo the new changes or download the task_3.ttt scene file again.")
                            sys.exit()
                    except:
                        end_program()
                        sys.exit()
                    else:
                        try:
                            return_code, vision_sensor_dummy_1 = sim.simxGetObjectHandle(client_id, 'vision_sensor_dummy_1', sim.simx_opmode_blocking)
                            if return_code != 0:
                                print("\n[ERROR] Unable to locate 'vision_sensor_dummy_1' in the scene hierarchy. Undo the new changes or download the task_3.ttt scene file again.")
                                sys.exit()
                        except:
                            end_program()
                            sys.exit()
                        else:
                            try:
                                return_code, vision_sensor_1 = sim.simxGetObjectHandle(client_id, 'vision_sensor_1', sim.simx_opmode_blocking)
                                if return_code != 0:
                                    print("\n[ERROR] Unable to locate 'vision_sensor_1' in the scene hierarchy. Undo the new changes or download the task_3.ttt scene file again.")
                                    sys.exit()
                            except:
                                end_program()
                                sys.exit()
                            else:
                                try:
                                    return_code, top_plate_respondable_1 = sim.simxGetObjectHandle(client_id, 'top_plate_respondable_1', sim.simx_opmode_blocking)
                                    if return_code != 0:
                                        print("\n[ERROR] Unable to locate 'top_plate_respondable_1' in the scene hierarchy. Undo the new changes or download the task_3.ttt scene file again.")
                                        sys.exit()
                                except:
                                    end_program()
                                    sys.exit()
                                else:
                                    try:
                                        return_code, child_object_handle = sim.simxGetObjectChild(client_id, error_ring_respondable_1, 0, sim.simx_opmode_blocking)
                                        if return_code != 0:
                                            print("\n[ERROR] Unable to locate child of 'error_ring_respondable_1' in the scene hierarchy. Undo the new changes or download the task_3.ttt scene file again.")
                                            sys.exit()
                                        if child_object_handle != error_ring_visual_1:
                                            print("\n[ERROR] Parent-child relationship of 'error_ring_respondable_1' has been tampered. Undo the new changes or download the task_3.ttt scene file again.")
                                            sys.exit()
                                    except:
                                        end_program()
                                        sys.exit()
                                    else:
                                        try:
                                            return_code, child_object_handle = sim.simxGetObjectChild(client_id, vision_sensor_dummy_1, 0, sim.simx_opmode_blocking)
                                            if return_code != 0:
                                                print("\n[ERROR] Unable to locate child of 'vision_sensor_dummy_1' in the scene hierarchy. Undo the new changes or download the task_3.ttt scene file again.")
                                                sys.exit()
                                            if child_object_handle != vision_sensor_1:
                                                print("\n[ERROR] Parent-child relationship of 'vision_sensor_dummy_1' has been tampered. Undo the new changes or download the task_3.ttt scene file again.")
                                                sys.exit()
                                        except:
                                            end_program()
                                            sys.exit()
                                        else:
                                            return_code, pos_top_plate_respondable_1 = sim.simxGetObjectPosition(client_id, top_plate_respondable_1, -1, sim.simx_opmode_blocking)
                                            try:
                                                if pos_top_plate_respondable_1[2] > 0.35:
                                                    print('"\n[ERROR] Height of the design exceeds the maximum limit mentioned. Reduce the height of the design and try again.')
                                                    sys.exit()
                                            except:
                                                end_program()
                                            else:
                                                return_code = sim.simxSetObjectPosition(client_id, error_ring_respondable_1, -1, [0, 0, pos_top_plate_respondable_1[2] + 0.03], sim.simx_opmode_oneshot)
                                                return_code = sim.simxSetObjectOrientation(client_id, error_ring_respondable_1, -1, [0, 0, 0], sim.simx_opmode_oneshot)
                                                return_code = sim.simxSetObjectPosition(client_id, green_ball_1, -1, [0.3235, 0.3235, pos_top_plate_respondable_1[2] + 0.03], sim.simx_opmode_oneshot)
                                                return_code = sim.simxSetObjectPosition(client_id, vision_sensor_dummy_1, -1, [0, 0, 1.225], sim.simx_opmode_oneshot)
                                                return_code = sim.simxSetObjectOrientation(client_id, vision_sensor_dummy_1, -1, [0, 0, 3.142857142857143], sim.simx_opmode_oneshot)


try:
    if __name__ == '__main__':
        print('\nWelcome to test script for Task 3 of Nirikshak Bot (NB) theme.')
        teamID = input('Please enter your team ID: NB_')
        try:
            conda_env = os.environ['CONDA_DEFAULT_ENV']
        except KeyError:
            print('\n[ERROR] Conda environment is not activated. Activate Conda environment named after your Team ID.')
            sys.exit()
        else:
            if conda_env != 'NB_' + teamID:
                print("Uh oh!! Your conda enviroment's name does not match with your Team ID. Please select the correct conda environment.")
                sys.exit()
            print('\nConnection to CoppeliaSim Remote API Server initiated.')
            print('Trying to connect to Remote API Server...')
            try:
                client_id = student_code_task_2a.init_remote_api_server()
                if client_id != -1:
                    print('\nConnected successfully to Remote API Server in CoppeliaSim!')
                    try:
                        return_code = student_code_task_2a.start_simulation()
                        if return_code == sim.simx_return_novalue_flag:
                            print('\nSimulation started correctly in CoppeliaSim.')
                            start_time_of_code = time.time()
                            check_scene()
                            evaluate_student_code()
                            end_time_of_code = time.time()
                            encode_and_delete_image(int(end_time_of_code - start_time_of_code), teamID)
                            end_program()
                        else:
                            print('\n[ERROR] Failed starting the simulation in CoppeliaSim!')
                            print('start_simulation function in task_2a.py is not configured correctly, check the code!')
                            print()
                            sys.exit()
                    except Exception:
                        print('\n[ERROR] Your start_simulation function in task_2a.py throwed an Exception, kindly debug your code!')
                        print('Stop the CoppeliaSim simulation manually.\n')
                        traceback.print_exc(file=(sys.stdout))
                        print()
                        sys.exit()

                else:
                    print('\n[ERROR] Failed connecting to Remote API server!')
                    print('[WARNING] Make sure the CoppeliaSim software is running and')
                    print('[WARNING] Make sure the Port number for Remote API Server is set to 19997.')
                    print('[ERROR] OR init_remote_api_server function in task_2a.py is not configured correctly, check the code!')
                    print()
                    sys.exit()
            except Exception:
                print('\n[ERROR] Your init_remote_api_server function in task_2a.py throwed an Exception, kindly debug your code!')
                print('Stop the CoppeliaSim simulation manually if started.\n')
                traceback.print_exc(file=(sys.stdout))
                print()
                sys.exit()
            except KeyboardInterrupt:
                print('\n[ERROR] Test script for Task 3 interrupted by user!')
                end_program()

except KeyboardInterrupt:
    print('\n[ERROR] Program interrupted by user!')
    end_program()
except Exception:
    print('\n[ERROR] An Exception occurred, kindly debug your code!')
    print('Stop the CoppeliaSim simulation manually if started.\n')
    traceback.print_exc(file=(sys.stdout))
    print()
    sys.exit()