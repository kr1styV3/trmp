
    document.addEventListener('DOMContentLoaded', function() {
        const imagePaths = ['../img/ex5/5_0.jpg', '../img/ex5/5_1.jpg', '../img/ex5/5_2.jpg', '../img/ex5/5_3.jpg', '../img/ex5/5_4.jpg', '../img/ex5/5_5.jpg', '../img/ex5/5_6.jpg', '../img/ex5/5_7.jpg', '../img/ex5/5_8.jpg', '../img/ex5/5_9.jpg', '../img/ex5/5_10.jpg', '../img/ex5/5_11.jpg', '../img/ex5/5_12.jpg', '../img/ex5/5_13.jpg', '../img/ex5/5_14.jpg', '../img/ex5/5_15.jpg', '../img/ex5/5_16.jpg', '../img/ex5/5_17.jpg'];

        const galleryContainer = document.querySelector('.carousel-container');

        // Shuffle the images array and select the first 4 for the carousel
        const shuffledImages = imagePaths.sort(() => 0.5 - Math.random()).slice(0, 4);

        // Add images to the carousel container (row of 4)
        shuffledImages.forEach(imagePath => {
            const imgElement = document.createElement('img');
            imgElement.src = imagePath;
            imgElement.alt = "Exhibition Image";
            galleryContainer.appendChild(imgElement);
        });

        // Carousel functionality to switch the 4 images without resetting the entire container
        let currentIndex = 0;
        const images = galleryContainer.querySelectorAll('img');

        setInterval(() => {
            const newShuffledImages = imagePaths.sort(() => 0.5 - Math.random()).slice(0, 4);

            // Replace each image individually to avoid page refresh or jump
            newShuffledImages.forEach((imagePath, index) => {
                images[index].src = imagePath;
            });

        }, 3000); // Change every 3 seconds
    });
    