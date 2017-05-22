# Logs Analysis

import psycopg2

DBNAME = "news"

def question1():
	"""Popular authors"""
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute("select title, count(*) as views "
			"from articles join log "
			"on concat('/article/', articles.slug) = log.path "
			"group by title "
			"order by views desc "
			"limit 3;")
	rows = c.fetchall()
	db.close()
	output_file = open("output.txt", "w")
	output_file.write("1/ Most popular 3 articles of all time:\n\n")
	for row in rows:
		output_file.write(row[0] + ": " + str(row[1]) + " views\n")
	output_file.write("\n===============\n\n")
	output_file.close()

def question2():
	"""Popular authors"""
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute("select name, count(*) as view "
			"from articles "
			"join log on concat('/article/', articles.slug) = log.path "
			"join authors on authors.id = articles.author "
			"group by name "
			"order by view desc;")
	rows = c.fetchall()
	db.close()
	output_file = open("output.txt", "a")
	output_file.write("2/ Most popular article authors of all time:\n\n")
	for row in rows:
		output_file.write(row[0] + ": " + str(row[1]) + " views\n")
	output_file.write("\n===============\n\n")
	output_file.close()

def question3():
	"""Error rates"""
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute("select to_char(alias.Day, 'YYYY-MM-DD') as Day, "
			"errors as Error_rate "
			"from "
			"(select date_trunc('day', time) as Day, "
			"round("
			"(100.0*sum(case when substring(status from 1 for 3) != '200' "
			"then 1 else 0 end)) / count (*), 2) as errors "
			"from log group by 1 order by 1) as alias "
			"where errors > 1 "
			"order by 1;")
	rows = c.fetchall()
	db.close()
	output_file = open("output.txt", "a")
	output_file.write("3/ More than 1% of requests lead to errors on:\n\n")
	for row in rows:
		output_file.write(row[0] + ": " + str(row[1]) + "% errors\n")
	output_file.close()

if __name__ == '__main__':
	question1()
	question2()
	question3()