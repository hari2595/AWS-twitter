# AWS-youtube
<br>
This an end to end project where we do some basic transformtion and data processing on youtube analytics Data from the youtube API. The data is stored in an initial landing bucket which is then transformed with the help of Amazon Glue and Amazon Lambda. Finally we use a Glue job to store our data in a analytics DB in Amazon Athena. This DB is connected with Tableau and we are able to do some data exploration and identify key metrics with Tableau Visualization.
<br>
<br>
<p>
    <img src="https://raw.githubusercontent.com/hari2595/AWS-youtube/main/Flowcharts.jpeg" height="440" />
</p>
<h3> Pre Requisites: </h3><br>
AWS Account <br>
Tableau <br>
<br>
<h3> Execution </h3>
<br>
<br>
Step 1: Login Into AWS. <br><br>
Step 2: Load the data into a landing bucket. <br><br>
Step 3: Create 2 new IAM roles that provide s3 full access and glue services for your lambda and glue resources. <br><br>
Step 4: Create a Lambda Function (file provided) that can Flatten the category JSON file and load it into the clean db(You have to create a ckean DB and Lambda automatically creates the table)<br><br>
Step 5: Input the DB and table details in the  function configuration.<br><br>
<p>
    <img src="https://raw.githubusercontent.com/hari2595/AWS-youtube/main/Lambda/config.PNG" width="880" height="440" />
</p>
Step 6: Create a test for the Lambda function and provide the landing bucket URI in the test as shown <br><br>
<p>
    <img src="https://raw.githubusercontent.com/hari2595/AWS-youtube/main/Lambda/test.PNG" width="880" height="440" />
</p>
Step 7: Now create a Glue crawler to load the CSV file into a raw DB. <br><br>
Step 8: Create a glue job to transform this db into a parquet file, refer the glue job file. <br><br>
Step 9: Now create a Glue crawler to load this Parquet file into the clean DB <br><br>
Step 10: Go to flue studio to create a Glue union job that joins both the file with a union function<br><br>
Step 11: Save the new table into an analytical DB, create a landing bucket to save the data <br><br>
Step 12: Use your IAM user credential to connect to tableau<br><br>
Step 13: An example of possible data exploration is attached in the tableau file and a tableau workbook is also given. <br><br>
