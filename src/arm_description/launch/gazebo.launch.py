import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = get_package_share_directory('arm_description')
    urdf_file = os.path.join(pkg_share, 'urdf', 'arm.urdf')
    world_file = os.path.join(pkg_share, 'worlds', 'arm_world.sdf')
    rviz_file = os.path.join(pkg_share, 'rviz', 'arm.rviz')

    with open(urdf_file, 'r') as f:
        robot_desc = f.read()

    bridge_args = ['/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock']
    for i in range(1, 5):
        bridge_args.append(f'/model/robotic_arm/joint/joint{i}/cmd_pos@std_msgs/msg/Float64]gz.msgs.Double')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_file],
        ),
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world_file],
            output='screen',
        ),
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-name', 'robotic_arm', '-topic', '/robot_description', '-z', '0.0'],
            output='screen',
        ),
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=bridge_args,
            output='screen',
        ),
        Node(
            package='arm_description',
            executable='trajectory_bridge',
            output='screen',
        ),
        Node(
            package='arm_description',
            executable='servo_serial_bridge',
            output='screen',
        ),
        Node(
            package='arm_description',
            executable='traj_pub',
            output='screen',
        ),
    ])
