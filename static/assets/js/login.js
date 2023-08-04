function login() {
  const username = document.querySelector(".cont_form_login input[type='text']").value;
  const password = document.querySelector(".cont_form_login input[type='password']").value;

  // Lógica para el inicio de sesión en el modelo Usuario
  // ...

  // Si el inicio de sesión es exitoso, puedes redirigir a la página del usuario
  // window.location.href = "/usuario/perfil/";
}

function sign_up() {
  const username = document.querySelector(".cont_form_sign_up input[placeholder='Username']").value;
  const email = document.querySelector(".cont_form_sign_up input[placeholder='Email']").value;
  const password = document.querySelector(".cont_form_sign_up input[placeholder='Password']").value;
  const confirmPassword = document.querySelector(".cont_form_sign_up input[placeholder='Confirm Password']").value;

  // Lógica para el registro de usuario en el modelo Usuario
  // ...

  // Si el registro es exitoso, puedes redirigir a la página de inicio de sesión
  // window.location.href = "/usuario/login/";
}

function change_to_login() {
  document.querySelector(".cont_forms").className = "cont_forms cont_forms_active_login";
  document.querySelector(".cont_form_login").style.display = "block";
  document.querySelector(".cont_form_sign_up").style.opacity = "0";

  setTimeout(function () {
    document.querySelector(".cont_form_login").style.opacity = "1";
  }, time_to_show_login);

  setTimeout(function () {
    document.querySelector(".cont_form_sign_up").style.display = "none";
  }, time_to_hidden_login);
}

function change_to_sign_up(at) {
  document.querySelector(".cont_forms").className = "cont_forms cont_forms_active_sign_up";
  document.querySelector(".cont_form_sign_up").style.display = "block";
  document.querySelector(".cont_form_login").style.opacity = "0";

  setTimeout(function () {
    document.querySelector(".cont_form_sign_up").style.opacity = "1";
  }, time_to_show_sign_up);

  setTimeout(function () {
    document.querySelector(".cont_form_login").style.display = "none";
  }, time_to_hidden_sign_up);
}

function hidden_login_and_sign_up() {
  document.querySelector(".cont_forms").className = "cont_forms";
  document.querySelector(".cont_form_sign_up").style.opacity = "0";
  document.querySelector(".cont_form_login").style.opacity = "0";

  setTimeout(function () {
    document.querySelector(".cont_form_sign_up").style.display = "none";
    document.querySelector(".cont_form_login").style.display = "none";
  }, time_to_hidden_all);
}
