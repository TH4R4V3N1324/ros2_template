cmake_minimum_required(VERSION 3.8)
project(example_interfaces)

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
find_package(rosidl_default_generators REQUIRED)

#--------------------------------------------------------------------------------
# Interfaces can be added here using the rosidl_generate_interfaces command
#
# Example:  rosidl_generate_interfaces(${PROJECT_NAME}
#             "msg/Message1.msg"
#             "srv/Service1.srv"
#             "action/Action1.action"
#           )
#--------------------------------------------------------------------------------

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Example.msg"
  "srv/Example.srv"
  "action/Example.action"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
