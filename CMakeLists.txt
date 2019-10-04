cmake_minimum_required(VERSION 3.15)

project(asl CXX)

add_library(asl INTERFACE)
target_sources(asl INTERFACE
    ${CMAKE_CURRENT_SOURCE_DIR}/include/gsl/assert
    ${CMAKE_CURRENT_SOURCE_DIR}/include/gsl/byte
    ${CMAKE_CURRENT_SOURCE_DIR}/include/gsl/not_null
    ${CMAKE_CURRENT_SOURCE_DIR}/include/gsl/span
    ${CMAKE_CURRENT_SOURCE_DIR}/include/gsl/string_span
    ${CMAKE_CURRENT_SOURCE_DIR}/include/gsl/util

    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/ct_string
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/debug_only
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/detect_features
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/expected
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/filesystem
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/functional
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/meta
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/ring
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/string_view
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/testing
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/types
    ${CMAKE_CURRENT_SOURCE_DIR}/include/asl/write_once
)
target_include_directories(asl INTERFACE
	$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
	$<INSTALL_INTERFACE:include>)
