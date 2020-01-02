#makefile 
MD = markdown
MDFLAGS = -T
#SOURCES := $(wildcard *.md)
#OBJECTS := $(patsubst %.md, %.html, $(wildcard *.md))

TOPDIR := $(shell pwd)
DIR := $(shell find $(TOPDIR) -type d)
SOURCES := $(foreach subdir,$(DIR),$(wildcard $(subdir)/*.md))
OBJECTS := $(patsubst %.md, %.html, $(SOURCES))

echo $(OBJECTS)

