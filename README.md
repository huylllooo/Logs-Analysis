Logs Analysis
===============================

A reporting tool that uses information from the database to discover what kind of articles the site's readers like.

## Code Design

Using the 'psycopg2' module to connect to the database.

The program executes three SQL queries that are defined in seperated functions to analyze the log data and save the results in 'output.txt' file.

## Run the code

Copy 'newsdata.py' into your 'vagrant' folder, then run:

	python newsdata.py