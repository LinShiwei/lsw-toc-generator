import os

def countingX_InLine(line):
	count = 0
	while line[count:count+1] == '#' and count < len(line):
		count = count + 1
	if line[count:count+1] == ' ':
		return count
	else:
		return 0

def correctLineFormatOffset(lineFormat):
	smallXCount = 100
	for fm in lineFormat:
		if fm[0] < smallXCount:
			smallXCount = fm[0] 
	for index in range(len(lineFormat)):
		lineFormat[index][1] = lineFormat[index][1][lineFormat[index][0]+1:-1]
		lineFormat[index][0] = lineFormat[index][0] - smallXCount + 1
	return lineFormat
	
def generateLineWith(fm):
	tocLinePrefix = '    ' * (fm[0]-1)
	tags = '' 
	for index in range(len(fm[1])):
		if fm[1][index] == ' ':
			tags = tags + '-'
		else:
			tags = tags + fm[1][index]
	return tocLinePrefix +'- ['+ fm[1] +']'+'(#'+tags.lower() +')\n'


def addTOCtoFile(fileName):
	toc = ['## Table of Contents\n']
	lines = []
	insertIndex = -1
	originTocLineFormat = []
	with open(fileName, 'r+') as f:
		for line in f:
			lines.append(line)
			
			count = countingX_InLine(line)
			if count > 0:
				if insertIndex == -1:
					insertIndex = len(lines)-1
				originTocLineFormat.append([count,line])
	correctTocLineFormat = correctLineFormatOffset(originTocLineFormat)
	for fm in correctTocLineFormat:
		toc.append(generateLineWith(fm))
	toc.append("\n")
	toc.reverse()
	for tocLine in toc:
		lines.insert(insertIndex,tocLine)

	os.remove(fileName)
	with open(fileName, 'w') as g:
		g.writelines(lines)

mdFileNames = []

for fileName in os.listdir(os.getcwd()):
	if fileName[-3:] == '.md':
		mdFileNames.append(fileName)

for name in mdFileNames:
	addTOCtoFile(name)


