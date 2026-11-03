// Native details remain independent of the existing click-to-enquire card handler.
document.querySelectorAll('.property-listings-page details').forEach(details => {
  details.addEventListener('click', event => event.stopPropagation());
});
