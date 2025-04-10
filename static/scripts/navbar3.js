document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".navbar3 a");
    const currentPath = window.location.pathname;

    navLinks.forEach(link => {
      // Check if the link href matches the current path
      if (link.getAttribute("href") === currentPath) {
        link.classList.add("active");
      } else {
        link.classList.remove("active");
      }
    });
  });