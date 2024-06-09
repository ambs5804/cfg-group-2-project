# Project Name 

## Description

This project is a food website that aims to provide users with the ability to find recipes based on what they have in the house.

## Features
Home
- intro to what's available
- unit converter page
- recipe search based on ingredients a user has
- recipe interaction annd link to external web link of original recipe source
- unit converstion on recipes a user links

## Installation

1. Clone the repository.
2. Install the required dependencies using `requirments.txt`
3. Set up the database and configure the connection in `config.py`.
  - Host = 'localhost'
  - User  = **this should be the name of your mysql workbench profile**
  - Password = **this should be your mysql workbench profile password**
4. Create an account with [https://www.edamam.com/] for required `API_ID` and `API_KEY` in config.py
4. Run the `routes.py` file to being the development server.

## Usage

Click through available tabs at the top
1. Choose some ingredients and find some recipes that contain them for some inspiration
  - based on a limited database, only 1 ingredient to be inputted at a time (e.g. Milk)

2. Find an ingredient substitution
  - takes string input inthe format (Onions,chicken,olives .. etc)

3. Convert a unit
  - this function takes float values

4. ~~Look at saved items~~ - save feature not yet finished

