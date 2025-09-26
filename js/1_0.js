document.addEventListener('DOMContentLoaded', function() {
    const imagePaths = [
        '../img/ex1/1_0.jpg',
        '../img/ex1/1_1.jpg',
        '../img/ex1/1_2.jpg',
        '../img/ex1/1_3.jpg',
        '../img/ex1/1_4.jpg',
        '../img/ex1/1_5.jpg',
        '../img/ex1/1_6.jpg',
        '../img/ex1/1_7.jpg',
        '../img/ex1/1_8.jpg',
        '../img/ex1/1_9.jpg',
        '../img/ex1/1_10.jpg',
        '../img/ex1/1_11.jpg',
        '../img/ex1/1_12.jpg',
        '../img/ex1/1_13.jpg',
    ];


    const galleryContainer = document.querySelector('.carousel-container');

    // --- Initial load of 4 random images ---
    let shuffledImages = imagePaths.sort(() => 0.5 - Math.random()).slice(0, 4);
    galleryContainer.innerHTML = ""; // clear just in case
    shuffledImages.forEach((imagePath) => {
        const imgElement = document.createElement('img');
        imgElement.src = imagePath;
        imgElement.alt = "Exhibition Image";
        imgElement.dataset.index = imagePaths.indexOf(imagePath);
        galleryContainer.appendChild(imgElement);
    });

    // Keep track of images in the carousel
    let images = galleryContainer.querySelectorAll('img');

    // --- Rotate carousel every 3 seconds ---
    setInterval(() => {
        shuffledImages = imagePaths.sort(() => 0.5 - Math.random()).slice(0, 4);

        shuffledImages.forEach((imagePath, index) => {
            images[index].src = imagePath;
            images[index].dataset.index = imagePaths.indexOf(imagePath);
        });
    }, 3000);

    // --- Lightbox elements ---
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.querySelector('.lightbox-close');
    const prevBtn = document.querySelector('.lightbox-prev');
    const nextBtn = document.querySelector('.lightbox-next');

    let currentIndex = 0;

    // Open lightbox on image click
    galleryContainer.addEventListener('click', function(e) {
        if (e.target.tagName === 'IMG') {
            currentIndex = parseInt(e.target.dataset.index, 10);
            showImage(currentIndex);
            lightbox.style.display = 'flex';
        }
    });

    // Close button
    closeBtn.onclick = () => {
        lightbox.style.display = 'none';
    };

    // Prev/Next buttons
    prevBtn.onclick = () => {
        currentIndex = (currentIndex - 1 + imagePaths.length) % imagePaths.length;
        showImage(currentIndex);
    };

    nextBtn.onclick = () => {
        currentIndex = (currentIndex + 1) % imagePaths.length;
        showImage(currentIndex);
    };

    // Close when clicking outside the image
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            lightbox.style.display = 'none';
        }
    });

    // Show image helper
    function showImage(index) {
        lightboxImg.src = imagePaths[index];
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (lightbox.style.display === 'flex') {
            if (e.key === 'ArrowRight') nextBtn.click();
            if (e.key === 'ArrowLeft') prevBtn.click();
            if (e.key === 'Escape') closeBtn.click();
        }
    });
});
