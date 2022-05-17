## Description

## Application Programming Interfaces(APIs)
Application Programming Interfaces(APIs) help different pieces of software talk to each other. When you write a program, you typically use a bunch of existing libraries for the programming language of your choice. These libraries provide APIs in the form of external or public functions, classes, and methods that other code can use to get their job done without having to create a lot of repeated code. 
### The project 'Scale and convert images using PIL'
In this project, you will write a script that uses PIL to perform the following operations:
Iterate through each file in the folder
For each file:
- Rotate the image 90 clockwise
- Resize the image from 192 x 192 to 128 x 128
- Save the image to a new folder in .jpeg format

You can check python script 'image.py'

## Web Applications and Services
A web application is an application that you interact with over HTTP. Web applications that have an API are also known as web services. Instead of browsing to a web page to type and click around, you can use your program to send a message known as an API call to the web service. The part of the program that listens on the network for API calls is called an API endpoint.

## Data Serialization Formats
JSON (JavaScript Object Notation) is the serialization format. let's just use the json module to convert our people list of dictionaries into JSON format. 

YAML (Yet Another Markup Language) has a lot in common with JSON. They’re both formats that can be easily understood by a human when looking at the contents.

You can check python script 'data_serialization_formats.py'

### Process Text Files with Python Dictionaries and Upload to Running Web Service
In this project, you will write a Python script that uploads all the feedback stored in this folder to the company's website, without having to turn it into a dictionary one by one

## Sending Emails from Python
## Generating PDFs from Python

### Automatically Generate a PDF and send it by Email
You work for a company that sells second hand cars. Management wants to get a summary of the amounts of vehicles that have been sold at the end of every month. The company already has a web service which serves sales data at the end of every month but management wants an email to be sent out with an attached PDF so that data is more easily readable.

In this project, you will do:
- Write a script that summarizes and processes sales data into different categories
- enerate a PDF using Python
- Automatically send a PDF by email

### Automate updating catalog information
You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.

- Write a script that summarizes and processes sales data into different categories
- Generate a PDF using Python
- Automatically send a PDF by email
- Write a script to check the health status of the system
