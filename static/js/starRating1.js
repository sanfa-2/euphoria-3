document.addEventListener('DOMContentLoaded', () => {
   
    const ratingContainers = document.querySelectorAll('.star-rating');

    ratingContainers.forEach(ratingContainer => {
       
        const testimonialRating = parseFloat(ratingContainer.dataset.rating);

        if (isNaN(testimonialRating)) {
            console.error('Invalid testimonial rating!');
            return;
        }

        const maxStars = 5;

       
        const fullStar = '/static/images/star copy.svg'; 
        const halfStar = '/static/images/Vector.svg'; 
        const emptyStar = '/static/images/Vector (1).svg';  

        const stars = ratingContainer.querySelectorAll('li a img');

        stars.forEach((star, index) => {
            if (index < Math.floor(testimonialRating)) {
                star.src = fullStar;
            } else if (index === Math.floor(testimonialRating) && testimonialRating % 1 !== 0) {
                star.src = halfStar;
            } else {
                star.src = emptyStar;
            }
        });
    });
});
