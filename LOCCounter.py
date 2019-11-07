import string
import re

class LOCCounter:
	"""
	Given a filename, this class will be able to get LOC metrics by calling getLOC()
	
	Args:
        file (str): File path to .py file that will be analyzed

	Methods:
		getLOC(): Returns all the LOC metrics 
		calcLOC(): Calculates and and stores LOC metrics
		choseRegexGroups(match): helper function to filter regex matches
		getSourceLOC(): returns source line count as an int
		getSingleCommentsLOC(): returns single comment coubt as an int
		getSingleDocstringLOC(): returns single quote docstring count as an int
		getDoubleDocstringLOC(): returns double quote docstring count as an int
		getTotalCommentsLOC(): returns the summmation of all comment metrics as an int
		getBlankLinesLOC(): returns blank line count as an int
		getTotalLineCountLOC(): returns line count as an int
	"""
	
	def __init__(self, file):
		self.file = file
		__calcLOC()

	__source_loc = 0
	__single_comment_loc = 0 
	__single_docstring_loc = 0 
	__double_docstring_loc = 0 
	__total_comments_loc = 0 
	__blank_loc = 0 
	__total_line_count = 0
	
	def getLOC(self):
		""" Returns all the LOC metrics as a dict
		
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

		return {"source_loc": self.__source_loc, "single_comments_loc": self.__single_comments_loc,
		"single_docstring_loc": single_docstring_loc, "double_docstring_loc": self.__double_docstring_loc,
		"total_comments_loc": self.__total_comments_loc, "blank_loc": self.__blank_loc,
		"total_line_count": self.__total_line_count}
		
	def __calcLOC(self):
		""" Opens file, calculates and stores LOC metrics in private variables
		
		Args:
		
		Returns:
			
		"""

		with open(self.file, "r") as fp:
			line = fp.readline()
			inDoubleDoc = False
			inSingleDoc = False

			while line:		
				self.__total_line_count +=1
				
				#Blank lines in docstrings only count as blank lines
				if line.strip(string.whitespace)=='':
					self.__blank_loc += 1
					line = fp.readline()
					continue
				
				#Remove quotes for some comment analysis
				l = re.sub(r"(\"\"\")|(''')|((\"|').*?\4)", __choseRegexGroups, line)
				#print(repr(l))
				
				inDoubleDoc = inDoubleDoc if (l.count('"""')%2 == 0) else not inDoubleDoc
				inSingleDoc = inSingleDoc if (l.count("'''")%2 == 0) else not inSingleDoc

				if "#" in l:
					self.__single_comment_loc += 1
					
				if ('"""' in l) or inDoubleDoc:
					self.__double_docstring_loc += 1
					
				if ("'''" in l) or inSingleDoc:
					self.__single_docstring_loc += 1
					
				#This regex will not work without removing comments first
				sourceTest = re.sub(r"((\"\"\")|(''')|(#)).*\1?", "", l).strip()
				if ((sourceTest!='') and (not inDoubleDoc) and (not inSingleDoc)):
					self.__source_loc += 1

				line = fp.readline()
				
		self.__total_comments_loc = self.__single_docstring_loc + self.__double_docstring_loc + self.__single_comment_loc
		
		#print ("source_loc: " + str(self.__source_loc))
		#print ("single_comments_loc: " + str(self.__single_comment_loc))
		#print ("single_docstring_loc: " + str(self.__single_docstring_loc))
		#print ("double_docstring_loc: " + str(self.__double_docstring_loc))
		#print ("total_comments_loc: " + str(self.__total_comments_loc))
		#print ("blank_loc: " + str(self.__blank_loc))
		#print ("total_line_count: " + str(self.__total_line_count))
		
	def __choseRegexGroups(self, match):
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
			
	def getSourceLOC(self):
		""" 
		Args:
		
		Returns:
			 int: source_loc
		"""
		return self.__source_loc;
			
	def getSingleCommentsLOC(self):
		""" 
		Args:
		
		Returns:
			 int: self.__single_comment_loc
		"""
		return self.__single_comment_loc;
			
	def getSingleDocstringLOC(self):
		""" 
		Args:
		
		Returns:
			 int: self.__single_docstring_loc
		"""
		return self.__single_docstring_loc;
			
	def getDoubleDocstringLOC(self):
		""" 
		Args:
		
		Returns:
			 int: self.__double_docstring_loc
		"""
		return self.__double_docstring_loc;
			
	def getTotalCommentsLOC(self):
		""" 
		Args:
		
		Returns:
			 int: self.__total_comments_loc
		"""
		return self.__total_comments_loc;
			
	def getBlankLinesLOC(self):
		""" 
		Args:
		
		Returns:
			 int: self.__blank_loc
		"""
		return self.__blank_loc;
			
	def getTotalLineCountLOC(self):
		""" 
		Args:
		
		Returns:
			 int: self.__total_line_count
		"""
		return self.__total_line_count;