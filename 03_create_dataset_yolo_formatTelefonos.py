import os
import shutil

# Rutas principales
DATA_ALL_DIR = './data_all'  # Carpeta con todas las imágenes originales
DATA_OUT_DIR = './data'  # Carpeta donde se guardará el conjunto de datos YOLO

# Crear carpetas de salida
for set_ in ['train', 'validation', 'test']:
    for dir_ in [os.path.join(DATA_OUT_DIR, set_),
                 os.path.join(DATA_OUT_DIR, set_, 'imgs'),
                 os.path.join(DATA_OUT_DIR, set_, 'anns')]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.makedirs(dir_)

# ID del objeto (Teléfono)
telefono_id = '/m/050k8'

# Archivos de anotaciones
train_bboxes_filename = './oidv6-train-annotations-bbox.csv'
validation_bboxes_filename = './validation-annotations-bbox.csv'
test_bboxes_filename = './test-annotations-bbox.csv'

# Procesar anotaciones y copiar imágenes
for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    set_ = ['train', 'validation', 'test'][j]
    print(f"Procesando archivo: {filename}")
    with open(filename, 'r') as f:
        line = f.readline()  # Leer la cabecera
        line = f.readline()  # Primera línea de datos
        while len(line) > 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name == telefono_id:
                # Copiar imagen
                img_src = os.path.join(DATA_ALL_DIR, f'{id}.jpg')
                img_dst = os.path.join(DATA_OUT_DIR, set_, 'imgs', f'{id}.jpg')
                if not os.path.exists(img_dst) and os.path.exists(img_src):
                    shutil.copy(img_src, img_dst)

                # Crear anotación YOLO
                x1, x2, y1, y2 = map(float, [x1, x2, y1, y2])
                xc = (x1 + x2) / 2
                yc = (y1 + y2) / 2
                w = x2 - x1
                h = y2 - y1

                with open(os.path.join(DATA_OUT_DIR, set_, 'anns', f'{id}.txt'), 'w') as ann_file:
                    ann_file.write(f"0 {xc} {yc} {w} {h}\n")
            line = f.readline()

print(f"Conjunto de datos YOLO creado en: {DATA_OUT_DIR}")
