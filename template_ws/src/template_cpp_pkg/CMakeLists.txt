cmake_minimum_required(VERSION 3.8)
project(template_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

#--------------------------------------------------------------------------------
# Dependencies can be added here using the find package command
# Dependencies are also required to be added in package.xml
#
# example: find_package(<dependency> REQUIRED)
#--------------------------------------------------------------------------------

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

#--------------------------------------------------------------------------------
# Any new nodes added to the package should be added here 
# using the add_executable command
#
# Example: add_executable(<node_name> src/<node_name>.cpp)
#--------------------------------------------------------------------------------
# followed by ament_target_dependencies to link the dependencies
#
# Example: ament_target_dependencies(<node_name> <dependency1> <dependency2>)
#--------------------------------------------------------------------------------

add_executable(template_node src/template.cpp)
ament_target_dependencies(template_node rclcpp)

#--------------------------------------------------------------------------------
# The node needs to be installed using the install command
# This makes sure the node is available after building the package
# Nodes can be added to the same install command
#
# Example: install(TARGETS <node_name1> <node_name2> <node_name3> DESTINATION lib/${PROJECT_NAME})
#--------------------------------------------------------------------------------

install(TARGETS template_node DESTINATION lib/${PROJECT_NAME})
ament_package()
