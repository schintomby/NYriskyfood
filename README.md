# NYriskyfood
Find out which NY dining facilities currently have health code inspection violations. 
This is a simple django app that reads and imports data from a csv file into sqlite3. 
The template is designed to allow users to search through the violations. In the views you will find the search function that has some string manipulation which will highlight the searchstring before sending back to the template. 

This application uses bootstrap, and the csv is from NY State, Dept. of Health (https://health.data.ny.gov/Health/Food-Service-Establishment-Last-Inspection/cnih-y5dw)

