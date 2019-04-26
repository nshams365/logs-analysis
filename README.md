#Log Analysis Project

### by Noor Shams
This is a project for Udacity Full Stack Nano Degree program. 
[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd005).

## Project Goal
This project requires SQL queries and Python code to analyse newspaper site data to answer 3 given questions.

	1.	What are the most popular three articles of all time? 
	2.	Who are the most popular article authors of all time?
	3.	On which days did more than 1% of requests lead to errors?

## System Prerequisite 
	*	Python 3
	*	PostgreSQL
	*	[VirtualBox](https://www.virtualbox.org/wiki/Downloads) Linux based virtual machine and 
	*	[Vagrant](https://www.vagrantup.com/fdownloads) to manage virtual machine

## Running the Project

download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) unzip newsdata.sql and load inside vagrant directory or clone this repository to your local machine.

Step1:  Navigate to the right directory
'''bash
$cd /vagrant
'''
Step 2: from terminal use the following command 
'''bash
$vagrant up
,,,
This will bring VM online
Step 3: 
For logging into the VM use command
'''bash
$vagrant ssh
'''

### Loading the database
1. unzip the zip file with the command:
'''bash
unzip newsdata.zip
'''
2. Command to load the logs into the database:
'''bash
psql -d news -f newsdata.sql
'''

### Running the reporting tool
Following command will run the reporting tool:
'''bash
python3 logs_analysis_tool.py
,,,
Shutting VM down
Press Ctrl-D to log out of VM and shut it down with this command:
'''bash
vagrant halt
'''
