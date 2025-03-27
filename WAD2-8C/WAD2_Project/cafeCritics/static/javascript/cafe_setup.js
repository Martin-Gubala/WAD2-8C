<<<<<<< HEAD
// Removed logic for dynamically adding drinks

// Function to remove a drink form dynamically
function removeDrink(index) {
    const drinkForm = document.getElementById(`drink-${index}`);
    if (drinkForm) {
        drinkForm.remove();
    }
}
=======
document.getElementById('add-drink').addEventListener('click', function() {
    // Get the drinks container and the TOTAL_FORMS management field.
    const container = document.getElementById('drinks-container');
    let totalForms = document.getElementById('id_drinks-TOTAL_FORMS');
    let index = parseInt(totalForms.value);
    
    // Increment TOTAL_FORMS count.
    totalForms.value = index + 1;
    
    // Create new drink form HTML.
    const newFormHtml = `
        <div class="drink-form">
            <label for="id_drinks-${index}-name" class="custom-color">Drink Name:</label>
            <input type="text" name="drinks-${index}-name" id="id_drinks-${index}-name">
            <label for="id_drinks-${index}-price" class="custom-color">Price:</label>
            <input type="text" name="drinks-${index}-price" id="id_drinks-${index}-price">
        </div>
    `;
    
    // Append the new drink form HTML to the container.
    container.insertAdjacentHTML('beforeend', newFormHtml);
});
>>>>>>> 5c5b023970d3a7ad167b5810c26539ca9e9a465b
