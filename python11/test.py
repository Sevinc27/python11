import os
import shutil

example_dir = 'Example'
os.makedirs(example_dir, exist_ok=True)

subdirect_dir = os.path.join(example_dir, 'subdirect')
os.makedirs(subdirect_dir, exist_ok=True)

picture_src = 'image.jpg'  
picture_dest = os.path.join(subdirect_dir, picture_src)
if os.path.exists(picture_src):
    shutil.copy(picture_src, picture_dest)
else:
    print(f"Şəkil faylı ({picture_src}) tapılmadı. Lütfən faylı cari qovluğa əlavə edin.")

text_file = os.path.join(subdirect_dir, 'example.txt')
with open(text_file, 'w') as file:
    file.write('Bu bir numune metn faylidir.')

for item in os.listdir(subdirect_dir):
    item_path = os.path.join(subdirect_dir, item)
    if os.path.isfile(item_path) and item_path.endswith('.txt'):
        shutil.move(item_path, example_dir)
        print(f"Mətn faylı {item} 'Example' qovluğuna köçürüldü.")