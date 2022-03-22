function initBootstrapForms() {
    $("form.bootstrap-form").find("input,textarea").addClass("form-control");
    $("form.bootstrap-form").find("input[type='submit']").removeClass("form-control");
}

$(document).ready(function(){
    initBootstrapForms();
});