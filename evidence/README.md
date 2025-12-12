# 📂 Evidence Artifact Inventory

> **⚠️ WARNING:** Per strict forensic policy and GitHub file size limitations, **NO BINARY EVIDENCE FILES** are stored in this repository.
>
> This directory serves as a **Chain of Custody index**. All physical evidence files listed below are stored on the secure forensic workstation or the original Disk Image.

## 🗃️ Master Evidence List

### 1. Chat Logs (Discord & Steam)
| Evidence ID | File Name | Origin Path (Disk Image) | SHA-256 Hash | Status |
| :--- | :--- | :--- | :--- | :--- |
| **EV-01** | `messages.db` | `\Users\John Smith\AppData\Roaming\Discord\` | `[PASTE_HASH_HERE]` | 🔒 Secure |
| **EV-02** | `activity.log` | `\Users\John Smith\AppData\Roaming\Discord\` | `[PASTE_HASH_HERE]` | 🔒 Secure |
| **EV-03** | `steam_chat.txt` | `\Steam\userdata\[ID]\760\` | `[PASTE_HASH_HERE]` | 🔒 Secure |

### 2. Video Artifacts
| Evidence ID | File Name | Origin Path (Disk Image) | SHA-256 Hash | Status |
| :--- | :--- | :--- | :--- | :--- |
| **EV-04** | `meme_video.mp4` | `[Unallocated Space] (Carved)` | `[PASTE_HASH_HERE]` | 🔒 Secure |
| **EV-05** | `meme_metadata.txt` | *Generated via ExifTool* | `[See Wiki]` | 📄 Text |

### 3. System & Registry Hives
| Evidence ID | File Name | Origin Path (Disk Image) | SHA-256 Hash | Status |
| :--- | :--- | :--- | :--- | :--- |
| **EV-06** | `SYSTEM` Hive | `C:\Windows\System32\config\SYSTEM` | `[PASTE_HASH_HERE]` | 🔒 Secure |
| **EV-07** | `NTUSER.DAT` | `C:\Users\John Smith\NTUSER.DAT` | `[PASTE_HASH_HERE]` | 🔒 Secure |
| **EV-08** | `PREMIERE.pf` | `C:\Windows\Prefetch\` | `[PASTE_HASH_HERE]` | 🔒 Secure |

---

## 🔗 Access Instructions
To access the raw binary files for analysis, authorized investigators must:
1.  Mount the original **Forensic Disk Image (CIS-3345-CASE.E01)**.
2.  Navigate to the **Origin Path** listed above.
3.  Verify the file hash matches the value in this table before opening.

For detailed analysis and findings, please refer to the **[Project Wiki Evidence Log](../../wiki/Evidence-Log)**.
