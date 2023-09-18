# -*- mode: makefile -*-
# -----------------------------------------------------------------
# Programmer(s): Radu Serban @ LLNL
#                David J. Gardner @ LLNL
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
# Makefile for IDA serial examples
#
# This file is generated from a template using variables
# set at configuration time. It can be used as a template for
# other user Makefiles.
# -----------------------------------------------------------------

SHELL = sh

prefix       = /home/aditya/Dev/sundials-install
exec_prefix  = /home/aditya/Dev/sundials-install
includedir   = /home/aditya/Dev/sundials-install/include
libdir       = /home/aditya/Dev/sundials-install/lib

CPP      = /usr/bin/cc
CPPFLAGS = -O3 -DNDEBUG
CC       = /usr/bin/cc
CFLAGS   = -O3 -DNDEBUG
LDFLAGS  = 
LIBS     =  -lm

LINKFLAGS = -Wl,-rpath,/home/aditya/Dev/sundials-install/lib

# -----------------------------------------------------------------------------------------

LIBRARIES_LAPACK = -lsundials_sunlinsollapackdense -lsundials_sunlinsollapackband 
LINKFLAGS_LAPACK = ${LINKFLAGS}:

INCLUDES_KLU  = /home/aditya/Dev/suitesparse/include
LIBRARIES_KLU = -lsundials_sunlinsolklu   /home/aditya/Dev/suitesparse/lib/libklu.so /home/aditya/Dev/suitesparse/lib/libamd.so /home/aditya/Dev/suitesparse/lib/libcolamd.so /home/aditya/Dev/suitesparse/lib/libbtf.so /home/aditya/Dev/suitesparse/lib/libsuitesparseconfig.so
LINKFLAGS_KLU = ${LINKFLAGS}:/home/aditya/Dev/suitesparse/lib

INCLUDES_SLUMT  = /home/aditya/Dev/superlu/SRC
LIBRARIES_SLUMT = -lsundials_sunlinsolsuperlumt  /home/aditya/Dev/superlu/lib/libsuperlu_mt_PTHREAD.a /usr/lib/x86_64-linux-gnu/libblas.so 
LINKFLAGS_SLUMT = ${LINKFLAGS}:/home/aditya/Dev/superlu/lib

TMP_INCS  = ${includedir} ${INCLUDES_SLUMT} ${INCLUDES_KLU}
INCLUDES  = $(addprefix -I, ${TMP_INCS})
LIBRARIES = -lsundials_ida -lsundials_nvecserial -lsundials_nvecmanyvector ${LIBS}

# -----------------------------------------------------------------------------------------

EXAMPLES =  idaAnalytic_mels idaFoodWeb_bnd idaFoodWeb_kry idaHeat2D_bnd idaHeat2D_kry idaKrylovDemo_ls idaRoberts_dns idaSlCrank_dns
EXAMPLES_DEPENDENCIES = 

OBJECTS = ${EXAMPLES:=.o}
OBJECTS_DEPENDENCIES = ${EXAMPLES_DEPENDENCIES:=.o}

# LAPACK Examples
EXAMPLES_BL = 
EXAMPLES_DEPENDENCIES_BL = 

OBJECTS_BL = ${EXAMPLES_BL:=.o}
OBJECTS_DEPENDENCIES_BL = ${EXAMPLES_DEPENDENCIES_BL:=.o}

# KLU Examples
EXAMPLES_KLU =  idaHeat2D_klu idaRoberts_klu
EXAMPLES_DEPENDENCIES_KLU = 

OBJECTS_KLU = ${EXAMPLES_KLU:=.o}
OBJECTS_DEPENDENCIES_KLU = ${EXAMPLES_DEPENDENCIES_KLU:=.o}

# SuperLU_MT Examples
EXAMPLES_SLUMT =  idaRoberts_sps
EXAMPLES_DEPENDENCIES_SLUMT = 

OBJECTS_SLUMT = ${EXAMPLES_SLUMT:=.o}
OBJECTS_DEPENDENCIES_SLUMT = ${EXAMPLES_DEPENDENCIES_SLUMT:=.o}

