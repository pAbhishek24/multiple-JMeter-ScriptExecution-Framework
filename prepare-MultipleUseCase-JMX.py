# Author      - Abhishek Pandey
# Date        - 16/01/2019
# Description - This file is intended to read data from CSV file
### import required module
import csv
import os
import shutil
import sys
# import pandas
import xml.etree.ElementTree as ET


## Defining the Functions

# Function - To Copy Script for execution
def copyScript(gitProjectName, scriptsToCpy, srcPATH, destPATH):
	global errorLevel
	global tree
	# Script Name, Source Path and Destination Path
	scpy = srcPATH + '/' + gitProjectName + '/' + scriptsToCpy
	dcpy = destPATH + '/' + scriptsToCpy

	# Check if file exist then Copy
	if os.path.isfile(scpy):
		shutil.copy(scpy, dcpy)
	# print('*** Scripts copied ***')
	else:
		print '!!! Error : Unable to locate files, Please check GIT repo for files', scpy
		errorLevel = True


# print('*** Script copy function executed ***')

# Function - To Copy datafiles for execution
def copyDataFiles(gitProjectName, dataFilesToCopy, srcPATH, destPATH):
	global errorLevel
	# DataFile name, source path and destination path
	#dFile = dataFilesToCopy.replace('.jmx', '.csv')
	#scpy = srcPATH + '/' + gitProjectName + '/' + dFile
	#dcpy = destPATH + '/' + dFile
	# Variable for Copy All files:
	scpyAllCSV = srcPATH + '/' + gitProjectName
	dst_dir = destPATH
	# Check if data files exists then Copy
	#if os.path.isfile(scpy):
		#shutil.copy(scpy, dcpy)
		# Copying all the  CSV files that are present in application directory
	if copyAllFiles == True:
		for root, dirs, files in os.walk(scpyAllCSV):
			for f in files:
				if f.endswith('.csv'):
					print os.path.join(root,f)
					shutil.copy(os.path.join(root,f), dst_dir)
	#else:
	#	print '!!! Warning : Unable to locate DATA files, Please check GIT repo ', scpy


# print('*** Data Files copy funtion executed ***')

