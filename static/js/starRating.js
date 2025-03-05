document.addEventListener('DOMContentLoaded', () => {
    const ratingContainer = document.querySelector('.star-rating-container');
    if (!ratingContainer) {
        console.error('Rating container not found!');
        return;
    }

    const productRating = parseFloat(ratingContainer.dataset.rating);
    if (isNaN(productRating)) {
        console.error('Invalid product rating!');
        return;
    }

    const maxStars = 5;

    const fullStar = '/static/images/star copy.svg';
    const halfStar = '/static/images/vector.svg';
    const emptyStar = '/static/images/vector (1).svg';

    for (let i = 1; i <= maxStars; i++) {
        const star = document.createElement('img');
        star.classList.add('star-icon');

        if (i <= Math.floor(productRating)) {
            star.src = fullStar;
        } else if (i === Math.ceil(productRating) && productRating % 1 !== 0) {
            star.src = halfStar;
        } else {
            star.src = emptyStar;
        }

        ratingContainer.appendChild(star);
    }
});
