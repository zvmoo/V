import os

# The root directory to scan
root_dir = "C:/Vialume"
output_file = os.path.join(root_dir, "vialume_file_structure.txt")

with open(output_file, "w", encoding="utf-8") as f:
    for foldername, subfolders, filenames in os.walk(root_dir):
        indent_level = foldername.replace(root_dir, "").count(os.sep)
        indent = "    " * indent_level
        f.write(f"{indent}[{os.path.basename(foldername)}]\n")
        for filename in filenames:
            f.write(f"{indent}    - {filename}\n")

print(f"📁 File structure saved to: {output_file}")
