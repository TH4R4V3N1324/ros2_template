"""
--------------------------------------------------------------------------------------------------
This is a template for creating a basic ROS2 node in Python.
It includes the essential structure and functions needed to set up a ROS2 node.
--------------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------------
Include necessary ROS2 imports here
--------------------------------------------------------------------------------------------------
Include rclpy for basic ROS2 functionalities.
Other imports can be added as needed for additional functionalities,
such as messages, services, and actions.
--------------------------------------------------------------------------------------------------
Examples found under "ROS2 headers (Python imports)" at the bottom of this file.
--------------------------------------------------------------------------------------------------
"""

import rclpy
from rclpy.node import Node


class NodeName(Node):
    def __init__(self):
        super().__init__('node_name')

        #------------------------------------------------------------------------------------------
        # Define ROS2 functionalities here:
        # publishers, subscribers, services, clients, timers, action servers, and action clients.
        #------------------------------------------------------------------------------------------
        # Examples found under "ROS2 functions" at the bottom of this file.
        #------------------------------------------------------------------------------------------

        # Keep ROS handles in self.* so they stay alive for the lifetime of the node.
        # self.timer = self.create_timer(1.0, self.timer_callback)
        # self.subscriber = self.create_subscription(String, 'topic_name', self.subscriber_callback, 10)
        # self.publisher = self.create_publisher(String, 'topic_name', 10)
        # self.client = self.create_client(AddTwoInts, 'service_name')
        # self.service = self.create_service(AddTwoInts, 'service_name', self.service_callback)
        # self.action_client = ActionClient(self, Fibonacci, 'action_name')
        # self.action_server = ActionServer(
        #     self,
        #     Fibonacci,
        #     'action_name',
        #     execute_callback=self.execute_callback,
        #     goal_callback=self.goal_callback,
        #     cancel_callback=self.cancel_callback,
        # )

    #----------------------------------------------------------------------------------------------
    # Add callback functions and other member functions here.
    #----------------------------------------------------------------------------------------------
    # Examples found under "Example function declarations" at the bottom of this file.
    #----------------------------------------------------------------------------------------------


def main(args=None):
    rclpy.init(args=args)
    node_name = NodeName()
    rclpy.spin(node_name)
    node_name.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


#----------------------------------------------------------------------------------------------
# ROS2 headers (Python imports):
#----------------------------------------------------------------------------------------------
# Called at the top of the file.
# Include ROS2 imports based on the functionalities used in the node.
#
# Standard ROS2 message types can be found in the ros2/common_interfaces repository:
# https://github.com/ros2/common_interfaces
#
# For custom message types, import from the package and module structure.
# Examples of common message, service, and action files can be found in example_interfaces.
#----------------------------------------------------------------------------------------------
#
# --CUSTOM MESSAGES, SERVICES, ACTIONS--
# from <package_name>.msg import <MessageType>
# from <package_name>.srv import <ServiceType>
# from <package_name>.action import <ActionType>
#
# --MESSAGES--
# from std_msgs.msg import String
#
# --SERVICES--
# from example_interfaces.srv import AddTwoInts
#
# --ACTIONS--
# from rclpy.action import ActionClient, ActionServer, CancelResponse, GoalResponse
# from example_interfaces.action import Fibonacci
#
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# ROS2 functions:
#----------------------------------------------------------------------------------------------
# Called within the constructor of a Node class.
# Must be defined inside __init__.
#----------------------------------------------------------------------------------------------
#
# --TIMER--
# self.timer = self.create_timer(1.0, self.timer_callback)
#
# --SUBSCRIBER--
# self.subscriber = self.create_subscription(MessageType, 'topic_name', self.subscriber_callback, 10)
#
# --PUBLISHER--
# self.publisher = self.create_publisher(MessageType, 'topic_name', 10)
#
# --CLIENT--
# self.client = self.create_client(ServiceType, 'service_name')
#
# --SERVICE--
# self.service = self.create_service(ServiceType, 'service_name', self.service_callback)
#
# --ACTION CLIENT--
# self.action_client = ActionClient(self, ActionType, 'action_name')
#
# --ACTION SERVER--
# self.action_server = ActionServer(
#     self,
#     ActionType,
#     'action_name',
#     execute_callback=self.execute_callback,
#     goal_callback=self.goal_callback,
#     cancel_callback=self.cancel_callback,
# )
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# Example function declarations:
#----------------------------------------------------------------------------------------------
# Some functions require specific signatures based on their ROS2 functionality.
# This includes callback functions for timers, subscribers, services, and actions.
#
# Function names should match those used in __init__,
# but can realistically be any valid Python function name.
#----------------------------------------------------------------------------------------------
#
# --TIMER CALLBACK--
# def timer_callback(self):
#     pass
#
# --SUBSCRIBER CALLBACK--
# def subscriber_callback(self, msg):
#     pass
#
# --SERVICE CALLBACK--
# def service_callback(self, request, response):
#     return response
#
# --ACTION GOAL HANDLER--
# def goal_callback(self, goal_request):
#     return GoalResponse.ACCEPT
#
# --ACTION CANCEL HANDLER--
# def cancel_callback(self, goal_handle):
#     return CancelResponse.ACCEPT
#
# --ACTION EXECUTE HANDLER--
# async def execute_callback(self, goal_handle):
#     return ActionType.Result()
#----------------------------------------------------------------------------------------------