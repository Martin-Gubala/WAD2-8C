//Function to add a new drink row in the edit cafe form
function addDrinkRow() {
    //Get the management form input for TOTAL_FORMS
    let totalFormsInput = document.querySelector('input[name="drinks-TOTAL_FORMS"]');
    let currentCount = parseInt(totalFormsInput.value);
    let newIndex = currentCount;
    
    //Create a new table row with the correct input names for a new form
    let newRow = document.createElement('tr');
    newRow.innerHTML = `
        <td>
            <input type="text" name="drinks-${newIndex}-name" class="form-control" placeholder="Drink Name">
        </td>
        <td>
            <input type="number" name="drinks-${newIndex}-price" class="form-control" placeholder="Price">
        </td>
        <td>
            <button type="button" class="btn btn-danger btn-sm" onclick="deleteNewDrinkRow(this)">Delete</button>
            <input type="checkbox" name="drinks-${newIndex}-DELETE" style="display:none;">
        </td>
    `;
    document.getElementById('drinks-table-body').appendChild(newRow);
    totalFormsInput.value = currentCount + 1;
}

// Function to mark an existing drink row for deletion and hide it
function deleteExistingDrinkRow(btn) {
    const row = btn.closest('tr');
    // Find the DELETE checkbox in this row
    const deleteCheckbox = row.querySelector('input[type="checkbox"][name$="-DELETE"]');
    if (deleteCheckbox) {
        deleteCheckbox.checked = true;
    }
    row.style.display = 'none';
}

// Function to mark a newly added drink row for deletion and hide it
function deleteNewDrinkRow(btn) {
    const row = btn.closest('tr');
    const deleteCheckbox = row.querySelector('input[type="checkbox"][name$="-DELETE"]');
    if (deleteCheckbox) {
        deleteCheckbox.checked = true;
    }
    row.style.display = 'none';
}