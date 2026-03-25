This is my personal portfolio project I worked on. It showcases my information, the skills I have, my education, and my contact info.

I made this using:

- HTML
- CSS
- DJANGO

## Features:

Simple Design: The website has a simple, not too flashy design for easier reading.
Responsive Icons: Users can click on the side icons to move towards a section 

## Technology Used:

- Python 3.14
- Django 6.x
- HTML5 / CSS3
- W3.CSS
- Font Awesome

## Setup Instructions:
1. Clone the repository:
```bash (on Pythonanywhere via the Console)
git clone <your-repo-url>
cd porfolioproject

2. On Bash, create a virtual environment:

python -m venv venv (second venv is the name, change if needed)
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies

'''bash
pip install Django

4. Apply Migrations:

'''bash
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser for managing content:

'''bash
python manage.py createsuperuser yourusername

6. Run development server:

'''bash
python manage.py runserver

