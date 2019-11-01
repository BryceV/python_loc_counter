"""
	'''
		nested docstring
	'''
	
	multiline docstring (note: ^ last line is not considered a comment)
"""
""" double quote docstring """
''' single quote docstring '''
s = 'string' """ docstring next to code """  
s = ' testing """ double docstring notation in a string """. '
s = " testing ''' single docstring notation in a string '''. "

#comment by itself
def func(): #comment with source code
s = " #comment in string "

"#A bit of" code '""" mixed with """' '''everything''' #finaltest
Expected: sloc: 7, single_comment_loc: 3, single_docstring_loc: 5, double_docstring_loc: 8, total_comment_loc: 16, blank_loc: 3, total_line_count: 19