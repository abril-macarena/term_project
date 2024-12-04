# term_project
public repository used for OIM2640 final term project 

team member: Abril Manrique

## Final Conclusions
### The 'Why?'
This Automated Task Management Assistant is designed to help organize daily activities, set priorities, and get timely reminders. By combining basic scheduling with a simple and user-friendly interface, it ensures tasks are tracked efficiently without requiring complex tools.

Imagine a college student managing coursework, exercise routines, and personal tasks. This tool helps them:
*Add tasks like "Submit assignment" with due dates and categories.
*View all tasks sorted by urgency.
*Receive timely reminders according to the type of task and deadline
*Edit tasks if priorities or deadlines change.

### Usage
The only prerequisites to use this application is to make sure the repository is cloned and ensure that flask is intsalled. From there, the user is able to open any browser and navigate to http://127.0.0.1:5000/. The user will immediately be taken to the homepage where they are able to access options like adding tasks, viewing tasks, and reminders.

![image](https://github.com/user-attachments/assets/4c9381a3-ddb7-4dda-a24c-9e31f055d86e)

### Project Evaluation
When I first developed my idea for this project, my goal was to implement various features that would differentiate this application from others that were similar such as email notifications and a pioritization algorithm. As I fledged out my project proposal, I decided to switch my focus to making an application that would be fully functional and user-friendly, keeping the additional features as strecth goals which I did not achieve due to time constraints. 

The initial version of this project started out as writing out the functions I wanted to incorporate with pseudo-code and then going on from there. I was then able to make a draft in python using this code before adapting it to the flask software and implementing html files.

### Attribution
I referenced previous class work assignments and projects various times, especially when it came to adapting my python code draft to the final app file that incorporated flask as I had limited experience with the software. I found Gen-AI to be very helpful when first developing the initial functions in my draft file, as it was able to explain the errors in my code and I really wanted to refine these functions before moving forward as I knew they would serve as the scaffolding for the rest of my project. Additionally, I did use GEN-AI to generate the code in the base.html file as including that file allowed for there to be a navigation bar of sorts across all the web pages which enhances user experience, and it was not something I had coded previously.

## Project Proposal
### The Big Idea
This project would aim to create a python-based app that would serve as a task and reminder management assistant. This app will help the user organize and prioritize their tasks all while receiving reminders. The goal is to incorporate ‘smart prioritization’ and context-based reminders that will help make task management more adaptive to the user’s needs, providing a more beneficial experience than traditional reminder and task apps currently on the market.  

The minimum viable product is creating a basic app that allows the user to add tasks, set due dates, and specify the task type (e.g., work, personal, exercise). This app would be able to use context-aware reminders that will notify the user about upcoming tasks dependent on the time of day. 

The stretch goal for this app would be to add features such as recurring tasks or making it so that the user receives their reminder via email or even through push notification. The main stretch goal that I want to focus on is implementing ‘smart prioritization’ into the app where tasks will be ranked by urgency using an algorithm factoring due date and importance.  

### Learning Objectives
My goal is to further develop my understanding of the Python language. I hope to better my technical skills with flask as it will be necessary in developing a user-friendly interface for this app. Overall, I hope that this project will help me with my time management skills as I will have to develop my own schedule over the following month and must stick to it. 

### Implementation Plan
As of now, the initial plan is to implement the app using basic Python libraries (such as datetime for date handling and task scheduling). Also, I plan to utilize flask to develop the interface for the user to easily be able to carry out the actions on the app to the full extent. 

### Project Schedule
**Week 1:** Write out project in pseudo code and map out code structure by identifying key functions 

**Week 2:** Implement basic task management (adding tasks, setting due dates, and calculating urgency) 

**Week 3:** Implement and test optimization features (smart prioritization and context reminder features) 

**Week 4:** Build user interface 

**Week 5:** Revisions and stretch goals 

### Collaboration Plan
I am working on this project individually. 

### Risks and Limitations
I think the biggest risk is expanding the app to include a flask-based user interface as I have limited knowledge and experience with the framework. Additional risks include developing the project to meet the stretch goals. Overall, I plan on making sure that the MVP is fully functional before adding additional features. 

### Additional Course Content
I think that the best content for this project would just be on how to structure our project in terms of organization – how many files to create, how to break up the functions, and how to source them across different files. 
