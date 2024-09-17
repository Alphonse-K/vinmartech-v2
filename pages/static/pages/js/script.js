document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        // Check if the current page URL matches the link's href
        if (link.href === window.location.href) {
            // Remove .active class from all links
            navLinks.forEach(link => link.classList.remove('active'));

            // Add .active class to the matching link
            link.classList.add('active');
        }
    });
});