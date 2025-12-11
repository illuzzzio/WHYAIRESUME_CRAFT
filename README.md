

WHYAIRESUME is a simple and easy-to-use non AI resume builder created using Python. It leverages the ReportLab library to generate professional PDF resumes directly from user input. With this tool, you can create clean, ATS-friendly resumes in just a few clicks.

Features

Fill in your personal details, skills, experience, projects, education, and links.

Upload your profile photo to include in the resume.

Automatically formats sections and text to generate a professional-looking resume.

Optimized mode available to fit the resume into one page.

Supports highlighting project names and tech stack separately.

Generates resumes in PDF format for easy sharing.

Technology Used

Python – main programming language

ReportLab – for PDF generation (pip install reportlab)

Tkinter – for creating the graphical user interface (GUI)

Repo Structure

The repository contains a combination of Python, HTML, and TeX files, with Python being the main driver. HTML and TeX files are included mainly to support PyInstaller, which converts the Python script into a standalone .exe file.

resume.py – main Python application

dist/ – contains the generated .exe file, which can be run directly without installing Python

assets/ – optional folder for images, templates, or other resources

How to Run
Using Python

Clone the repository:

git clone <repo_name>


Navigate to the project directory:

cd <repo_name>


Install dependencies:

pip install reportlab


Run the application:

python resume.py

Using the Pre-built Executable

Navigate to the dist/ directory.

Run resume.exe (no Python installation required).

How It Works

Fill in the fields in the GUI including your name, email, phone, skills, projects, and education.

Upload a profile photo (optional).

Choose the “Optimize Resume Length” option if you want the resume to fit on a single page.

Click Generate PDF Resume – your resume is saved as a professional PDF file ready to share or print.
