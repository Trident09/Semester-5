// Function to extract the word 'doctor' from a string
function extractDoctor(phrase) {
  var word = "doctor";
  const startIndex = phrase.indexOf(word);
  const endIndex = startIndex + word.length;
  return phrase.slice(startIndex, endIndex);
}

const testStr = "Property to Alert the Text Input";
console.log(`Length of '${testStr}': ${testStr.length}`);

const str1 = "Hello";
const str2 = "World";
console.log(`Concatenation of '${str1}' and '${str2}': ${str1.concat(str2)}`);

console.log(`'${testStr}' in upper case: ${testStr.toUpperCase()}`);
console.log(`'${testStr}' in lower case: ${testStr.toLowerCase()}`);

const phrase = "an apple a day keeps the doctor away";
console.log(`Extracted 'doctor' from '${phrase}': ${extractDoctor(phrase)}`);
