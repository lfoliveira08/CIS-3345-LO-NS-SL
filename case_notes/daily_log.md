# 🛡️ Digital Forensics Case Journal
**Case Name:** The Cyberbullying Case
**Case Number:** CIS-3345-LO-NS-SL
**Subject:** John Smith
**Target OS:** Windows 10 Desktop

## 👥 Investigation Team
* **Lead Investigator:** Seth
* **Scribe:** Nicholas
* **Evidence Analyst:** Luis

---

## 📦 Chain of Custody Log
*Record every time evidence files are accessed, moved, or analyzed.*

| Date | Time | Evidence Item | Action Taken | Performed By |
| :--- | :--- | :--- | :--- | :--- |
| 2025-10-XX | 00:00 | Disk Image (DD/E01) | Acquired image from source | Seth |
| 2025-10-XX | 00:00 | messages.db | Extracted from AppData for analysis | Luis |
| | | | | |

---

## 🔎 Investigation Log & Task Status

### 1. Chat Application Artifacts (Discord & Steam)
**Objective:** Recover chat logs to identify insults/threats against Jane Doe.

#### **Discord Analysis**
- [ ] **Task 1:** Navigate to `C:\Users\John Smith\AppData\Roaming\Discord\`
- [ ] **Task 2:** Extract `messages.db` and other log files.
- [ ] **Task 3:** Create sub-directory in `/evidence/discord` and hash the files.
- [ ] **Task 4 (SQL):** Run query to filter by John Smith's User ID (Oct 2025).
- [ ] **Task 5 (SQL):** Run keyword search (Jane Doe, meme, etc.) and export CSV.
    * **Findings:** [Enter notes here - e.g., "Found 14 messages matching keywords..."]

#### **Steam Analysis**
- [ ] **Task 1:** Navigate to `\Steam\userdata\` and locate user ID folder.
- [ ] **Task 2:** Copy chat log files to `/evidence/steam`.
- [ ] **Task 3:** Run `steam_parser.py` or `grep` to search for keywords.
- [ ] **Task 4:** Screenshot incriminating text.
    * **Findings:** [Enter notes here]

---

### 2. Video Artifacts ("The Meme")
**Objective:** Locate the video file and prove creation/distribution.

#### **File Recovery**
- [ ] **Task 1:** Run `Scalpel` or `Foremost` on unallocated space (Carving).
- [ ] **Task 2:** Run Hash Search (SHA-256) if hash is provided.
    * **Findings:** [Enter notes here - e.g., "Recovered video_final.mp4 at sector..."]

#### **Metadata & Execution**
- [ ] **Task 1:** Run `ExifTool` on the recovered video. (Check Creation Date).
- [ ] **Task 2:** Check `C:\Windows\Prefetch` for video editing software (Premiere/DaVinci).
- [ ] **Task 3:** Check Registry `UserAssist` (ROT-13) for program run counts.
    * **Findings:** [Enter notes here]

---

### 3. Browser History & Downloads
**Objective:** Identify social media visits and upload evidence.

#### **History Analysis**
- [ ] **Task 1:** Parse Chrome/Firefox history files.
- [ ] **Task 2:** Filter for Social Media (Discord web, YouTube) and Cloud Storage.
- [ ] **Task 3:** Screenshot relevant URLs with timestamps.
    * **Findings:** [Enter notes here]

#### **Download/Cache Analysis**
- [ ] **Task 1:** Check Download History for the "meme" filename.
- [ ] **Task 2:** Check Browser Cache for video remnants.
    * **Findings:** [Enter notes here]

---

### 4. USB Device History
**Objective:** Determine if the video was distributed via external drive.

#### **Registry Analysis**
- [ ] **Task 1:** Extract `SYSTEM` hive -> Analyze `Enum\USBSTOR` (Device Serial Numbers).
- [ ] **Task 2:** Extract `NTUSER.DAT` -> Analyze `MountedDevices` (Volume GUIDs).
- [ ] **Task 3:** Correlate Serial Numbers to User Accounts.
    * **Findings:** [Enter notes here - e.g., "SanDisk Cruzer detected, inserted Oct 30..."]

---

### 5. Final Reporting
**Objective:** Timeline and Conclusion.

- [ ] **Task 1:** Aggregate all timestamps into Master Timeline (Excel).
- [ ] **Task 2:** Draft "Findings" section (Non-technical summary).
- [ ] **Task 3:** Draft "Conclusion" (Supported/Refuted).
- [ ] **Task 4:** Compile final PDF with Appendices.
