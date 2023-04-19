const form = document.querySelector(".contact_form");

form.addEventListener("submit", function (e) {
  e.preventDefault();
  const name = document.querySelector("#id_name").value;
  const email = document.querySelector("#id_email").value;
  const message = document.querySelector("#id_message").value;
  const csrf_token = document.querySelector(
    "input[name=csrfmiddlewaretoken]"
  ).value;

  $.ajax({
    type: "POST",
    url: "/",
    data: {
      name: name,
      email: email,
      message: message,
      csrfmiddlewaretoken: csrf_token,
    },
    success: function (response) {
      if (response.status === "success") {
        swal({
          title: "Your message was sent successfully!",
          text: "",
          icon: "success",
        });
      } else {
        swal({
          title: "There was a problem sending your message",
          text: "",
          icon: "error",
        });
      }
      form.reset();
    },
  });
});
