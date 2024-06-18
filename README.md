# Django To-Do List Application

A simple To-Do List application built with Django that allows users to add, view, mark as completed, and delete tasks. This project is a great introduction to Django and covers essential CRUD operations.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)

## Introduction

This To-Do List application is designed to help users manage their tasks efficiently. Users can add new tasks, view all tasks, mark tasks as completed or pending, and delete tasks. This project demonstrates the use of Django's MVC architecture, forms, and ORM.

## Technologies Used

- Python
- Django
- HTML and CSS for the frontend
- Conda for environment management

## Features

- Add new tasks
- View all tasks with their completion status
- Toggle task completion status
- Delete tasks

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/todo-list-django.git
   cd todo-list-django
   
2. **Create and activate conda environment:**
   ```bash
   conda create --name django_env python=3.9
   conda activate django_env

3. Install Django:

   ```bash
   conda install -c conda-forge django
   
4. Navigate to the project directory and run migrations:

   ```bash
   cd todoproject
   python manage.py makemigrations
   python manage.py migrate
   
5. Run the development server:

   ```bash
   python manage.py runserver
   
6. Access the application:
   Open your web browser and go to http://127.0.0.1:8000/ to see the To-Do List application in action.
