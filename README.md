# Netflix Recommendation System

## Overview
This repository contains homework assignment for the "Introduction to Database Systems" course that involves creating a Database Management System (DBMS) hosted on AWS, with an accompanying application.
Netflix Recommendation System is designed to suggest movies and TV shows based on factors such as title, directors, cast, genres, and descriptions. The system is built using Python, Tkinter for the GUI, and PostgreSQL for the database hosted on AWS.

## Motivation
People often spend too much time deciding what to watch. This system aims to solve that problem by providing personalized recommendations based on a selected movie, helping users find content quickly.

## Application Description
The application uses a Tkinter GUI where users can input a movie title. The system then provides the top ten similar movie or show recommendations using cosine similarity. The data is sourced from Kaggle (Netflix Movies and TV Shows dataset).

## Data Sources and Import Methods
* Data Source: Kaggle (Netflix Movies and TV Shows)
* Import Methods: Data is imported from a CSV file into a **PostgreSQL database on AWS** using the **pgAdmin** tool. The data is updated manually.

## Database Schema
* The schema includes attributes like *id*, *type*, *title*, *release year*, *genres*, and *descriptions*.
* Constraints include non-null values for critical fields.

## Application Functions
* Recommendation System: Utilizes cosine similarity to find and rank similar movies.
* Libraries Used: `psycopg2` for database connection, `pandas` for data manipulation, and `sklearn` for the Count Vectorizer and similarity calculations.

## Integration
* Database and Application: The application relies heavily on the database for input and output operations.
* GUI: Implemented using Tkinter, the GUI allows users to input a movie title and view recommendations.

## Usage
* Run the Application: Execute the Python script to launch the Tkinter GUI.
* Input Movie Title: Enter the title of a movie or show.
* View Recommendations: The application displays the top ten similar movies or shows.

## Conclusion
This project includes database design, data collection,  data integration, database management, and application development to create a functional Netflix recommendation system. This project involves the usage of Python, PostgreSQL, and Tkinter, as well as applying machine learning techniques for recommendations.
