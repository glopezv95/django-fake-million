# django-fake-million
A <a href="https://www.django-rest-framework.org/" target="_blank">Django REST Framework</a> **REST API** that contains data generated with the <a href="https://faker.readthedocs.io/en/master/" target="_blank">faker</a> library.

The API contains a **login endpoint** that checks if the user data in a **POST request** exists in the database and retrieves the users **token** if it does.

Once the **token** is retrieved, it can be used in **GET requests** to retrieve data from the database with the different endpoints configured in the API.