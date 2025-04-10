const swiper = new Swiper('.swiper', {
  slidesPerView: 4,  // Display 4 cars at once
  spaceBetween: 15,   // Gap between the car items
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true, // Allows clicking on pagination dots
  },
  breakpoints: {
    // On smaller screens, display fewer cars
    768: {
      slidesPerView: 2,  // Show 2 cars on smaller screens
    },
    1024: {
      slidesPerView: 3,  // Show 3 cars on medium-sized screens
    },
    1440: {
      slidesPerView: 4,  // Show 4 cars on larger screens
    }
  },
});