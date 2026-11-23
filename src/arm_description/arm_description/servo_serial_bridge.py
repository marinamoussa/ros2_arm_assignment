import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory


def rad_to_deg_clamped(rad_val: float) -> int:
    deg = (float(rad_val) + 1.5707963) * (180.0 / 3.1415926)
    return max(0, min(180, int(round(deg))))


class ServoSerialBridge(Node):
    def __init__(self):
        super().__init__('servo_serial_bridge')
        self.declare_parameter('port', '/dev/ttyUSB0')
        self.declare_parameter('baud', 115200)
        self.port = self.get_parameter('port').value
        self.baud = int(self.get_parameter('baud').value)
        self.ser = None

        try:
            import serial
            self.ser = serial.Serial(self.port, self.baud, timeout=0.1)
            self.get_logger().info(f'Opened serial {self.port} @ {self.baud}')
        except Exception as e:
            self.get_logger().warn(f'Serial not opened ({self.port}): {e} — printing angles only')

        self.sub = self.create_subscription(
            JointTrajectory,
            '/arm_controller/joint_trajectory',
            self.on_trajectory,
            10,
        )

    def on_trajectory(self, msg: JointTrajectory):
        if not msg.points:
            return
        pt = msg.points[-1]
        angles = [rad_to_deg_clamped(p) for p in pt.positions[:4]]
        while len(angles) < 4:
            angles.append(90)
        line = f'{angles[0]},{angles[1]},{angles[2]},{angles[3]}\n'
        if self.ser and self.ser.is_open:
            try:
                self.ser.write(line.encode('utf-8'))
            except Exception as e:
                self.get_logger().warn(f'Serial write failed: {e}')
        self.get_logger().info(f'Servo deg: {line.strip()}')


def main(args=None):
    rclpy.init(args=args)
    node = ServoSerialBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
