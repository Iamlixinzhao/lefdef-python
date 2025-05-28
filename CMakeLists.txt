cmake_minimum_required(VERSION 3.19)
project(lefdef_project VERSION 1.0 LANGUAGES C CXX)

# Manually add C++20 (or C++2a) standard switches before all add_subdirectory
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  if(CMAKE_CXX_COMPILER_VERSION VERSION_LESS "8.0")
    message(STATUS "GCC < 8 detected (${CMAKE_CXX_COMPILER_VERSION}), using -std=gnu++2a")
    add_compile_options(-std=gnu++2a)
  else()
    message(STATUS "GCC >= 8 detected (${CMAKE_CXX_COMPILER_VERSION}), using -std=c++20")
    add_compile_options(-std=c++20)
  endif()
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
  message(STATUS "Clang detected, using -std=c++20")
  add_compile_options(-std=c++20)
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
  message(STATUS "MSVC detected, using /std:c++20")
  add_compile_options(/std:c++20)
endif()

# (Optional) If you still have an old CMAKE_CXX_STANDARD setting, you can delete it or change it to OFF
# set(CMAKE_CXX_STANDARD        20)
# set(CMAKE_CXX_STANDARD_REQUIRED ON)
# set(CMAKE_CXX_EXTENSIONS       OFF)

# 2. external/def subproject (will generate def, defzlib)
add_subdirectory(${CMAKE_SOURCE_DIR}/external/def)

# 3. If external/lef has CMakeLists, use add_subdirectory in the same way, otherwise use add_library by yourself
add_subdirectory(${CMAKE_SOURCE_DIR}/external/lef)
# 4. Main project source code
file(GLOB_RECURSE MAIN_SOURCES
  ${CMAKE_SOURCE_DIR}/src/*.cpp
  ${CMAKE_SOURCE_DIR}/src/*.c
  ${CMAKE_SOURCE_DIR}/src/*.hpp
  ${CMAKE_SOURCE_DIR}/src/*.h
)

# 5. Executable test
add_executable(test
  ${CMAKE_SOURCE_DIR}/test.cpp
  ${MAIN_SOURCES}
)
target_link_libraries(test PRIVATE
  def
  defzlib
  lef
)

#6. Shared library lefdef
add_library(lefdef SHARED
  ${MAIN_SOURCES}
)
target_link_libraries(lefdef PRIVATE
  def
  defzlib
  lef
)

# 7. Installation (optional)
install(TARGETS lefdef
  RUNTIME   DESTINATION bin
  LIBRARY   DESTINATION lib
  ARCHIVE   DESTINATION lib
)
