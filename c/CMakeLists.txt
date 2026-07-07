cmake_minimum_required(VERSION 3.10)
project(kindle_facebook_browser C)

# Set C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Set compilation flags for Kindle (ARM Cortex-A9)
set(CMAKE_C_FLAGS "-O2 -march=armv7-a -mfpu=neon -mfloat-abi=softfp -Wall -Wextra")

# Source files
set(SOURCES
    src/main.c
    src/browser.c
    src/network.c
    src/touch_handler.c
)

# Include directories
include_directories(include)

# Find required packages
find_package(CURL REQUIRED)
find_package(OpenSSL REQUIRED)

# Create executable
add_executable(facebook_browser ${SOURCES})

# Link libraries
target_link_libraries(facebook_browser
    ${CURL_LIBRARIES}
    ${OPENSSL_LIBRARIES}
    m  # math library
)

# Installation
install(TARGETS facebook_browser
    RUNTIME DESTINATION bin
)
