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


## 🚀 How to Clone and Run
To get started with this project, follow these steps:

1. Clone the repository
```
git clone https://github.com/Joseph-Enkaoua/Python.git
```

2. Go into the project repository
```
cd Python/Data
```

3. Set up a virtual environment:
```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

4. Run the Make command which will apply the migrations and start the server:
```
make
```

You should now see the site available on http://127.0.0.1:8000/ex00/init/

If you get the error ```ERROR: Failed building wheel for psycopg2-binary``` try to remove the version (```==2.9.10```) from the psycopg2-binary line in Data/requirements.txt file.

## 📜 License
This repository is open-source.
