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

            # Detecta imágenes estilo Obsidian ![[image.png]]
            images = re.findall(r'!?\[\[([^/\]]+\.png)\]\]', content)

            for image in images:
                original_path = os.path.join(attachments_dir, image)
                new_obsidian_path = os.path.join(obsidian_images_dir, image)

                # Mueve la imagen desde root a /images si no existe ya ahí
                if os.path.exists(original_path) and not os.path.exists(new_obsidian_path):
                    shutil.move(original_path, new_obsidian_path)
                    print(f"✅ Movida: {image} → /images/")
                elif not os.path.exists(original_path) and not os.path.exists(new_obsidian_path):
                    print(f"⚠️ No encontrada: {original_path}")

                # Cambia el link en el .md al formato absoluto para GitHub Pages
                markdown_image = f"![Image Description](/darthpedro-obsidian/images/{image.replace(' ', '%20')})"
                pattern = re.compile(rf'!?(\[\[{re.escape(image)}\]\])')
                content = pattern.sub(markdown_image, content)

                # Copia la imagen a static/images/ para Hugo
                if os.path.exists(new_obsidian_path):
                    shutil.copy(new_obsidian_path, os.path.join(static_images_dir, image))

            # Guarda el nuevo contenido del markdown
            with open(filepath, "w") as file:
                file.write(content)

print("🎉 ¡Todo listo! Imágenes movidas, copiadas y markdowns corregidos.")
