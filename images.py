import os
import re
import shutil

# Paths
attachments_dir = "/home/porky/public-notes"
posts_dir = os.path.join(attachments_dir, 'public')
obsidian_images_dir = os.path.join(attachments_dir, 'images')
static_images_dir = "/home/porky/darthpedro/obsidian-darthpedro/static/images"

os.makedirs(obsidian_images_dir, exist_ok=True)

# Recorre todos los subdirectorios
for root, _, files in os.walk(posts_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)

            with open(filepath, "r") as file:
                content = file.read()

            # Detecta imágenes Obsidian-style
            images = re.findall(r'!?\[\[([^/\]]+\.png)\]\]', content)

            for image in images:
                original_path = os.path.join(attachments_dir, image)
                new_obsidian_path = os.path.join(obsidian_images_dir, image)

                # Mueve la imagen desde el root de la vault a /images
                if os.path.exists(original_path) and not os.path.exists(new_obsidian_path):
                    shutil.move(original_path, new_obsidian_path)
                    print(f"✅ Movida: {image} → /images/")
                elif not os.path.exists(original_path) and not os.path.exists(new_obsidian_path):
                    print(f"⚠️ No encontrada: {original_path}")

                # Reemplaza en el contenido del markdown
                markdown_image = f"![Image Description](images/{image.replace(' ', '%20')})"
                pattern = re.compile(rf'!?(\[\[{re.escape(image)}\]\])')
                content = pattern.sub(markdown_image, content)

                # Copia imagen a static/images de Hugo
                if os.path.exists(new_obsidian_path):
                    shutil.copy(new_obsidian_path, os.path.join(static_images_dir, image))

            # Escribe los cambios al archivo
            with open(filepath, "w") as file:
                file.write(content)

print("🎉 ¡Todo listo! Archivos corregidos, imágenes movidas y copiadas.")
