# Robotic Arm ROS 2 Assignment

## Dimensions
- Base: 8 cm (0.18x0.18x0.08 m)
- L1: 12 cm, L2: 15 cm, L3: 9 cm, end_effector: 6 cm (height ~35 cm, reach/width ~15-20 cm)
- 4 revolute joints: joint1, joint2, joint3, joint4

## Dependencies
- ROS 2 Jazzy (rclpy, sensor_msgs, std_msgs, trajectory_msgs, robot_state_publisher, rviz2, ros_gz_sim, ros_gz_bridge)
- Gazebo (gz sim), pyserial, Arduino Servo library

## Build and Run
- Build: cd ~/ros2_ws && colcon build --symlink-install --packages-select arm_description && source install/setup.bash
- Sim: ros2 launch arm_description gazebo.launch.py
- Sliders GUI: ros2 run arm_description joint_slider_gui
- Serial bridge: ros2 run arm_description servo_serial_bridge

## Transport and Format
- Topic: /arm_controller/joint_trajectory (trajectory_msgs/msg/JointTrajectory)
- Transport: USB Serial via pyserial at 115200 baud (/dev/ttyUSB0)
- Format: CSV deg1,deg2,deg3,deg4
 clamped to 0-180 deg

## Pin Mapping
- Pin 3 PWM: Servo 1 (joint1)
- Pin 5 PWM: Servo 2 (joint2)
- Pin 6 PWM: Servo 3 (joint3)
- Pin 9 PWM: Servo 4 (joint4)
- GND: Common ground with external 5V-6V servo supply
