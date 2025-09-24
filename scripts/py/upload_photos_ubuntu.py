import os
import shutil
import json

def read_multiline_input(prompt):
    print(prompt)
    print("Paste your text below. When you're done, enter a single line with just 'END':")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == 'END':
            break
        lines.append(line)
    return '\n'.join(lines)

def prompt_for_file(prompt):
    while True:
        file_path = input(prompt + " (or 'q' to quit): ").strip()
        if file_path.lower() == 'q':
            return None
        file_path = os.path.expanduser(file_path)  # Expand ~ to home directory
        if os.path.isfile(file_path):
            return file_path
        else:
            print("Invalid file path. Please try again.")

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Set base directories based on your directory structure
    # From tmp/py/ to tmp/img/ and tmp/json/
    img_dir = os.path.abspath(os.path.join(script_dir, '../img/'))
    json_dir = os.path.abspath(os.path.join(script_dir, '../json/'))

    # Ensure the directories exist
    if not os.path.isdir(img_dir):
        print(f"Image directory does not exist: {img_dir}")
        return
    if not os.path.isdir(json_dir):
        print(f"JSON directory does not exist: {json_dir}")
        return

    # Step 1: Determine the next exhibition number
    exhibitions = [
        name for name in os.listdir(img_dir)
        if os.path.isdir(os.path.join(img_dir, name)) and name.startswith('ex')
    ]
    ex_numbers = [int(name[2:]) for name in exhibitions if name[2:].isdigit()]
    if ex_numbers:
        next_ex_num = max(ex_numbers) + 1
    else:
        next_ex_num = 1  # Start from 1 if no existing exhibitions

    # Step 2: Create the new folder
    new_ex_folder = os.path.join(img_dir, f'ex{next_ex_num}')
    os.makedirs(new_ex_folder, exist_ok=True)

    # Step 3: Select logo image
    print("Please provide the path to the logo image.")
    logo_path = prompt_for_file("Enter path to logo image")
    if not logo_path:
        print("No logo image selected. Exiting.")
        return
    # Copy and rename the logo image
    logo_filename = f'{next_ex_num}_logo.jpg'
    logo_dest_path = os.path.join(new_ex_folder, logo_filename)
    shutil.copyfile(logo_path, logo_dest_path)

    # Step 4: Select artist images and enter descriptions
    artists = []
    artist_counter = 0
    print("Now, let's upload artist images. Provide image paths one by one. Enter 'q' when done.")
    while True:
        artist_image_path = prompt_for_file("Enter path to artist image (or 'q' to quit)")
        if not artist_image_path:
            print("No more artist images selected.")
            break
        # Copy and rename the artist image
        artist_image_filename = f'{next_ex_num}_artist_{artist_counter}.jpg'
        artist_image_dest_path = os.path.join(new_ex_folder, artist_image_filename)
        shutil.copyfile(artist_image_path, artist_image_dest_path)
        # Prompt for artist name and descriptions
        artist_name = input("Enter the name of the artist: ").strip()
        short_desc = read_multiline_input("Enter short description for the artist:")
        full_desc = read_multiline_input("Enter full description for the artist:")
        # Add artist data to the list
        artist_data = {
            'name': artist_name,
            'photo': f'../img/ex{next_ex_num}/{artist_image_filename}',
            'short_desc': short_desc,
            'full_desc': full_desc
        }
        artists.append(artist_data)
        artist_counter += 1

    # Step 5: Select normal images
    carousel_images = []
    normal_image_counter = 0
    print("Now, let's upload normal images. Provide image paths one by one. Enter 'q' when done.")
    while True:
        normal_image_path = prompt_for_file("Enter path to normal image (or 'q' to quit)")
        if not normal_image_path:
            print("No more normal images selected.")
            break
        # Copy and rename the normal image
        normal_image_filename = f'{next_ex_num}_{normal_image_counter}.jpg'
        normal_image_dest_path = os.path.join(new_ex_folder, normal_image_filename)
        shutil.copyfile(normal_image_path, normal_image_dest_path)
        # Add image path to carousel_images list
        carousel_images.append(f'../img/ex{next_ex_num}/{normal_image_filename}')
        normal_image_counter += 1

    # Step 6: Update the artists.json file
    # Prompt for the exhibition description
    exhibition_description = read_multiline_input(f"Enter the description of the featured art for Exhibition {next_ex_num}:")

    # Construct the data
    artists_json_data = {
        "logo": f"../img/ex{next_ex_num}/{logo_filename}",
        "description": exhibition_description,
        "artists": artists,
        "carousel_images": carousel_images
    }

    # Write the data to artists.json
    artists_json_path = os.path.join(json_dir, 'artists.json')
    with open(artists_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(artists_json_data, json_file, ensure_ascii=False, indent=4)

    print(f"Exhibition {next_ex_num} setup is complete.")

if __name__ == "__main__":
    main()
