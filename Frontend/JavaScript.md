
# String methods

| Name | Description | Accepts | Return | Example |
| ---- | ----------- | ------- | ------ | ------- |
| at   | The at() method is used to find the character at the specified index, allows for positive and negative integers. Negative integers count back from the last string character.  | `index` The index (position) of the string character to be returned. | a new String consisting of the single UTF-16 code unit located at the specified offset | string.at(index) <br>[at](https://github.com/acvetochka/useful-links/blob/main/Frontend/JavaScript.md#at)
| concat | The concat() function concatenates the string arguments to the calling string and returns a new string. | `str1`, `…`, `strN` One or more strings to concatenate to str| A new string containing the combined text of the strings provided. | concat(str1, str2) <br>[concat](https://github.com/acvetochka/useful-links/blob/main/Frontend/JavaScript.md#concat) |
| endsWith | This method lets you determine whether or not a string ends with another string. This method is case-sensitive. |  `searchString` The characters to be searched for at the end of str <br> `endPosition` The end position at which searchString is expected to be found (the index of searchString's last character plus 1). Defaults to str.length. | `true` if the given characters are found at the end of the string, including when searchString is an empty string; otherwise, `false`. | string.endsWith(searchString, endPosition*) <br>   [endsWith](https://github.com/acvetochka/useful-links/blob/main/Frontend/JavaScript.md#endsWith) |
| includes | This method lets you determine whether or not a string includes another string. | `searchString` - A string to be searched for within str. Cannot be a regex.  <br>  `position` (optional) The position within the string at which to begin searching for searchString. (Defaults to 0.) | `true` if the search string is found anywhere within the given string, including when searchString is an empty string; otherwise, `false`. | string.includes(searchString, position*)<br> [includes](https://github.com/acvetochka/useful-links/blob/main/Frontend/JavaScript.md#includes) |
| indexOf | The indexOf() method of String values searches this string and returns the index of the first occurrence of the specified substring. | `searchString` Substring to search for. <br> `position`(optional) The method returns the index of the first occurrence of the specified substring at a position greater than or equal to position, which defaults to 0 | The index of the first occurrence of searchString found, or -1 if not found. | string.indexOf(searchString, position*)<br> [indexOf](https://github.com/acvetochka/useful-links/blob/main/Frontend/JavaScript.md#indexOf)  |
| lastIndexOf | searches this string and returns the index of the last occurrence of the specified substring | `searchString` Substring to search for.  <br> `position` (optional) The method returns the index of the last occurrence of the specified substring at a position less than or equal to position, which defaults to +Infinity | The index of the last occurrence of searchString found, or -1 if not found. | string.lastIndexOf(searchString, position) |

## Examples
### at
```javaScript
const sentence = 'The quick brown fox jumps over the lazy dog.';
let index = 5;
console.log(`An index of ${index} returns the character ${sentence.at(index)}`);
// Expected output: "An index of 5 returns the character u"
index = -4;
console.log(`An index of ${index} returns the character ${sentence.at(index)}`);
// Expected output: "An index of -4 returns the character d"
```

### concat 
```javaScript
const str1 = 'Hello';
const str2 = 'World';

console.log(str1.concat(' ', str2));
// Expected output: "Hello World"

console.log(str2.concat(', ', str1));
// Expected output: "World, Hello"
```

### endsWith

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

### includes 
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

### indexOf 
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

### lastIndexOf 
```javaScript
const paragraph = "I think Ruth's dog is cuter than your dog!";

const searchTerm = 'dog';

console.log(
  `Index of the last ${searchTerm} is ${paragraph.lastIndexOf(searchTerm)}`,
);
// Expected output: "Index of the last "dog" is 38"
```

