const unitConversions = {
  'cups:cups': 1,
  'tbsp:tbsp': 1,
  'tsp:tsp': 1,
  'g:g': 1,
  'oz:oz': 1,
  'fl oz:fl oz': 1,
  'ml:ml': 1,
  'cups:tbsp': 16,
  'tbsp:cups': 1 / 16,
  'cups:g': 250,
  'g:cups': 1 / 250,
  'cups:ml': 250,
  'ml:cups': 1 / 250,
  'tbsp:tsp': 3,
  'tsp:tbsp': 1 / 3,
  'tbsp:g': 15,
  'g:tbsp': 1 / 15,
  'tbsp:ml': 3,
  'ml:tbsp': 1 / 3,
  'tsp:g': 5,
  'g:tsp': 1 / 5,
  'tsp:ml': 5,
  'ml:tsp': 1 / 5,
  'oz:g': 28,
  'g:oz': 1 / 28,
  'fl oz:ml': 30,
  'ml:fl oz': 1 / 30,
  'cup:cup': 1,
  'cup:tbsp': 16,
  'tbsp:cup': 1 / 16,
  'cup:g': 250,
  'g:cup': 1 / 250,
  'cup:ml': 250,
  'ml:cup': 1 / 250,
};


function fractionToDecimal(fraction) {
  if (fraction.includes('/')) {
    const [numerator, denominator] = fraction.split('/');
    return parseFloat(numerator) / parseFloat(denominator);
  }
  return parseFloat(fraction);
}

function convertUnits() {

  const toUnitSelect = document.getElementById('to_unit');
  if (toUnitSelect.value === 'original') {
    location.reload();
  }
  const ddElements = document.querySelectorAll('dd');
  ddElements.forEach(dd => {
    const amountSpan = dd.querySelector('.amount');
    const fromUnitSpan = dd.querySelector('.from_unit');

    if (amountSpan && fromUnitSpan && toUnitSelect) {
      const amountText = amountSpan.textContent.trim();
      const fromUnit = fromUnitSpan.textContent.trim();
      const toUnit = toUnitSelect.value;

      // Handle mixed numbers (e.g., "1 1/2") by splitting and summing the parts
      const amountParts = amountText.split(' ');
      const amount = amountParts.reduce((total, part) => total + fractionToDecimal(part), 0);

      const conversionKey = `${fromUnit}:${toUnit}`;


      if (unitConversions.hasOwnProperty(conversionKey)) {
        const convertedAmount = amount * unitConversions[conversionKey];
        amountSpan.textContent = `${convertedAmount}`;
        fromUnitSpan.textContent = `${toUnit}`;
      }
    }
  });
}
