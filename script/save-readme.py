import os

readme_file_path = "../save/README.md"
if not os.path.exists("../save"):
  os.makedirs("../save")

readme = open(readme_file_path, "w")
readme.write("# Test")
readme.close()
