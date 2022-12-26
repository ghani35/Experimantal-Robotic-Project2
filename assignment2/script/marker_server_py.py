#!/usr/bin/env python
import rospy
from assignment2.srv import RoomInformation, RoomInformationResponse
from assignment2.msg import RoomConnection
from armor_api.armor_client import ArmorClient

def marker_callback(req):
  conn = RoomConnection()
  res = RoomInformationResponse()
  if req.id == 11:
      res.room = "E"
      res.x = 1.5
      res.y = 8.0
      conn.connected_to = "C1"
      conn.through_door = "D7" ##I changed this from D5 to D7 to much my ontology from Ass1
      res.connections.append(conn)
      conn.connected_to = "C2"
      conn.through_door = "D6"
      res.connections.append(conn)
      print("Marker " + str(req.id) + " scanned correctly")
      print("It is room " + res.room + "located in x= " + str(res.x) + "  y= " + str(res.y) +"\n" )
      ## E has door D6, has door D7 is visited at
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'E', 'D6'])
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'E', 'D7'])
      client.call('ADD','DATAPROP','IND',['visitedAt', 'E', 'Long', '1665579740'])
      client.call('REASON','','',[''])
      client.call('SAVE','','',['/root/ros_ws/src/assignment2/src/topological_map_loaded.owl'])

      return res
  elif req.id == 12:
      res.room = "C1"
      res.x = -1.5
      res.y = 0.0
      conn.connected_to = "E"
      conn.through_door = "D7"
      res.connections.append(conn)
      conn.connected_to = "C2"
      conn.through_door = "D5" ##I changed this from D7 to D5 to much my ontology from Ass1
      res.connections.append(conn)
      conn.connected_to = "R1"
      conn.through_door = "D1"
      res.connections.append(conn)
      conn.connected_to = "R2"
      conn.through_door = "D2"
      res.connections.append(conn)
      print("Marker " + str(req.id) + " scanned correctly")
      print("It is room " + res.room + "located in x= " + str(res.x) + "  y= " + str(res.y) +"\n" )
      #C1 has door D7,D2,D1,D5   C1 is visited at
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'C1', 'D7'])
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'C1', 'D1'])
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'C1', 'D2'])
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'C1', 'D5'])
      client.call('ADD','DATAPROP','IND',['visitedAt', 'C1', 'Long', '1665579740'])
      client.call('REASON','','',[''])
      client.call('SAVE','','',['/root/ros_ws/src/assignment2/src/topological_map_loaded.owl'])
      return res
  elif req.id == 13:
      res.room = "C2"
      res.x = 3.5
      res.y = 0.0
      conn.connected_to = "E"
      conn.through_door = "D6"
      res.connections.append(conn)
      conn.connected_to = "C1"
      conn.through_door = "D5"
      res.connections.append(conn)
      conn.connected_to = "R3"
      conn.through_door = "D3"
      res.connections.append(conn)
      conn.connected_to = "R4"
      conn.through_door = "D4"
      res.connections.append(conn)
      print("Marker " + str(req.id) + " scanned correctly")
      print("It is room " + res.room + "located in x= " + str(res.x) + "  y= " + str(res.y) +"\n" )
      #C2 has door D6, D5, D3, D4  is visited at 
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'C2', 'D3'])
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'C2', 'D4'])
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'C2', 'D5'])
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'C2', 'D6'])
      client.call('ADD','DATAPROP','IND',['visitedAt', 'C2', 'Long', '1665579740'])
      client.call('REASON','','',[''])
      client.call('SAVE','','',['/root/ros_ws/src/assignment2/src/topological_map_loaded.owl'])
      return res
  elif req.id == 14:
      res.room = "R1"
      res.x = -7.0
      res.y = 3.0
      conn.connected_to = "C1"
      conn.through_door = "D1"
      res.connections.append(conn)
      print("Marker " + str(req.id) + " scanned correctly")
      print("It is room " + res.room + "located in x= " + str(res.x) + "  y= " + str(res.y) +"\n" )
      #R1 had D1  is vissited at 
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'R1', 'D1'])
      client.call('ADD','DATAPROP','IND',['visitedAt', 'R1', 'Long', '1665579734'])
      client.call('REASON','','',[''])
      client.call('SAVE','','',['/root/ros_ws/src/assignment2/src/topological_map_loaded.owl'])
      return res
  elif req.id == 15:
      res.room = "R2"
      res.x = -7.0
      res.y = -4.0
      conn.connected_to = "C1"
      conn.through_door = "D2"
      res.connections.append(conn)
      print("Marker " + str(req.id) + " scanned correctly")
      print("It is room " + res.room + "located in x= " + str(res.x) + "  y= " + str(res.y) +"\n" )
      #R2 had D2  is vissited at
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'R2', 'D2'])
      client.call('ADD','DATAPROP','IND',['visitedAt', 'R2', 'Long', '1665579736'])
      client.call('REASON','','',[''])
      client.call('SAVE','','',['/root/ros_ws/src/assignment2/src/topological_map_loaded.owl'])      
  elif req.id == 16:
      res.room = "R3"
      res.x = 9.0
      res.y = 3.0
      conn.connected_to = "C2"
      conn.through_door = "D3"
      res.connections.append(conn)
      print("Marker " + str(req.id) + " scanned correctly")
      print("It is room " + res.room + "located in x= " + str(res.x) + "  y= " + str(res.y) +"\n" )
      #R3 had D3  is vissited at 
      #Reason 
      #Disjoint C1 C2 E R1 .. R4
      #Disjoint D1 .. D7 
      #Reason 
      #Robot is in E
      #Reason
      #Save 
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'R3', 'D3'])
      client.call('ADD','DATAPROP','IND',['visitedAt', 'R3', 'Long', '1665579738'])
      client.call('REASON','','',[''])
      client.call('DISJOINT','IND','',['E', 'C1', 'C2','R1','R2','R3','R4'])
      client.call('REASON','','',[''])
      client.call('DISJOINT','IND','',['D1', 'D2', 'D3','D4','D5','D6','D7'])     
      client.call('REASON','','',[''])
      client.call('ADD','OBJECTPROP','IND',['isIn', 'Robot1', 'E'])
      client.call('REASON','','',[''])
      client.call('SAVE','','',['/root/ros_ws/src/assignment2/src/topological_map_loaded.owl'])
      return res
  elif req.id == 17:
      res.room = "R4"
      res.x = 9.0
      res.y = -4.0
      conn.connected_to = "C2"
      conn.through_door = "D4"
      res.connections.append(conn)
      print("Marker " + str(req.id) + " scanned correctly")
      print("It is room " + res.room + "located in x= " + str(res.x) + "  y= " + str(res.y) +"\n" )
      #R4 had D4  is vissited at
      client.call('ADD','OBJECTPROP','IND',['hasDoor', 'R4', 'D4'])
      client.call('ADD','DATAPROP','IND',['visitedAt', 'R4', 'Long', '1665579740'])
      client.call('REASON','','',[''])
      client.call('SAVE','','',['/root/ros_ws/src/assignment2/src/topological_map_loaded.owl'])
      return res
if __name__ == "__main__":
  rospy.init_node("assignment2")
  client = ArmorClient("example", "ontoRef")
  oracle = rospy.Service("/room_info", RoomInformation, marker_callback)
  client.call('LOAD','FILE','',['/root/ros_ws/src/assignment2/src/topological_map_loaded.owl', 'http://bnc/exp-rob-lab/2022-23', 'true', 'PELLET', 'false'])
  rospy.spin()
  rospy.shutdown()

