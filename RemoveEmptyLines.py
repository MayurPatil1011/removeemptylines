import os
import sys
# Get real folder of EXE
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))
exe_name = os.path.basename(sys.executable)
for filename in os.listdir(base_dir):
    if filename == exe_name:
        continue
    file_path = os.path.join(base_dir, filename)
    if not os.path.isfile(file_path):
        continue
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        # Remove ALL empty / whitespace-only lines
        cleaned = [line.rstrip() for line in lines if line.strip()]
        if cleaned:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n".join(cleaned))
        else:
            # File becomes empty
            open(file_path, "w").close()
    except:
        pass