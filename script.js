const container = document.querySelector('.image-container');
        let scrollPosition = 0;

        window.addEventListener('scroll', () => {
            const newScrollPosition = window.scrollY;

            if (newScrollPosition > scrollPosition) {
                // Scrolling down, shuffle images
                container.style.transform = 'translateY(-16.666%)'; // Move the container up by one image's height
            } else {
                // Scrolling up, shuffle images
                container.style.transform = 'translateY(0)'; // Reset the container position
            }

            scrollPosition = newScrollPosition;
        });
