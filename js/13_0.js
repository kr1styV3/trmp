
    document.addEventListener('DOMContentLoaded', function() {
        const imagePaths = ['../../img/ex13/13_0.jpg', '../../img/ex13/13_1.jpg', '../../img/ex13/13_2.jpg', '../../img/ex13/13_3.jpg', '../../img/ex13/13_4.jpg', '../../img/ex13/13_5.jpg', '../../img/ex13/13_6.jpg', '../../img/ex13/13_7.jpg', '../../img/ex13/13_8.jpg', '../../img/ex13/13_9.jpg', '../../img/ex13/13_10.jpg', '../../img/ex13/13_11.jpg', '../../img/ex13/13_12.jpg', '../../img/ex13/13_13.jpg'];

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
    