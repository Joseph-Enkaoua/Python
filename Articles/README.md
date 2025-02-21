# 📑 Django Articles project

Welcome to my Django Articles project. This project focuses on mastering advanced functionalities in Django, including generic views, internationalization, and automated testing.

## 🐝 Key Takeaways

This project strengthened my ability to develop full-featured Django applications, optimize user interactions, and implement scalable architectures with automation, security, and internationalization in mind.

## 💪 What I Learned

Through a series of exercises, I gained hands-on experience with:

* Generic Views: Implementing a fully functional site using Django's built-in class-based views.

* User Authentication & Permissions: Managing users, login/logout, and access restrictions.

* Article Management System: Creating, displaying, and handling user-generated content efficiently.

* Favorite System: Allowing users to save and manage favorite articles.

* Bootstrap for UI Design: Enhancing the project’s interface with a consistent and responsive design.

* Internationalization (i18n): Implementing multi-language support based on URL prefixes.

* Automated Testing: Writing Django tests to verify functionality and security.




#### 📺 Demo
![Django data project gif](https://github.com/Joseph-Enkaoua/Python/blob/main/Articles/ScreenRecording.gif)


## 🚀 How to Clone and Run
To get started with this project, follow these steps:

1. Clone the repository
```
git clone https://github.com/Joseph-Enkaoua/Python.git
```

2. Go into the project repository
```
cd Python/Articles
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

You should now see the site available on http://127.0.0.1:8000

If you get the error ```ERROR: Failed building wheel for psycopg2-binary``` try to remove the version (```==2.9.10```) from the psycopg2-binary line in Data/requirements.txt file.

## 📜 License
This repository is open-source.
