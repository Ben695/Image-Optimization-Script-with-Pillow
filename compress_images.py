from PIL import Image
import os
import json
import time

# Nom du fichier de configuration
config_file = "config.json"

# Fonction pour obtenir une réponse valide de l'utilisateur
def get_user_response(question, valid_responses):
    response = input(question).lower()
    while response not in valid_responses:
        # Corrige les fautes de frappe courantes
        if response.startswith('n') or response.startswith('no'):
            response = 'non'
        elif response.startswith('o') or response.startswith('oiu'):
            response = 'oui'
        else:
            print()
            print("Oops! Réponse invalide. Réessaie.")
            response = input(question).lower()
    return response

# Fonction pour normaliser les slashes dans les chemins
def normalize_path(path):
    return path.replace("\\", "/")

# Fonction pour demander et mettre à jour les chemins d'accès
def update_paths():
    print()
    input_folder = normalize_path(input("Chemin du dossier contenant les images à compresser : "))
    
    # Demande le chemin du dossier de sortie
    output_folder = os.path.join(input_folder, "img-optimize")
    
    return {'input_folder': input_folder, 'output_folder': output_folder}

# Vérifie si le fichier de configuration existe
if os.path.exists(config_file):
    # Charge les chemins d'accès depuis le fichier de configuration
    with open(config_file, 'r') as file:
        config = json.load(file)

    # Demande à l'utilisateur s'il veut changer les chemins
    print()
    change_paths = get_user_response("Voulez-vous changer les chemins d'accès ? (oui/non): ", ['oui', 'non'])

    if change_paths == 'oui':
        # Mise à jour des chemins d'accès
        config = update_paths()
        # Enregistre les chemins d'accès mis à jour dans le fichier de configuration
        with open(config_file, 'w') as file:
            json.dump(config, file, indent=4)
else:
    # Si le fichier de configuration n'existe pas, demande les chemins d'accès
    config = update_paths()
    # Enregistre les chemins d'accès dans le fichier de configuration
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)

# Assurez-vous que le dossier de sortie existe
os.makedirs(config['output_folder'], exist_ok=True)

# Taille maximale pour redimensionner les images (1920 x 1080)
max_width = 1920
max_height = 1080

# Demande à l'utilisateur s'il souhaite redimensionner les images
print()
response = get_user_response("Veux-tu redimensionner les images ? (oui/non): ", ['oui', 'non'])

# Si l'utilisateur veut redimensionner les images
if response == 'oui':
    # Demande les dimensions en x et y
    print()
    new_width = int(input("Nouvelle largeur (en pixels) : "))
    print()
    new_height = int(input("Nouvelle hauteur (en pixels) : "))

# Demande à l'utilisateur le pourcentage de compression
print()
compression_percentage = int(input("Sur quelle qualité de compression veux-tu (en pourcentage) ? (1-100): "))

# Calcul du temps d'attente en fonction du nombre d'images
nombre_images = len([f for f in os.listdir(config['input_folder']) if f.endswith((".jpg", ".jpeg", ".png"))])
temps_attente = int(nombre_images * 0.8)

# Affiche un message sympa avec le temps d'attente
print()
print("-"*60)
print(f"Chill mec, ça va prendre environ {temps_attente} secondes pour tes {nombre_images} images. Grab some ☕️ (Le temps d'attente peut varier en fonction de la puissance de ton PC.)")
print("-"*60)

# Boucle à travers les fichiers du dossier d'entrée
for filename in os.listdir(config['input_folder']):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        # Ouvre l'image
        img = Image.open(os.path.join(config['input_folder'], filename))

        # Vérifie si l'image doit être redimensionnée
        if response == 'oui':
            img = img.resize((new_width, new_height), Image.LANCZOS)
        elif img.width > max_width or img.height > max_height:
            # Redimensionne l'image en conservant son ratio en utilisant LANCZOS
            img.thumbnail((max_width, max_height), Image.LANCZOS)

        # Obtient le nom du fichier sans extension
        base_filename = os.path.splitext(filename)[0]

        # Compose le nouveau chemin de sortie en corrigeant les slashes
        output_path = os.path.join(config['output_folder'], f"{base_filename}.webp").replace("\\", "/")

        # Comprime l'image avec le pourcentage spécifié
        img.save(output_path, "WEBP", quality=compression_percentage)

# Ajoute une petite pause pour l'effet dramatique
time.sleep(temps_attente)

print("-"*60)
print("Les {nombre_images} images ont été redimensionnées, compressées et converties en WebP avec succès ! Tu peux retrouver les versions optimisées dans le dossier 'img-optimize' situé dans le répertoire que tu as spécifié précédemment.")
print("-"*60)
