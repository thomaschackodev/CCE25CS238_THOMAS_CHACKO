// Client-side validation for the Add/Edit Booking form
document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('bookingForm');
    if (!form) return;

    form.addEventListener('submit', function (e) {
        var inputs = form.querySelectorAll('input[required]');
        var hasError = false;

        inputs.forEach(function (input) {
            var errorSpan = document.getElementById(input.name + '_error');
            if (input.value.trim() === '') {
                hasError = true;
                if (errorSpan) errorSpan.textContent = 'This field cannot be empty.';
                input.style.borderColor = '#dc2626';
            } else {
                if (errorSpan) errorSpan.textContent = '';
                input.style.borderColor = '#d1d5db';
            }
        });

        if (hasError) {
            e.preventDefault();
        }
    });
});
