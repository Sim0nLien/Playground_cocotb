cmake_minimum_required(VERSION 3.15)
project(MonProjet VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Boost REQUIRED)

include_directories(include ${Boost_INCLUDE_DIRS})
set(SOURCES
    Srcs/cpp_model/main.cpp
)

add_executable(exe ${SOURCES})

