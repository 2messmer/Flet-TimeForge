📘 README — Flet-TimeForge

Copie tout ce qui suit dans ton README.md :

⏰ TimeForge — From Console Logic to Modern UI with Flet

TimeForge is a learning project that demonstrates the evolution of a simple academic subject manager from a console-based Python program to a modern graphical interface using Flet.

This repository documents not only the final result, but the learning journey behind it.

🎯 Project Vision

The goal of TimeForge is simple:

Help students manage their subjects and weekly study hours in an organized way.

But beyond that, this project was used to progressively learn:

Python fundamentals
Program structure and modular thinking
Input validation
State management
UI development with Flet
Theme management (Dark/Light mode)
Dynamic interface updates

This repository reflects that progression.

📚 Project Evolution
🟢 1️⃣ Console Version — Core Logic First

File:

timeforge_console.py

The project began as a terminal-based subject manager.

Features:
Add a subject
Search a subject
Delete a subject
Display all subjects
Calculate total weekly hours
Duplicate prevention
Input validation
What I Learned:
Structuring a program with functions
Separating logic from user interaction
Using dictionaries and lists
Preventing duplicate entries
Validating numeric input safely
Using if **name** == "**main**"

This phase focused on logic before interface.

🟡 2️⃣ Flet Welcome UI — First GUI Experience

File:

timeforge_welcome_ui.py

The second step was moving from console to graphical interface using Flet.

Features:
Text input fields
Status selection (Student / Professor)
Dynamic welcome message
Theme toggle (Dark/Light mode)
Reset button
Real-time UI updates
What I Learned:
Flet page configuration
Page state management
Updating UI dynamically
Handling button events
Using page.update()
Building layouts with Column and Row
Working with icons and styling

This phase introduced GUI concepts and reactive updates.

🔵 3️⃣ Flet Subject Manager — Full Dynamic Interface

File:

timeforge_subject_manager.py

This is the most advanced version of the project.

It combines logic and UI into a dynamic application.

Features:
Add subjects with validation
Prevent duplicate subjects
Validate numeric input
Dynamic list generation
Delete button per subject
Automatic total hours calculation
Dark/Light theme toggle
UI rebuild on theme change
Error messaging system
Technical Improvements:
Separation of validation logic
Reusable UI generation functions
Dynamic event binding
Clean state updates
Structured layout hierarchy
What I Learned:
Managing UI state with lists
Dynamic widget rebuilding
Creating callback closures
Clean error handling in UI
User experience improvements
Designing a small but structured application

This version represents the transition from beginner-level UI experimentation to structured UI development.

🧠 Design Philosophy

This project was intentionally built in stages:

First understand the logic.
Then build a simple interface.
Then combine validation, logic, and UI into a cohesive system.

Each stage builds on the previous one.

🛠 Technologies Used
Python 3
Flet (Python UI framework)
Basic state management
Functional programming concepts
🚀 How to Run
Console Version
python timeforge_console.py
Flet UI Versions

Make sure Flet is installed:

pip install flet

Then run:

python timeforge_welcome_ui.py

or

python timeforge_subject_manager.py
📈 Learning Outcomes

Through this project I improved:

Code structure discipline
Input validation strategies
Separation of concerns
UI state management
Event-driven programming
Clean naming conventions
Project organization

This repository reflects a real progression from foundational Python to structured GUI application development.

🔮 Future Improvements

Possible next steps:

Persistent storage (JSON or database)
Weekly schedule generation
Drag-and-drop UI
Charts for time visualization
Multi-page Flet application
User authentication
Export to PDF
👨‍💻 Author : Demessmer NGUEDJIO

Built as part of a structured learning journey in Python and UI development.

Puis ajoute une section comme celle-ci après les autres projets Flet.

🔎 Dynamic Fruit Search (Flet Mini-App)

File:

fruit_search_ui.py

This small interface demonstrates dynamic filtering in a Flet application.

Features
Live text search
Dynamic list update
Reactive UI behavior
Simple state management
What this exercise demonstrates

This mini-app was created while learning how to handle dynamic UI updates in Flet.

The interface contains a search field and a list of fruits.
Each time the user types something, the list automatically updates to show only matching items.

This exercise helped practice:

Handling on_change events
Updating UI components dynamically
Managing shared state inside a Flet application
Building simple reactive interfaces
Run the example
python fruit_search_ui.py

## 🗓️ Time Slots Manager (Flet Mini-App)

File:
`timeforge_time_slots.py`

This mini-application allows a student to define and manage available study time slots during the week.

### Features

- Day selection
- Start and end time selection
- Validation of complete input
- Duplicate prevention
- Dynamic list display
- Deletion of existing time slots

### What this exercise demonstrates

This project helped practice:

- working with Dropdown components in Flet
- validating structured input
- managing shared state
- dynamically updating UI components
- generating reusable interface elements

## 📊 TimeForge Planner Pro

File:
`timeforge_planner_pro.py`

A larger Flet application designed as a planning dashboard for students.

### Features

- subject management
- free time slot management
- weekly planner view
- navigation with `NavigationRail`
- dashboard cards with summary statistics
- light/dark theme toggle

### What this project demonstrates

This project helped me practice:

- multi-section app structure in Flet
- shared state management
- dynamic UI updates
- navigation between different sections
- building a more complete and presentable application
