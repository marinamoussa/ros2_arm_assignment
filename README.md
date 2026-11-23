# Robotic Arm ROS 2 Assignment

## Repository Structure
- `src/arm_description`: URDF model (`urdf/arm.urdf`), RViz2 config (`rviz/arm.rviz`), Gazebo world (`worlds/arm_world.sdf`), launch files, trajectory publisher (`traj_pub.py`), slider GUI (`joint_slider_gui.py`), serial bridge (`servo_serial_bridge.py`), and Arduino firmware (`firmware/arm_servo_controller.ino`)

## Dimensions & Kinematics
- **Base:** 8 cm height from working plane (`0.18 x 0.18 x 0.08 m`)
- **Links:** `L1` = 12 cm, `L2` = 15 cm, `L3` = 9 cm, `end_effector` = 6 cm (height ~35 cm, width/reach ~15–20 cm)
- **Kinematic Chain & Joints:** 4 revolute joints (`joint1`, `joint2`, `joint3`, `joint4`) along `base_link -> joint1 -> L1 -> joint2 -> L2 -> joint3 -> L3 -> joint4 -> end_effector`

## Dependencies
- **ROS 2 Jazzy:** `rclpy`, `sensor_msgs`, `std_msgs`, `trajectory_msgs`, `robot_state_publisher`, `rviz2`, `ros_gz_sim`, `ros_gz_bridge`
- **Python / Firmware:** `pyserial`, Arduino `Servo` library

## Build and Run
```bash
cd ~/ros2_ws
colcon build --symlink-install --packages-select arm_description
source install/setup.bash
```

- **Simulation (Gazebo + RViz2):**
  ```bash
  ros2 launch arm_description gazebo.launch.py
  ```
- **Trajectory Publisher Node:**
  ```bash
  ros2 run arm_description traj_pub
  ```
- **Sliders GUI:**
  ```bash
  ros2 run arm_description joint_slider_gui
  ```
- **Hardware Serial Bridge:**
  ```bash
  ros2 run arm_description servo_serial_bridge
  ```

## Transport and Message Format
- **Topic:** `/arm_controller/joint_trajectory` (`trajectory_msgs/msg/JointTrajectory`)
- **Transport:** USB Serial via `pyserial` at `115200` baud (`/dev/ttyUSB0`)
- **Message Format:** CSV string `deg1,deg2,deg3,deg4\n`, converted from radians to degrees and clamped to `0–180` deg

## Pin Mapping

| Board Pin | Connects To |
| :--- | :--- |
| Pin 3 (PWM) | Servo 1 (`joint1`) |
| Pin 5 (PWM) | Servo 2 (`joint2`) |
| Pin 6 (PWM) | Servo 3 (`joint3`) |
| Pin 9 (PWM) | Servo 4 (`joint4`) |
| GND | Common ground with external 5V–6V servo power supply |

## Pin Mapping

| Board Pin | Connects To |
| :--- | :--- |
| Pin 3 (PWM) | Servo 1 (`joint1`) |
| Pin 5 (PWM) | Servo 2 (`joint2`) |
| Pin 6 (PWM) | Servo 3 (`joint3`) |
| Pin 9 (PWM) | Servo 4 (`joint4`) |
| GND | Common ground with external 5V–6V servo power supply |
