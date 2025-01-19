import os

# Definir el ID del objeto "Teléfonos"
telefono_id = '/m/050k8'  # ID para "Mobile phone" en Open Images Dataset

# Definir rutas de los archivos de anotaciones
train_bboxes_filename = os.path.join('.', 'oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('.', 'validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join('.', 'test-annotations-bbox.csv')

# Archivo de salida
image_list_file_path = os.path.join('.', 'image_list_fileTelefonos.txt')

# Lista para almacenar IDs únicos de imágenes
image_list_file_list = []

# Iterar por los archivos de anotaciones (entrenamiento, validación, prueba)
for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    print(f"Procesando archivo: {filename}")
    with open(filename, 'r') as f:
        # Saltar la primera línea (cabecera)
        line = f.readline()
        line = f.readline()  # Leer la primera línea de datos
        while len(line) != 0:
            # Extraer columnas relevantes de la línea
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            
            # Verificar si la clase coincide con "Teléfonos" y evitar duplicados
            if class_name == telefono_id and id not in image_list_file_list:
                image_list_file_list.append(id)  # Añadir ID único
                with open(image_list_file_path, 'a') as fw:
                    # Guardar en el archivo de salida según el tipo de conjunto (train/val/test)
                    fw.write('{}/{}\n'.format(['train', 'validation', 'test'][j], id))
            
            # Leer la siguiente línea
            line = f.readline()

        f.close()

print(f"Archivo de lista de imágenes creado: {image_list_file_path}")
