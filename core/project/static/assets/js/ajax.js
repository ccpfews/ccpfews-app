dormElement = {
  fullName: document.getElementById("consult_name"),
  email: document.getElementById("consult_email"),
  message: document.getElementById("consult_message"),
  submitBtn: document.getElementById("consult_submit"),
  formAlert: document.getElementById("consult_form-msg"),
};

//init form data object
const formData = new FormData();

//set post link
const formActionLink = "/contact/consultation/";

//get csrf token
const csrf = document.getElementsByName("csrfmiddlewaretoken");

//append form csrf to form data object
formData.append("csrfmiddlewaretoken", csrf[1].value);

dormElement.submitBtn.addEventListener("click", (e) => {
  e.preventDefault();

  //append data to form data object
  formData.append("consult_name", dormElement.fullName.value);
  formData.append("consult_email", dormElement.email.value);
  formData.append("consult_message", dormElement.message.value);

  $.ajax({
    type: "POST",
    url: formActionLink,
    data: formData,
    beforeSend: function () {
      console.log("before send");

      // reset alert
      dormElement.formAlert.style.display = "none";

      //disable submit btn.
      dormElement.submitBtn.style.pointerEvents = "none";
      dormElement.submitBtn.textContent = "Processing ...";
    },
    xhr: function (response) {
      const xhr = new window.XMLHttpRequest();
      let percent;
      xhr.upload.addEventListener("progress", (e) => {
        //calculate percentage
        percent = (e.loaded / e.total) * 100;
      });

      return xhr;
    },
    success: function (response) {
      //loop through error
      console.log(response);
      if (response.status === "error") {
        //reset all error fields firsts
        Array.from(document.querySelectorAll(".error-info")).forEach(
          (field) => {
            //set empty content
            field.textContent = "";

            //ensure error display is none
            field.style.display = "none";

            //reset all input error
            let inputs = document.querySelectorAll("input");
            Array.from(inputs).forEach((input) => {
              input.style.border = "none";
            });

            //reset text area
            let textarea_field = document.querySelector("textarea");
            textarea_field.style.border = "none";
          }
        );

        //loop through error
        for (let [key, value] of Object.entries(response.message)) {
          if (key !== "captcha") {
            //set error display text
            document.getElementById(`error-${key}`).textContent = value[0];
            //show error
            document.getElementById(`error-${key}`).style.display = "block";
            //add error styling to input
            document.getElementById(
              `error-${key}`
            ).previousElementSibling.style.border = "1px solid #dc3545";

            // style displayed alert
            dormElement.formAlert.style.display = "block";
            dormElement.formAlert.innerHTML = `Invalid Form Field(s). Kindly check field(s) and try again; all fields are required.`;
          }
        }
      } else {
        //style displayed alert
        dormElement.formAlert.style.display = "block";
        dormElement.formAlert.innerHTML = `${response.message}`;

        //reset form
        dormElement.fullName.value = "";
        dormElement.email.value = "";
        dormElement.message.value = "";

        //reset error
        Array.from(document.querySelectorAll(".error-info")).forEach(
          (field) => {
            //set empty content
            field.textContent = "";

            //ensure error display is none
            field.textContent = ''
            field.style.display = "none";

            //reset all input error
            let inputs = document.querySelectorAll("input");
            Array.from(inputs).forEach((input) => {
              input.style.border = "1px solid rgba(255,255,255,0.2)";
            });

            //reset text area
            let textarea_field = document.querySelector("textarea");
            textarea_field.style.border = "1px solid rgba(255,255,255,0.2)";
          }
        );
      }

      //reset submit btn as long there is a response.
      dormElement.submitBtn.style.pointerEvents = "all";
      dormElement.submitBtn.textContent = "SEND NOW";
    },
    error: function (error) {
      console.log(error);
    },
    cache: false,
    contentType: false,
    processData: false,
  });
});
