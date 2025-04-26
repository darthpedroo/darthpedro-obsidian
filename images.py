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
           #     print("xf", content)

            # Detecta imágenes Obsidian-style
            images = re.findall(r'!?\[\[([^\]]+\.(?:png|jpg|jpeg|webp|gif|PNG|JPG))\]\]', content)
            # Detecta imágenes estilo Obsidian: ![[image.png]] o [[image.png]]
            obsidian_images = re.findall(r'!?\[\[([^/\]]+\.png)\]\]', content)

            # Detecta imágenes ya procesadas: ![...](.../image.png)
            processed_images = re.findall(r'!\[.*?\]\((?:.*/)?([^/\]]+\.png)\)', content)

            # Combina ambos, sin repetir
            all_images = list(set(obsidian_images + processed_images))

            if not all_images:
                pass
              #  print(f"⚠️ No se detectaron imágenes en: {filename}")
            else:
                pass
              #  print("imagenes encontradas en :", filename, "las imagenes son: ", all_images )

            images = all_images
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
                markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
                
                escaped_image = re.escape(image)
                pattern = re.compile(r'!?\[\[' + escaped_image + r'\]\]')

                #pattern = re.compile(rf'!?(\[\[{re.escape(image)}\]\])')
                content = pattern.sub(lambda m: markdown_image, content)


                print("MARKDOWN IMAGE : ", markdown_image)
              #  print("content", content)


                # Copia imagen a static/images de Hugo
                if os.path.exists(new_obsidian_path):
                    shutil.copy(new_obsidian_path, os.path.join(static_images_dir, image))

            # Escribe los cambios al archivo
            with open(filepath, "w") as file:
                file.write(content)
             #   print("escribiendo contenido: ", content)

print("🎉 ¡Todo listo! Archivos corregidos, imágenes movidas y copiadas.")
