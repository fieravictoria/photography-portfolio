from PIL import Image
import os

# Папки
INPUT_DIR = "src/images"
OUTPUT_DIR = "dist/images"

# Создаём папку для оптимизированных изображений, если её нет
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Проходим по всем файлам
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)
        with Image.open(input_path) as img:
            img.save(output_path, optimize=True, quality=85)
            print(f"✅ Optimized: {filename}")

