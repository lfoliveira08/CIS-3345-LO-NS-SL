# CIS-3345-LO-NS-SL

💻 Digital Forensics Investigation: The Cyberbullying Case
📋 Case Objective
Our team is conducting a complete digital forensic investigation of a Windows 10 desktop computer belonging to a student, John Smith, who is suspected of cyberbullying. Using a provided forensic disk image, our objective is to forensically prove or disprove his involvement in the harassment of a fellow student, Jane Doe.

We will focus our analysis on recovering and analyzing chat logs , locating an embarrassing "meme" video , and examining user activity, including browser history and USB device connections, to determine if John Smith's computer was used to create, distribute, and send harassing content.

👥 Team
| Role | Name |
| :--- | :--- |
| **Lead Investigator** | Seth |
| **Scribe** | Nicholas |
| **Evidence Analyst** | Luis |

🔬 Investigation Plan: Key Objectives and User Stories
The investigation is organized into five key objectives, detailed below with corresponding user stories and investigative issues/tasks.

Chat Application Artifacts

Objective: Recover and analyze chat logs from Discord and Steam to find messages containing insults and threats directed at Jane Doe.


Video Artifacts

Objective: Locate and analyze the "meme" video file and its metadata to determine the video's creation, distribution, and origin.


Browser History & Downloads

Objective: Analyze browser history and download artifacts to identify visits to file-sharing websites and evidence of video upload/download.


USB Device History

Objective: Analyze the Windows Registry for USB device history to determine if the "meme" video was transferred to an external drive for distribution.

Overall Case Management

Objective: Create a detailed forensic timeline to correlate all recovered artifacts and produce a final, professional forensic report

Project Status Update

Milestone 1: Chat Application Artifacts
| User Story | Issue | Status | Assignee(s) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Discord Analysis** | **Locate and Extract Discord Data** | **Completed ✅** | Luis, Nicholas | Core Discord SQLite files were successfully extracted from the disk image and secured in the evidence folder. Cryptographic hashes have been calculated and documented in the Case Wiki to verify integrity. |
| **Discord Analysis** | Analyze Discord Databases | **In Progress** | Seth, Nicholas | Next up: Opening the extracted database files and running SQL queries to filter user messages by date and keywords. |
| **Steam Analysis** | Recover Steam Chat Logs | **Completed ✅** | Luis | Search the disk image for the \Steam\userdata\ directory, locate John Smith's specific user ID folder and identify the log files containing chat history. Copy the chat log files to the evidence directory. |
| **Steam Analysis** | Review Steam Logs for Keywords | **To Do** | Seth, Nicholas | |


Milestone 2: Video Artifacts 
| User Story | Issue | Statues | Assignee(s) | notes |
| :--- | :--- | :--- | :--- | :--- |
| **Locate Video File** | **Carve for Video File** | **Completed ✅** | Luis, Seth | Run file carving (e.g., Scalpel) on unallocated space using video signatures, then review results to identify the ""meme"" video. |
| **Locate Video File** | **Search by Hash** | **Completed ✅** | Luis | Obtain the SHA-256 hash from the complaint and run a hash-based search to quickly locate the specific file on the disk image. |
| **Video Metadata** | **Extract Video Metadata** | **To Do** | Luis, Nicholas, Seth | Run ExifTool against the recovered video, export metadata to a text file, and analyze creation, modification, and access timestamps. |
| **Video Metadata** | **Correlate Timestamps** | **To Do** | Nicholas, Seth | Update the master timeline with video timestamps and identify user activity (e.g., app usage) occurring immediately prior to creation. |
| **Video Editing Evidence** | **Analyze Prefetch Files** | **To Do** | Luis, Seth | Parse C:\Windows\Prefetch to identify execution counts and last run times for specific video editing applications. |
| **Video Editing Evidence** | **Examine UserAssist Key** | **To Do** | Luis, Nicholas | Mount NTUSER.DAT, decode UserAssist registry keys, and document run counts/dates for video editing software. |
