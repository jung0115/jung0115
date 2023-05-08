import os
from os import path
import shutil

origin_readme_file_path = "../README.md"
save_readme_file_path = "../save/README.md"

# 폴더 없으면 생성
if not os.path.exists("../save"):
  os.makedirs("../save")

#readme = open(readme_file_path, "w")
#readme.write("# Test")
#readme.close()

# readme 내용 copy
shutil.copy(origin_readme_file_path, save_readme_file_path)
