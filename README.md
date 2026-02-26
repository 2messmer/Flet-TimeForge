\# ⏰ TimeForge — From Console Logic to Modern UI with Flet



TimeForge is a learning project that demonstrates the evolution of a simple academic subject manager from a \*\*console-based Python program\*\* to a \*\*modern graphical interface using Flet\*\*.



This repository documents not only the final result, but the learning journey behind it.



---



\## 🎯 Project Vision



The goal of TimeForge is simple:



> Help students manage their subjects and weekly study hours in an organized way.



But beyond that, this project was used to progressively learn:



\* Python fundamentals

\* Program structure and modular thinking

\* Input validation

\* State management

\* UI development with Flet

\* Theme management (Dark/Light mode)

\* Dynamic interface updates



This repository reflects that progression.



---



\# 📚 Project Evolution



---



\## 🟢 1️⃣ Console Version — Core Logic First



File:



```

timeforge\_console.py

```



The project began as a terminal-based subject manager.



\### Features:



\* Add a subject

\* Search a subject

\* Delete a subject

\* Display all subjects

\* Calculate total weekly hours

\* Duplicate prevention

\* Input validation



\### What I Learned:



\* Structuring a program with functions

\* Separating logic from user interaction

\* Using dictionaries and lists

\* Preventing duplicate entries

\* Validating numeric input safely

\* Using `if \_\_name\_\_ == "\_\_main\_\_"`



This phase focused on \*\*logic before interface\*\*.



---



\## 🟡 2️⃣ Flet Welcome UI — First GUI Experience



File:



```

timeforge\_welcome\_ui.py

```



The second step was moving from console to graphical interface using \*\*Flet\*\*.



\### Features:



\* Text input fields

\* Status selection (Student / Professor)

\* Dynamic welcome message

\* Theme toggle (Dark/Light mode)

\* Reset button

\* Real-time UI updates



\### What I Learned:



\* Flet page configuration

\* Page state management

\* Updating UI dynamically

\* Handling button events

\* Using `page.update()`

\* Building layouts with `Column` and `Row`

\* Working with icons and styling



This phase introduced GUI concepts and reactive updates.



---



\## 🔵 3️⃣ Flet Subject Manager — Full Dynamic Interface



File:



```

timeforge\_subject\_manager.py

```



This is the most advanced version of the project.



It combines logic and UI into a dynamic application.



\### Features:



\* Add subjects with validation

\* Prevent duplicate subjects

\* Validate numeric input

\* Dynamic list generation

\* Delete button per subject

\* Automatic total hours calculation

\* Dark/Light theme toggle

\* UI rebuild on theme change

\* Error messaging system



\### Technical Improvements:



\* Separation of validation logic

\* Reusable UI generation functions

\* Dynamic event binding

\* Clean state updates

\* Structured layout hierarchy



\### What I Learned:



\* Managing UI state with lists

\* Dynamic widget rebuilding

\* Creating callback closures

\* Clean error handling in UI

\* User experience improvements

\* Designing a small but structured application



This version represents the transition from beginner-level UI experimentation to structured UI development.



---



\# 🧠 Design Philosophy



This project was intentionally built in stages:



1\. First understand the logic.

2\. Then build a simple interface.

3\. Then combine validation, logic, and UI into a cohesive system.



Each stage builds on the previous one.



---



\# 🛠 Technologies Used



\* Python 3

\* Flet (Python UI framework)

\* Basic state management

\* Functional programming concepts



---



\# 🚀 How to Run



\## Console Version



```bash

python timeforge\_console.py

```



\## Flet UI Versions



Make sure Flet is installed:



```bash

pip install flet

```



Then run:



```bash

python timeforge\_welcome\_ui.py

```



or



```bash

python timeforge\_subject\_manager.py

```



---



\# 📈 Learning Outcomes



Through this project I improved:



\* Code structure discipline

\* Input validation strategies

\* Separation of concerns

\* UI state management

\* Event-driven programming

\* Clean naming conventions

\* Project organization



This repository reflects a real progression from foundational Python to structured GUI application development.



---



\# 🔮 Future Improvements



Possible next steps:



\* Persistent storage (JSON or database)

\* Weekly schedule generation

\* Drag-and-drop UI

\* Charts for time visualization

\* Multi-page Flet application

\* User authentication

\* Export to PDF



---



\# 👨‍💻 Author



Built as part of a structured learning journey in Python and UI development.





