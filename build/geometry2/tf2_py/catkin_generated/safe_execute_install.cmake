execute_process(COMMAND "/home/mamad/Hubby/autonomy_ws/build/geometry2/tf2_py/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/mamad/Hubby/autonomy_ws/build/geometry2/tf2_py/catkin_generated/python_distutils_install.sh) returned error code ")
endif()