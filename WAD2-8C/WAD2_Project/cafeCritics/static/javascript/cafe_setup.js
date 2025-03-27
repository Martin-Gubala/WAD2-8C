// Removed logic for dynamically adding drinks

// Function to remove a drink form dynamically
function removeDrink(index) {
    const drinkForm = document.getElementById(`drink-${index}`);
    if (drinkForm) {
        drinkForm.remove();
    }
}
