cmake_minimum_required(VERSION 3.1)

project(asl CXX)

include_directories(include)

add_library(asl INTERFACE)
target_include_directories(asl INTERFACE
	$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
	$<INSTALL_INTERFACE:include>)
