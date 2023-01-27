#include <moveit/move_group_interface/move_group_interface.h>

int main(int argc, char** argv)
{
  ros::init(argc, argv, "my_node");
  ros::NodeHandle nh;

  // Create a MoveGroupInterface object
  moveit::planning_interface::MoveGroupInterface move_group("arm");
  

  // Set the first named target position
  
  /* move_group.setNamedTarget("pose11");
  std::cout<<"between set target and move" <<std::endl;
  // Plan and execute the motion to the first position
  

  while(1){
  move_group.move();
   break;
  }
  std::cout<<"after first move move" <<std::endl;
  // Set the second named target position
  move_group.setNamedTarget("pose12");
  std::cout<<"between set target and move 22222" <<std::endl;
  // Plan and execute the motion to the second position
  move_group.move();
  std::cout<<" move 22222" <<std::endl; */
  
  ros::AsyncSpinner spinner(1);
  spinner.start();
  
   while(ros::ok()){
	 
	  move_group.setNamedTarget("pose11");
	  std::cout<<"target1"<<std::endl;
	  move_group.move();
	  
            std::cout<<"move1"<<std::endl;
	  
	  move_group.setNamedTarget("pose12");
	   std::cout<<"target2"<<std::endl;
	  move_group.move();
	   std::cout<<"move2"<<std::endl;
	 
  
  }
 
  return 0;
}

