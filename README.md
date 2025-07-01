# Wiki Encyclopedia

A simple Wikipedia-like encyclopedia web application built with Django.


## Features

- View, search, and browse encyclopedia entries written in Markdown
- Create new entries
- Edit existing entries
- Random page navigation
- Markdown rendering for entry content

## Project Structure

- `encyclopedia/`: Django app containing views, templates, and utility functions
- `entries/`: Markdown files for each encyclopedia entry
- `wiki/`: Django project configuration

## Requirements

- Python 3.13.3
- Django==5.2.3
- markdown2==2.5.3

Install dependencies with:

```sh
pip install -r requirements.txt
```

## Running the Project

1. Navigate to the project directory:

    ```sh
    cd wiki
    ```

2. Run migrations (if needed):

    ```sh
    python manage.py migrate
    ```

3. Start the development server:

    ```sh
    python manage.py runserver
    ```

4. Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- Use the sidebar to search for entries, create new pages, or visit a random page.
- Click on an entry to view its content.
- Use the "Edit Page" link to modify an entry.

## License

This project is for educational purposes (Harvard CS50 Web Programming with Python and JavaScript).