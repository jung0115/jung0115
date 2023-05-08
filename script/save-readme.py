import os
import shutil
from datetime import datetime

# 복사본 저장할 폴더 경로
year_and_month = datetime.today().year + "." + datetime.today().month
day = datetime.today().year + "." + datetime.today().month + "." + datetime.today().day

save_root_folder_path = "../pastRecords"
save_month_folder_path = year_and_month
save_day_folder_path = day
save_folder_path = save_root_folder_path + "/" + save_month_folder_path + "/" + save_day_folder_path

# 폴더 없으면 생성
if not os.path.exists(save_root_folder_path):
  os.makedirs(save_root_folder_path)
if not os.path.exists(save_root_folder_path + "/" + save_month_folder_path):
  os.makedirs(save_root_folder_path + "/" + save_month_folder_path)
if not os.path.exists(save_folder_path):
  os.makedirs(save_folder_path)

# 원본 readme와 복사본 저장할 readme 경로
origin_readme_file_path = "../README.md"
save_readme_file_path = save_folder_path + "/README.md"

#readme = open(readme_file_path, "w")
#readme.write("# Test")
#readme.close()

# readme 내용 copy
shutil.copy(origin_readme_file_path, save_readme_file_path)
