# String methods

## Menu
- [at](#at)
- [concat](#concat)
- [endsWith](#endsWith)
- [includes](#includes)
- [indexOf](#indexOf)
- [lastIndexOf](#lastIndexOf)
- [localeCompare](#localeCompare)
- [match](#match)

## at

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| at   | The at() method is used to find the character at the specified index, allows for positive and negative integers. Negative integers count back from the last string character.  | `index` The index (position) of the string character to be returned. | a new String consisting of the single UTF-16 code unit located at the specified offset | string.at(index) |

**Example**
```javaScript
const sentence = 'The quick brown fox jumps over the lazy dog.';
let index = 5;
console.log(`An index of ${index} returns the character ${sentence.at(index)}`);
// Expected output: "An index of 5 returns the character u"
index = -4;
console.log(`An index of ${index} returns the character ${sentence.at(index)}`);
// Expected output: "An index of -4 returns the character d"
```

[Back to Menu](#Menu)

## concat

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| concat | The concat() function concatenates the string arguments to the calling string and returns a new string. | `str1`, `…`, `strN` One or more strings to concatenate to str| A new string containing the combined text of the strings provided. | concat(str1, str2) |

**Example**
```javaScript
const str1 = 'Hello';
const str2 = 'World';

console.log(str1.concat(' ', str2));
// Expected output: "Hello World"

console.log(str2.concat(', ', str1));
// Expected output: "World, Hello"
```

[Back to Menu](#Menu)

## endsWith

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| endsWith | This method lets you determine whether or not a string ends with another string. This method is case-sensitive. |  `searchString` The characters to be searched for at the end of str <br> `endPosition` The end position at which searchString is expected to be found (the index of searchString's last character plus 1). Defaults to str.length. | `true` if the given characters are found at the end of the string, including when searchString is an empty string; otherwise, `false`. | string.endsWith(searchString, endPosition*) |

**Example**
```javaScript
const str1 = 'Cats are the best!';
console.log(str1.endsWith('best!'));
// Expected output: true

console.log(str1.endsWith('best', 17));
// Expected output: true

const str2 = 'Is this a question?';
console.log(str2.endsWith('question'));
// Expected output: false
```

[Back to Menu](#Menu)

## includes

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| includes | This method lets you determine whether or not a string includes another string. | `searchString` - A string to be searched for within str. Cannot be a regex.  <br>  `position` (optional) The position within the string at which to begin searching for searchString. (Defaults to 0.) | `true` if the search string is found anywhere within the given string, including when searchString is an empty string; otherwise, `false`. | string.includes(searchString, position*) |

**Example**
```javaScript
const sentence = 'The quick brown fox jumps over the lazy dog.';
const word = 'fox';
console.log(
  `The word "${word}" ${
    sentence.includes(word) ? 'is' : 'is not'
  } in the sentence`,
);
// Expected output: "The word "fox" is in the sentence"
```

[Back to Menu](#Menu)

## indexOf

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| indexOf | The indexOf() method of String values searches this string and returns the index of the first occurrence of the specified substring. | `searchString` Substring to search for. <br> `position`(optional) The method returns the index of the first occurrence of the specified substring at a position greater than or equal to position, which defaults to 0 | The index of the first occurrence of searchString found, or -1 if not found. | string.indexOf(searchString, position*) |

**Example**
```javaScript
const paragraph = "I think Ruth's dog is cuter than your dog!";

const searchTerm = 'dog';
const indexOfFirst = paragraph.indexOf(searchTerm);

console.log(`The index of the first "${searchTerm}" is ${indexOfFirst}`);
// Expected output: "The index of the first "dog" is 15"

console.log(
  `The index of the second "${searchTerm}" is ${paragraph.indexOf(
    searchTerm,
    indexOfFirst + 1,
  )}`,
);
// Expected output: "The index of the second "dog" is 38"
```

[Back to Menu](#Menu)

## lastIndexOf

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| lastIndexOf | searches this string and returns the index of the last occurrence of the specified substring | `searchString` Substring to search for.  <br> `position` (optional) The method returns the index of the last occurrence of the specified substring at a position less than or equal to position, which defaults to +Infinity | The index of the last occurrence of searchString found, or -1 if not found. | string.lastIndexOf(searchString, position)|

**Example**
```javaScript
const paragraph = "I think Ruth's dog is cuter than your dog!";

const searchTerm = 'dog';

console.log(
  `Index of the last ${searchTerm} is ${paragraph.lastIndexOf(searchTerm)}`,
);
// Expected output: "Index of the last "dog" is 38"
```

[Back to Menu](#Menu)

## localeCompare

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| localeCompare | The localeCompare() method of String values returns a number indicating whether this string comes before, or after, or is the same as the given string in sort order. | `compareString` The string against which the referenceStr is compared. <br> `locales` (Optional) - A string with a BCP 47 language tag, or an array of such strings. <br> `options` (Optional) - An object adjusting the output format. | A negative number if referenceStr occurs before compareString; positive if the referenceStr occurs after compareString; 0 if they are equivalent. | localeCompare(compareString, locales, options) |

**Example**
```javaScript
const a = 'réservé'; // With accents, lowercase
const b = 'RESERVE'; // No accents, uppercase

console.log(a.localeCompare(b));
// Expected output: 1
console.log(a.localeCompare(b, 'en', { sensitivity: 'base' }));
// Expected output: 0
```

[Back to Menu](#Menu)

## match

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| match |The match() method of String values retrieves the result of matching this string against a regular expression. | `regexp` A regular expression object, or any object that has a Symbol.match method. | An Array whose contents depend on the presence or absence of the global (g) flag, or null if no matches are found. | match(regexp)|

**Example**
```javaScript
const str = "For more information, see Chapter 3.4.5.1";
const re = /see (chapter \d+(\.\d)*)/i;
const found = str.match(re);

console.log(found);
// [
//   'see Chapter 3.4.5.1',
//   'Chapter 3.4.5.1',
//   '.1',
//   index: 22,
//   input: 'For more information, see Chapter 3.4.5.1',
//   groups: undefined
// ]
```

[Back to Menu](#Menu)
