INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DSSS dsss)

FIND_PATH(
    DSSS_INCLUDE_DIRS
    NAMES dsss/api.h
    HINTS $ENV{DSSS_DIR}/include
        ${PC_DSSS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DSSS_LIBRARIES
    NAMES gnuradio-dsss
    HINTS $ENV{DSSS_DIR}/lib
        ${PC_DSSS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DSSS DEFAULT_MSG DSSS_LIBRARIES DSSS_INCLUDE_DIRS)
MARK_AS_ADVANCED(DSSS_LIBRARIES DSSS_INCLUDE_DIRS)

