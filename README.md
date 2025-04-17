# Hybrid Locomotion Robot

## Featured Video
Click on image to get to video or view it on portfolio (link below)!
[![Featured Video](https://img.youtube.com/vi/Cmba8ZEuzpo/0.jpg)](https://www.youtube.com/watch?v=Cmba8ZEuzpo)

## Portfolio Link
To read more about this project, check it out on my portfolio [here](https://snydergi.github.io/portfolio_featured/rajad/)!

## Project Needs
### Hardware
- Laptop
- Crazyflie 2.1+
- CrazyRadio 2.0
- Crazyflie Flow Deck V2
- Crazyflie Thrust Upgrade Bundle

### Software
- Python `venv` with the following installed:
  - `crazyflie-firmware`
  - `crazyflie-lib-python`
  - `cfclient`

## Startup
The general startup can be found [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/).

A helpful page for getting started writing autonomous programs can be found [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-stem-drone-bundle/#).

Follow [this](https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/building-and-flashing/build/#build-python-bindings) tutorial for building and flashing firmware to the Crazyflie.

To begin the startup process, activate the Python `venv` where the Crazyflie software packages were installed. 

For teleoperating, run the `cfclient` in the terminal, connect to the Crazyflie, and begin piloting.

For autonomous operation, run the program with the `venv` version of Python.
