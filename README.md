# FSND Project 1 : Logs Analysis

Logs analysis project submitted in partial fulfillment of [Full Stack Web Developer Nanodegree](https://eu.udacity.com/course/full-stack-web-developer-nanodegree--nd004) course on Udacity.

## Project Goal
To create a reporting tool that prints out a report based on data into the database. It is a [Python](https://www.python.org) program to connect to the database and performs queries to produce the report.

The [PostgreSQL](https://www.postgresql.org) database contains server access log related to published articles and authors of a fictional newspaper site. The Python reporting tool will analyse those data into database and answer the following 3 questions -

	1. What are the most popular three articles of all time? 
	2. Who are the most popular article authors of all time?
	3. On which days did more than 1% of requests lead to errors?

## System Requirements and Environment Setup
1. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant](https://www.vagrantup.com/fdownloads) to provision the VM with required software
3. Python and psycopg2 module
4. PostgreSql database
	
After installing VirtualBox and Vagrant, clone or download [FSND-VM](https://github.com/udacity/fullstack-nanodegree-vm.git) and follow the instruction on the repository to provision the environment and configure the VM.	

Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) unzip newsdata.sql and move inside vagrant directory.

## Running the Project

### Spin up the vm with vagrant file provided for FSND-VM
Step1:  Navigate to the right directory
```bash
$ cd /vagrant
```
Step 2: From terminal use the following command 
```bash
$ vagrant up
```
This will bring VM online

Step 3: 
For logging into the VM use command
```bash
$ vagrant ssh
```
### Loading the database
Step 1. Unzip the zip file with the command
```bash
$ unzip newsdata.zip
```
Step 2. Command to load the logs into the database
```bash
$ psql -d news -f newsdata.sql
```
### Running the reporting tool
Following command will run the reporting tool
```bash
$ python3 logs-analysis.py
```
If any error message thrown related to psycopg2 module import, then run
```bash
 $ python logs-analysis.py
 ```
### Expected output
*logs-analysis.py* program will produce plain text report on the terminal. Exact sample output is provided as text file in *logs-analysis.txt*

### Shutting VM down
Press Ctrl-D to log out of VM and shut it down with this command
```bash
$ vagrant halt
```
### Author
- Noor Shams
