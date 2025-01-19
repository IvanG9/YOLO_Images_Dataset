import os
import shutil

# Directorios originales
DATA_DIR = './data'  # Carpeta inicial con las subcarpetas 'train', 'validation', 'test'

# Directorios de destino
IMAGES_DIR = './data/images'
LABELS_DIR = './data/labels'

# Crear estructura final
for subset in ['train', 'validation', 'test']:
    os.makedirs(os.path.join(IMAGES_DIR, subset), exist_ok=True)
    os.makedirs(os.path.join(LABELS_DIR, subset), exist_ok=True)

# Reorganizar los archivos
for subset in ['train', 'validation', 'test']:
    # Directorios de origen
    imgs_src_dir = os.path.join(DATA_DIR, subset, 'imgs')
    anns_src_dir = os.path.join(DATA_DIR, subset, 'anns')

    # Directorios de destino
    imgs_dst_dir = os.path.join(IMAGES_DIR, subset)
    anns_dst_dir = os.path.join(LABELS_DIR, subset)

    # Mover imágenes
    if os.path.exists(imgs_src_dir):
        for img_file in os.listdir(imgs_src_dir):
            shutil.move(os.path.join(imgs_src_dir, img_file), os.path.join(imgs_dst_dir, img_file))

    # Mover anotaciones
    if os.path.exists(anns_src_dir):
        for ann_file in os.listdir(anns_src_dir):
            shutil.move(os.path.join(anns_src_dir, ann_file), os.path.join(anns_dst_dir, ann_file))

for subset in ['train', 'validation', 'test']:
    subset_dir = os.path.join(DATA_DIR, subset)
    if os.path.exists(subset_dir):
        shutil.rmtree(subset_dir)

print(f"Reorganización completada. Verifica las carpetas '{IMAGES_DIR}' y '{LABELS_DIR}'.")
