// Add functionality to toggle dropdown visibility on click
const dropdowns = document.querySelectorAll('.dropdown');

dropdowns.forEach(dropdown => {
    const button = dropdown.querySelector('.dropdown-button'); // Select the button for the current dropdown
    const dropdownContent = dropdown.querySelector('.dropdown-content'); // Select the dropdown menu
    const options = dropdown.querySelectorAll('.dropdown-content a'); // All the links (options)

    // Toggle the dropdown visibility when clicking on the button
    button.addEventListener('click', (event) => {
        event.stopPropagation(); // Prevent the event from bubbling up to the window
        
        // First, close all other dropdowns
        dropdowns.forEach(otherDropdown => {
            const otherDropdownContent = otherDropdown.querySelector('.dropdown-content');
            if (otherDropdown !== dropdown) {
                otherDropdownContent.style.display = 'none';
                otherDropdown.classList.remove('open'); // Remove the open class from other dropdowns
            }
        });

        // Toggle the current dropdown
        if (dropdownContent.style.display === 'block') {
            dropdownContent.style.display = 'none';
            dropdown.classList.remove('open'); // Remove the open class when closed
        } else {
            dropdownContent.style.display = 'block';
            dropdown.classList.add('open'); // Add the open class when opened
        }
    });

    // When an option is clicked, update the button text and close the dropdown
    options.forEach(option => {
        option.addEventListener('click', (e) => {
            // Update the button text with the selected option
            button.textContent = e.target.textContent;

            // Close the dropdown after selection
            dropdownContent.style.display = 'none';
            dropdown.classList.remove('open'); // Remove the open class when an option is selected
        });
    });
});

// Close dropdown if clicked outside of it
window.addEventListener('click', (event) => {
    dropdowns.forEach(dropdown => {
        const dropdownContent = dropdown.querySelector('.dropdown-content');
        if (!dropdown.contains(event.target)) {
            dropdownContent.style.display = 'none';
            dropdown.classList.remove('open'); // Remove the open class when clicked outside
        }
    });
});