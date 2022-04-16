# Deploy a Python (Django) web app to Azure App Service - Sample Application

This is the sample Django application for the Azure Quickstart [Deploy a Python (Django or Flask) web app to Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python).  For instructions on how to create the Azure resources and deploy the application to Azure, refer to the Quickstart article.

A Flask sample application is also available for the article at [https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart).

If you need an Azure account, you can [create one for free](https://azure.microsoft.com/en-us/free/).

Create a virtual environment for the app:
`python3.9 -m venv .venv`

`source .venv/bin/activate`

Install the dependencies:

`pip install -r requirements.txt`

Set environment variables to specify how to connect to a local PostgreSQL instance.

This sample application requires an .env file describing how to connect to your local PostgreSQL instance. Create an .env file using the .env.sample file as a guide. Set the value of DBNAME to the name of an existing database in your local PostgreSQL instance. This tutorial assumes the database name is restaurant. Set the values of DBHOST, DBUSER, and DBPASS as appropriate for your local PostgreSQL instance.