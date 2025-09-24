import os
from bs4 import BeautifulSoup

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, '../../index.html')
HTML_DIR = os.path.join(BASE_DIR, '../../html')
IMG_DIR = '../../img/'

# List of exhibitions in order (current -> previous -> others)
exhibitions = ['7_0', '6_0', '5_0', '2_0', '1_0', '3_0', '4_0', '9_0']  # Modify as needed

def update_index():
    # Read the index.html content
    with open(INDEX_FILE, 'r') as f:
        index_content = f.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(index_content, 'html.parser')

    # Get the exhibition to display in the hero section
    current_hero_exhibition = exhibitions[0]

    # Extract the exhibition number (e.g., '2' from '2_0')
    exhibition_number = current_hero_exhibition.split('_')[0]

    # Update the Hero Section
    hero_link = soup.find('a', class_='hero-link')
    if hero_link:
        # Construct the new hero section
        new_hero_section = soup.new_tag('a', href=f"html/{current_hero_exhibition}.html", **{'class': 'hero-link'})

        hero_section = soup.new_tag('section', **{'class': 'hero-section'})
        hero_content = soup.new_tag('div', **{'class': 'hero-content'})

        # Corrected image filename
        img_src = f"../../img/ex{exhibition_number}/{exhibition_number}_logo.jpg"
        hero_image = soup.new_tag('img', src=img_src, alt="Featured Art", **{'class': 'hero-image'})

        hero_description = soup.new_tag('div', **{'class': 'hero-description'})
        description_text = f"This is the description of the featured art for Exhibition {current_hero_exhibition}."
        hero_description.append(soup.new_tag('p'))
        hero_description.p.string = description_text

        # Build the structure
        hero_content.append(hero_image)
        hero_content.append(hero_description)
        hero_section.append(hero_content)
        new_hero_section.append(hero_section)

        # Replace the existing hero section
        hero_link.replace_with(new_hero_section)
    else:
        print("Hero section not found, please check index.html.")

    # Update the Carousel Section
    carousel_container = soup.find('div', class_='carousel-container')
    if carousel_container:
        # Clear existing carousel items
        carousel_container.clear()

        # Add new carousel items
        for exhibition in exhibitions[1:]:
            exhibition_number = exhibition.split('_')[0]

            carousel_item = soup.new_tag('div', **{'class': 'carousel-item'})
            link = soup.new_tag('a', href=f"html/{exhibition}.html")
            img_src = f"../../img/ex{exhibition_number}/{exhibition_number}_logo.jpg"  # Corrected filename
            img = soup.new_tag('img', src=img_src, alt=f"Exhibition {exhibition}")
            caption = soup.new_tag('p')
            caption.string = f"Exhibition {exhibition}"

            link.append(img)
            link.append(caption)
            carousel_item.append(link)
            carousel_container.append(carousel_item)
    else:
        print("Carousel container not found, please check index.html.")

    # Write the updated HTML back to index.html
    with open(INDEX_FILE, 'w') as f:
        f.write(str(soup.prettify()))

    print(f"Updated index.html with the current exhibition: {current_hero_exhibition} and updated the carousel.")

if __name__ == "__main__":
    update_index()
