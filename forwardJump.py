"""
This script shows a simple scripted flight path using the MotionCommander class.

Simple example that connects to the crazyflie at `URI` and runs a
sequence. Change the URI variable to your Crazyflie configuration.
"""
import logging
import time

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/2M'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI) as scf:
        # Arm the Crazyflie
        scf.cf.platform.send_arming_request(True)
        time.sleep(1.0)

        # We take off when the commander is created
        with MotionCommander(scf, 0.04) as mc:
            print('Taking off!')
            time.sleep(1)

            print('Moving forward 0.5m')
            mc.forward(0.5)
            time.sleep(1)

            mc.up(0.5)
            time.sleep(1)

            mc.forward(1.5)
            time.sleep(1)

            mc.down(0.5)
            time.sleep(1)

            mc.forward(0.5)
            time.sleep(1)

            # We land when the MotionCommander goes out of scope
            print('Landing!')
