document.addEventListener("DOMContentLoaded", function () {
  const spans = document.querySelectorAll('.spam-protect');
  spans.forEach(span => {
    if (span.dataset.user && span.dataset.domain) {
      span.textContent = span.dataset.user + "@" + span.dataset.domain;
    }
    if (span.dataset.phone) {
      span.textContent = span.dataset.phone;
    }
  });
});

