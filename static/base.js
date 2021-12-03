$(document).ready(() => {
    const form_fields = document.getElementsByTagName('input');
    form_fields[1].placeholder = 'Enter Artist Name';
    form_fields[2].placeholder = 'Enter Artist Age';
    form_fields[3].placeholder = 'Enter Song Title';
    form_fields[5].placeholder = 'Enter Album Cover Image URL';
    form_fields[6].placeholder = 'Enter Date Published';
    
    for(let f in form_fields) {
        form_fields[f].className += 'form-control'
    }

    $('.toast').toast('show');


    // $("#MyModal").modal();

    console.log($("#updateModal"));

    $('#updateModal').on('show.bs.modal', function (event) {

        
        var button = $(event.relatedTarget) // Button that triggered the modal
        var id = button.data('id') // Extract info from data-* attributes
        console.log(id)
        // // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        // var modal = $(this)
        // modal.find('.modal-title').text('New message to ' + recipient)
        // modal.find('.modal-body input').val(recipient)
    })

});
