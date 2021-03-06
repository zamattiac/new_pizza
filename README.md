# Pizza 2.0!
# README from 1.0

#### Pizza is a dynamic, multifaceted functional-paradigm language that can serve as breakfast, lunch, or dinner
##### (Brunch coming in pizza3.0)

## Running the interpreter
`python new_pizza <filename> [FLAGS]`

<!-- 
### Flags:
- m: show memory configuration after execution
- o: output the parsed commands
- w: show warnings (recommended)
 -->

## Syntax
- Main method is enclosed within `comeinwereopen` and `sorrywereclosed`
<!-- 
- Anything after main is considered function-like and can be accessed with the `knead` keyword in any file
    (e.g. knead file2)
 -->
- Comments: `|>` (shaped like pizza). <!-- Inline is not supported. -->
- Dietary custom: the interpreter will reject any program with unsavory (e.g. olives) or unkosher (e.g. ham) content
<!-- - See the Parser section for syntax guidelines -->

## Memory
- Data is stored in arrays <!-- as a tuple of type and value -->
- Namespace for memory can be declared with the `toppings` keyword and size: `toppings cheese 10`.
<!-- - Datatypes are: thincrust (int), thickcrust (float), deepdish (string) -->
- Each array has a pointer that can be increased with `extra [namespace]` and reset with `hold the [namespace]`
- Initializing/mutating a memory location is done with `lemmegeta [namespace] [value]`
- Accessing a memory location (delivery) is done with `delivery [namespace]`
<!-- - Because cheese is default, `[namespace]-` is unnecessary -->
<!-- - In a similar vein: takeorder-[prompt] takes input and directly replaces -->
- When using values inline, preface with the keyword `digiornos`. Handy rule: if it's not `delivery`, it's `digiornos`.
- Dereferencing a null pointer will not cause a fatal error! The interpreter will assume you meant the word pizza. 
    It is handy to have warnings on.
    
## Parser
<!-- - Every line must end with `;`, including comments -->
<!-- - The previous line is a lie! Comments do not need a semicolon, despite what Big Punctuation has to say -->
<!-- - But not comeinwereopen and sorrywereclosed either. Don't do it. -->
- This program is vegetarian!!
- Lines that end in ? are loops (for, if). They must be on a newline.
- `yougotta` is the keyword for an if statement (e.g. `yougotta delivery?` => `if current pointer set`
- tip: `yougotta pizza?` always evaluates to false. This interpreter doesn't like to share its meal.
- comparators: 
    - `samepriceas` (==)
    - `cheaperthan` (<) 
    - there is no "more expensive than" because no one wants more expensive pizza
- `gimme` is the keyword for for loops. it is similar to above. It pythonically iterates.
- Every line in a loop block must begin with `!`. Pizza doesn't care if you indent.

## Error
- using the `w` flag is really really recommended.
- Turn your sound off when errors reporting is on. Error messages can be loud!
- Many traditional fatal errors are just suggestions for a food as hardy as pizza, and they won't cause crashes.
- Pizza is a forgiving language: for example, when you dereference a null pointer it assumes you meant to say 'pizza'
- Many traditional warnings are taken seriously by a food as diligent as pizza, and they will cause crashes!

Example code:
```
|> begin main execution
comeinwereopen

|> simple print line
ooze hello world;

|> create a string in cheese location 0
lemmegeta deepdish foo;
|> increase pointer
extra cheese;
|> create a string in location 1
lemmegeta deepdish bar;

|> reset pointer to 0
holdthe cheese;

|> get value from position 0
ooze delivery;
extra cheese;
ooze delivery;

|> declare pineapple namespace
toppings pineapple;
|> set integer 3
lemmegeta pineapple-thincrust 3;
extra pineapple;

|> is pineapple-delivery set? (answer: no)
yougotta pineapple-delivery?
    !ooze yes i do;

|> include code after main
knead [this file's name];

sorrywereclosed

ooze 'outside main';
```