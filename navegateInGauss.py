import os
from functools import lru_cache

ignore = []
htmlMaper = {} # "path":"file",
@lru_cache()
def findHtml(Path, *ignore):
	global htmlMaper
	for directory_file in os.listdir(Path):
		if os.path.isdir(Path + f"/{directory_file}"):
			findHtml(Path + f"/{directory_file}")
		elif directory_file.endswith(".html"):
			if f'{ignore[0]}' in directory_file or f'{ignore[1]}' in directory_file or f'{ignore[2]}' in directory_file:
				pass
			else:
				htmlMaper[directory_file] = Path

findHtml(".")
print(htmlMaper)
print(len(htmlMaper))
# paths = htmlMaper
# print(len(paths))

