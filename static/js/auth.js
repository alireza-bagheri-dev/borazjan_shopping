document.addEventListener('DOMContentLoaded', function () {
    // Add smooth scrolling to the login button
    const loginButton = document.querySelector('.btn-primary');
    if (loginButton) {
        loginButton.addEventListener('click', function (event) {
            event.preventDefault();
            alert('شما به صفحه ورود هدایت خواهید شد!');
            window.location.href = this.getAttribute('href');
        });
    }

    // Example: Add a loading spinner on button click (Optional)
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            this.textContent = 'در حال بارگذاری...';
            this.disabled = true;
            setTimeout(() => {
                this.textContent = 'ورود به حساب کاربری';
                this.disabled = false;
            }, 2000); // Simulate a 2-second delay
        });
    });
});
