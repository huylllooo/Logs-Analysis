Logs Analysis
===============================

A reporting tool that uses information from the database to discover what kind of articles the site's readers like.

## Prepare the data

### Download the data

Download the data ['here'](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). The file inside is called 'newsdata.sql'. Put this file into the 'vagrant' directory, which is shared with your virtual machine.

### Load data

To load the data, use command

    psql -d news -f newsdata.sql

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## Code Design

Using the 'psycopg2' module to connect to the database.

The program executes three SQL queries that are defined in seperated functions to analyze the log data and save the results in 'output.txt' file.

## Run the code

Copy 'newsdata.py' into your 'vagrant' folder, then run:

	python newsdata.py