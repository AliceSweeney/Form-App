$(document).ready(function() {	
	const form = document.getElementById('myForm');
	const checkboxes = form.querySelectorAll('input[name="animal"]');

	form.addEventListener('submit', function(event) {
		let atLeastOneChecked = false;
		for (const checkbox of checkboxes) {
			if (checkbox.checked) {
				atLeastOneChecked = true;
				break;
			}
		}

		if (!atLeastOneChecked) {
			event.preventDefault(); // Prevent form submission
			alert('Please select at least one option.');
		}
	}); //Code from google AI adapted for this project
});