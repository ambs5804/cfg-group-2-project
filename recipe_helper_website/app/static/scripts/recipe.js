
let recipe_data = JSON.parse(localStorage.getItem('recipes'));

const path = window.location.pathname;
const segments = path.split('/');
const recipeId = segments[segments.length - 1];

var index;
recipe_data.some(function (recipe, i) {
  if (recipe.id == recipeId) {
    index = i;
    return true;
  }
});

const cur_recipe = recipe_data[index];


// Function to render the list of ingredients
function renderIngredientList(recipe) {
  let ingredientHTML = `<h1 class="header1" >${recipe['title']}</h1> <img src="${recipe['img']}"> <a href="${recipe['url']}" target="blank">
    <p>Click here to see full recipe</p></a> <button class = "small-button"> Save </button>`;
  let html = '';
  cur_recipe['ingredients'].forEach((ingredient) => {
    if (ingredient.convertable === true) {
      html = `
                        <dd><span class= "amount">${ingredient.quantity}</span><span class="from_unit"> ${ingredient.unit}</span> ${ingredient.item}<dd>`;
      console.log('cconvert')
      console.log(html);
      ingredientHTML += html;
    } else {
      html = `
                        <dd><span>${ingredient.item}</span><br><dd>`;
      console.log('no convert')
      console.log(html);

      ingredientHTML += html;
    }
  });
  document.querySelector('.ingredient-list').innerHTML = ingredientHTML;
}

// Render the ingredients list
renderIngredientList(cur_recipe);