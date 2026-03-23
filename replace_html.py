import re

file_path = "index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Patrón para buscar img/XXXX.jpg o img/XXXX.jpeg o img/XXXX.png o ./img/XXXX...
# Excluyendo los enlaces externos obvios, aunque img/ ya asegura que sean locales.
pattern = r'(?P<prefix>img\/[^\"\']+)\.(?:jpg|jpeg|png|JPG|JPEG|PNG)'

def replace_ext(match):
    return match.group('prefix') + '.avif'

new_content = re.sub(pattern, replace_ext, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replaced all extensions in index.html to .avif")
