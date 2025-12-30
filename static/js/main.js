document.addEventListener("DOMContentLoaded", function () {

  /* ========= SLIDER ========= */
  const slides = document.querySelectorAll(".slide");
  let currentSlide = 0;

  if (slides.length > 0) {
    function showSlide(index) {
      slides.forEach(slide => slide.classList.remove("active"));
      slides[index].classList.add("active");
    }

    showSlide(0);

    setInterval(() => {
      currentSlide = (currentSlide + 1) % slides.length;
      showSlide(currentSlide);
    }, 5000);
  }

  /* ========= ENQUIRY FORM ========= */
  const form = document.getElementById("enquiryForm");
  const modal = document.getElementById("successModal");

  // 🔒 SAFETY CHECK (THIS FIXES EVERYTHING)
  if (!form || !modal) return;

  form.addEventListener("submit", function (e) {
    e.preventDefault(); // ⛔ stop normal submit

    fetch("/submit-enquiry", {
      method: "POST",
      body: new FormData(form)
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        modal.classList.add("show");
        form.reset();

        setTimeout(() => {
          modal.classList.remove("show");
        }, 5000);
      }
    })
    .catch(() => {
      alert("Something went wrong");
    });
  });

});
	