# Function to create template-MultipleUseCase.jmx script
def templateMultipleUseCase(tree, rootNode, scenarioName, numberOfUsers, scriptFileName, pacingTime, thinkTime, startUpDelay, fileToExecute):

	global debug
	scenarioName = scenarioName.replace('.jmx','')
	if debug:
		print 'Adding ' + scenarioName + ' to template.'

	newThreadGroupNode = ET.Element('ThreadGroup')
	newThreadGroupNode.set('guiclass', 'ThreadGroupGui')
	newThreadGroupNode.set('testclass', 'ThreadGroup')
	newThreadGroupNode.set('testname', scenarioName)
	newThreadGroupNode.set('enabled', 'true')

	subNode = ET.Element('stringProp')
	subNode.set('name', 'ThreadGroup.on_sample_error')
	subNode.text = 'startnextloop'
	newThreadGroupNode.append(subNode)

	subNode = ET.Element('elementProp')
	subNode.set('name', 'ThreadGroup.main_controller')
	subNode.set('elementType', 'LoopController')
	subNode.set('guiclass', 'LoopControlPanel')
	subNode.set('testclass', 'LoopController')
	subNode.set('testname', 'Loop Controller')
	subNode.set('enabled', 'true')
	subSubNode = ET.Element('boolProp')
	subSubNode.set('name', 'LoopController.continue_forever')
	subSubNode.text = 'false'
	subNode.append(subSubNode)
	subSubNode = ET.Element('stringProp')
	subSubNode.set('name', 'LoopController.loops')
	subSubNode.text = '-1'
	subNode.append(subSubNode)
	newThreadGroupNode.append(subNode)

	subNode = ET.Element('stringProp')
	subNode.set('name', 'ThreadGroup.num_threads')
	subNode.text = numberOfUsers
	newThreadGroupNode.append(subNode)

	subNode = ET.Element('stringProp')
	subNode.set('name', 'ThreadGroup.ramp_time')
	subNode.text = '${__P(Test.RampUpInSec)}'
	newThreadGroupNode.append(subNode)

	subNode = ET.Element('longProp')
	subNode.set('name', 'ThreadGroup.start_time')
	subNode.text = '1418746522000'
	newThreadGroupNode.append(subNode)

	subNode = ET.Element('longProp')
	subNode.set('name', 'ThreadGroup.end_time')
	subNode.text = '1418746522000'
	newThreadGroupNode.append(subNode)

	subNode = ET.Element('boolProp')
	subNode.set('name', 'ThreadGroup.scheduler')
	subNode.text = 'true'
	newThreadGroupNode.append(subNode)

	subNode = ET.Element('stringProp')
	subNode.set('name', 'ThreadGroup.duration')
	subNode.text = '${__P(Test.DurationInSec)}'
	newThreadGroupNode.append(subNode)

	subNode = ET.Element('stringProp')
	subNode.set('name', 'ThreadGroup.delay')
	subNode.text = startUpDelay
	newThreadGroupNode.append(subNode)

	newHashTree = ET.Element('hashTree')
	subNode = ET.Element('Arguments')
	subNode.set('guiclass', 'ArgumentsPanel')
	subNode.set('testclass', 'Arguments')
	subNode.set('testname', 'User Defined Variables')
	subNode.set('enabled', 'true')
	subsubNode = ET.Element('collectionProp')
	subsubNode.set('name', 'Arguments.arguments')

	subsubsubNode = ET.Element('elementProp')
	subsubsubNode.set('name', 'threadGroupName')
	subsubsubNode.set('elementType', 'Argument')
	subsubsubsubNode = ET.Element('stringProp')
	subsubsubsubNode.set('name', 'Argument.name')
	subsubsubsubNode.text = 'threadGroupName'
	subsubsubNode.append(subsubsubsubNode)
	subsubsubsubNode = ET.Element('stringProp')
	subsubsubsubNode.set('name', 'Argument.value')
	subsubsubsubNode.text = scenarioName
	subsubsubNode.append(subsubsubsubNode)
	subsubsubsubNode = ET.Element('stringProp')
	subsubsubsubNode.set('name', 'Argument.metadata')
	subsubsubsubNode.text = '='
	subsubsubNode.append(subsubsubsubNode)
	subsubNode.append(subsubsubNode)

	subsubsubNode = ET.Element('elementProp')
	subsubsubNode.set('name', 'PacingTime')
	subsubsubNode.set('elementType', 'Argument')
	subsubsubsubNode = ET.Element('stringProp')
	subsubsubsubNode.set('name', 'Argument.name')
	subsubsubsubNode.text = 'PacingTime'
	subsubsubNode.append(subsubsubsubNode)
	subsubsubsubNode = ET.Element('stringProp')
	subsubsubsubNode.set('name', 'Argument.value')
	subsubsubsubNode.text = pacingTime + "000"
	subsubsubNode.append(subsubsubsubNode)
	subsubsubsubNode = ET.Element('stringProp')
	subsubsubsubNode.set('name', 'Argument.metadata')
	subsubsubsubNode.text = '='
	subsubsubNode.append(subsubsubsubNode)
	subsubNode.append(subsubsubNode)

	subsubsubNode = ET.Element('elementProp')
	subsubsubNode.set('name', 'ThinkTime')
	subsubsubNode.set('elementType', 'Argument')
	subsubsubsubNode = ET.Element('stringProp')
	subsubsubsubNode.set('name', 'Argument.name')
	subsubsubsubNode.text = 'ThinkTime'
	subsubsubNode.append(subsubsubsubNode)
	subsubsubsubNode = ET.Element('stringProp')
	subsubsubsubNode.set('name', 'Argument.value')
	subsubsubsubNode.text = thinkTime + "000"
	subsubsubNode.append(subsubsubsubNode)
	subsubsubsubNode = ET.Element('stringProp')
	subsubsubsubNode.set('name', 'Argument.metadata')
	subsubsubsubNode.text = '='
	subsubsubNode.append(subsubsubsubNode)
	subsubNode.append(subsubsubNode)
	subNode.append(subsubNode)
	newHashTree.append(subNode)
	newHashTree.append(ET.Element('hashTree'))

	subNode = ET.Element('IncludeController')
	subNode.set('guiclass', 'IncludeControllerGui')
	subNode.set('testclass', 'IncludeController')
	subNode.set('testname', 'Include Controller')
	subNode.set('enabled', 'true')
	subsubNode = ET.Element('stringProp')
	subsubNode.set('name', 'IncludeController.includepath')
	subsubNode.text = scriptFileName
	subNode.append(subsubNode)
	newHashTree.append(subNode)

	rootNode[0][1].append(newThreadGroupNode)
	rootNode[0][1].append(newHashTree)

	if debug:
		print 'Adding ' + scenarioName + ' to template complete.'
	
	tree.write(fileToExecute)

