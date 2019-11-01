import string
import re

# Define a class
class LOCCounter:
	def __init__(self, file):
		self.file = file

	#if __name__ == '__main__':
		#main()
		
	def getLOC():
		source_loc = 0 #Source lines - includes end of source symbols like {}
		single_comment_loc = 0 # Comments made using pound key
		single_docstring_loc = 0 # ''' docstrings
		double_docstring_loc = 0 # """ docstrings
		total_comments_loc = 0 #Summation of other comment fields. Note: if single_docstring and double_docstring overlap it will count twice
		blank_loc = 0 # Anything that consists of string.whitespace
		total_line_count = 0 #No distinguishing - just the number of lines

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
		m = match.group()

		if m is not None and (m=='"""' or m=="'''"):
			return m 
		else:
			return ''