import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fyp3/Desktop/ros2_swarm_mapping/install/hardware_software'
