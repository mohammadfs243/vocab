import json
import re

with open("harry-potter-and-the-sorcerers-stone.txt") as file:
    document = file.read()

chapters = re.split("\|[A-Z]+\|", document)
index, *chapters = chapters
chapters_meta = re.findall("(.*) . (\d+)", index, re.MULTILINE)
for (chapter_index, _), meta in zip(enumerate(chapters), chapters_meta):
    name, start_page = meta
    chapters[chapter_index] = {
        "name": name,
        "start_page": start_page,
        "pages": [
            page.strip()
            for page in re.split("\n\d+\n", chapters[chapter_index])
            if page != ""
        ],
    }
    chapters[chapter_index]["length"] = len(chapters[chapter_index]["pages"])

with open("harry-potter-and-the-sorcerers-stone.json", "w") as file:
    json.dump(chapters, file, indent=2, ensure_ascii=False)
