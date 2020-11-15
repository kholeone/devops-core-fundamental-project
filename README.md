# Lucky Duck App

## Resources 
- Trello Board: https://trello.com/b/9r3rbJG2/lucky-duck-app

## Contents

### Brief
To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

#### Additional Requirements
- A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.

- A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it.

- Clear Documentation from a design phase describing the architecture
used for the project as well as a detailed Risk Assessment.

- A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
the Kanban Board

- Fully designed test suites for the application, as
well as automated tests for validation of the application. 
Providing high test coverage in the backend and provide consistent
reports and evidence to support a TDD approach.

- A functioning front-end website and integrated API's, using Flask.

- Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

#### My Approach
The approach that was chosen was to make an application that is like an online classified advertisement.
It will be a simple design of just allowing the creating of listings that can be read by other users.
This can be in a form of a service, or an item that is for sale. Updates can be applied to the listing 
to allow adjustment, along with the deletion of a listing.Everything in the additional requirements have been 
taken in consideration when having a approach to this project.

### Architecture
Here is an entity relationship diagram (ERD) that shows the construction of the database 
which has gone through many iterations to provide the most realistic and logical implementation in the app.

## Database Structure
Here is a Entity relationship diagram (ERD). This is the final database structure chosen to build with the application.
It is able to store all the information in the database, able to create, read, update and delete everything associated database.

![alt text](https://github.com/kholeone/devops-core-fundamental-project-/blob/main/Documents/erd_ver_1.0.png)

## CI Pipeline

### Project Tracking 
This is the Trello board used throughout the duration of the project. Utilising it to help track the development of the project. This has been 
very helpful as it displays what needs to be done and what has been completed, focusing on the areas of the projects that need requires attention the most.
![alt text](https://github.com/kholeone/devops-core-fundamental-project-/blob/main/Documents/Screenshot%202020-11-15%20025715.png)

Here is a link to my Trello board, that was used to track the progress of the project:
https://trello.com/b/9r3rbJG2/lucky-duck-app


### Risk Assessment
The Risk Assessment was done to prepare, anticipate and deliver the reliefs of potential threats that can occur with the project.
![alt text](https://github.com/kholeone/devops-core-fundamental-project-/blob/main/Documents/risk_assessment_snippet.png "risk assessment")
Risk Assessment link: 
https://drive.google.com/file/d/18dbeBYOijlBn2jIVVrRpjJASh52iZTPC/view?usp=sharing

### Testing 
Testing has been done with Pytest, used in Python in a form of Unit Testing.
This is to analyse and detect differences in existing and required conditions, and to evaluate the features of the application.

![alt text](https://github.com/kholeone/devops-core-fundamental-project-/blob/main/Documents/Screenshot%202020-11-15%20223302.png "unit testing")

81% was achieved in the Unit Testing. There are areas of improvement in the testing which lies in the '**applications.routes.py**', but as it stands
it was not huge of an issue to have the application fail as it is still functional.


### Front-End Design
The front-end design is relatively simple, it features the basics of text boxes, hyperlinks,
drop down menus, buttons and also a layout that provides ease of navigation.
The focus of this area was not primary as the focus was directed to the back-end development of the application. 
However a little effort was made to make it seem usable when interacted with and give an idea to the user what the design is asking them to do.


### Known Issues
- An issue with updating the details of a listing
- When updating text, additional characters are present
- Adding a detail when it has already been done will cause an issue



### Future Improvements
There are many improvements that can be made to the application
assuming having less time constraints and broadening of knowledge.
Improvements such as:

- Having a login for sellers that want to create a listing.
- Allow pictures to be uploaded to display the product.
- Have a messaging system where users can publically or privately message each other in regards of the listing.
- Have a stylistic front-end design to make the application more appealing
- Produce an application that was close to the original concept 
- To have an application with minimal bugs

### Authors
Kholeo Taylor 
