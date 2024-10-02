FILE_PATH = "DATA/schwarma.txt"

try:
    file_in = None
    file_in = open(FILE_PATH)
except Exception as err:
    print(err)
# except (NotADirectoryError, FileNotFoundError) as err:
#     print(err)
# except PermissionError as err:
#     print(err)
else:  # if there were no errors
    contents = file_in.read()
finally:  # if there was an error or not
    if file_in:
        file_in.close()

print("ALL DONE")
