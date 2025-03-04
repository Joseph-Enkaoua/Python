# 📀 Django Data project

Welcome to my Django Data project. The project focuses on mastering data management in Django using both Django's ORM and raw SQL with the Psycopg2 library.

## 📌 What I Learned

Through a series of exercises, I gained hands-on experience with:

* Database Management in Django: Creating and structuring databases using Django Models and raw SQL queries.

* Django ORM: Defining models, querying data efficiently, and managing relationships between tables.

* Raw SQL with Psycopg2: Executing SQL commands directly within Django to manipulate databases.

* CRUD Operations: Implementing create, read, update, and delete functionality for structured datasets.

* Form Handling & User Interaction: Creating interactive views that allow users to modify and interact with database records.

* Foreign Keys & Many-to-Many Relationships: Managing complex relationships between entities using Django's ORM.

* Data Validation & Error Handling: Ensuring database integrity and handling errors effectively.


#### 🎥 Demo

![Django data project gif](https://github.com/Joseph-Enkaoua/Python/blob/main/Data/ScreenRecording.gif)

## 💾 Exercise List

#### Exercise 00: SQL - Creating a Table

* URL: http://127.0.0.1:8000/ex00/init
* Creates a table named ex00_movies in PostgreSQL using psycopg2.

#### Exercise 01: ORM - Creating a Table

* Uses Django models to create a Movies model.

#### Exercise 02: SQL - Inserting and Displaying Data

* URL: http://127.0.0.1:8000/ex02/init - Creates ex02_movies table.
* URL: http://127.0.0.1:8000/ex02/populate - Inserts predefined movie data.
* URL: http://127.0.0.1:8000/ex02/display - Displays all data in ex02_movies.

#### Exercise 03: ORM - Inserting and Displaying Data

* URL: http://127.0.0.1:8000/ex03/populate - Inserts data using Django ORM.
* URL: http://127.0.0.1:8000/ex03/display - Displays all data from Movies.

#### Exercise 04: SQL - Deleting Data

* URL: http://127.0.0.1:8000/ex04/init - Creates ex04_movies table.
* URL: http://127.0.0.1:8000/ex04/populate - Inserts movie data.

* URL: http://127.0.0.1:8000/ex04/display - Displays all data.
* URL: http://127.0.0.1:8000/ex04/remove - Allows removal of entries via dropdown.

#### Exercise 05: ORM - Deleting Data

* URL: http://127.0.0.1:8000/ex05/populate - Inserts data into the ORM-based Movies model.
* URL: http://127.0.0.1:8000/ex05/display - Displays all data.
* URL: http://127.0.0.1:8000/ex05/remove - Provides a dropdown to delete movies.

#### Exercise 06: SQL - Updating Data

* URL: http://127.0.0.1:8000/ex06/init - Creates ex06_movies table with created and updated timestamps.
* URL: http://127.0.0.1:8000/ex06/populate - Inserts data.
* URL: http://127.0.0.1:8000/ex06/display - Displays data.
* URL: http://127.0.0.1:8000/ex06/update - Updates opening_crawl field.

#### Exercise 07: ORM - Updating Data

* URL: http://127.0.0.1:8000/ex07/populate - Inserts data.
* URL: http://127.0.0.1:8000/ex07/display - Displays data.
* URL: http://127.0.0.1:8000/ex07/update - Updates opening_crawl.

#### Exercise 08: SQL - Foreign Key Relations

* URL: http://127.0.0.1:8000/ex08/init - Creates ex08_planets and ex08_people tables.
* URL: http://127.0.0.1:8000/ex08/populate - Populates tables from CSV files.
* URL: http://127.0.0.1:8000/ex08/display - Displays characters and homeworlds.

#### Exercise 09: ORM - Foreign Key Relations

* URL: http://127.0.0.1:8000/ex09/display - Displays characters, their homeworlds, and climates.
* Populates data using ex09_initial_data.json.

#### Exercise 10: ORM - Many-to-Many Relationships

* URL: http://127.0.0.1:8000/ex10 - Displays a form to filter characters based on movie release date, planet size, and gender.

## 🚀 How to Clone and Run

To get started with this project, follow these steps:

1. Clone the repository
```
git clone https://github.com/Joseph-Enkaoua/Python.git
cd Python/Data
```

2. Set up a virtual environment:
```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Run the Make command which will apply the migrations and start the server:
```
make
```

## 📜 License

This repository is open-source.
