
    document.addEventListener('DOMContentLoaded', function() {
        const imagePaths = ['../img/ex6/6_0.jpg', '../img/ex6/6_1.jpg', '../img/ex6/6_2.jpg', '../img/ex6/6_3.jpg', '../img/ex6/6_4.jpg', '../img/ex6/6_5.jpg', '../img/ex6/6_6.jpg', '../img/ex6/6_7.jpg', '../img/ex6/6_8.jpg', '../img/ex6/6_9.jpg', '../img/ex6/6_10.jpg', '../img/ex6/6_11.jpg', '../img/ex6/6_12.jpg', '../img/ex6/6_13.jpg', '../img/ex6/6_14.jpg', '../img/ex6/6_15.jpg', '../img/ex6/6_16.jpg', '../img/ex6/6_17.jpg', '../img/ex6/6_18.jpg', '../img/ex6/6_19.jpg'];

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
    