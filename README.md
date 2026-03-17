# Nokia-3310-logic-simulation
A multi-level CLI navigation system built in Python 3.10+ simulating legacy mobile OS logic using structural pattern matching.
This project is a functional reconstruction of a hierarchical mobile menu system, designed to demonstrate nested control flow and efficient data routing. Using Python's modern match-case syntax, I mapped out 13 primary system modules (Phone Book, Messaging, Settings, etc.) and their respective sub-menus to create a seamless user navigation experience in a terminal environment.

Key Engineering Problems Solved:
Deep Nesting: Managed up to four levels of menu depth without losing logical integrity or causing recursion errors.
UI Clarity: Utilized multi-line strings and formatted output to ensure a clean, readable Command Line Interface (CLI).
Logic Efficiency: Replaced heavy if-elif chains with match-case for better performance and code readability.
