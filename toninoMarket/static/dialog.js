// Ensure Bootstrap library is loaded before this script
const modalElement = document.getElementById("modal");
const modal = new bootstrap.Modal(modalElement);

htmx.on("htmx:afterSwap", (e) => {
    // Response targeting #dialog => show the modal
    if (e.detail.target.id === "dialog") {
        modal.show();
    }
});

