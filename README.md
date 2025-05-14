
# Wiki Encyclopedia

A simple Wikipedia-like online encyclopedia built with Django that allows users to create, edit, and view encyclopedia entries in Markdown format.  
The demo video:https://youtu.be/2QnT3tXxk6c

## Features

- **Entry Page**: View encyclopedia entries at `/wiki/TITLE`
- **Index Page**: Lists all available entries with clickable links
- **Search Functionality**: 
  - Direct match redirects to entry page
  - Partial matches show search results
- **New Page Creation**: Create new encyclopedia entries
- **Edit Existing Pages**: Modify content of existing entries
- **Random Page**: Redirects to a random encyclopedia entry
- **Markdown Support**: Converts Markdown content to HTML

## Technologies Used

### Backend
- Python 3
- Django web framework
- Markdown2 (for Markdown to HTML conversion)

### Frontend
- HTML5
- CSS3
- Bootstrap 5

## Installation and Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps

- Clone the repository:  
   
- Create and activate a virtual environment:
python -m venv venv  
-- On Windows:    
venv\Scripts\activate  
-- On macOS/Linux:    
source venv/bin/activate

- Install dependencies:  
pip install -r requirements.txt

- Run migrations:  
python manage.py migrate

- Create a superuser (optional for admin access):
python manage.py createsuperuser

- Run the development server:  
python manage.py runserver

- Access the application at:  
http://localhost:8000
   
