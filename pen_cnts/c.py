import os
for file_nm in os.listdir('./'):
    if os.stat(file_nm).st_size == 0:
        print(file_nm)
