from setuptools import find_packages, setup

package_name = 'drive_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jeremychong',
    maintainer_email='jchong37@myseneca.ca',
    description='Drive robot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'drive_robot = drive_robot.drive_robot:main',

        ],
    },
)

