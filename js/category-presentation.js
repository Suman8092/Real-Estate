// Keep complete project information accessible without expanding listing cards.
document.querySelectorAll('.reference-property-page .property-listing-card').forEach(card => {
  card.addEventListener('click', event => {
    const trigger = card.querySelector('[data-property-dialog]');
    const dialog = trigger && document.getElementById(trigger.dataset.propertyDialog);
    if (!dialog) return;
    event.stopImmediatePropagation();
    dialog.showModal();
  }, true);
});
