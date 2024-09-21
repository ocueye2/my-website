
const slidesContainer = document.getElementById("slides-container");
const subs = document.querySelectorAll("table"); // Select all elements with the class 'sub'
const slide = document.querySelector(".slide");
const prevButton = document.getElementById("slide-arrow-prev");
const nextButton = document.getElementById("slide-arrow-next");

function moveSubDownAndSlide(action) {
    // Move all elements with the 'sub' class down out of view

    subs.forEach(sub => {
        sub.style.transition = "transform .7s ease"; // Add transition for smooth animation
        sub.style.transform = "translateY(100%)"; // Move sub down (100% of its height)
    });

    // Wait for the subs to move out of sight before advancing the slide
    setTimeout(() => {
        const slideWidth = slide.clientWidth;

        // Advance or go back the slide
        if (action === "next") {
            slidesContainer.scrollLeft += slideWidth;
        } else if (action === "prev") {
            slidesContainer.scrollLeft -= slideWidth;
        }

        // After the slide movement, move the subs back into view
        setTimeout(() => {
            subs.forEach(sub => {
                sub.style.transform = "translateY(0%)"; // Bring sub back up
            });
        }, 200); // Delay slightly to give room for the slide to change
    }, 500); // Wait for subs to move down before advancing slide
}

// Handle the next button click
nextButton.addEventListener("click", () => {
    moveSubDownAndSlide("next");
});

// Handle the previous button click
prevButton.addEventListener("click", () => {
    moveSubDownAndSlide("prev");
});

        