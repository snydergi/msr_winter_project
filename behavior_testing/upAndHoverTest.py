import logging
import sys
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils.multiranger import Multiranger

# URI = 'radio://0/82/2M/E7E7E7E7E8'
URI = 'radio://0/80/2M/E7E7E7E7E7'

if len(sys.argv) > 1:
    URI = sys.argv[1]

# Only output errors from the logging framework
logging.basicConfig(level=logging.DEBUG)


def is_close(range):
    MIN_DISTANCE = 0.15  # m

    if range is None:
        return False
    else:
        return range < MIN_DISTANCE


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    cf = Crazyflie(rw_cache='./cache')

    jumpBool = False

    with SyncCrazyflie(URI, cf=cf) as scf:
        # Arm the Crazyflie
        scf.cf.platform.send_arming_request(True)
        time.sleep(1.0)

        with MotionCommander(scf, 0.1) as motion_commander:
            with Multiranger(scf) as multi_ranger:
                keep_flying = True

                while keep_flying:
                    VELOCITY = 0.5
                    velocity_x = 0.0
                    velocity_y = 0.0
                    velocity_z = 0.0

                    if is_close(multi_ranger.front):
                        velocity_z = 0.2

                    # if is_close(multi_ranger.up):
                    #     keep_flying = False

                    motion_commander.start_linear_motion(
                        velocity_x, velocity_y, velocity_z)

                    time.sleep(0.01)

            print('Demo terminated!')
