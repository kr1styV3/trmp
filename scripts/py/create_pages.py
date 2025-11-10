import os
import json
import random

# Define paths relative to the 'py' folder, with absolute path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, '../../html')
CSS_DIR = os.path.join(BASE_DIR, '../../css')
JS_DIR = os.path.join(BASE_DIR, '../../js')
JSON_FILE = os.path.join(BASE_DIR, '../json/artists.json')

# Load artist data from JSON
def load_artist_data(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

# Generate exhibition HTML page
def generate_exhibition_page(artist_data, page_id):
    template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exhibition {page_id} - Temporanea</title>
    <link rel="stylesheet" href="../css/{page_id}.css">
</head>
<body>
    <div class="page-container">
        <header>
            <a href="../index.html">
                <h1 class="logo" style="position: relative; bottom: -2px">
                    <img alt="Temporanea Logo" class="logo-image" style="position: relative; bottom: 4px;" src="../img/logo.png"/>
                    TEMPORANEA
                </h1>
            </a>
        </header>

        <main>
            <h1>Mostra di {artist_data.get('title', 'Untitled Exhibition')}</h1>
            <h1>{artist_data.get('location', '')}</h1>
            
            <!-- Artists Section -->
    '''
    for artist in artist_data.get('artists', []):
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

    template += '''
            <!-- Carousel Section -->
            <section class="carousel">
                <h2>Exhibition Gallery</h2>
                <div class="carousel-container">
                    <!-- JavaScript will dynamically add images here -->
                </div>
            </section>
        </main>
    </div>

    <!-- Lightbox -->
    <div id="lightbox" class="lightbox">
        <span class="lightbox-close">&times;</span>
        <img class="lightbox-content" id="lightbox-img">
        <span class="lightbox-prev">&#10094;</span>
        <span class="lightbox-next">&#10095;</span>
    </div>

    <footer>
        <p>&copy; 2025 Temporanea. All rights reserved.</p>
    </footer>

    <script src="../js/{page_id}.js"></script>
</body>
</html>'''

    output_file = os.path.join(HTML_DIR, f'{page_id}.html')
    with open(output_file, 'w') as f:
        f.write(template)

    return output_file

# Generate CSS
def generate_css_file(page_id):
    css_content = '''
/* General Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #fff;
    color: #000;
    text-align: center;
}

header {
    padding: 20px;
    background-color: #000;
    color: #fff;
}

.logo {
    font-size: 2.5rem;
    letter-spacing: 5px;
}

main {
    margin: 20px 0;
}

/* Artists Section */
.artist {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    margin: 20px auto;
    background-color: #000;
    color: #fff;
    max-width: 800px;
    padding: 20px;
}

.artist-intro {
    width: 150px;
    height: auto;
    margin-right: 20px;
    align-self: center;
}

.artist-info {
    flex: 1;
    max-width: 600px;
    text-align: left;
    position: relative;
    overflow: hidden;
    transition: max-height 0.5s ease-in-out, height 0.5s ease-in-out;
    max-height: 80px;
}

.artist-info p {
    font-size: 1.1rem;
    margin-bottom: 0.5em;
}

.artist-info .full-desc {
    display: none;
}

.artist-info:hover {
    max-height: none;
    height: auto;
}

.artist-info:hover .short-desc {
    display: none;
}

.artist-info:hover .full-desc {
    display: block;
}

footer {
    padding: 20px;
    background-color: #000;
    color: #fff;
    text-align: center;
}

/* Carousel Section */
.carousel {
    margin: 50px 0;
}

.carousel-container {
    display: flex;
    justify-content: space-between;
    overflow: hidden;
    width: calc(100% - 40px);
    margin: 0 auto;
    padding: 0 20px;
}

.carousel-container img {
    width: calc(25% - 10px);
    height: auto;
    transition: transform 0.5s ease-in-out;
    object-fit: cover;
    margin: 0 10px;
}

.carousel-container img:hover {
    transform: scale(1.05);
}

/* Lightbox */
.lightbox {
    display: none;
    position: fixed;
    z-index: 9999;
    padding-top: 60px;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background-color: rgba(0, 0, 0, 0.95);
    justify-content: center;
    align-items: center;
}

.lightbox-content {
    max-width: 80%;
    max-height: 80%;
    border-radius: 5px;
}

.lightbox-close, .lightbox-prev, .lightbox-next {
    position: absolute;
    color: white;
    font-size: 2rem;
    cursor: pointer;
    user-select: none;
    padding: 10px;
}

.lightbox-close {
    top: 10px;
    right: 25px;
}

.lightbox-prev {
    left: 10%;
    top: 50%;
    transform: translateY(-50%);
}

.lightbox-next {
    right: 10%;
    top: 50%;
    transform: translateY(-50%);
}

@media (max-width: 768px) {
    .carousel-container img {
        width: calc(50% - 10px);
    }

    .lightbox-prev, .lightbox-next {
        font-size: 1.5rem;
    }
}
'''
    output_file = os.path.join(CSS_DIR, f'{page_id}.css')
    with open(output_file, 'w') as f:
        f.write(css_content)

# Generate JS
def generate_js_file(page_id):
    exhibition_num = page_id.split("_")[0]
    num_images = int(input(f"Quante foto sono state inserite per {page_id}? "))

    image_paths = [f'../../img/ex{exhibition_num}/{exhibition_num}_{i}.jpg' for i in range(num_images)]

    js_content = f'''
document.addEventListener('DOMContentLoaded', function() {{
    const imagePaths = {image_paths};
    const galleryContainer = document.querySelector('.carousel-container');

    // Initial load of 4 random images
    let shuffledImages = imagePaths.sort(() => 0.5 - Math.random()).slice(0, 4);
    galleryContainer.innerHTML = "";
    shuffledImages.forEach((imagePath) => {{
        const imgElement = document.createElement('img');
        imgElement.src = imagePath;
        imgElement.alt = "Exhibition Image";
        imgElement.dataset.index = imagePaths.indexOf(imagePath);
        galleryContainer.appendChild(imgElement);
    }});

    let images = galleryContainer.querySelectorAll('img');

    // Rotate carousel every 3 seconds
    setInterval(() => {{
        shuffledImages = imagePaths.sort(() => 0.5 - Math.random()).slice(0, 4);
        shuffledImages.forEach((imagePath, index) => {{
            images[index].src = imagePath;
            images[index].dataset.index = imagePaths.indexOf(imagePath);
        }});
    }}, 3000);

    // Lightbox elements
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.querySelector('.lightbox-close');
    const prevBtn = document.querySelector('.lightbox-prev');
    const nextBtn = document.querySelector('.lightbox-next');
    let currentIndex = 0;

    galleryContainer.addEventListener('click', function(e) {{
        if (e.target.tagName === 'IMG') {{
            currentIndex = parseInt(e.target.dataset.index, 10);
            showImage(currentIndex);
            lightbox.style.display = 'flex';
        }}
    }});

    closeBtn.onclick = () => lightbox.style.display = 'none';
    prevBtn.onclick = () => {{ currentIndex = (currentIndex - 1 + imagePaths.length) % imagePaths.length; showImage(currentIndex); }};
    nextBtn.onclick = () => {{ currentIndex = (currentIndex + 1) % imagePaths.length; showImage(currentIndex); }};

    lightbox.addEventListener('click', (e) => {{ if (e.target === lightbox) lightbox.style.display = 'none'; }});

    function showImage(index) {{
        lightboxImg.src = imagePaths[index];
    }}

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {{
        if (lightbox.style.display === 'flex') {{
            if (e.key === 'ArrowRight') nextBtn.click();
            if (e.key === 'ArrowLeft') prevBtn.click();
            if (e.key === 'Escape') closeBtn.click();
        }}
    }});

    // Swipe support
    let touchStartX = 0;
    let touchEndX = 0;
    lightboxImg.addEventListener('touchstart', (e) => {{ touchStartX = e.changedTouches[0].screenX; }});
    lightboxImg.addEventListener('touchend', (e) => {{
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    }});

    function handleSwipe() {{
        const swipeDistance = touchEndX - touchStartX;
        if (Math.abs(swipeDistance) > 50) {{
            if (swipeDistance < 0) nextBtn.click();
            else prevBtn.click();
        }}
    }}
}});
'''
    output_file = os.path.join(JS_DIR, f'{page_id}.js')
    with open(output_file, 'w') as f:
        f.write(js_content)

# Main process
def main():
    artist_data = load_artist_data(JSON_FILE)

    existing_pages = [int(f.split('_')[0]) for f in os.listdir(HTML_DIR) if f.endswith('.html')]
    next_page_id = f'{max(existing_pages) + 1}_0' if existing_pages else '1_0'

    generate_exhibition_page(artist_data, next_page_id)
    generate_css_file(next_page_id)
    generate_js_file(next_page_id)

    print(f"✅ Generated: {next_page_id}.html, {next_page_id}.css, {next_page_id}.js")

if __name__ == "__main__":
    main()
        
