# Working with ZIP files in Python
import zipfile


# TODO: Create a new ZIP archive
# zfile = zipfile.ZipFile("archive.zip","w")
# zfile.write("file1.txt")
# zfile.write("file2.txt")
# zfile.write("file3.txt")
# zfile.close()

# TODO: Check validity of the file
# print(zipfile.is_zipfile("archive.zip"))

# TODO: Read the properties of a ZIP archive
zfile = zipfile.ZipFile("archive.zip","r")
print(zfile.namelist())
print(zfile.infolist)

# TODO: Read the properties of ZIP contents


# TODO: Extract ZIP file contents
# zfile.extract("file2.txt")
# zfile.extractall()


# TODO: Ensure that the file is closed
