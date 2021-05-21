console.log("Hello from modals!")


$(function () {
          // Log in & Sign up buttons
          // The formURL is given explicitly
          // $("#login").modalForm({
          //   formURL: "{% url 'auth:login' %}"
          // });
          //
          //
          // $("#signup").modalForm({
          //   formURL: "{% url 'auth:register' %}"
          // });
          //
          // $("#edit").modalForm({
          //   formURL: "{% url 'auth:edit' %}"
          // });

          


          $(".read-bookmark").each(function () {
              $(this).modalForm({formURL: $(this).data("form-url")});
          });
          
          $(".delete-bookmark").each(function () {
              $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
          });

          // Hide message
          $(".alert").fadeTo(2000, 500).slideUp(500, function () {
              $(".alert").slideUp(500);
          });
      });