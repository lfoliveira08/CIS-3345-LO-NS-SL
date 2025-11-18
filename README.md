# CIS-3345-LO-NS-SL

💻 Digital Forensics Investigation: The Cyberbullying Case
📋 Case Objective

 Our team is conducting a complete digital forensic investigation of a Windows 10 desktop computer belonging to a student, John Smith, who is suspected of cyberbullying. Using a provided forensic disk image, our objective is to forensically prove or disprove his involvement in the harassment of a fellow student, Jane Doe.

We will focus our analysis on recovering and analyzing chat logs, locating an embarrassing "meme" video, and examining user activity, including browser history and USB device connections, to determine if John Smith's computer was used to create, distribute, and send harassing content.

👥 Team
Role              Name
Lead Investigator Seth 
Scribe            Nicholas 
Evidence Analyst  Luis 

🔬 Investigation Plan: Key Objectives and User Stories
The investigation is organized into five key objectives, detailed below with corresponding user stories and investigative issues/tasks.

1. Chat Application Artifacts

Objective: Recover and analyze chat logs from Discord and Steam to find messages containing insults and threats directed at Jane Doe.

User Story	Investigative Issues & Tasks

Discord Logs: Recover all chat logs from Discord to find messages containing insults and threats.



Issue 1: Locate and Extract Discord Data : 



- Navigate to C:\Users\John Smith\AppData\Roaming\Discord\. 


- Copy core SQLite database files (.db files). 


- Document file paths and cryptographic hashes in the GitHub Wiki. 



Issue 2: Analyze Discord Databases : 



- Use a SQLite browser to query and export messages to/from John Smith's user ID. 



- Filter results by the specified date range (early to late October 2025) and keywords (insults, threats, Jane Doe's name). 


- Export final filtered results as a .csv file.



Steam Logs: Recover chat logs from Steam to identify communications related to harassment.



Issue 1: Recover Steam Chat Logs : 



- Search for \Steam\userdata\ directory. 


- Locate John Smith's specific user ID folder and copy chat log files. 



Issue 2: Review Steam Logs for Keywords : 



- Open and use a "find" function to search for relevant keywords from the complaint.
