cmake_minimum_required(VERSION 3.20)
project(kmr_iiwa_nav2)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch
 DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY config
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY rviz
  DESTINATION share/${PROJECT_NAME}
)

# ament
ament_package()
