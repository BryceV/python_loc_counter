import string
import re

class LOCCounter:
	"""
	Given a filename, this class will be able to get LOC metrics by calling getLOC()
	
	Args:
        file (str): File path to .py file that will be analyzed

	Methods:
		getLOC(): Calculates and returns LOC
		choseRegexGroups(match): helper function to filter regex matches
	"""
	
	def __init__(self, file):
		self.file = file

	#if __name__ == '__main__':
		#main()
		
	def getLOC():
		""" Opens file, calculates LOC metrics
		
		Args:
		
		Returns:
			dict:
			{
				source_loc, #Includes end of source symbols like {}
				single_comment_loc, #Comments made using pound key
				single_docstring_loc, #Docstring using single quotes 
				double_docstring_loc, #Docstring using double quotes 
				total_comments_loc, #Summation of other comment fields. Note: if single_docstring and double_docstring overlap it will count twice
				blank_loc = 0, #Anything that consists of string.whitespace
				total_line_count, #No distinguishing - just the number of lines
			}
		"""
	
		source_loc = 0
		single_comment_loc = 0 
		single_docstring_loc = 0 
		double_docstring_loc = 0 
		total_comments_loc = 0 
		blank_loc = 0 
		total_line_count = 0

		with open(self.file, "r") as fp:
			line = fp.readline()
			inDoubleDoc = False
			inSingleDoc = False

			while line:		
				total_line_count +=1
				
				#Blank lines in docstrings only count as blank lines
				if line.strip(string.whitespace)=='':
					blank_loc += 1
					line = fp.readline()
					continue
				
				#Remove quotes for some comment analysis
				l = re.sub(r"(\"\"\")|(''')|((\"|').*?\4)", choseRegexGroups, line)
				#print(repr(l))
				
				inDoubleDoc = inDoubleDoc if (l.count('"""')%2 == 0) else not inDoubleDoc
				inSingleDoc = inSingleDoc if (l.count("'''")%2 == 0) else not inSingleDoc

				if "#" in l:
					single_comment_loc += 1
					
				if ('"""' in l) or inDoubleDoc:
					double_docstring_loc += 1
					
				if ("'''" in l) or inSingleDoc:
					single_docstring_loc += 1
					
				#This regex will not work without removing comments first
				sourceTest = re.sub(r"((\"\"\")|(''')|(#)).*\1?", "", l).strip()
				if ((sourceTest!='') and (not inDoubleDoc) and (not inSingleDoc)):
					source_loc += 1

				line = fp.readline()
				
		total_comments_loc = single_docstring_loc + double_docstring_loc + single_comment_loc
		
		#print ("source_loc: " + str(source_loc))
		#print ("single_comments_loc: " + str(single_comment_loc))
		#print ("single_docstring_loc: " + str(single_docstring_loc))
		#print ("double_docstring_loc: " + str(double_docstring_loc))
		#print ("total_comments_loc: " + str(total_comments_loc))
		#print ("blank_loc: " + str(blank_loc))
		#print ("total_line_count: " + str(total_line_count))
		
		return {"source_loc": source_loc, "single_comments_loc": single_comments_loc,
		"single_docstring_loc": single_docstring_loc, "double_docstring_loc": double_docstring_loc,
		"total_comments_loc": total_comments_loc, "blank_loc": blank_loc,
		"total_line_count": total_line_count}
		
	def choseRegexGroups(match):
		""" Helper function used to filter docstrings when getLOC() removes quotes
		
		Args:
			param1 (match): match object that needs to be filtered
		Returns:
			 string: If the match is not a docstring, return its substitute string. Else, return an empty string.
		"""
		
		m = match.group()

		if m is not None and (m=='"""' or m=="'''"):
			return m 
		else:
			return ''
			
help(LOCCounter)