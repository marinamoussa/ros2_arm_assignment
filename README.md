# Iron Robotic Arm - ROS 2 Jazzy Assignment

- **Dimensions & Material**: Height 35 cm (within 30-40 cm), width 18 cm (within 15-20 cm), iron links (`base_link`, `L1`, `L2`, `L3`, `end_effector`) with 4 revolute joints (`joint1`–`joint4`).
- **Packages**: `arm_description`, `arm_sim`, `arm_control`, and `firmware/servo_controller/servo_controller.ino`.
- **Transport & Message Format**: USB serial (`pyserial`, 115200 baud) sending CSV angles `angle1,angle2\n` clamped to `0-180` deg.

| Board Pin | Connects To |
|---|---|
| Pin 9 | Servo 1 signal (base rotation) |
| Pin 10 | Servo 2 signal (arm joint) |
| External 5V + GND | Servo power + common ground with board |

## Build and Run

1. `cd ~/ros2_ws`
2. `colcon build --symlink-install`
3. `source install/setup.bash`
4. `ros2 launch arm_sim sim.launch.py`
