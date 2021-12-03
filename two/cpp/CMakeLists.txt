
cmake_minimum_required (VERSION 3.8)
project (aoc21)

file(GLOB_RECURSE SOURCES "**.cpp")

foreach(FILE IN LISTS SOURCES)
  if ( ${FILE} MATCHES ".*\/src\/(.*).cpp" )
    string(REGEX REPLACE ".*\/src\/(.*).cpp" "\\1" EXEC ${FILE} )
    message(STATUS "Building ${EXEC}...")
    
    add_executable(${EXEC} ${FILE})
    if(MSVC)
      target_compile_options(${EXEC} PRIVATE "/std:c++latest")
    else()
      target_compile_options(${EXEC} PRIVATE "-std=c++20")
    endif()
  endif()
endforeach()
