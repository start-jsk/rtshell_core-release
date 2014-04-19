cmake_minimum_required(VERSION 2.8.3)
project(rtshell)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED mk rostest)

# Build rtshell
# <devel>/lib/<package>/bin
# <devel>/lib/python2.7/dist-packages
# <src>/<package>/share
if(NOT EXISTS ${CMAKE_CURRENT_BINARY_DIR}/installed)
  execute_process(
    COMMAND cmake -E chdir ${CMAKE_CURRENT_BINARY_DIR}
    make -f ${PROJECT_SOURCE_DIR}/Makefile.rtshell installed
    INSTALL_DIR=${CATKIN_DEVEL_PREFIX}
    INSTALL_SCRIPTS_DIR=${CATKIN_DEVEL_PREFIX}/lib/${PROJECT_NAME}
    INSTALL_DATA_DIR=${PROJECT_SOURCE_DIR}
    PATCH_DIR=${PROJECT_SOURCE_DIR}/patch
    MK_DIR=${mk_PREFIX}/share/mk
    MD5SUM_FILE=${PROJECT_SOURCE_DIR}/rtshell-3.0.1.zip.md5sum
    RESULT_VARIABLE _make_failed)
  if (_make_failed)
    message(FATAL_ERROR "Build of rtshell failed")
  endif(_make_failed)
endif()

## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
#catkin_python_setup()

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES openrtm_tools
#  CATKIN_DEPENDS openrtm_aist openrtm_aist_python
#  DEPENDS system_lib
)

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

install(
  DIRECTORY ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_PYTHON_DESTINATION}/
  DESTINATION ${CATKIN_PACKAGE_PYTHON_DESTINATION})
install(
  DIRECTORY ${CATKIN_DEVEL_PREFIX}/lib/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  USE_SOURCE_PERMISSIONS)
install(
  DIRECTORY test share
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS)

install(CODE
  "execute_process(COMMAND echo \"sed -i s@${PROJECT_SOURCE_DIR}@${CMAKE_INSTALL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}@g \$ENV{DESTDIR}/${CMAKE_INSTALL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}/share/rtshell/shell_support\")
   execute_process(COMMAND sed -i s@${PROJECT_SOURCE_DIR}@${CMAKE_INSTALL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}@g \$ENV{DESTDIR}/${CMAKE_INSTALL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}/share/${PROJECT_NAME}/shell_support)
 ")

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_openrtm_tools.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)

add_rostest(test/test_rtshell.test)

