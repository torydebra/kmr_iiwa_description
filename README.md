# kmr_iiwa_description
Package for the Kuka Mobile Robotic Base (MRB) with the LBR-IIWA arm. The standalone base is called KMP-200.  
Repo include urdf and description for the mobile base, which I could not find available for ROS2 jazzy.

Use of the mobile base + arm in ROS2 jazzy is still work in progress. So far I could not find a working repo that utilize both in ROS2



## Mobile base

- Meshes and urdf for the kmp200, that is, the mobile base part of the kmr_iiwa, Taken from
https://github.com/kidpaul94/kmr-iiwa-gripkit-cr-plus-l/tree/main

- Simulated base use virtual base hardware interface and relative controller: https://github.com/torydebra/gz_virtual_base_system

## Arm description
Geometry, kinematic, meshes, ROS2 controllers taken from what should be the official one  https://github.com/lbr-stack/lbr_fri_ros2_stack/tree/582fbb06d0b964f1a6fc49fe48c6ee132c0d8b9f/lbr_description/urdf/iiwa14

# Code

## arm + base software
- https://github.com/LAKY911/kmriiwa_ws_devel/, check also its fork of fork

## mobile base code
- https://github.com/JonahEggenkemper/kuka-kmr-project/tree/main. Using custom java-ros1 interface to control the mobile base in ros1

## kuka IIWA Arm controllers
- first google results, lot of star, ros2, only arm https://github.com/ICube-Robotics/iiwa_ros2
- another with some starts https://github.com/idra-lab/kuka_lbr_control, Trento Uni


## useful commands
### controllers
`ros2 control switch_controllers --activate joint_trajectory_controller --deactivate forward_position_controller -c /kmr_iiwa/controller_manager`  

`ros2 control list_controllers -c /kmr_iiwa/controller_manager`

### Others
`ros2 run topic_tools relay   /kmr_iiwa/robot_description   /robot_description`  
`ros2 run rqt_joint_trajectory_controller rqt_joint_trajectory_controller`
