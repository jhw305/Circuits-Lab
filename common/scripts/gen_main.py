#!/usr/bin/python

import common
import sys

MAIN = "main"

# section_name :: string of the section name
def section_dirname( section_name ) :
	# TODO Need stricter rules to accomodate :'s and other misc. characters
	return section_name.lower( ).replace( " " , "_" )

# section_name :: string of the section name
def section_source( section_name ) :
	txt = ""
	txt += "\section{" + section_name + "}" + common.NEWLINE
	txt += "\input{./" + section_dirname( section_name ) + "/" + common.content_fname( section_dirname( section_name ) ) + "}" + common.NEWLINE
	return txt

# sections :: list of strings of section names
def gen_main_txt( sections ) :
	txt = ""
	txt += "\documentclass{article}" + common.NEWLINE
	txt += "\input{preamble.tex}" + common.NEWLINE
	txt += "\\begin{document}" + common.NEWLINE
	txt += "\\begin{titlepage}" + common.NEWLINE
	txt += "\\input{./cover_page/cover.tex}" + common.NEWLINE
	txt += "\end{titlepage}" + common.NEWLINE
	for sect in sections :
		txt += section_source( sect )
	txt += "\end{document}" + common.NEWLINE
	return txt

def gen_main_files( sections ) :
	# generate main file
	with open( common.content_fname( MAIN ) , common.WRITE ) as main_handle :
		main_handle.write( gen_main_txt( sections ) )
	# generate Makefile
	with open( "Makefile" , common.WRITE ) as makefile_handle :
		makefile_handle.write( common.gen_makefile_txt( MAIN ) )

if __name__ == "__main__" :
	sections = sys.argv[ 1: ]
	# TODO Fix. We don't want main_wrap.tex in there.
	gen_main_files( sections )
