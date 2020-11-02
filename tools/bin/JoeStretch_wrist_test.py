#!/usr/bin/env python
from stretch_body.hello_utils import *
import sys
import stretch_body.wrist_yaw as wrist_yaw
import argparse
import stretch_body.xbox_controller as xc

print_stretch_re_use()

parser=argparse.ArgumentParser(description='Jog the wrist_yaw joint from the keyboard')
args=parser.parse_args()

poses = {'zero':0, 'left':deg_to_rad(90), 'right': deg_to_rad(-45)}
w=wrist_yaw.WristYaw()
w.startup()

xbox_controller = xc.XboxController()
xbox_controller.start()

v_des=w.params['motion']['default']['vel']
a_des=w.params['motion']['default']['accel']
 wrist_yaw_left = controller_state['left_shoulder_button_pressed']
wrist_yaw_right = controller_state['right_shoulder_button_pressed']
def menu_top():
    print('------ MENU -------')
    print('m: menu')
    print('controller left shoulder: increment 15 deg')
    print('controller right shoulder: decrement 15 deg')
    

def step_interaction():
    global v_des, a_des
    menu_top()
    x=sys.stdin.readline()
    if wrist_yaw_left:
        w.move_by(deg_to_rad(15), v_des, a_des)

    if wrist_yaw_right == 'b':
        w.move_by(deg_to_rad(-15), v_des, a_des)

    else:
        w.pretty_print()

try:
    while True:
        try:
            step_interaction()
        except (ValueError):
            print('Bad input...')
        w.pull_status()
except (ThreadServiceExit, KeyboardInterrupt):
    w.stop()

