#!/usr/bin/python
import common
import sys

# Arg1 : report name
# Arg2 : course
# Arg3 and above : author names

# TODO: Python docs
# TODO: Error checking

COVER_PG_SECT = "cover"

# report_name :: string with the name of the report
# course :: string with the name of the course
# authors :: list of strings of the author names
def cover_page_txt( report_name , course , authors ) :
	txt = ""
	txt += "\centering" + common.NEWLINE
	txt += "\\vspace{2.5cm}" + common.NEWLINE
	txt += "{\huge " + report_name + " \par}" + common.NEWLINE
	txt += "{\Large " + course + " \par}" + common.NEWLINE
	txt += "{\Large \\today \par}" + common.NEWLINE
	txt += "\\vspace{1cm}" + common.NEWLINE
	for author_name in authors :
		txt += "{\large " + author_name + " \par}" + common.NEWLINE
	txt += "\\vspace{1cm}" + common.NEWLINE
	return txt

def cover_page_wrap( ) :
	txt = ""
	txt += "\documentclass{article}" + common.NEWLINE
	txt += "\input{../preamble.tex}" + common.NEWLINE
	txt += "\\begin{document}" + common.NEWLINE
	txt += "\\begin{titlepage}" + common.NEWLINE
	txt += "\\input{" + common.content_fname( COVER_PG_SECT ) + "}" + common.NEWLINE
	txt += "\\end{titlepage}" + common.NEWLINE
	txt += "\\end{document}" + common.NEWLINE
	return txt

def gen_cover_page_files( report_name , course , authors ) :
	# generate wrap file
	with open( common.wrap_fname( COVER_PG_SECT ) , common.WRITE ) as wrap_handle :
		wrap_handle.write( cover_page_wrap( ) )
	# generate cover page file
	with open( common.content_fname( COVER_PG_SECT ) , common.WRITE ) as content_handle :
		content_handle.write( cover_page_txt( report_name , course , authors ) )
	# generate Makefile
	with open( "Makefile" , common.WRITE ) as makefile_handle :
		makefile_handle.write( common.gen_makefile_txt( COVER_PG_SECT ) )

if __name__ == "__main__" :
	# TODO: Error checking plz
	report_name = sys.argv[ 1 ]
	course = sys.argv[ 2 ]
	authors = sys.argv[ 3: ]
	gen_cover_page_files( report_name , course , authors )
