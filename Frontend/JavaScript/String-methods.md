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
- [matchAll](#matchAll)
- [padEnd](#padEnd)
- [padStart](#padStart)
- [repeat](#repeat)
- [replace](#replace)
- [replaceAll](#replaceAll)
- [search](#search)
- [slice](#slice)
- [split](#split)
- [startsWith](#startsWith)
- [substring](#substring)

## at

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| at   | The at() method is used to find the character at the specified index, allows for positive and negative integers. Negative integers count back from the last string character.  | `index` The index (position) of the string character to be returned. | a new `String` consisting of the single UTF-16 code unit located at the specified offset | string.at(index) |

<details>
  <summary>ua</summary>

|  Назва	|Опис |	Приймає |	Повертає |	Синтаксис |
| ---- | ----------- | ------- | ------ | ------- |
| at	|Метод at() використовується для отримання символу за вказаним індексом; підтримує як додатні, так і від’ємні числа. Від’ємні індекси відраховуються від останнього символу рядка.	| index — індекс (позиція) символу рядка, який потрібно повернути. |	Новий рядок, що складається з одного UTF-16 коду символу на вказаній позиції. | string.at(index) |
</details>

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
| concat | The concat() function concatenates the string arguments to the calling string and returns a new string. | `str1`, `…`, `strN` One or more strings to concatenate to str| A new `string` containing the combined text of the strings provided. | concat(str1, str2) |

<details>
  <summary>ua</summary>

|  Назва	|Опис |	Приймає |	Повертає |	Синтаксис |
| ---- | ----------- | ------- | ------ | ------- |
| concat	|! Функція concat() об’єднує (конкатенує) рядки-аргументи з вихідним рядком і повертає новий рядок.	| str1, …, strN — один або кілька рядків для об’єднання з вихідним рядком. | Новий рядок, що містить об’єднаний текст усіх переданих рядків. |	concat(str1, str2) |
</details>

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

<details>
  <summary>ua</summary>

| Назва |	Опис |	Приймає |	Повертає |	Синтаксис |
| ---- | ----------- | ------- | ------ | ------- |
| endsWith	| Метод endsWith() дозволяє визначити, чи закінчується рядок на інший заданий рядок. Метод чутливий до регістру.	| `searchString` — символи, які потрібно знайти в кінці рядка str. <br/> `endPosition` — позиція в рядку, на якій очікується знайти searchString (це індекс останнього символу searchString плюс 1). За замовчуванням — str.length. |	`true`, якщо вказані символи знайдено в кінці рядка (включно з випадком, коли searchString порожній); інакше — `false`.	| string.endsWith(searchString, endPosition*) |
</details>

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

<details>
<summary>ua</summary>

  | Назва        | Опис                                                                           | Приймає                                                                                                                                                                                                       | Повертає                                                                                                                              | Синтаксис                                  |
| ------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **includes** | Метод **includes()** дозволяє визначити, чи містить рядок інший заданий рядок. | `searchString` — рядок, який потрібно знайти в межах `str`. Не може бути регулярним виразом.  <br>  `position` (необов’язково) — позиція в рядку, з якої почати пошук `searchString`. (За замовчуванням — 0.) | `true`, якщо рядок пошуку знайдено будь-де в межах даного рядка (включно з випадком, коли `searchString` порожній); інакше — `false`. | `string.includes(searchString, position*)` |
</details>

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
| indexOf | The indexOf() method of String values searches this string and returns the index of the first occurrence of the specified substring. | `searchString` Substring to search for. <br> `position`(optional) The method returns the index of the first occurrence of the specified substring at a position greater than or equal to position, which defaults to 0 | The `index of the first occurrence` of searchString found, or `-1` if not found. | string.indexOf(searchString, position*) |

<details>
  <summary>ua</summary>

| Назва       | Опис    | Приймає    | Повертає    | Синтаксис    |
| ----------- | -------- | ------ | -------------| ------------ |
| **indexOf** | Метод **indexOf()** для значень типу String виконує пошук у рядку та повертає індекс першого входження вказаного підрядка. | `searchString` — підрядок для пошуку. <br> `position` (необов’язково) — метод повертає індекс першого входження підрядка, починаючи з позиції, більшої або рівної `position`. За замовчуванням — 0. | `Індекс першого входження` підрядка `searchString`, або `-1`, якщо не знайдено. | `string.indexOf(searchString, position*)` |

</details>


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
| lastIndexOf | searches this string and returns the index of the last occurrence of the specified substring | `searchString` Substring to search for.  <br> `position` (optional) The method returns the index of the last occurrence of the specified substring at a position less than or equal to position, which defaults to +Infinity | The `index of the last occurrence` of searchString found, or `-1` if not found. | string.lastIndexOf(searchString, position)|


<details>
  <summary>ua</summary>
  
| Назва           | Опис      | Приймає      | Повертає      | Синтаксис       |
| --------------- | --------- | ------------- | ------------- | ------------------- |
| **lastIndexOf** | Виконує пошук у рядку та повертає індекс останнього входження вказаного підрядка. | `searchString` — підрядок для пошуку. <br> `position` (необов’язково) — метод повертає індекс останнього входження підрядка на позиції, меншій або рівній `position`. За замовчуванням — `+Infinity`. | `Індекс останнього входження` підрядка `searchString`, або `-1`, якщо не знайдено. | `string.lastIndexOf(searchString, position)` |


</details>


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
| localeCompare | The localeCompare() method of String values returns a number indicating whether this string comes before, or after, or is the same as the given string in sort order. | `compareString` The string against which the referenceStr is compared. <br> `locales` (Optional) - A string with a BCP 47 language tag, or an array of such strings. <br> `options` (Optional) - An object adjusting the output format. | - A `negative number` if referenceStr occurs before compareString; <br/> = `positive` if the referenceStr occurs after compareString; <br/> - 0 if they are equivalent. | localeCompare(compareString, locales, options) |


<details>
  <summary>ua</summary>

| Назва             | Опис                                                                                                                                                                        | Приймає                                                                                                                                                                                                                     | Повертає                                                                                                                            | Синтаксис                                        |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **localeCompare** | Метод **localeCompare()** для значень типу String повертає число, яке вказує, чи розташований рядок до, після або на тому ж місці, що й заданий рядок у порядку сортування. | `compareString` — рядок, з яким порівнюється `referenceStr`. <br> `locales` (необов’язково) — рядок із мовним тегом BCP 47 або масив таких рядків. <br> `options` (необов’язково) — об’єкт для налаштування формату виводу. | - `Від’ємне число`, якщо `referenceStr` розташований перед `compareString`; <br/> - `додатне число`, якщо після; <br/> - `0`, якщо вони еквівалентні. | `localeCompare(compareString, locales, options)` |


</details>


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
| match |The match() method of String values retrieves the result of matching this string against a regular expression. | `regexp` - A regular expression object, or any object that has a Symbol.match method. | An `Array` whose contents depend on the presence or absence of the global (g) flag, or `null` if no matches are found. | match(regexp)|


 <details>
  <summary>ua</summary>
  
| Назва           | Опис      | Приймає      | Повертає      | Синтаксис       |
| --------------- | --------- | ------------- | ------------- | ------------------- |
| **match** | Метод **match()** для значень типу String отримує результат зіставлення рядка з регулярним виразом. | `regexp` — об’єкт регулярного виразу або будь-який об’єкт, що має метод `Symbol.match`. | `Масив (Array)`, вміст якого залежить від наявності або відсутності глобального прапора `g`, або `null`, якщо збігів не знайдено. | `match(regexp)` |


</details>


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

## matchAll

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| matchAll | The matchAll() method of String values returns an iterator of all results matching this string against a regular expression, including capturing groups. | `regexp` - A regular expression object, or any object that has a Symbol.matchAll method. | An `iterable iterator object` (which is not restartable) of matches or an empty iterator if no matches are found. Each value yielded by the iterator is an array with the same shape as the return value of RegExp.prototype.exec(). | matchAll(regexp) |

<details>
  <summary>ua</summary>

| Назва           | Опис      | Приймає      | Повертає      | Синтаксис       |
| --------------- | --------- | ------------- | ------------- | ------------------- |
| **matchAll** | Метод **matchAll()** для значень типу String повертає ітератор усіх результатів зіставлення рядка з регулярним виразом, включно з групами захоплення. | `regexp` — об’єкт регулярного виразу або будь-який об’єкт, що має метод `Symbol.matchAll`. | `Ітерабельний об’єкт-ітератор` (який не можна перезапустити) зі збігами, або порожній ітератор, якщо збігів не знайдено. Кожне значення, яке повертає ітератор, є масивом з тією ж структурою, що й результат `RegExp.prototype.exec()`. | `matchAll(regexp)` |


</details>


**Example** 
```javaScript
const regexp = /t(e)(st(\d?))/g;
const str = "test1test2";

const array = [...str.matchAll(regexp)];

console.log(array[0]);
// Expected output: Array ["test1", "e", "st1", "1"]

console.log(array[1]);
// Expected output: Array ["test2", "e", "st2", "2"]
```

[Back to Menu](#Menu)

## padEnd

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| padEnd | The padEnd() method of String values pads this string with a given string (repeated, if needed) so that the resulting string reaches a given length. The padding is applied from the end of this string. | `targetLength` - The length of the resulting string once the current str has been padded. If the value is less than or equal to str.length, the current string will be returned as-is. <br> `padString` (Optional) - The string to pad the current str with. If padString is too long to stay within targetLength, it will be truncated: for left-to-right languages the left-most part and for right-to-left languages the right-most will be applied. The default value for this parameter is " " (U+0020).| A `String` of the specified targetLength with the padString applied at the end of the current str. | padEnd(targetLength) <br> padEnd(targetLength, padString) |

 <details>
  <summary>ua</summary>

| Назва           | Опис      | Приймає      | Повертає      | Синтаксис       |
| --------------- | --------- | ------------- | ------------- | ------------------- |
|padEnd	| Метод padEnd() для значень типу String доповнює рядок вказаним рядком (повторюваним за потреби), щоб отриманий рядок досяг певної довжини. Доповнення застосовується з кінця вихідного рядка.	| `targetLength` — довжина отриманого рядка після доповнення. Якщо значення менше або дорівнює str.length, повертається вихідний рядок без змін. <br> `padString` (необов’язково) — рядок, яким доповнюється вихідний рядок. Якщо padString занадто довгий для розміщення в межах targetLength, він буде обрізаний: для мов з написанням зліва направо використовується ліва частина, а для мов з написанням справа наліво — права. Значення за замовчуванням — " " (U+0020).	| Рядок (String) заданої довжини targetLength з доданим у кінці padString.	| padEnd(targetLength) <br> padEnd(targetLength, padString) |


</details>



**Example** 
```javaScript
const str1 = "Breaded Mushrooms";

console.log(str1.padEnd(25, "."));
// Expected output: "Breaded Mushrooms........"
const str2 = "200";

console.log(str2.padEnd(5));
// Expected output: "200  "
```

[Back to Menu](#Menu)

## padStart

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| padStart | The padStart() method of String values pads this string with another string (multiple times, if needed) until the resulting string reaches the given length. The padding is applied from the start of this string. | `targetLength` - The length of the resulting string once the current str has been padded. If the value is less than or equal to str.length, then str is returned as-is. <br> `padString` (Optional) - The string to pad the current str with. If padString is too long to stay within the targetLength, it will be truncated from the end. The default value is the unicode "space" character (U+0020). | A `String` of the specified targetLength with padString applied from the start. | padStart(targetLength) <br> padStart(targetLength, padString) |


<!-- <details>
  <summary>ua</summary>


</details>
-->

**Example** 
```javaScript
const str1 = "5";

console.log(str1.padStart(2, "0"));
// Expected output: "05"

const fullNumber = "2034399002125581";
const last4Digits = fullNumber.slice(-4);
const maskedNumber = last4Digits.padStart(fullNumber.length, "*");

console.log(maskedNumber);
// Expected output: "************5581"
```

[Back to Menu](#Menu)

## repeat

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| repeat |  The repeat() method of String values constructs and returns a new string which contains the specified number of copies of this string, concatenated together. | `count` - An integer between 0 and +Infinity, indicating the number of times to repeat the string. | A new `string` containing the specified number of copies of the given string. | repeat(count) |

<!-- <details>
  <summary>ua</summary>


</details>
-->


**Example**
```javaScript
const mood = "Happy! ";

console.log(`I feel ${mood.repeat(3)}`);
// Expected output: "I feel Happy! Happy! Happy! "
```

[Back to Menu](#Menu)

## replace

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| replace | The replace() method of String values returns a new string with one, some, or all matches of a pattern replaced by a replacement.  | `pattern` - Can be a string or an object with a Symbol.replace method — the typical example being a regular expression. <br> `replacement` -Can be a string or a function. | A new `string`, with one, some, or all matches of the pattern replaced by the specified replacement. | replace(pattern, replacement) |


<!-- <details>
  <summary>ua</summary>


</details>
-->


**Example**
```javaScript 
const paragraph = "I think Ruth's dog is cuter than your dog!";

console.log(paragraph.replace("Ruth's", "my"));
// Expected output: "I think my dog is cuter than your dog!"

const regex = /Dog/i;
console.log(paragraph.replace(regex, "ferret"));
// Expected output: "I think Ruth's ferret is cuter than your dog!" 
```

[Back to Menu](#Menu)

## replaceAll

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| replaceAll | The replaceAll() method of String values returns a new string with all matches of a pattern replaced by a replacement. | `pattern`- Can be a string or an object with a Symbol.replace method — the typical example being a regular expression. If pattern is a regex, then it must have the global (g) flag set, or a TypeError is thrown. <br> `replacement` - Can be a string or a function. | A new `string`, with all matches of a pattern replaced by a replacement. | replaceAll(pattern, replacement) |


<!-- <details>
  <summary>ua</summary>


</details>
-->


**Example**
```javaScript
const paragraph = "I think Ruth's dog is cuter than your dog!";

console.log(paragraph.replaceAll("dog", "monkey"));
// Expected output: "I think Ruth's monkey is cuter than your monkey!"

// Global flag required when calling replaceAll with regex
const regex = /Dog/gi;
console.log(paragraph.replaceAll(regex, "ferret"));
// Expected output: "I think Ruth's ferret is cuter than your ferret!"
```

[Back to Menu](#Menu)

## search

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| search | The search() method of String values executes a search for a match between a regular expression and this string, returning the index of the first match in the string. | `regexp`- A regular expression object, or any object that has a Symbol.search method. | The `index of the first match` between the regular expression and the given string, or `-1` if no match was found. | search(regexp) |


<!-- <details>
  <summary>ua</summary>


</details>
-->


**Example**
```javaScript
const paragraph = "I think Ruth's dog is cuter than your dog!";

// Anything not a word character, whitespace or apostrophe
const regex = /[^\w\s']/g;

console.log(paragraph.search(regex));
// Expected output: 41

console.log(paragraph[paragraph.search(regex)]);
// Expected output: "!"
```

[Back to Menu](#Menu)

## slice

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| slice | The slice() method of String values extracts a section of this string and returns it as a new string, without modifying the original string. | `indexStart` - The index of the first character to include in the returned substring. <br> `indexEnd` (Optional) - The index of the first character to exclude from the returned substring. | A new `string` containing the extracted section of the string. | slice(indexStart) <br> slice(indexStart, indexEnd) |


<!-- <details>
  <summary>ua</summary>


</details>
-->


**Example**
```javaScript
const str = "The quick brown fox jumps over the lazy dog.";

console.log(str.slice(31));
// Expected output: "the lazy dog."

console.log(str.slice(4, 19));
// Expected output: "quick brown fox"

console.log(str.slice(-4));
// Expected output: "dog."

console.log(str.slice(-9, -5));
// Expected output: "lazy"
```

[Back to Menu](#Menu)

## split

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| split | The split() method of String values takes a pattern and divides this string into an ordered list of substrings by searching for the pattern, puts these substrings into an array, and returns the array. |`separator` - The pattern describing where each split should occur. Can be undefined, a string, or an object with a Symbol.split method — the typical example being a regular expression. <br> `limit` (Optional) - A non-negative integer specifying a limit on the number of substrings to be included in the array. If provided, splits the string at each occurrence of the specified separator, but stops when limit entries have been placed in the array. Any leftover text is not included in the array at all. | If separator is a string, an `Array of strings` is returned, split at each point where the separator occurs in the given string. <br> If separator is a regex, the returned `Array` also contains the captured groups for each separator match. <br> If separator has a custom [Symbol.split]() method, its return value is directly returned. | split(separator) <br> split(separator, limit) |


<!-- <details>
  <summary>ua</summary>


</details>
-->


**Example**
```javaScript
const str = "The quick brown fox jumps over the lazy dog.";

const words = str.split(" ");
console.log(words[3]);
// Expected output: "fox"

const chars = str.split("");
console.log(chars[8]);
// Expected output: "k"

const strCopy = str.split();
console.log(strCopy);
// Expected output: Array ["The quick brown fox jumps over the lazy dog."]
```

[Back to Menu](#Menu)

## startsWith

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| startsWith | The startsWith() method of String values determines whether this string begins with the characters of a specified string, returning true or false as appropriate. | `searchString` - The characters to be searched for at the start of this string. Cannot be a regex. All values that are not regexes are coerced to strings, so omitting it or passing undefined causes startsWith() to search for the string "undefined", which is rarely what you want. <br> `position` (Optional) - The start position at which searchString is expected to be found (the index of searchString's first character). Defaults to 0 | `true` if the given characters are found at the beginning of the string, including when searchString is an empty string; otherwise, `false`. | startsWith(searchString) <br> startsWith(searchString, position) |


<!-- <details>
  <summary>ua</summary>


</details>
-->


**Example**
```javaScript
const str1 = "Saturday night plans";

console.log(str1.startsWith("Sat"));
// Expected output: true

console.log(str1.startsWith("Sat", 3));
// Expected output: false
```

[Back to Menu](#Menu)


## substring

| Name | Description | Accepts | Return | Syntax |
| ---- | ----------- | ------- | ------ | ------- |
| substring | The substring() method of String values returns the part of this string from the start index up to and excluding the end index, or to the end of the string if no end index is supplied. | `indexStart` - The index of the first character to include in the returned substring. <br> `indexEnd` (Optional) - The index of the first character to exclude from the returned substring. | A new `string` containing the specified part of the given string. | substring(indexStart) <br> substring(indexStart, indexEnd) |


<!-- <details>
  <summary>ua</summary>


</details>
-->


**Example**
```javaScript
const str = "Mozilla";

console.log(str.substring(1, 3));
// Expected output: "oz"

console.log(str.substring(2));
// Expected output: "zilla"
```


