import os
import json
import random

# Define paths relative to the 'py' folder, with absolute path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
HTML_DIR = os.path.join(BASE_DIR, '../../html')  # Folder where exhibition pages are stored
CSS_DIR = os.path.join(BASE_DIR, '../../css')  # Folder where CSS files are stored
JS_DIR = os.path.join(BASE_DIR, '../../js')  # Folder where JS files are stored
JSON_FILE = os.path.join(BASE_DIR, '../json/artists.json')  # Data file for exhibitions

# Load artist data from the JSON file
def load_artist_data(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

# Generate HTML for each new exhibition page
def generate_exhibition_page(artist_data, page_id):
    template = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Exhibition {page_id} - Temporanea</title>
        <link rel="stylesheet" href="../css/{page_id}.css">
    </head>
    <body>
        <header>
            <h1 class="logo" href="../index.html">TEMPORANEA</h1>
            <h2>Exhibition {page_id}</h2>
        </header>

        <main>
            <!-- Artists Section -->
        '''
    # Add each artist
    for artist in artist_data['artists']:
        template += f'''
            <div class="artist">
                <img src="{artist['photo']}" alt="{artist['name']} Intro" class="artist-intro">
                <div class="artist-info">
                    <h3>{artist['name']}</h3>
                    <p class="short-desc">{artist['short_desc']}</p>
                    <p class="full-desc">{artist['full_desc']}</p>
                </div>
            </div>
        '''

    # Carousel Section
    template += '''
        <!-- Carousel Section -->
        <section class="carousel">
            <h2>Exhibition Gallery</h2>
            <div class="carousel-container">
                <!-- JavaScript will dynamically add images here -->
            </div>
        </section>
        </main>
        <footer>
            <p>&copy; 2024 Temporanea. All rights reserved.</p>
        </footer>
    '''

    # Ensure correct f-string formatting in the script tag
    template += f'''
        <script src="../js/{page_id}.js"></script>
    </body>
    </html>
    '''

    # Write the new exhibition HTML page inside the html folder
    output_file = os.path.join(HTML_DIR, f'{page_id}.html')
    with open(output_file, 'w') as f:
        f.write(template)

    return output_file

# Generate CSS file for the exhibition page
def generate_css_file(page_id):
    css_content = f'''
    /* General Styles */
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}

    body {{
        font-family: Arial, sans-serif;
        background-color: #fff;
        color: #000;
        text-align: center;
    }}

    header {{
        padding: 20px;
        background-color: #000;
        color: #fff;
    }}

    .logo {{
        font-size: 2.5rem;
        letter-spacing: 5px;
    }}

    main {{
        margin: 20px 0;
    }}

    /* Artists Section */
    .artist {{
        display: flex;
        justify-content: center;
        align-items: flex-start;
        margin: 20px auto;
        background-color: #000;
        color: #fff;
        max-width: 800px;
        padding: 20px;
        border-radius: 5px;
    }}

    .artist-intro {{
        width: 150px;
        height: auto;
        margin-right: 20px;
        align-self: center;
    }}

    .artist-info {{
        flex: 1;
        max-width: 600px;
        text-align: left;
        position: relative;
        overflow: hidden;
        transition: max-height 0.5s ease-in-out, height 0.5s ease-in-out;
        max-height: 80px;
    }}

    .artist-info p {{
        font-size: 1.1rem;
        margin-bottom: 0.5em;
    }}

    .artist-info .full-desc {{
        display: none;
    }}

    .artist-info:hover {{
        max-height: none;
        height: auto;
    }}

    .artist-info:hover .short-desc {{
        display: none;
    }}

    .artist-info:hover .full-desc {{
        display: block;
    }}

    footer {{
        padding: 20px;
        background-color: #000;
        color: #fff;
        text-align: center;
    }}

    /* Carousel Section */
    .carousel {{
        margin: 50px 0;
    }}

    .carousel-container {{
        display: flex;
        justify-content: space-between;
        overflow: hidden;
        width: calc(100% - 40px);
        margin: 0 auto;
        padding: 0 20px;
    }}

    .carousel-container img {{
        width: calc(25% - 10px);
        height: auto;
        transition: transform 0.5s ease-in-out;
        object-fit: cover;
        border-radius: 5px;
        margin: 0 10px;
    }}

    .carousel-container img:hover {{
        transform: scale(1.05);
    }}
    '''
    output_file = os.path.join(CSS_DIR, f'{page_id}.css')
    with open(output_file, 'w') as f:
        f.write(css_content)

# Generate JS file for the exhibition page
# Generate JS file for the exhibition page
def generate_js_file(page_id):
    # Extract the exhibition number (e.g., '3' from '3_0')
    exhibition_num = page_id.split("_")[0]

    # Ask the user how many images are there
    num_images = int(input(f"quante foto sono state inserite {page_id}? "))

    # Construct the image paths based on the user input
    image_paths = [
        f'../../img/ex{exhibition_num}/{exhibition_num}_{i}.jpg' for i in range(num_images)
    ]

    # Generate the JS content
    js_content = f'''
    document.addEventListener('DOMContentLoaded', function() {{
        const imagePaths = {image_paths};

        const galleryContainer = document.querySelector('.carousel-container');

        // Shuffle the images array and select the first 4 for the carousel
        const shuffledImages = imagePaths.sort(() => 0.5 - Math.random()).slice(0, 4);

        // Add images to the carousel container (row of 4)
        shuffledImages.forEach(imagePath => {{
            const imgElement = document.createElement('img');
            imgElement.src = imagePath;
            imgElement.alt = "Exhibition Image";
            galleryContainer.appendChild(imgElement);
        }});

        // Carousel functionality to switch the 4 images without resetting the entire container
        let currentIndex = 0;
        const images = galleryContainer.querySelectorAll('img');

        setInterval(() => {{
            const newShuffledImages = imagePaths.sort(() => 0.5 - Math.random()).slice(0, 4);

            // Replace each image individually to avoid page refresh or jump
            newShuffledImages.forEach((imagePath, index) => {{
                images[index].src = imagePath;
            }});

        }}, 3000); // Change every 3 seconds
    }});
    '''
    output_file = os.path.join(JS_DIR, f'{page_id}.js')
    with open(output_file, 'w') as f:
        f.write(js_content)


# Main process
def main():
    artist_data = load_artist_data(JSON_FILE)  # Load data from JSON

    # Determine the next exhibition page ID (e.g., '3_0')
    existing_pages = [int(f.split('_')[0]) for f in os.listdir(HTML_DIR) if f.endswith('.html')]
    next_page_id = f'{max(existing_pages) + 1}_0' if existing_pages else '1_0'

    # Generate the new exhibition page
    generate_exhibition_page(artist_data, next_page_id)

    # Generate CSS and JS files
    generate_css_file(next_page_id)
    generate_js_file(next_page_id)

    print(f"Generated exhibition page: {next_page_id}.html, {next_page_id}.css, and {next_page_id}.js")

if __name__ == "__main__":
    main()
