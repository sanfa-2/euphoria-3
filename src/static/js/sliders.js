document.addEventListener('DOMContentLoaded', () => {
  // Sportlight Swiper Initialization
  const sportlightSection = document.querySelector('#sportlight');

  const sportlightSwiper = new Swiper('.sportlight .swiper', {
    loop: true,
    autoplay: {
      delay: 3000, 
      disableOnInteraction: false, 
  },
   
    navigation: {
      nextEl: '.sportlight .swiper-button-next',
      prevEl: '.sportlight .swiper-button-prev',
    },
    slidesPerView: 1,
    on: {
      slideChange: function () {
        const activeSlide = sportlightSwiper.slides[sportlightSwiper.activeIndex];
        const bgImage = activeSlide.getAttribute('data-bg');
        sportlightSection.style.backgroundImage = `url(${bgImage})`;
      },
    },
  });

  const initialBgImage = sportlightSwiper.slides[0].getAttribute('data-bg');
  sportlightSection.style.backgroundImage = `url(${initialBgImage})`;

  // New Arrival Swiper Initialization
  const newArrivalSwiper = new Swiper('.new_arrival .newslide', {
    loop: true,
    navigation: {
      nextEl: '.arrow_2.swiper-button-next',
      prevEl: '.arrow_1.swiper-button-prev',
    },
    breakpoints: {
      1100: {
        slidesPerView: 4,
        spaceBetween: 20,
      },
      640: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
      480: {
        slidesPerView: 2,
        spaceBetween: 10,
      },
      320: {
        slidesPerView: 1,
        spaceBetween: 15,
      },
    },
  });
});  

document.addEventListener('DOMContentLoaded', () => {
  var swiper = new Swiper('.feedback .respons.swiper', {
    loop: true,
    slidesPerView: 3,
    spaceBetween: 20,
    slidesPerView: 1, 
    spaceBetween: 10,
    breakpoints: {
      1280: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      680: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      640: {
        slidesPerView: 2,
        spaceBetween: 15,
      },
      
    },
    pagination: {
      el: '.swiper-pagination', 
      clickable: true,          
      dynamicBullets: true,     
    },
  });
});

