# -*- mode: makefile -*-
# -----------------------------------------------------------------
# Programmer: Radu Serban @ LLNL
# -----------------------------------------------------------------
# SUNDIALS Copyright Start
# Copyright (c) 2002-2023, Lawrence Livermore National Security
# and Southern Methodist University.
# All rights reserved.
#
# See the top-level LICENSE and NOTICE files for details.
#
# SPDX-License-Identifier: BSD-3-Clause
# SUNDIALS Copyright End
# -----------------------------------------------------------------
# Makefile for IDA parallel examples
#
# This file is generated from a template using various variables
# set at configuration time. It can be used as a template for
# other user Makefiles.
# -----------------------------------------------------------------

SHELL = sh

prefix       = /home/aditya/Dev/sundials-install
exec_prefix  = /home/aditya/Dev/sundials-install
includedir   = /home/aditya/Dev/sundials-install/include
libdir       = /home/aditya/Dev/sundials-install/lib

CPP         = /usr/bin/cc
CPPFLAGS    = -O3 -DNDEBUG
CC          = /usr/bin/cc
CFLAGS      = -O3 -DNDEBUG
LDFLAGS     = 
LIBS        =  -lm

LINKFLAGS = -Wl,-rpath,/home/aditya/Dev/sundials-install/lib

MPICC       = /usr/bin/mpicc
MPI_INC_DIR = .
MPI_LIB_DIR = .
MPI_LIBS    = 
MPI_FLAGS   = 

TMP_INCS  = ${includedir} ${MPI_INC_DIR}
INCLUDES  = $(addprefix -I, ${TMP_INCS})
LIBRARIES = -lsundials_ida -lsundials_nvecparallel -lsundials_nvecserial \
						-lsundials_nvecmpimanyvector -lsundials_nvecmpiplusx ${LIBS}

EXAMPLES =  idaFoodWeb_kry_bbd_p idaFoodWeb_kry_p idaHeat2D_kry_bbd_p idaHeat2D_kry_p
EXAMPLES_DEPENDENCIES = 

OBJECTS = ${EXAMPLES:=.o}
OBJECTS_DEPENDENCIES = ${EXAMPLES_DEPENDENCIES:=.o}

# -----------------------------------------------------------------------------------------

.SUFFIXES : .o .c

.c.o :
	${MPICC} ${CPPFLAGS} ${CFLAGS} ${MPI_FLAGS} ${INCLUDES} -c $<

# -----------------------------------------------------------------------------------------

all: ${OBJECTS}
	@for i in ${EXAMPLES} ; do \
	  echo "${MPICC} -o $${i} $${i}.o ${OBJECTS_DEPENDENCIES} ${MPI_FLAGS} ${CFLAGS} ${LDFLAGS} ${INCLUDES} -L${libdir} ${LIBRARIES} -L${MPI_LIB_DIR} ${MPI_LIBS} ${LINKFLAGS}" ; \
	  ${MPICC} -o $${i} $${i}.o ${OBJECTS_DEPENDENCIES} ${MPI_FLAGS} ${CFLAGS} ${LDFLAGS} ${INCLUDES} -L${libdir} ${LIBRARIES} -L${MPI_LIB_DIR} ${MPI_LIBS} ${LINKFLAGS} ; \
	done

${OBJECTS}: ${OBJECTS_DEPENDENCIES}

clean:
	rm -f ${OBJECTS_DEPENDENCIES}
	rm -f ${OBJECTS}
	rm -f ${EXAMPLES}

# -----------------------------------------------------------------------------------------
