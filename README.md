# Assignment2_Exporo

![image](https://user-images.githubusercontent.com/91313196/201306579-1b867e35-9d8b-467a-963b-1c0c09856d1a.png)
# Outline 
1. Introduction 
2. Desrciption of software architecture 
   * Component diagram
   * state diagram 
3. Instalation and running procedures
4. A small video showing the relevent parts of the running code
5. Working hypothesis and environment
   * System's features 
   * System's limitations
   * Possible technical improvements 
6. Doxygen documentation
7. Authors and Teachers contact  
# 1. Introduction 
This github repository shows how to creat a robot model and spawn it in a given environment such that it can navigate and do patroling task. To achieve these behavior this steps are nedded 
   1. Creat a robot model such that the robot can:
         * Navigate 
         * Scan aruco codes by rgb camera
         * Detect obstacles by lidar sensor 
   2. Build a topolofical ontology strating from the data collected in aruco codes 
   3. Creat a state machine
   
The finit-state machine is built in ROS environment based on [SMACH](http://wiki.ros.org/smach/Tutorials) ros-package, and how to build a topological onotology of the wrold, in this small project, Protogé is used for building the ontology, [ARMOR](https://github.com/EmaroLab/armor_rds_tutorial) service is used for access and modify the ontology. 
#### Environment
 It is a 2D-environmen built up with 4 rooms `R1 R2 R3 R4`, 2 corridors `C1 C2` and one special room `E` used as a waiting room befor filling the map, and a charging station as well. And 7 doors `D1 ... D7`  
 
![image](https://user-images.githubusercontent.com/91313196/201313573-47fa3ac7-dc9e-4a9b-910c-f0b998e1ad7e.png)


#### Senario
 We have a survallience robot that moves in a 2D environment. First the robot waits in room **E** untill the whol map  is loaded into the ontology, then the robot keeps moving between the corridors **C1** and **C2** for infinit time. The robot must go to the charging station **E** when its battery is low, otherwise he must visit the **urgent** rooms if any, then goes back to its normal behavior moving between cooridors.
 
 #### Ontology
* Entity 
  * ![image](https://user-images.githubusercontent.com/91313196/198834787-d1b4f43c-764f-4f75-a29a-a5316d517ae6.png)
* Individuals 
  * `C1 C2 E`: Cooridors 
  * `R1 R2 R3 R4`: Rooms
  * `D1 D2 D3 D4 D5 D6 D7`: Doors
* Object properties
  * isIn
  * canReach
  * hasDoor 
  * connectedTo
* Data properties 
  * Now
  * visitedAt
  * uregencyThreshold
 # 2. Discreption of software architecture 
 ## Component diagram 
![diagram (1)](https://user-images.githubusercontent.com/91313196/209484116-8ebc2832-6c4f-4a04-bc5f-a4f6a7cfb3d3.png)


 ### 2- state_machine
It controlls how the robot changes its state based on the reasoning of the topological ontology, and the battery state of the robot. This node subscribes to two topics `/battery_state` and `/map_state`, and it calls the armor server for updating the loaded ontology. The states of the robot are listed bellow.
  * filling_map
  * moving_in_corridors
  * visiting_urgent
  * charging
 
 ### 3- battery_controller 
 This is a publisher to the topic `/baterry_state`, it publishes different state of the battery `True`or`False` in a specific duration, the durations to be full or low are passed as **parameters**.
 ### 4- armor
 The ARMOR package is an external package used to communicate with the Cluedo OWL ontology, it is a ROS wrapper that helps to make this communication possible. For more information about ARMOR [click here](https://github.com/EmaroLab/armor_rds_tutorial)
 ### List of parameters 
 It is a **yaml** file that list all the parameters used in this project which are 
 * time_to_stay_in_location defeault value = 1 (s)
 * time_of_one_charge  defeault value = 30 (s)
 * time_of_charging  defeault value = 15 (s)
 * visitedAt_R1  defeault value = 1665579740
 * visitedAt_R2  defeault value = 1665579740
 * visitedAt_R3  defeault value = 1665579740
 * visitedAt_R4  defeault value = 1665579740
 * visitedAt_C1  defeault value = 1665579740
 * visitedAt_C2  defeault value = 1665579740
 * visitedAt_E  defeault value = 1665579740
### List of messages 
* Map_state.msg: `int32 map_state`, carry the state of the map
  * It is 1 if the map is fully loaded 
  * It is 0 if the map is not fully loaded
* Battry_state.msg: `int32 battery_state`, carry the state of the battery
  * It is 1 if the battery is full
  * It is 0 if the battery is low
## State diagram 
![image](https://user-images.githubusercontent.com/91313196/198852520-90de1eb7-e835-48dc-acd0-007a13d0e306.png)

There are four states in this state diagram, the task of each state is explained below:
1. **Filling_Map**: The robots keeps waiting in room **E** untill the whole map is loaded, the robot can know if the map is fully loaded by subscribing to the topic `/map_state`. When the map is fully loaded the robot go to `MOVING_IN_CORRIDORS` state trough the transition `move`.
2. **Moving in corridors**: The robots keeps moving between `C1` and `C2` for infinit time, the robots keep cheking the state of the battery by subscribing to the topic `/battery_state`, if the battery is `low` the robot goes to `CHARGING` state trough the transition `tired`. if the battery is not low, the robot cheks if there is an `urgent` room by quering the `individuals of the class urg`. If there is an urgent room the robot goes to `VISITING_URGENT` state through the transition `urgent`.
3. **Visiting_urgent**:  First, the robots checks if the battery is low goes to `CHARGING` state, else it checkes it the urgent room is reacheable by quering the object properties of the robot `canReach`, if the room can be reached it visit it and return back to the `MOVING_IN_CORRIDORS` trough the transition `visited`. If the urgent room is not reacheable it goes to `MOVING_IN_CORRIDORS` state through the transition `not_reached`, in this case the robot will change the corridors and visit it again.
4. **CHARGING**: The robot keeps checking the state of the battery, if it is full it goes to `MOVING_IN_COORIDORS` state the the transition `charged`, otherwise, it stays in the `CHARGING` state. 

# 3. Instalation and running procedures
1. Clone the repository in your work_space `git clone https://github.com/ghani35/Experimental-robotics-Ass1.git`
2. go to `/root/your_work_space/src/assignment/parameters`, open `parameters.yaml` file 
3. Change the path to `path = '/root/your_work_space/src/assignment/src/topological_map.owl'` 
5. (optional!) Change the other parameters if you want to test some relevent parts of the code
6. If you do not have [smach_package](http://wiki.ros.org/smach/Tutorials/Getting%20Started), run this command:
 `sudo apt-get install ros-noetic-smach-ros`
6. If you do not have armor installed, follow this git hub repository 
`https://github.com/EmaroLab/armor_rds_tutorial.git`
7. Open new terminal and run `roslaunch assignment solution.launch`
* When you run this command, three windows and the should pop-up
  1. user_interface.py
  2. state_machine.py
  3. battery.py
  * user_inerface.py: allows you to load the ontology, and notify the algorithm if the map is fully loaded
  * state_machine.py: prints the state transition of the robot, helps you to understand and debug 
  * battery.py: allows you to monitor the state of the batter
8. In another terminal run the smach_viewer to visualize the state machine
`rosrun smach_viewer smach_viewer.py` 
9. If you want to **SKIP** the part of filing the map from **user_interfaca.py**, you can use `topological_map_loaded.owl` instead of `topological_map.owl`
   All the you have to do is to **set the path** from step **2** to
   `path = '/root/your_work_space/src/assignment/src/topological_map_loaded.owl'`
10. Once you launch the nodes to teste, the `topological_map_loaded` will change, so if you to test again you have to start from the same topology, hence you need to copy the starting ontology when the map is fully loaded from `topolofical_map_loaded_initial` to `topological_map_laoded`.
# 4. A small video showing the relevent parts of the running code
https://user-images.githubusercontent.com/91313196/198888618-3acce94f-d051-485e-9753-c39f3e8622dd.mp4

This video shows how the state machine behaves when we have an event. 
* phase1: The state machine is in the state `FILLING_MAP`, the user enter the last individual `D1` and telling the state machine taht the map is fully loaded.
* phase2: State machine goes to `MOVING_IN_CORRIDORS`, then the battery is low and the state machine goes to `CHARGING`. after charging it goes back to `MOVING_IN_CORRIDORS`.
* phase3: The room R1 becomes urgent, the SM goes to `VISITING_URGENT`. then goig back to `MOVING_IN_CORRIDORS`
For more detail, watch the video.
# 5. Working hypothesis and environement
In this project there are many assumptions made on the environement in order to make the project simpler, the assumptions are explained bellow
1. The movement of the robot from one location to another location is considered to be only one time step in the onotology, it means that if the robot takes 2 minutes to go from R1 to C1, this will be considered as one time step on the ontology
3. Initializing the `visitedAt` data proporty of a location to different values to avoid making all of them **urgent** at the same time 
4. When a robot is in a specific location, it can reach only the locations that need **one door** transmition

## Pssible Limitations
1. If the battery is low during the transition from one location to another location, the robot will not cancel the goal and go to charging, but it reache the current target than it goes to to charge
2. The time step for any transitions between two locations is constant from the ontology point of view while it is not constant in the simulation 


## Possible improvements  
2. The time can be continuously updated and depends on the distance and speed of the robot to reach a specific location

# 6. Doxygen documentation
[Click here](https://ghani35.github.io/Assignment1/)

# 7. Author and Teachers contacts 
* Author 
  * name: BAKOUR Abdelghani
  * email: bakourabdelghani1999@gmail.com
* Teachers
  * name: Luca Buoncompagni luca.buoncompagni@edu.unige.it
  * name: Carmine Recchiuto carmine.recchiuto@dibris.unige.it

 
