# robotics-project-2
ROS2 node that moves gazebo simulation robot across room.

World file uses the following fuel models:
https://app.gazebosim.org/OpenRobotics/fuel/models/RoboCup%202014%20SPL%20Field
https://app.gazebosim.org/OpenRobotics/fuel/models/Oak%20tree

Be sure to download them, extract them to a directory and source the folder to gazebo before starting the simulation. 
As an example (replacing the path below with your own):


```export GZ_SIM_RESOURCE_PATH="$HOME/my-local/models"```


## To run:

1. Download package and extract into src folder of your ros2 workspace.
2. Download simulation world file into ros2 workspace.
3. Open 3 terminals in the workspace directory. (One for ROS2, one for GAZEBO, one for BRIDGE)
4. Source ros into the terminals.
5. In ROS2 terminal, run ```colcon build```, then ```source install/setup.bash```.
6. In GAZEBO terminal, export resource path as above, then run ```gz sim fieldwithtrees.sdf```.
7. In bridge terminal, run ```ros2 run ros_gz_bridge parameter_bridge /cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist```.
8. In ROS2 terminal, run ```ros2 run drive_robot drive_robot```.
9. Go to simulation and press play button.
10. Return to terminal, used WASD to move robot.



