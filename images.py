import os
import re
import shutil

# Paths
posts_dir = '/home/porky/notes/public'  # Archivos markdown exportados para Hugo
attachments_dir = "/home/porky/notes"   # Tu vault original de Obsidian
obsidian_images_dir = os.path.join(attachments_dir, 'images')  # Donde moveremos las imágenes
static_images_dir = "/home/porky/darthpedro/obsidian-darthpedro/static/images"  # Hugo

# Asegura que exista la carpeta /images en Obsidian
os.makedirs(obsidian_images_dir, exist_ok=True)

# Procesar cada markdown en public/
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r") as file:
            content = file.read()

        # Encontrar todos los matches ![[...]] o [[...]]
        images = re.findall(r'!?\[\[([^/\]]+\.png)\]\]', content)

        for image in images:
            original_path = os.path.join(attachments_dir, image)
            new_obsidian_path = os.path.join(obsidian_images_dir, image)

            # Mover imagen si aún está en la raíz de la vault
            if os.path.exists(original_path) and not os.path.exists(new_obsidian_path):
                shutil.move(original_path, new_obsidian_path)
                print(f"✅ Movida: {image} → /images/")
            elif not os.path.exists(original_path) and not os.path.exists(new_obsidian_path):
                print(f"⚠️ No encontrada: {original_path}")

            # Cambiar los enlaces en el contenido del .md
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            pattern = re.compile(rf'!?(\[\[{re.escape(image)}\]\])')  # detecta ambos: ![[...]] y [[...]]
            content = pattern.sub(markdown_image, content)

            # Copiar imagen a Hugo static/images
            if os.path.exists(new_obsidian_path):
                image_dest = os.path.join(static_images_dir, image)
                shutil.copy(new_obsidian_path, image_dest)

        # Guardar cambios en el archivo markdown
        with open(filepath, "w") as file:
            file.write(content)

print("🎉 Todo listo: ¡Markdowns corregidos y las imágenes están en static/images!")