# -----------------------------------------------------------------------------------------

.SUFFIXES : .o .c

.c.o :
	${CC} ${CPPFLAGS} ${CFLAGS} ${INCLUDES} -c $<

# -----------------------------------------------------------------------------------------

all: examples examples_bl examples_klu examples_slumt

examples: ${OBJECTS}
	@for i in ${EXAMPLES} ; do \
	  echo "${CC} -o $${i} $${i}.o ${OBJECTS_DEPENDENCIES} ${CFLAGS} ${LDFLAGS} ${INCLUDES} -L${libdir} ${LIBRARIES} ${LINKFLAGS}" ; \
	  ${CC} -o $${i} $${i}.o ${OBJECTS_DEPENDENCIES} ${CFLAGS} ${LDFLAGS} ${INCLUDES} -L${libdir} ${LIBRARIES} ${LINKFLAGS} ; \
	done

examples_bl: ${OBJECTS_BL}
	@for i in ${EXAMPLES_BL} ; do \
	  echo "${CC} -o $${i} $${i}.o ${OBJECTS_DEPENDENCIES_BL} ${CFLAGS} ${LDFLAGS} ${INCLUDES} -L${libdir} ${LIBRARIES} ${LIBRARIES_LAPACK} ${LINKFLAGS_LAPACK}" ; \
	  ${CC} -o $${i} $${i}.o ${OBJECTS_DEPENDENCIES_BL} ${CFLAGS} ${LDFLAGS} ${INCLUDES} -L${libdir} ${LIBRARIES} ${LIBRARIES_LAPACK} ${LINKFLAGS_LAPACK} ; \
	done

examples_klu: ${OBJECTS_KLU}
	@for i in ${EXAMPLES_KLU} ; do \
	  echo "${CC} -o $${i} $${i}.o ${OBJECTS_DEPENDENCIES_KLU} ${CFLAGS} ${LDFLAGS} ${INCLUDES} -L${libdir} ${LIBRARIES} ${LIBRARIES_KLU} ${LINKFLAGS_KLU}" ; \
	  ${CC} -o $${i} $${i}.o ${OBJECTS_DEPENDENCIES_KLU} ${CFLAGS} ${LDFLAGS} ${INCLUDES} -L${libdir} ${LIBRARIES} ${LIBRARIES_KLU} ${LINKFLAGS_KLU} ; \
	done

examples_slumt: ${OBJECTS_SLUMT}
	@for i in ${EXAMPLES_SLUMT} ; do \
	  echo "${CC} -o $${i} $${i}.o ${OBJECTS_DEPENDENCIES_SLUMT} ${CFLAGS} ${LDFLAGS} ${INCLUDES} -L${libdir} ${LIBRARIES} ${LIBRARIES_SLUMT} ${LINKFLAGS_SLUMT}" ; \
	  ${CC} -o $${i} $${i}.o ${OBJECTS_DEPENDENCIES_SLUMT} ${CFLAGS} ${LDFLAGS} ${INCLUDES} -L${libdir} ${LIBRARIES} ${LIBRARIES_SLUMT} ${LINKFLAGS_SLUMT} ; \
	done

${OBJECTS}: ${OBJECTS_DEPENDENCIES}

${OBJECTS_BL}: ${OBJECTS_DEPENDENCIES_BL}

${OBJECTS_KLU}: ${OBJECTS_DEPENDENCIES_KLU}

${OBJECTS_SLUMT}: ${OBJECTS_DEPENDENCIES_SLUMT}

clean:
	rm -f ${OBJECTS_DEPENDENCIES} ${OBJECTS_DEPENDENCIES_BL} ${OBJECTS_DEPENDENCIES_KLU} ${OBJECTS_DEPENDENCIES_SLUMT}
	rm -f ${OBJECTS} ${OBJECTS_BL} ${OBJECTS_KLU} ${OBJECTS_SLUMT}
	rm -f ${EXAMPLES} ${EXAMPLES_BL} ${EXAMPLES_KLU} ${EXAMPLES_SLUMT}

# -----------------------------------------------------------------------------------------
