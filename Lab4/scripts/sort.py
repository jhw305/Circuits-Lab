#!/usr/bin/python

def sort( list_to_sort ) :
	# Not the best sorting algorithm, but it'll do for small lists :)
	sorted_list = [ list_to_sort[ 0 ] ]
	for list_to_sort_count in range( 0 , len( list_to_sort ) ) :
		for sorted_list_count in range( 0 , len( sorted_list ) ) :
			if list_to_sort[ list_to_sort_count ] < sorted_list[ sorted_list_count ] :
				sorted_list.insert( sorted_list_count , list_to_sort[ list_to_sort_count ] )
				break
		if list_to_sort[ list_to_sort_count ] not in sorted_list :
			sorted_list.append( list_to_sort[ list_to_sort_count ] )
	return sorted_list

def test_sort( list_to_sort ) :
	print( "Before: " + str( list_to_sort ) )
	print( "After: " + str( sort( list_to_sort ) ) )
	print( "" )

my_list = [ 3 , 9 , 8 ]
test_sort( my_list )
my_list = [ 1 , 7 , 2 , 3 , 2 , 2 , 1 ]
test_sort( my_list )
my_list = [ 3 , 2 , 3 , 8 , 4 , 6 , 2 , 6 ]
test_sort( my_list )
