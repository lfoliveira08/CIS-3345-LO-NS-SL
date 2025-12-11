# Forensic Tools & Technologies
**Project:** The Cyberbullying Case (CIS-3345)
**Target System:** Windows 10 Desktop (John Smith)

## Team Roles
* **Lead Investigator:** Seth
* **Scribe:** Nicholas
* **Evidence Analyst:** Luis

---

## 1. Chat Application Analysis Tools
Tools used to extract, parse, and analyze communication logs from social platforms.

* **SQLite Database Browser (e.g., DB Browser for SQLite)**
    * **Usage:** Opening and querying `messages.db` and other SQLite files found in `\AppData\Roaming\Discord\`.
    * **Specific Task:** Exporting chat logs to CSV and filtering for specific User IDs and timestamps.
* **Text Editor (e.g., Notepad++, VS Code)**
    * **Usage:** Viewing raw log files and configuration files.
    * **Specific Task:** Parsing Steam chat logs found in `\Steam\userdata\` and performing keyword searches for "Jane Doe" or "meme".

## 2. File Recovery & Carving
Tools used to recover deleted data and analyze file integrity.

* **Scalpel or Foremost**
    * **Usage:** File carving on unallocated disk space.
    * **Specific Task:** Recovering deleted video files (.mp4, .mov) related to the "meme" video.
* **Hashing Utilities (e.g., CertUtil, QuickHash)**
    * **Usage:** Calculating and verifying cryptographic hashes (SHA-256).
    * **Specific Task:** Searching the disk image for a known hash of the specific "meme" video file provided in the complaint.

## 3. Metadata & Artifact Analysis
Tools used to examine file properties and program execution history.

* **ExifTool**
    * **Usage:** Reading, writing, and editing meta-information.
    * **Specific Task:** Extracting creation, modification, and device metadata from the recovered video file to determine origin.
* **Prefetch Parser (e.g., PECmd)**
    * **Usage:** Parsing Windows Prefetch (`.pf`) files.
    * **Specific Task:** Analyzing `C:\Windows\Prefetch` to prove execution of video editing software (Adobe Premiere, DaVinci Resolve).

## 4. Registry & Browser Forensics
Tools used to analyze system hives and web activity.

* **Registry Viewer / Analyzer (e.g., Registry Explorer)**
    * **Usage:** Parsing `NTUSER.DAT` and `SYSTEM` hives.
    * **Specific Task:**
        * Decoding ROT-13 data in the `UserAssist` key to view program execution history.
        * Analyzing `Enum\USBSTOR` and `MountedDevices` to track USB connections and serial numbers.
* **Browser History Capturer / Parser (e.g., BrowsingHistoryView)**
    * **Usage:** Extracting history from Chrome, Firefox, or Edge.
    * **Specific Task:** Recovering visited URLs (social media, file sharing) and analyzing download history/cache for video file remnants.

## 5. 🛠️ Custom Automation Scripts
* **Tools:** Python 3.x, Pandas, SQLite3

To enhance efficiency and simulate a realistic environment, the following custom scripts were developed by the team:

* **scripts/generate_evidence.py**
    * **Purpose:** Generates a mock messages.db Discord database populated with background noise and specific incriminating evidence timestamps.
    * **Usage:** python scripts/generate_evidence.py

* **notebooks/01_data_exploration.ipynb**
  * **Purpose:** The primary analysis dashboard. It ingests raw evidence databases, normalizes timestamps, filters for harassment keywords, and exports findings to CSV.


## 6. Reporting & Management
Tools used for timeline creation and final documentation.

* **Spreadsheet Software (Excel / Google Sheets)**
    * **Usage:** Data aggregation.
    * **Specific Task:** Creating the Master Forensic Timeline to correlate chat logs, file creation, and USB events.
* **Word Processor (Word / Google Docs)**
    * **Usage:** Documentation.
    * **Specific Task:** Drafting the final "Findings and Conclusions" report and Chain of Custody logs.
