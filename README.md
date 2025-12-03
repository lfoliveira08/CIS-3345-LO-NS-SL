# CIS-3345-LO-NS-SL: Digital Forensics Investigation

## 💻 Project Description: The Cyberbullying Case

Our team is conducting a complete digital forensic investigation of a **Windows 10 desktop computer** belonging to a student, **John Smith**, who is suspected of cyberbullying. Using a provided forensic disk image, our objective is to forensically prove or disprove his involvement in the harassment of a fellow student, **Jane Doe**.

We will focus our analysis on recovering and analyzing chat logs, locating an embarrassing "meme" video, and examining user activity, including browser history and USB device connections, to determine if John Smith's computer was used to create, distribute, and send harassing content.

---

## 👥 Team

| Role | Name |
| :--- | :--- |
| **Lead Investigator** | Seth |
| **Scribe** | Nicholas |
| **Evidence Analyst** | Luis |

---

## 📊 Current Project Status

The repository is actively tracking tasks across all five investigation phases.

| Metric | Status | Details |
| :--- | :--- | :--- |
| **Total Issues Tracked** | **58** | **41 Open** and **17 Closed**. The full list of issues can be reviewed on the [Issues Tab](https://github.com/lfoliveira08/CIS-3345-LO-NS-SL/issues). |
| **Key Tasks Completed** | **4** | Locate and Extract Discord Data, Recover Steam Chat Logs, Carve for Video File, Search for Video File by Hash|
| **Key Tasks In Progress** | **6** | Analyze Discord Databases, Review Steam Logs for Keywords, Extract Video Metadata, Correlate Video Timestamps, Analyze Prefetch Files,Examine UserAssist Registry Key |
| **Key Tasks To Do** | **10** | This includes the remaining tasks across all Milestones (M1, M2, M3, M4, M5). |

---

## 🔬 Investigation Plan: Key Objectives and Progress

The investigation is organized into five **Milestones**, with detailed status updates for each task.

### Objective 1: Chat Application Artifacts (Milestone 1)

**Goal:** Recover and analyze chat logs from Discord and Steam to find messages containing insults and threats directed at Jane Doe.

| User Story | Issue | Status | Assignee(s) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Discord Analysis** | **Locate and Extract Discord Data** | **Completed ✅** | Luis, Nicholas | Tasks include navigating to the Discord directory, identifying/copying core SQLite database files, creating an evidence directory, and documenting file paths and cryptographic hashes. |
| **Discord Analysis** | **Analyze Discord Databases** | **In Progress** | Seth, Nicholas | Tasks include opening database files with a SQLite browser, running SQL queries to retrieve John Smith's messages, filtering by date (Oct 2025) and keywords, and exporting the final results as a `.csv` file. |
| **Steam Analysis** | **Recover Steam Chat Logs** | **Completed ✅** | Luis | Tasks include searching for the `\Steam\userdata\` directory, locating John Smith's specific user ID folder, and copying the chat log files to the evidence directory. |
| **Steam Analysis** | **Review Steam Logs for Keywords** | **In Progress** | Seth, Nicholas | Tasks include opening recovered chat logs with a text editor, searching for relevant keywords from the complaint, and taking screenshots of any incriminating conversations found. |

### Objective 2: Video Artifacts (Milestone 2)

**Goal:** Locate and analyze the "meme" video file and its metadata so that its creation, distribution, and origin can be determined.

| User Story | Issue | Status | Assignee(s) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Locate Video File** | **Carve for Video File** | **Completed ✅** | Luis, Seth | Tasks include running a file carving tool (Scalpel) on unallocated space, configuring it to search for video signatures, and reviewing the carved files to identify the video. |
| **Locate Video File** | **Search for Video File by Hash** | **Completed ✅** | Luis | Tasks include obtaining the cryptographic hash (e.g., SHA-256) from the complaint and running a hash-based search to quickly locate the video file. |
| **Video Metadata** | **Extract Video Metadata** | **In Progress** | Luis, Nicholas, Seth | Tasks include running ExifTool against the recovered video, exporting the metadata output, and examining creation, modification, and access timestamps. |
| **Video Metadata** | **Correlate Video Timestamps** | **In Progress** | Nicholas, Seth | Tasks include adding the video file's timestamps to the master timeline spreadsheet and looking for user activity that occurred just before the video's creation. |
| **Video Editing Software** | **Analyze Prefetch Files** | **In Progress** | Luis, Seth | Tasks include navigating to the `C:\Windows\Prefetch` directory, using a parser to examine files, and searching for prefetch files related to video editing applications. |
| **Video Editing Software** | **Examine UserAssist Registry Key** | **In Progress** | Luis, Nicholas | Tasks include mounting the `NTUSER.DAT` hive, navigating to the UserAssist key, decoding the key data, and documenting programs, run counts, and execution dates. |

### Objective 3: Browser History & Downloads (Milestone 3)

**Goal:** Analyze browser history and download artifacts to identify visits to websites used for sharing the video or other social media platforms.

| User Story | Issue | Status | Assignee(s) | Notes/Description |
| :--- | :--- | :--- | :--- | :--- |
| **Browser History Analysis** | **Recover Browser History** | **To Do** | Luis | Navigate to the browser's data directory for Chrome, Firefox, or Edge, and use a forensic parser to extract the history into a readable format. |
| **Browser History Analysis** | **Filter History for Relevant Sites** | **To Do** | Seth, Nicholas | Review the parsed history for visits to social media, video-sharing, or file-upload sites and take screenshots of any relevant URLs and timestamps. |
| **Download Artifacts** | **Analyze Download History** | **To Do** | Luis, Seth | Use a forensic tool to parse the browser's download history and search for entries related to the "meme" video file. |
| **Download Artifacts** | **Investigate Browser Cache** | **To Do** | Luis, Seth | Analyze the browser cache directory for remnants of the video file itself or cached web pages related to video uploads or streaming. |

### Objective 4: USB Device History (Milestone 4)

**Goal:** Analyze the Windows Registry for USB device history so that it can be determined if the 'meme' video was transferred to an external drive for distribution.

| User Story | Issue | Status | Assignee(s) | Notes/Description |
| :--- | :--- | :--- | :--- | :--- |
| **USB Registry Analysis** | **Extract and Analyze SYSTEM Registry Hive** | **To Do** | Luis | Extract the SYSTEM hive, open it with a registry viewer, navigate to `SYSTEM\CurrentControlSet\Enum\USBSTOR`, and document all connected USB devices. |
| **USB Registry Analysis** | **Extract and Analyze NTUSER.DAT Registry Hive** | **To Do** | Luis | Extract the `NTUSER.DAT` hive, identify and document volume GUIDs from the `MountedDevices` key, and correlate these entries with the USBSTOR documentation. |

### Objective 5: Overall Case Management (Milestone 5)

**Goal:** Create a detailed forensic timeline to correlate all recovered artifacts and produce a final, professional forensic report.

| User Story | Issue | Status | Assignee(s) | Notes/Description |
| :--- | :--- | :--- | :--- | :--- |
| **Timeline Creation** | **Aggregate All Timestamps** | **To Do** | Nicholas | Create a master spreadsheet and manually enter data from all previous analysis steps, including timestamp, artifact type, source, and description. |
| **Timeline Creation** | **Build a Narrative Timeline** | **To Do** | Nicholas, Seth | Sort the aggregated data chronologically and write a narrative that connects the events on the timeline to the allegations in the complaint. |
| **Final Report** | **Draft the Findings and Conclusions** | **To Do** | Seth | Write a draft of the "Findings" section (describing the evidence found) and the "Conclusion" section (stating whether the evidence supports or disproves the allegations). |
| **Final Report** | **Prepare the Final Report with Appendices** | **To Do** | Nicholas | Tasks include adding a table of contents, including all supporting evidence in an appendix, performing a final spell check, and saving the final report as a PDF. |

---

## 📜 License

This project is licensed under the [MIT License](/lfoliveira08/CIS-3345-LO-NS-SL/blob/main/LICENSE).
