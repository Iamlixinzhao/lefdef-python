cmake_minimum_required(VERSION 3.19)
project(lefdef_project VERSION 1.0 LANGUAGES C CXX)

# 手动添加 C++20 (或 C++2a) 标准开关，放到所有 add_subdirectory 之前
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

# （可选）如果还有老的 CMAKE_CXX_STANDARD 设置也可以删掉或者改成 OFF
# set(CMAKE_CXX_STANDARD        20)
# set(CMAKE_CXX_STANDARD_REQUIRED ON)
# set(CMAKE_CXX_EXTENSIONS       OFF)

# 2. external/def 子项目（会生成 def, defzlib）
add_subdirectory(${CMAKE_SOURCE_DIR}/external/def)

# 3. external/lef 若有 CMakeLists 同理 add_subdirectory，否则自行 add_library
add_subdirectory(${CMAKE_SOURCE_DIR}/external/lef)
# 4. 主项目源码
file(GLOB_RECURSE MAIN_SOURCES
  ${CMAKE_SOURCE_DIR}/src/*.cpp
  ${CMAKE_SOURCE_DIR}/src/*.c
  ${CMAKE_SOURCE_DIR}/src/*.hpp
  ${CMAKE_SOURCE_DIR}/src/*.h
)

# 5. 可执行 test
add_executable(test
  ${CMAKE_SOURCE_DIR}/test.cpp
  ${MAIN_SOURCES}
)
target_link_libraries(test PRIVATE
  def
  defzlib
  lef
)

# 6. 共享库 lefdef
add_library(lefdef SHARED
  ${MAIN_SOURCES}
)
target_link_libraries(lefdef PRIVATE
  def
  defzlib
  lef
)

# 7. 安装（可选）
install(TARGETS lefdef
  RUNTIME   DESTINATION bin
  LIBRARY   DESTINATION lib
  ARCHIVE   DESTINATION lib
)
