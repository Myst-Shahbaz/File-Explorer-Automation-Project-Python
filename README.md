⚙️ Automated File Organizer

A simple yet powerful Python script that automatically organizes your messy folders into clean, well-structured categories 📂✨.
It scans all files, creates folders by file type, and moves everything where it belongs — all in one click!

🚀 How It Works

1️⃣ Set your target folder path inside the script.
2️⃣ Scan all files in that folder automatically.
3️⃣ Create folders for each file type (if they don’t exist).
4️⃣ Move files to their respective folders based on their extensions.
5️⃣ Print the final organized folder structure in the console.

🗂️ File Type Categories

By default, the script organizes files into the following groups:

📸 Images — .png, .jpg, .jpeg, .gif
📊 Excel Files — .xls, .xlsx, .csv
📄 Text Files — .txt
📕 PDF Files — .pdf
📝 Documents — .doc, .docx
🎬 Videos — .mp4, .mov, .avi

💡 You can easily add more file types by editing the file_types dictionary.

💻 How to Use

1️⃣ Copy the script into a new file, e.g., auto_file_sorter.py
2️⃣ Update the path variable with your target folder path
3️⃣ Run the script in your terminal or VS Code

🧰 Requirements

1️⃣ No external libraries needed!
2️⃣ This script uses only built-in Python modules:

– os
– shutil
