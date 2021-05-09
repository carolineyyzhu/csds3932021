# csds3932021
The Computer Science program of study builder (CSPOSB) allows users to explore the graduation requirements for both a BS and a BA in computer science at Case Western Reserve University. 
The website is composed of three parts: general degree information, schedule builder and requirements checker. The general information explains the requirements for each degree and is static.
The schedule builder allows for users to plan out their course of study by selecting classes for each semester and displays the created four year plan. This feature also certifies that the entered
schedule fulfills graduation requirements. The final feature allows for a student to check which degree requirements they do not meet and suggests classes to fufill that requirement.

All of the code needed to run the CSPOSB project is found in the /CSPOSB/ directory.
In the /CSPOSB/ directory, the /CSB/ directory contains the python code that runs the application.
In this directory the 'urls.py' file defines the urls used for the project, the 'models.py' file defines the sqlite database used for the project, and the 'views.py' file interfaces with the database and determines what page to show and with what information.
The files used for testing are found in /csds3932021/CSPOSB/CSPOSB/tests/. The test are in both pythons standard unittesting library and the Django testing library. The unittesting library tests the requirement checking function while the Django testing tests the models and individual website pages. These tests have a code coverage of 58%.
/csds3932021/CSPOSB/templates/ contains all of our html files used in the application.
The css style sheet can be found in /csds3932021/CSPOSB/static/css/.
The database file is found in /csds3932021/CSPOSB/ as the 'db.sqlite3' file, but for aa better experience using the database use the admin page.
The 'manage.py' file in /csds3932021/CSPOSB/ is the file used to launch to the application

To deploy a local instance of the CSPOSB applicaation navigate to the /csds3932021/CSPOSB/ directory via the command line.
Once in the correct directory run the 'manage.py' file by typing either 'python3 manage.py runserver' or 'python manage.py runserver'
Once this line has been executed open a web browser and navigate to 127.0.0.1:8000 to use the CSPOSB.

To access the admin page run the application as normaal and navigate to 127.0.0.1:8000/admin
Login in useing the provided credentials:
	Username: Professor
	Password: Go-Spartans

Best,
CSDS 393 Group 1
