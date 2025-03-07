"""
Example script that allows a user to "push" the Crazyflie 2.x around
using your hands while it's hovering.

This examples uses the Flow and Multi-ranger decks to measure distances
in all directions and tries to keep away from anything that comes closer
than 0.2m by setting a velocity in the opposite direction.

The demo is ended by either pressing Ctrl-C or by holding your hand above the
Crazyflie.
"""
import logging
import sys
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils.multiranger import Multiranger

URI = 'radio://0/82/2M/E7E7E7E7E8'

if len(sys.argv) > 1:
    URI = sys.argv[1]

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


def is_close(range):
    MIN_DISTANCE = 0.2  # m

    if range is None:
        return False
    else:
        return range < MIN_DISTANCE


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    cf = Crazyflie(rw_cache='./cache')

    jumpBool = False
    velocity_z = 0.0

    with SyncCrazyflie(URI, cf=cf) as scf:
        # Arm the Crazyflie
        scf.cf.platform.send_arming_request(True)
        time.sleep(1.0)

        with MotionCommander(scf) as motion_commander:
            with Multiranger(scf) as multi_ranger:
                keep_flying = True

                while keep_flying:
                    VELOCITY = 0.5
                    velocity_x = 0.5
                    velocity_y = 0.0

                    # if is_close(multi_ranger.front):
                    #     velocity_x -= VELOCITY
                    # if is_close(multi_ranger.back):
                    #     velocity_x += VELOCITY

                    # if is_close(multi_ranger.left):
                    #     velocity_y -= VELOCITY
                    # if is_close(multi_ranger.right):
                    #     velocity_y += VELOCITY

                    # if is_close(multi_ranger.up):
                    #     keep_flying = False

                    if is_close(multi_ranger.front):
                        if jumpBool is False:
                            velocity_x -= VELOCITY
                            velocity_z += 0.1
                            jumpBool = True

                    if not is_close(multi_ranger.front):
                        jumpBool = False
                        velocity_z = 0.0

                    motion_commander.start_linear_motion(
                        velocity_x, velocity_y, velocity_z)

                    time.sleep(0.1)

            print('Demo terminated!')