# Reading the Environment Variable
#WSPACE = '/Users/abhishek.pandey/Desktop/WORKSPACE/template-MultipleUseCase-Execution'
#ESPACE = '/Users/abhishek.pandey/Desktop/WORKSPACE/template-MultipleUseCase-Execution/1'

debug = os.environ.get("DEBUG")
WSPACE = os.environ.get("WORKSPACE")
ESPACE = os.environ.get("EXECSPACE")
errorLevel = False
copyAllFiles = True
#######
# Main Starts here
####

# Validating the environment variable
if debug is None:
	print '!!! Warining : DEBUG level is not set, setting to TRUE'
	debug = True

if ESPACE is None:
	print '!!! Error : EXECUTION SPACE environment variable is NOT SET'
	errorLevel = True
else:
	print '+++ Message : WORKSPACE = ' + WSPACE
	print '+++ Message : EXECUTION SPACE = ' + ESPACE

# Copy multiple-UseCase-template.jmx from JMETER_LIBS direcotry
tempToCopy = WSPACE + '/JMETER_LIBS/' + 'multiple-UseCase-template.jmx'
jmxTemplate = ESPACE + '/' + 'multiple-UseCase-template.jmx'

if os.path.isfile(tempToCopy):
	print '+++ Message : Template to Copy = ' + tempToCopy
	print '+++ Message : Place to copy = ' + jmxTemplate

	shutil.copy(tempToCopy, jmxTemplate)

	# Parsing the dynamic template for JMeter which is a XML file
	tree = ET.parse(ESPACE + '/' + 'multiple-UseCase-template.jmx')
	root = tree.getroot()
	#print(root[0][0])
	# CSV Fle
	loadTestCSVFile = WSPACE + '/test-execution.csv'
	# Checking if CSV file is present or not
	if os.path.isfile(loadTestCSVFile):
		print "+++ Message : LoadTest execution CSV file is present LOCATION=", loadTestCSVFile
		# Reading CSV file
		with open(loadTestCSVFile, 'r') as lTF:
			csvReader = csv.reader(lTF)
			# Reading the next Row - AS First Row is HEADER ROW
			next(csvReader)
			for row in csvReader:
				gitPName = row[0]
				sName = row[1]
				users = row[2]
				delay = row[3]
				pTime = row[4]
				tTime = row[5]

				if debug:
					print '***************************************************'
					print '* Adding scripts to multiple-UseCase-template.jmx *'
					print '***************************************************'
					print '* Project Name  : ' + gitPName
					print '* Users         : ' + users
					print '* Script Name   : ' + sName
					print '* StartUp Delay : ' + delay
					print '* Pacing Time   : ' + pTime
					print '* Think Time    : ' + tTime
					print '***************************************************'
				copyScript(gitPName, sName, WSPACE, ESPACE)
				# Copy Files from all folder
				copyDataFiles(gitPName, sName, WSPACE, ESPACE)

				# Adding scripts to the multiple-execution-template.jmx
				scriptFileName = ESPACE + '/' + sName
				fileToExecute = ESPACE + '/' + 'test-Dynamic.jmx'
				# template-MultipleUseCase( rootNode, scenarioName, numberOfUsers, scriptFileName, pacingTime, thinkTime, startUpDelay )
				templateMultipleUseCase(tree, root, sName, users, scriptFileName, pTime, tTime, delay, fileToExecute)
			
	else:
		print "!!! Warning : LoadTest execution CSV file is ABSENT"
		errorLevel = True
else:
	print '!!! Error : Unable to locate multiple-UseCase-template.jmx, Please check GIT repo JMETER_LIBS/'
	errorLevel = True

# Error Level - Understanding script execution status
if errorLevel:
	print '!!! Error : encountered, exiting with error '
	print '!!! Aborting !!!'
	sys.exit(1)
else:
	print '*** prepare-MultipleUseCase-JMX.py -- Script Execution Complete, Prepared test-Dynamic.jmx file for load test ***'
