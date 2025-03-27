document.getElementById('add-drink').addEventListener('click', function() {
    const container = document.getElementById('drinks-container');
    const index = container.children.length - 1; // Get index for the next drink item
    // HTML for the new drink form, using backticks for multi-line strings
    const drinkForm = `
        <div class="drink-form">
            <label for="drinks-${index}-name" class="custom-color">Drink Name:</label>
            <input type="text" name="drinks-${index}-name" id="drinks-${index}-name">
            <label for="drinks-${index}-photo" class="custom-color">Drink Photo:</label>
            <input type="file" name="drinks-${index}-photo" id="drinks-${index}-photo">
        </div>
    `;
    // Insert the new drink form into the container
    container.insertAdjacentHTML('beforeend', drinkForm);
});