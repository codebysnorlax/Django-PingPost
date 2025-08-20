// Show floating help when password field is focused or has value
document.addEventListener("DOMContentLoaded", function () {
  var pwdField = document.querySelector(".field-with-help input");
  var help = document.querySelector(".field-with-help .field-help");
  if (!pwdField || !help) return;
  var toggle = function () {
    help.classList.toggle(
      "show",
      !!pwdField.value || document.activeElement === pwdField
    );
  };
  pwdField.addEventListener("focus", toggle);
  pwdField.addEventListener("blur", toggle);
  pwdField.addEventListener("input", toggle);
  toggle();
});
