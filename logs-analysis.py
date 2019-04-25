#!/usr/bin/env python3

"""Project 1: Logs Analysis for Full Stack Nanodegree by Udacity"""

import psycopg2

DBNAME = "news"

#Query for the reporting tool
query1 = """SELECT articles.title, count(*) as accessed 
			FROM articles join log
			ON log.path LIKE '%'||articles.slug
			WHERE log.status = '200 OK'
			GROUP BY articles.title
			ORDER BY accessed desc limit 3;"""

query2 = """SELECT authors.name, count(*) as accessed 
			FROM  log, authors, articles
			WHERE log.status = '200 OK'
			and log.path LIKE '%'||articles.slug
			and authors.id=articles.author
			GROUP BY authors.name
			ORDER BY accessed desc;"""

query3 = """WITH total_requests AS (
                SELECT time::date AS day, count(*)
                FROM log
                GROUP BY time::date
                ORDER BY time::date
              ), total_errors AS (
                SELECT time::date AS day, count(*)
                FROM log
                WHERE status = '404 NOT FOUND'
                GROUP BY time::date
                ORDER BY time::date
              ), error_rate AS (
                SELECT total_requests.day,
                       total_errors.count::float / total_requests.count::float * 100 AS err_percentage
                FROM total_requests, total_errors
                WHERE total_requests.day = total_errors.day
              )
            SELECT * FROM error_rate WHERE err_percentage > 1;"""


#Function to connect to databse and get report
def fetch_query_report(query):
	#Connect to database
		db = psycopg2.connect(database=DBNAME)
		c = db.cursor()
	#Execute queries
		c.execute(query)
	#Get results
		report = c.fetchall()
		db.close()
		return report


#Function for popular three articles of all time
def most_popular_three_articles(query):
	report = fetch_query_report(query)
	print('')
	print("1. Three most popular articles of all time are:")
	for i in report:
		print('\t' + str(i[0]) + ' : ' +"accessed" + ' ' + str(i[1]) + ' ' +'times')


#Finction for most popular authors of all time
def popular_authors(query):
	report = fetch_query_report(query)
	print('')
	print("2. Most popular article authors of all time are:")
	for i in report:
		print('\t' + str(i[0]) + ' : ' +"accessed" + ' ' + str(i[1]) + ' ' +'times')


#Function to find the days with >1% error occured
def errored_days(query):
	report = fetch_query_report(query)
	print('')
	print("3. Date more than 1% error occured:")
	for i in report:
		print('\t' + str(i[0]) + ' : ' + str(i[1]) + '%' +' error')


#Execute functions
if __name__ == '__main__':

	most_popular_three_articles(query1)
	popular_authors(query2)
	errored_days(query3)
	

