# django-fake-million
A `django` **REST API** that contains data generated with the `faker` library.

The API contains a **login endpoint** that checks if the user data in a **POST request** exists in the database and retrieves the users **token** if it does.

Once the **token** is retrieved, it can be used in **GET requests** to retrieve data from the database with the different endpoints configured in the API.