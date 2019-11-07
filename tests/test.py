from python_loc_counter import LOCCounter

def main():
	file = "./tests/randomFile.txt"
	counter = LOCCounter(file)
	
	print(counter.getLOC())
	print(counter.getSourceLOC())
	print(counter.getSingleCommentsLOC())
	print(counter.getSingleDocstringLOC())
	print(counter.getDoubleDocstringLOC())
	print(counter.getTotalCommentsLOC())
	print(counter.getBlankLinesLOC())
	print(counter.getTotalLineCountLOC())

main()
