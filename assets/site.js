function toggleMobileNav() {
  var nav = document.getElementById('mobileNav');
  var btn = document.getElementById('navToggleBtn');
  var open = nav.classList.toggle('open');
  btn.setAttribute('aria-expanded', open ? 'true' : 'false');
}
