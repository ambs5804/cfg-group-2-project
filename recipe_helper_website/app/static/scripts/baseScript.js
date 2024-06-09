function saveRecipeId(id) {
  // Retrieve existing saved IDs from local storage
  let savedIds = localStorage.getItem('savedRecipeIds');

  if (savedIds) {
    // Parse the existing IDs
    savedIds = JSON.parse(savedIds);
  } else {
    // Initialize an empty array if no IDs are saved yet
    savedIds = [];
  }
  // Check if the ID is already saved
  if (!savedIds.includes(id)) {
    // Add the new ID to the array
    savedIds.push(id);

    // Save the updated array back to local storage
    localStorage.setItem('savedRecipeIds', JSON.stringify(savedIds));

  }
}
