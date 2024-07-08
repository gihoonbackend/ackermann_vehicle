1. installation S

```
cd catkin_ws/src
git clone https://github.com/gihoonbackend/ackermann_vehicle.git
sudo apt install ros-noetic-ackermann-msgs
cd ..
rosdep install --from-paths src --ignore-src -r -y
catkin_make
source devel/setup.bash
```

2. run in gazebo

```
activate model and map
roslaunch ackermann_vehicle_gazebo ackermann_vehicle_noetic.launch
line following algorithm
cd catkin_ws/src/ackermann_vehicle/ackermann_vehicle_gazebo/scripts
python3 lane_detect.py
publish /cmd_vel -> 동작
```

3. 수정
맵 수정 시 arkermann_vehicle_gazebo/worlds 에 world 파일 추가 후, ackermann_vehicle_noetic.launch에서 world 파일 선언된 부분 수정