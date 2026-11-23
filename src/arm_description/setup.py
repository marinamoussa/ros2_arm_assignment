import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'arm_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.sdf')),
        (os.path.join('share', package_name, 'firmware'), glob('firmware/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marina-hany',
    maintainer_email='marina.hanymoussa@gmail.com',
    description='Robotic arm URDF, simulation, and trajectory control',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'trajectory_bridge = arm_description.trajectory_bridge:main',
            'traj_pub = arm_description.traj_pub:main',
            'servo_serial_bridge = arm_description.servo_serial_bridge:main',
            'joint_slider_gui = arm_description.joint_slider_gui:main',
        ],
    },
)
