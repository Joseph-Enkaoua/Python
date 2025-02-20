# 👾 Django Session project

Welcome to my Django Session project. This project focuses on mastering user authentication, session management, and permissions in Django

## 💪 What I Learned

Through a series of exercises, I gained hands-on experience with:

* Anonymous Sessions: Implementing temporary usernames with expiration policies.

* User Authentication: Creating a registration and login system with session handling.

* User-Generated Content: Developing a Tip system with Django models and forms.

* Voting Mechanism: Implementing upvotes, downvotes, and ensuring integrity.

* Access Control & Permissions: Restricting actions based on user roles and reputation.

* Custom Permissions & Automated Privileges: Creating a dynamic authorization system based on user contributions.

* Django Admin & Custom User Model: Managing permissions efficiently and extending Django’s default user system.



#### 🎥 Demo
![Django sessions project gif](https://github.com/Joseph-Enkaoua/Python/blob/main/Sessions/ScreenRecording.gif)


## 🚀 How to Clone and Run
To get started with this project, follow these steps:

1. Clone the repository
```
git clone https://github.com/Joseph-Enkaoua/Python.git
```

2. Go into the project repository
```
cd Python/Sessions
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

If you get the error ```ERROR: Failed building wheel for psycopg2-binary``` try to remove the version (```==2.9.10```) from the psycopg2-binary line in Sessions/requirements.txt file.


## 📜 License
This repository is open-source.
