
# String methods

| Name | Description | Accepts | Return | Example |
| ---- | ----------- | ------- | ------ | ------- |
| at   |  | integer value | a new String consisting of the single UTF-16 code unit located at the specified offset | string.at(index) <br> [at](https://github.com/acvetochka/useful-links/new/main/Frontend#at) |
| concat | The concat() function concatenates the string arguments to the calling string and returns a new string. | One or more strings to concatenate to str| A new string containing the combined text of the strings provided. | concat(str1, str2) <br>[concat](https://github.com/acvetochka/useful-links/new/main/Frontend#concat) |
| endsWith | This method lets you determine whether or not a string ends with another string. This method is case-sensitive. | - `searchString` The characters to be searched for at the end of str <br>- `endPosition` The end position at which searchString is expected to be found (the index of searchString's last character plus 1). Defaults to str.length. | `true` if the given characters are found at the end of the string, including when searchString is an empty string; otherwise, `false`. | <br>const str1 = 'Cats are the best!';<br>console.log(str1.endsWith('best!'));<br>// Expected output: true<br>console.log(str1.endsWith('best', 17));<br>// Expected output: true<br>const str2 = 'Is this a question?';<br>console.log(str2.endsWith('question'));<br>// Expected output: false

## Examples
### at
```
const sentence = 'The quick brown fox jumps over the lazy dog.';
let index = 5;
console.log(`An index of ${index} returns the character ${sentence.at(index)}`);
// Expected output: "An index of 5 returns the character u"
index = -4;
console.log(`An index of ${index} returns the character ${sentence.at(index)}`);
// Expected output: "An index of -4 returns the character d"
```

### concat 
```
const str1 = 'Hello';
const str2 = 'World';

console.log(str1.concat(' ', str2));
// Expected output: "Hello World"

console.log(str2.concat(', ', str1));
// Expected output: "World, Hello"
```

### endsWith

```
const sentence = 'The quick brown fox jumps over the lazy dog.';
let index = 5;
console.log(`An index of ${index} returns the character ${sentence.at(index)}`);
// Expected output: "An index of 5 returns the character u"
index = -4;
console.log(`An index of ${index} returns the character ${sentence.at(index)}`);
// Expected output: "An index of -4 returns the character d" |
```
