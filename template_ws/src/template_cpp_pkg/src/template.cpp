/*
--------------------------------------------------------------------------------------------------
This is a template for creating a basic ROS2 node in C++ using the C++17 standard.
It includes the essential structure and functions needed to set up a ROS2 node.
--------------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------------
Include necessary ROS2 headers here
--------------------------------------------------------------------------------------------------
Include rclcpp for basic ROS2 functionalities
Other headers can be included as needed for additional functionalities
Such as messages, services, actions, etc.
--------------------------------------------------------------------------------------------------
Examples found under "ROS2 headers" at the bottom of this file
--------------------------------------------------------------------------------------------------
*/

#include "rclcpp/rclcpp.hpp"

class NodeName : public rclcpp::Node{public: NodeName() : Node("node_name"){
    /*
    ----------------------------------------------------------------------------------------------
    Define ROS2 functionalities here
    Such as publishers, subscribers, services, clients, timers, action servers, and action clients
    ----------------------------------------------------------------------------------------------
    Examples found under "ROS2 functions" at the bottom of this file
    ----------------------------------------------------------------------------------------------
    */
}    
private:
    /*
    ----------------------------------------------------------------------------------------------
    Declare publishers, subscribers, services, clients, timers, action servers, and action clients here
    ----------------------------------------------------------------------------------------------
    Examples found under "Function definitions" at the bottom of this file
    ----------------------------------------------------------------------------------------------
    */

public:
    /*
    ----------------------------------------------------------------------------------------------
    declare callback functions and other member functions here
    ----------------------------------------------------------------------------------------------
    Examples found under "Example function declarations" at the bottom of this file
    ----------------------------------------------------------------------------------------------
    */
};

int main(int argc, char **argv){    
    rclcpp::init(argc, argv);    
    auto node = std::make_shared<NodeName>();    
    rclcpp::spin(node);    
    rclcpp::shutdown();    
    return 0;
}

/*
----------------------------------------------------------------------------------------------
Implement the functions declared in the class here
This includes callback functions and other member functions
----------------------------------------------------------------------------------------------
Example:
----------------------------------------------------------------------------------------------
void NodeName::FunctionName(){
    // Function implementation
}
----------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------
ROS2 headers:
----------------------------------------------------------------------------------------------
Called at the top of the file
Include necessary ROS2 headers based on the functionalities used in the node

Standard ROS2 message types can be found in the ros2/common_interfaces repository
https://github.com/ros2/common_interfaces

For custom message types, include the appropriate package and message types based on the package structure
Examples of common message, service, and action files can be found in the example_interfaces package
----------------------------------------------------------------------------------------------

--CUSTOM MESSAGES, SERVICES, ACTIONS--
#include "<package_name>/msg/<MessageType>.hpp"
#include "<package_name>/srv/<ServiceType>.hpp"
#include "<package_name>/action/<ActionType>.hpp"

--MESSAGES--
#include "std_msgs/msg/string.hpp"

--SERVICES--
#include "example_interfaces/srv/add_two_ints.hpp"

--ACTIONS--
#include "example_interfaces/action/fibonacci.hpp"

----------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------
ROS2 functions:
----------------------------------------------------------------------------------------------
Called within constructor of a Node class
Must be defined inside the class definition
----------------------------------------------------------------------------------------------

--TIMER--
timer = this->create_wall_timer(std::chrono::milliseconds(1000), std::bind(&ClassName::FunctionName, this));

--SUBSCRIBER--
subscriber = this->create_subscription<MessageType>("topic_name", 10, std::bind(&ClassName::CallbackFunction, this, std::placeholders::_1));

--PUBLISHER--
publisher = this->create_publisher<MessageType>("topic_name", 10);

--CLIENT--
client = this->create_client<ServiceType>("service_name");

--SERVICE--
service = this->create_service<ServiceType>("service_name", std::bind(&ClassName::ServiceCallback, this, std::placeholders::_1, std::placeholders::_2));

--ACTION CLIENT--
action_client = rclcpp_action::create_client<ActionType>(this, "action_name");

--ACTION SERVER--
action_server = rclcpp_action::create_server<ActionType>(this, "action_name",
    std::bind(&ClassName::HandleGoal, this, std::placeholders::_1, std::placeholders::_2),
    std::bind(&ClassName::HandleCancel, this, std::placeholders::_1),
    std::bind(&ClassName::HandleAccepted, this, std::placeholders::_1));

----------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------
Function definitions:
----------------------------------------------------------------------------------------------
ROS2 functionality needs to be declared in the private section of the class
The functionality can be given any valid name
But the names should match those used in the constructor when creating the functionality
----------------------------------------------------------------------------------------------

--TIMER--
rclcpp::TimerBase::SharedPtr timer;

--SUBSCRIBER--
rclcpp::Subscription<MessageType>::SharedPtr subscriber;

--PUBLISHER--
rclcpp::Publisher<MessageType>::SharedPtr publisher;

--CLIENT--
rclcpp::Client<ServiceType>::SharedPtr client;

--SERVICE--
rclcpp::Service<ServiceType>::SharedPtr service;

--ACTION CLIENT--
rclcpp_action::Client<ActionType>::SharedPtr action_client;

--ACTION SERVER--
rclcpp_action::Server<ActionType>::SharedPtr action_server;

----------------------------------------------------------------------------------------------



----------------------------------------------------------------------------------------------
Example function declarations:
----------------------------------------------------------------------------------------------
Some functions require specific signatures based on their ROS2 functionality
This can include callback functions for timers, subscribers, services, and action servers

The names of the functions in these examples should match those used in the class definition
But can realistically be any valid function name
----------------------------------------------------------------------------------------------
--TIMER CALLBACK--
void TimerCallback();

--SUBSCRIBER CALLBACK--
void SubscriberCallback(const std_msgs::msg::String::SharedPtr msg);

--SERVICE CALLBACK--
void ServiceCallback(const std::shared_ptr<ServiceType::Request> request, std::shared_ptr<ServiceType::Response> response);

--ACTION GOAL HANDLER--
rclcpp_action::GoalResponse HandleGoal(const rclcpp_action::GoalUUID & uuid, std::shared_ptr<const ActionType::Goal> goal);

--ACTION CANCEL HANDLER--
rclcpp_action::CancelResponse HandleCancel(const std::shared_ptr<rclcpp_action::ServerGoalHandle<ActionType>> goal_handle);

--ACTION ACCEPTED HANDLER--
void HandleAccepted(const std::shared_ptr<rclcpp_action::ServerGoalHandle<ActionType>> goal_handle);
----------------------------------------------------------------------------------------------
*/