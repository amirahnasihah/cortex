# TypeScript - Get Started


## Typescript From Scratch

Was this page helpful?

# TypeScript for the New Programmer
 Congratulations on choosing TypeScript as one of your first languages — you’re already making good decisions!

You’ve probably already heard that TypeScript is a “flavor” or “variant” of JavaScript.
The relationship between TypeScript (TS) and JavaScript (JS) is rather unique among modern programming languages, so learning more about this relationship will help you understand how TypeScript adds to JavaScript.

## What is JavaScript? A Brief History

 JavaScript (also known as ECMAScript) started its life as a simple scripting language for browsers.
At the time it was invented, it was expected to be used for short snippets of code embedded in a web page — writing more than a few dozen lines of code would have been somewhat unusual.
Due to this, early web browsers executed such code pretty slowly.
Over time, though, JS became more and more popular, and web developers started using it to create interactive experiences.

Web browser developers responded to this increased JS usage by optimizing their execution engines (dynamic compilation) and extending what could be done with it (adding APIs), which in turn made web developers use it even more.
On modern websites, your browser is frequently running applications that span hundreds of thousands of lines of code.
This is the long and gradual growth of “the web”, starting as a simple network of static pages, and evolving into a platform for rich applications of all kinds.

More than this, JS has become popular enough to be used outside the context of browsers, such as implementing JS servers using node.js.
The “run anywhere” nature of JS makes it an attractive choice for cross-platform development.
There are many developers these days that use only JavaScript to program their entire stack!

To summarize, we have a language that was designed for quick uses, and then grew to a full-fledged tool to write applications with millions of lines.
Every language has its own quirks — oddities and surprises, and JavaScript’s humble beginning makes it have many of these. Some examples:

-
JavaScript’s equality operator (`==`) coerces its operands, leading to unexpected behavior:

 js ` if ( "" == 0 ) { // It is! But why?? } if ( 1 < x < 3 ) { // True for *any* value of x! } `

-
 JavaScript also allows accessing properties which aren’t present:

 js ` const obj = { width: 10 , height: 15 }; // Why is this NaN? Spelling is hard! const area = obj . width * obj . heigth ; `

 Most programming languages would throw an error when these sorts of errors occur, some would do so during compilation — before any code is running.
When writing small programs, such quirks are annoying but manageable; when writing applications with hundreds or thousands of lines of code, these constant surprises are a serious problem.

## TypeScript: A Static Type Checker

 We said earlier that some languages wouldn’t allow those buggy programs to run at all.
Detecting errors in code without running it is referred to as static checking .
Determining what’s an error and what’s not based on the kinds of values being operated on is known as static type checking.

TypeScript checks a program for errors before execution, and does so based on the kinds of values , making it a static type checker .
For example, the last example above has an error because of the type of `obj`.
Here’s the error TypeScript found:

 ts ` const obj = { width : 10 , height : 15 }; const area = obj . width * obj . heigth ; Property 'heigth' does not exist on type '{ width: number; height: number; }'. Did you mean 'height'? 2551 Property 'heigth' does not exist on type '{ width: number; height: number; }'. Did you mean 'height'? ` Try

### A Typed Superset of JavaScript

 How does TypeScript relate to JavaScript, though?

#### Syntax

 TypeScript is a language that is a superset of JavaScript: JS syntax is therefore legal TS.
Syntax refers to the way we write text to form a program.
For example, this code has a syntax error because it’s missing a `)`:

 ts ` let a = ( 4 ')' expected. 1005 ')' expected. ` Try
 TypeScript doesn’t consider any JavaScript code to be an error because of its syntax.
This means you can take any working JavaScript code and put it in a TypeScript file without worrying about exactly how it is written.

#### Types

 However, TypeScript is a typed superset, meaning that it adds rules about how different kinds of values can be used.
The earlier error about `obj.heigth` was not a syntax error: it is an error of using some kind of value (a type ) in an incorrect way.

As another example, this is JavaScript code that you can run in your browser, and it will log a value:

 js ` console . log ( 4 / []); `
 This syntactically-legal program logs `Infinity`.
TypeScript, though, considers division of number by an array to be a nonsensical operation, and will issue an error:

 ts ` console . log ( 4 / [] ); The right-hand side of an arithmetic operation must be of type 'any', 'number', 'bigint' or an enum type. 2363 The right-hand side of an arithmetic operation must be of type 'any', 'number', 'bigint' or an enum type. ` Try
 It’s possible you really did intend to divide a number by an array, perhaps just to see what happens, but most of the time, though, this is a programming mistake.
TypeScript’s type checker is designed to allow correct programs through while still catching as many common errors as possible.
(Later, we’ll learn about settings you can use to configure how strictly TypeScript checks your code.)

If you move some code from a JavaScript file to a TypeScript file, you might see type errors depending on how the code is written.
These may be legitimate problems with the code, or TypeScript being overly conservative.
Throughout this guide we’ll demonstrate how to add various TypeScript syntax to eliminate such errors.

#### Runtime Behavior

 TypeScript is also a programming language that preserves the runtime behavior of JavaScript.
For example, dividing by zero in JavaScript produces `Infinity` instead of throwing a runtime exception.
As a principle, TypeScript never changes the runtime behavior of JavaScript code.

This means that if you move code from JavaScript to TypeScript, it is guaranteed to run the same way, even if TypeScript thinks that the code has type errors.

Keeping the same runtime behavior as JavaScript is a foundational promise of TypeScript because it means you can easily transition between the two languages without worrying about subtle differences that might make your program stop working.

#### Erased Types

 Roughly speaking, once TypeScript’s compiler is done with checking your code, it erases the types to produce the resulting “compiled” code.
This means that once your code is compiled, the resulting plain JS code has no type information.

This also means that TypeScript never changes the behavior of your program based on the types it inferred.
The bottom line is that while you might see type errors during compilation, the type system itself has no bearing on how your program works when it runs.

Finally, TypeScript doesn’t provide any additional runtime libraries.
Your programs will use the same standard library (or external libraries) as JavaScript programs, so there’s no additional TypeScript-specific framework to learn.

## Learning JavaScript and TypeScript

 We frequently see the question “Should I learn JavaScript or TypeScript?“.

The answer is that you can’t learn TypeScript without learning JavaScript!
TypeScript shares syntax and runtime behavior with JavaScript, so anything you learn about JavaScript is helping you learn TypeScript at the same time.

There are many, many resources available for programmers to learn JavaScript; you should not ignore these resources if you’re writing TypeScript.
For example, there are about 20 times more StackOverflow questions tagged `javascript` than `typescript`, but all of the `javascript` questions also apply to TypeScript.

If you find yourself searching for something like “how to sort a list in TypeScript”, remember: TypeScript is JavaScript’s runtime with a compile-time type checker .
The way you sort a list in TypeScript is the same way you do so in JavaScript.
If you find a resource that uses TypeScript directly, that’s great too, but don’t limit yourself to thinking you need TypeScript-specific answers for everyday questions about how to accomplish runtime tasks.

## Next Steps

 This was a brief overview of the syntax and tools used in everyday TypeScript. From here, you can:

-
Learn some of the JavaScript fundamentals, we recommend either:

 Microsoft’s JavaScript Resources or

- JavaScript guide at the Mozilla Web Docs

-
Continue to TypeScript for JavaScript Programmers

-
Read the full Handbook from start to finish

-
Explore the Playground examples

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: OT EB XL NS AO 8+ Last updated: Jun 15, 2026

## Typescript In 5 Minutes

Was this page helpful?

# TypeScript for JavaScript Programmers
 TypeScript stands in an unusual relationship to JavaScript. TypeScript offers all of JavaScript’s features, and an additional layer on top of these: TypeScript’s type system.

For example, JavaScript provides language primitives like `string` and `number`, but it doesn’t check that you’ve consistently assigned these. TypeScript does.

This means that your existing working JavaScript code is also TypeScript code. The main benefit of TypeScript is that it can highlight unexpected behavior in your code, lowering the chance of bugs.

This tutorial provides a brief overview of TypeScript, focusing on its type system.

## Types by Inference

 TypeScript knows the JavaScript language and will generate types for you in many cases.
For example in creating a variable and assigning it to a particular value, TypeScript will use the value as its type.

 ts ` let helloWorld = "Hello World" ; let helloWorld: string ` Try
 By understanding how JavaScript works, TypeScript can build a type-system that accepts JavaScript code but has types. This offers a type-system without needing to add extra characters to make types explicit in your code. That’s how TypeScript knows that `helloWorld` is a `string` in the above example.

You may have written JavaScript in Visual Studio Code, and had editor auto-completion. Visual Studio Code uses TypeScript under the hood to make it easier to work with JavaScript.

## Defining Types

 You can use a wide variety of design patterns in JavaScript. However, some design patterns make it difficult for types to be inferred automatically (for example, patterns that use dynamic programming). To cover these cases, TypeScript supports an extension of the JavaScript language, which offers places for you to tell TypeScript what the types should be.

For example, to create an object with an inferred type which includes `name: string` and `id: number`, you can write:

 ts ` const user = { name : "Hayes" , id : 0 , }; ` Try
 You can explicitly describe this object’s shape using an `interface` declaration:

 ts ` interface User { name : string ; id : number ; } ` Try
 You can then declare that a JavaScript object conforms to the shape of your new `interface` by using syntax like `: TypeName` after a variable declaration:

 ts ` const user : User = { name : "Hayes" , id : 0 , }; ` Try
 If you provide an object that doesn’t match the interface you have provided, TypeScript will warn you:

 ts ` interface User { name : string ; id : number ; } const user : User = { username : "Hayes" , Object literal may only specify known properties, and 'username' does not exist in type 'User'. 2353 Object literal may only specify known properties, and 'username' does not exist in type 'User'. id : 0 , }; ` Try
 Since JavaScript supports classes and object-oriented programming, so does TypeScript. You can use an interface declaration with classes:

 ts ` interface User { name : string ; id : number ; } class UserAccount { name : string ; id : number ; constructor ( name : string , id : number ) { this . name = name ; this . id = id ; } } const user : User = new UserAccount ( "Murphy" , 1 ); ` Try
 You can use interfaces to annotate parameters and return values to functions:

 ts ` function deleteUser ( user : User ) { // ... } function getAdminUser (): User { //... } ` Try
 There is already a small set of primitive types available in JavaScript: `boolean`, `bigint`, `null`, `number`, `string`, `symbol`, and `undefined`, which you can use in an interface. TypeScript extends this list with a few more, such as `any` (allow anything), `unknown` (ensure someone using this type declares what the type is), `never` (it’s not possible that this type could happen), and `void` (a function which returns `undefined` or has no return value).

You’ll see that there are two syntaxes for building types: Interfaces and Types . You should prefer `interface`. Use `type` when you need specific features.

## Composing Types

 With TypeScript, you can create complex types by combining simple ones. There are two popular ways to do so: unions and generics.

### Unions

 With a union, you can declare that a type could be one of many types. For example, you can describe a `boolean` type as being either `true` or `false`:

 ts ` type MyBool = true | false ; ` Try
 Note: If you hover over `MyBool` above, you’ll see that it is classed as `boolean`. That’s a property of the Structural Type System. More on this below.

A popular use-case for union types is to describe the set of `string` or `number` literals that a value is allowed to be:

 ts ` type WindowStates = "open" | "closed" | "minimized" ; type LockStates = "locked" | "unlocked" ; type PositiveOddNumbersUnderTen = 1 | 3 | 5 | 7 | 9 ; ` Try
 Unions provide a way to handle different types too. For example, you may have a function that takes an `array` or a `string`:

 ts ` function getLength ( obj : string | string []) { return obj . length ; } ` Try
 To learn the type of a variable, use `typeof`:

| **

 Type**
| **Predicate**
|

| string
| `typeof s === "string"`
|

| number
| `typeof n === "number"`
|

| boolean
| `typeof b === "boolean"`
|

| undefined
| `typeof undefined === "undefined"`
|

| function
| `typeof f === "function"`
|

| array
| `Array.isArray(a)`
|

For example, you can make a function return different values depending on whether it is passed a string or an array:

 ts ` function wrapInArray ( obj : string | string []) { if ( typeof obj === "string" ) { return [ obj ]; (parameter) obj: string } return obj ; } ` Try

### Generics

 Generics provide variables to types. A common example is an array. An array without generics could contain anything. An array with generics can describe the values that the array contains.

 ts ` type StringArray = Array < string >; type NumberArray = Array < number >; type ObjectWithNameArray = Array <{ name : string }>; `
 You can declare your own types that use generics:

 ts ` interface ' >Backpack < ' >Type > { .add: (obj: Type) => void' >add : ( obj : ' >Type ) => void ; .get: () => Type' >get : () => ' >Type ; } // This line is a shortcut to tell TypeScript there is a // constant called `backpack`, and to not worry about where it came from. declare const ' >backpack : ' >Backpack < string >; // object is a string, because we declared it above as the variable part of Backpack. const object = ' >backpack . .get: () => string' >get (); // Since the backpack variable is a string, you can&apos;t pass a number to the add function. ' >backpack . .add: (obj: string) => void' >add ( 23 ); Argument of type 'number' is not assignable to parameter of type 'string'. 2345 Argument of type 'number' is not assignable to parameter of type 'string'. ` Try

## Structural Type System

 One of TypeScript’s core principles is that type checking focuses on the shape that values have. This is sometimes called “duck typing” or “structural typing”.

In a structural type system, if two objects have the same shape, they are considered to be of the same type.

 ts ` interface Point { x : number ; y : number ; } function logPoint ( p : Point ) { console . log ( ` ${ p . x } , ${ p . y } ` ); } // logs "12, 26" const point = { x : 12 , y : 26 }; logPoint ( point ); ` Try
 The `point` variable is never declared to be a `Point` type. However, TypeScript compares the shape of `point` to the shape of `Point` in the type-check. They have the same shape, so the code passes.

The shape-matching only requires a subset of the object’s fields to match.

 ts ` const point3 = { x : 12 , y : 26 , z : 89 }; logPoint ( point3 ); // logs "12, 26" const rect = { x : 33 , y : 3 , width : 30 , height : 80 }; logPoint ( rect ); // logs "33, 3" const color = { hex : "#187ABF" }; logPoint ( color ); Argument of type '{ hex: string; }' is not assignable to parameter of type 'Point'.
 Type '{ hex: string; }' is missing the following properties from type 'Point': x, y 2345 Argument of type '{ hex: string; }' is not assignable to parameter of type 'Point'.
 Type '{ hex: string; }' is missing the following properties from type 'Point': x, y ` Try
 There is no difference between how classes and objects conform to shapes:

 ts ` class VirtualPoint { x : number ; y : number ; constructor ( x : number , y : number ) { this . x = x ; this . y = y ; } } const newVPoint = new VirtualPoint ( 13 , 56 ); logPoint ( newVPoint ); // logs "13, 56" ` Try
 If the object or class has all the required properties, TypeScript will say they match, regardless of the implementation details.

## Next Steps

 This was a brief overview of the syntax and tools used in everyday TypeScript. From here, you can:

- Read the full Handbook from start to finish

- Explore the Playground examples

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: OT JB DS MK JCR 19+ Last updated: Jun 15, 2026

## Typescript In 5 Minutes Oop

Was this page helpful?

# TypeScript for Java/C# Programmers
 TypeScript is a popular choice for programmers accustomed to other languages with static typing, such as C# and Java.

TypeScript’s type system offers many of the same benefits, such as better code completion, earlier detection of errors, and clearer communication between parts of your program.
While TypeScript provides many familiar features for these developers, it’s worth stepping back to see how JavaScript (and therefore TypeScript) differ from traditional OOP languages.
Understanding these differences will help you write better JavaScript code, and avoid common pitfalls that programmers who go straight from C#/Java to TypeScript may fall into.

## Co-learning JavaScript

 If you’re familiar with JavaScript already but are primarily a Java or C# programmer, this introductory page can help explain some of the common misconceptions and pitfalls you might be susceptible to.
Some of the ways that TypeScript models types are quite different from Java or C#, and it’s important to keep these in mind when learning TypeScript.

If you’re a Java or C# programmer that is new to JavaScript in general, we recommend learning a little bit of JavaScript without types first to understand JavaScript’s runtime behaviors.
Because TypeScript doesn’t change how your code runs , you’ll still have to learn how JavaScript works in order to write code that actually does something!

It’s important to remember that TypeScript uses the same runtime as JavaScript, so any resources about how to accomplish specific runtime behavior (converting a string to a number, displaying an alert, writing a file to disk, etc.) will always apply equally well to TypeScript programs.
Don’t limit yourself to TypeScript-specific resources!

## Rethinking the Class

 C# and Java are what we might call mandatory OOP languages.
In these languages, the class is the basic unit of code organization, and also the basic container of all data and behavior at runtime.
Forcing all functionality and data to be held in classes can be a good domain model for some problems, but not every domain needs to be represented this way.

### Free Functions and Data

 In JavaScript, functions can live anywhere, and data can be passed around freely without being inside a pre-defined `class` or `struct`.
This flexibility is extremely powerful.
“Free” functions (those not associated with a class) working over data without an implied OOP hierarchy tend to be the preferred model for writing programs in JavaScript.

### Static Classes

 Additionally, certain constructs from C# and Java such as singletons and static classes are unnecessary in TypeScript.

## OOP in TypeScript

 That said, you can still use classes if you like!
Some problems are well-suited to being solved by a traditional OOP hierarchy, and TypeScript’s support for JavaScript classes will make these models even more powerful.
TypeScript supports many common patterns such as implementing interfaces, inheritance, and static methods.

We’ll cover classes later in this guide.

## Rethinking Types

 TypeScript’s understanding of a type is actually quite different from C# or Java’s.
Let’s explore some differences.

### Nominal Reified Type Systems

 In C# or Java, any given value or object has one exact type - either `null`, a primitive, or a known class type.
We can call methods like `value.GetType()` or `value.getClass()` to query the exact type at runtime.
The definition of this type will reside in a class somewhere with some name, and we can’t use two classes with similar shapes in lieu of each other unless there’s an explicit inheritance relationship or commonly-implemented interface.

These aspects describe a reified, nominal type system.
The types we wrote in the code are present at runtime, and the types are related via their declarations, not their structures.

### Types as Sets

 In C# or Java, it’s meaningful to think of a one-to-one correspondence between runtime types and their compile-time declarations.

In TypeScript, it’s better to think of a type as a set of values that share something in common.
Because types are just sets, a particular value can belong to many sets at the same time.

Once you start thinking of types as sets, certain operations become very natural.
For example, in C#, it’s awkward to pass around a value that is either a `string` or `int`, because there isn’t a single type that represents this sort of value.

In TypeScript, this becomes very natural once you realize that every type is just a set.
How do you describe a value that either belongs in the `string` set or the `number` set?
It simply belongs to the union of those sets: `string | number`.

TypeScript provides a number of mechanisms to work with types in a set-theoretic way, and you’ll find them more intuitive if you think of types as sets.

### Erased Structural Types

 In TypeScript, objects are not of a single exact type.
For example, if we construct an object that satisfies an interface, we can use that object where that interface is expected even though there was no declarative relationship between the two.

 ts ` interface Pointlike { x : number ; y : number ; } interface Named { name : string ; } function logPoint ( point : Pointlike ) { console . log ( "x = " + point . x + ", y = " + point . y ); } function logName ( x : Named ) { console . log ( "Hello, " + x . name ); } const obj = { x : 0 , y : 0 , name : "Origin" , }; logPoint ( obj ); logName ( obj ); ` Try
 TypeScript’s type system is structural , not nominal: We can use `obj` as a `Pointlike` because it has `x` and `y` properties that are both numbers.
The relationships between types are determined by the properties they contain, not whether they were declared with some particular relationship.

TypeScript’s type system is also not reified : There’s nothing at runtime that will tell us that `obj` is `Pointlike`.
In fact, the `Pointlike` type is not present in any form at runtime.

Going back to the idea of types as sets , we can think of `obj` as being a member of both the `Pointlike` set of values and the `Named` set of values.

### Consequences of Structural Typing

 OOP programmers are often surprised by two particular aspects of structural typing.

#### Empty Types

 The first is that the empty type seems to defy expectation:

 ts ` class Empty {} function fn ( arg : Empty ) { // do something? } // No error, but this isn&apos;t an &apos;Empty&apos; ? fn ({ k : 10 }); ` Try
 TypeScript determines if the call to `fn` here is valid by seeing if the provided argument is a valid `Empty`.
It does so by examining the structure of `{ k: 10 }` and `class Empty { }`.
We can see that `{ k: 10 }` has all of the properties that `Empty` does, because `Empty` has no properties.
Therefore, this is a valid call!

This may seem surprising, but it’s ultimately a very similar relationship to one enforced in nominal OOP languages.
A subclass cannot remove a property of its base class, because doing so would destroy the natural subtype relationship between the derived class and its base.
Structural type systems simply identify this relationship implicitly by describing subtypes in terms of having properties of compatible types.

#### Identical Types

 Another frequent source of surprise comes with identical types:

 ts ` class Car { drive () { // hit the gas } } class Golfer { drive () { // hit the ball far } } // No error? let w : Car = new Golfer (); `
 Again, this isn’t an error because the structures of these classes are the same.
While this may seem like a potential source of confusion, in practice, identical classes that shouldn’t be related are not common.

We’ll learn more about how classes relate to each other in the Classes chapter.

### Reflection

 OOP programmers are accustomed to being able to query the type of any value, even a generic one:

 csharp ` // C# static void LogType < T >() { Console . WriteLine ( typeof ( T ). Name ); } `
 Because TypeScript’s type system is fully erased, information about e.g. the instantiation of a generic type parameter is not available at runtime.

JavaScript does have some limited primitives like `typeof` and `instanceof`, but remember that these operators are still working on the values as they exist in the type-erased output code.
For example, `typeof (new Car())` will be `"object"`, not `Car` or `"Car"`.

## Next Steps

 This was a brief overview of the syntax and tools used in everyday TypeScript. From here, you can:

- Read the full Handbook from start to finish

- Explore the Playground examples

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: OT TZ SP L GD Last updated: Jun 15, 2026

## Typescript In 5 Minutes Func

Was this page helpful?

# TypeScript for Functional Programmers
 TypeScript began its life as an attempt to bring traditional object-oriented types
to JavaScript so that the programmers at Microsoft could bring
traditional object-oriented programs to the web. As it has developed, TypeScript’s type
system has evolved to model code written by native JavaScripters. The
resulting system is powerful, interesting and messy.

This introduction is designed for working Haskell or ML programmers
who want to learn TypeScript. It describes how the type system of
TypeScript differs from Haskell’s type system. It also describes
unique features of TypeScript’s type system that arise from its
modelling of JavaScript code.

This introduction does not cover object-oriented programming. In
practice, object-oriented programs in TypeScript are similar to those
in other popular languages with OO features.

## Prerequisites

 In this introduction, I assume you know the following:

- How to program in JavaScript, the good parts.

- Type syntax of a C-descended language.

If you need to learn the good parts of JavaScript, read
 JavaScript: The Good Parts .
You may be able to skip the book if you know how to write programs in
a call-by-value lexically scoped language with lots of mutability and
not much else.
 R 4 RS Scheme is a good example.

 The C++ Programming Language is
a good place to learn about C-style type syntax. Unlike C++,
TypeScript uses postfix types, like so: `x: string` instead of `string x`.

## Concepts not in Haskell

### Built-in types

 JavaScript defines 8 built-in types:

| **

 Type**
| **Explanation**
|

| `Number`
| a double-precision IEEE 754 floating point.
|

| `String`
| an immutable UTF-16 string.
|

| `BigInt`
| integers in the arbitrary precision format.
|

| `Boolean`
| `true` and `false`.
|

| `Symbol`
| a unique value usually used as a key.
|

| `Null`
| equivalent to the unit type.
|

| `Undefined`
| also equivalent to the unit type.
|

| `Object`
| similar to records.
|

 See the MDN page for more detail .

TypeScript has corresponding primitive types for the built-in types:

- `number`

- `string`

- `bigint`

- `boolean`

- `symbol`

- `null`

- `undefined`

- `object`

#### Other important TypeScript types

| **

 Type**
| **Explanation**
|

| `unknown`
| the top type.
|

| `never`
| the bottom type.
|

| object literal
| e.g. `{ property: Type }`
|

| `void`
| for functions with no documented return value
|

| `T[]`
| mutable arrays, also written `Array&#x3C;T>`
|

| `[T, T]`
| tuples, which are fixed-length but mutable
|

| `(t: T) => U`
| functions
|

 Notes:

-
Function syntax includes parameter names. This is pretty hard to get used to!

 ts ` let fst : ( a : any , b : any ) => any = ( a , b ) => a ; // or more precisely: let fst : < T , U >( a : T , b : U ) => T = ( a , b ) => a ; `

-
 Object literal type syntax closely mirrors object literal value syntax:

 ts ` let o : { n : number ; xs : object [] } = { n: 1 , xs: [] }; `

-
 `[T, T]` is a subtype of `T[]`. This is different than Haskell, where tuples are not related to lists.

#### Boxed types

 JavaScript has boxed equivalents of primitive types that contain the
methods that programmers associate with those types. TypeScript
reflects this with, for example, the difference between the primitive
type `number` and the boxed type `Number`. The boxed types are rarely
needed, since their methods return primitives.

 ts ` ( 1 ). toExponential (); // equivalent to Number . prototype . toExponential . call ( 1 ); `
 Note that calling a method on a numeric literal requires it to be in
parentheses to aid the parser.

### Gradual typing

 TypeScript uses the type `any` whenever it can’t tell what the type of
an expression should be. Compared to `Dynamic`, calling `any` a type
is an overstatement. It just turns off the type checker
wherever it appears. For example, you can push any value into an
`any[]` without marking the value in any way:

 ts ` // with "noImplicitAny": false in tsconfig.json, anys: any[] const anys = []; anys . .push(...items: any[]): number' >push ( 1 ); anys . .push(...items: any[]): number' >push ( "oh no" ); anys . .push(...items: any[]): number' >push ({ anything : "goes" }); ` Try
 And you can use an expression of type `any` anywhere:

 ts ` anys . map ( anys [ 1 ]); // oh no, "oh no" is not a function `
 `any` is contagious, too — if you initialize a variable with an
expression of type `any`, the variable has type `any` too.

 ts ` let sepsis = anys [ 0 ] + anys [ 1 ]; // this could mean anything `
 To get an error when TypeScript produces an `any`, use
`"noImplicitAny": true`, or `"strict": true` in `tsconfig.json`.

### Structural typing

 Structural typing is a familiar concept to most functional
programmers, although Haskell and most MLs are not
structurally typed. Its basic form is pretty simple:

 ts ` // @strict: false let o = { x: "hi" , extra: 1 }; // ok let o2 : { x : string } = o ; // ok `
 Here, the object literal `{ x: "hi", extra: 1 }` has a matching
literal type `{ x: string, extra: number }`. That
type is assignable to `{ x: string }` since
it has all the required properties and those properties have
assignable types. The extra property doesn’t prevent assignment, it
just makes it a subtype of `{ x: string }`.

Named types just give a name to a type; for assignability purposes
there’s no difference between the type alias `One` and the interface
type `Two` below. They both have a property `p: string`. (Type aliases
behave differently from interfaces with respect to recursive
definitions and type parameters, however.)

 ts ` type One = { p : string }; interface Two { p : string ; } class Three { p = "Hello" ; } let x : One = { p : "hi" }; let two : Two = x ; two = new Three (); ` Try

### Unions

 In TypeScript, union types are untagged. In other words, they are not
discriminated unions like `data` in Haskell. However, you can often
discriminate types in a union using built-in tags or other properties.

 ts ` function string) | {
 s: string;
}): string' >start ( string)' >arg : string | string [] | (() => string ) | { s : string } ): string { // this is super common in JavaScript if ( typeof string)' >arg === "string" ) { return commonCase ( arg ); } else if ( Array . isArray ( string)' >arg )) { return arg . .map<string>(callbackfn: (value: string, index: number, array: string[]) => string, thisArg?: any): string[]' >map ( commonCase ). .join(separator?: string): string' >join ( "," ); } else if ( typeof string)' >arg === "function" ) { return commonCase ( string' >arg ()); } else { return commonCase ( arg . s ); } function commonCase ( s : string ): string { // finally, just convert a string to another string return s ; } } ` Try
 `string`, `Array` and `Function` have built-in type predicates,
conveniently leaving the object type for the `else` branch. It is
possible, however, to generate unions that are difficult to
differentiate at runtime. For new code, it’s best to build only
discriminated unions.

The following types have built-in predicates:

| **

 Type**
| **Predicate**
|

| string
| `typeof s === "string"`
|

| number
| `typeof n === "number"`
|

| bigint
| `typeof m === "bigint"`
|

| boolean
| `typeof b === "boolean"`
|

| symbol
| `typeof g === "symbol"`
|

| undefined
| `typeof undefined === "undefined"`
|

| function
| `typeof f === "function"`
|

| array
| `Array.isArray(a)`
|

| object
| `typeof o === "object"`
|

Note that functions and arrays are objects at runtime, but have their
own predicates.

#### Intersections

 In addition to unions, TypeScript also has intersections:

 ts ` type Combined = { a : number } & { b : string }; type Conflicting = { a : number } & { a : string }; ` Try
 `Combined` has two properties, `a` and `b`, just as if they had been
written as one object literal type. Intersection and union are
recursive in case of conflicts, so `Conflicting.a: number &#x26; string`.

### Unit types

 Unit types are subtypes of primitive types that contain exactly one
primitive value. For example, the string `"foo"` has the type
`"foo"`. Since JavaScript has no built-in enums, it is common to use a set of
well-known strings instead. Unions of string literal types allow
TypeScript to type this pattern:

 ts ` declare function pad ( s : string , n : number , direction : "left" | "right" ): string ; pad ( "hi" , 10 , "left" ); ` Try
 When needed, the compiler widens — converts to a
supertype — the unit type to the primitive type, such as `"foo"`
to `string`. This happens when using mutability, which can hamper some
uses of mutable variables:

 ts ` let s = "right" ; pad ( "hi" , 10 , s ); // error: &apos;string&apos; is not assignable to &apos;"left" | "right"&apos; Argument of type 'string' is not assignable to parameter of type '"left" | "right"'. 2345 Argument of type 'string' is not assignable to parameter of type '"left" | "right"'. ` Try
 Here’s how the error happens:

- `"right": "right"`

- `s: string` because `"right"` widens to `string` on assignment to a mutable variable.

- `string` is not assignable to `"left" | "right"`

You can work around this with a type annotation for `s`, but that
in turn prevents assignments to `s` of variables that are not of type
`"left" | "right"`.

 ts ` let s : "left" | "right" = "right" ; pad ( "hi" , 10 , s ); ` Try

## Concepts similar to Haskell

### Contextual typing

 TypeScript has some obvious places where it can infer types, like
variable declarations:

 ts ` let s = "I&apos;m a string!" ; ` Try
 But it also infers types in a few other places that you may not expect
if you’ve worked with other C-syntax languages:

 ts ` declare function (f: (t: T) => U, ts: T[]): U[]' >map < (f: (t: T) => U, ts: T[]): U[]' >T , (f: (t: T) => U, ts: T[]): U[]' >U >( U' >f : ( t : (f: (t: T) => U, ts: T[]): U[]' >T ) => (f: (t: T) => U, ts: T[]): U[]' >U , ts : (f: (t: T) => U, ts: T[]): U[]' >T []): (f: (t: T) => U, ts: T[]): U[]' >U []; let sns = (f: (t: number) => string, ts: number[]): string[]' >map (( n ) => n . toString (), [ 1 , 2 , 3 ]); ` Try
 Here, `n: number` in this example also, despite the fact that `T` and `U`
have not been inferred before the call. In fact, after `[1,2,3]` has
been used to infer `T=number`, the return type of `n => n.toString()`
is used to infer `U=string`, causing `sns` to have the type
`string[]`.

Note that inference will work in any order, but intellisense will only
work left-to-right, so TypeScript prefers to declare `map` with the
array first:

 ts ` declare function (ts: T[], f: (t: T) => U): U[]' >map < (ts: T[], f: (t: T) => U): U[]' >T , (ts: T[], f: (t: T) => U): U[]' >U >( ts : (ts: T[], f: (t: T) => U): U[]' >T [], U' >f : ( t : (ts: T[], f: (t: T) => U): U[]' >T ) => (ts: T[], f: (t: T) => U): U[]' >U ): (ts: T[], f: (t: T) => U): U[]' >U []; ` Try
 Contextual typing also works recursively through object literals, and
on unit types that would otherwise be inferred as `string` or
`number`. And it can infer return types from context:

 ts ` declare function (thunk: (t: T) => void): T' >run < (thunk: (t: T) => void): T' >T >( void' >thunk : ( t : (thunk: (t: T) => void): T' >T ) => void ): (thunk: (t: T) => void): T' >T ; let i : { inference : string } = (thunk: (t: {
 inference: string;
}) => void): {
 inference: string;
}' >run (( o ) => { o . inference = "INSERT STATE HERE" ; }); ` Try
 The type of `o` is determined to be `{ inference: string }` because

- Declaration initializers are contextually typed by the
declaration’s type: `{ inference: string }`.

- The return type of a call uses the contextual type for inferences,
so the compiler infers that `T={ inference: string }`.

- Arrow functions use the contextual type to type their parameters,
so the compiler gives `o: { inference: string }`.

And it does so while you are typing, so that after typing `o.`, you
get completions for the property `inference`, along with any other
properties you’d have in a real program.
Altogether, this feature can make TypeScript’s inference look a bit
like a unifying type inference engine, but it is not.

### Type aliases

 Type aliases are mere aliases, just like `type` in Haskell. The
compiler will attempt to use the alias name wherever it was used in
the source code, but does not always succeed.

 ts ` type Size = [ number , number ]; let x : Size = [ 101.1 , 999.9 ]; ` Try
 The closest equivalent to `newtype` is a tagged intersection :

 ts ` type FString = string & { __compileTimeOnly : any }; `
 An `FString` is just like a normal string, except that the compiler
thinks it has a property named `__compileTimeOnly` that doesn’t
actually exist. This means that `FString` can still be assigned to
`string`, but not the other way round.

### Discriminated Unions

 The closest equivalent to `data` is a union of types with discriminant
properties, normally called discriminated unions in TypeScript:

 ts ` type Shape = | { kind : "circle" ; radius : number } | { kind : "square" ; x : number } | { kind : "triangle" ; x : number ; y : number }; `
 Unlike Haskell, the tag, or discriminant, is just a property in each
object type. Each variant has an identical property with a different
unit type. This is still a normal union type; the leading `|` is
an optional part of the union type syntax. You can discriminate the
members of the union using normal JavaScript code:

 ts ` type Shape = | { kind : "circle" ; radius : number } | { kind : "square" ; x : number } | { kind : "triangle" ; x : number ; y : number }; function area ( s : Shape ) { if ( s . kind === "circle" ) { return Math . PI * s . radius * s . radius ; } else if ( s . kind === "square" ) { return s . x * s . x ; } else { return ( s . x * s . y ) / 2 ; } } ` Try
 Note that the return type of `area` is inferred to be `number` because
TypeScript knows the function is total. If some variant is not
covered, the return type of `area` will be `number | undefined` instead.

Also, unlike Haskell, common properties show up in any union, so you
can usefully discriminate multiple members of the union:

 ts ` function height ( s : Shape ) { if ( s . kind === "circle" ) { return 2 * s . radius ; } else { // s.kind: "square" | "triangle" return s . x ; } } ` Try

### Type Parameters

 Like most C-descended languages, TypeScript requires declaration of
type parameters:

 ts ` function liftArray < T >( t : T ): Array < T > { return [ t ]; } `
 There is no case requirement, but type parameters are conventionally
single uppercase letters. Type parameters can also be constrained to a
type, which behaves a bit like type class constraints:

 ts ` function firstish < T extends { length : number }>( t1 : T , t2 : T ): T { return t1 . length > t2 . length ? t1 : t2 ; } `
 TypeScript can usually infer type arguments from a call based on the
type of the arguments, so type arguments are usually not needed.

Because TypeScript is structural, it doesn’t need type parameters as
much as nominal systems. Specifically, they are not needed to make a
function polymorphic. Type parameters should only be used to
 propagate type information, such as constraining parameters to be
the same type:

 ts ` function length < T extends ArrayLike < unknown >>( t : T ): number {} function length ( t : ArrayLike < unknown >): number {} `
 In the first `length`, T is not necessary; notice that it’s only
referenced once, so it’s not being used to constrain the type of the
return value or other parameters.

#### Higher-kinded types

 TypeScript does not have higher kinded types, so the following is not legal:

 ts ` function length < T extends ArrayLike < unknown >, U >( m : T < U >) {} `

#### Point-free programming

 Point-free programming — heavy use of currying and function
composition — is possible in JavaScript, but can be verbose.
In TypeScript, type inference often fails for point-free programs, so
you’ll end up specifying type parameters instead of value parameters. The
result is so verbose that it’s usually better to avoid point-free
programming.

### Module system

 JavaScript’s modern module syntax is a bit like Haskell’s, except that
any file with `import` or `export` is implicitly a module:

 ts ` import { value , Type } from "npm-package" ; import { other , Types } from "./local-package" ; import * as prefix from "../lib/third-package" ; `
 You can also import commonjs modules — modules written using node.js’
module system:

 ts ` import f = require ( "single-function-package" ); `
 You can export with an export list:

 ts ` export { f }; function f () { return g (); } function g () {} // g is not exported `
 Or by marking each export individually:

 ts ` export function f () { return g () } function g () { } `
 The latter style is more common but both are allowed, even in the same
file.

### `readonly` and `const`

 In JavaScript, mutability is the default, although it allows variable
declarations with `const` to declare that the reference is
immutable. The referent is still mutable:

 js ` const a = [ 1 , 2 , 3 ]; a . push ( 102 ); // ): a [ 0 ] = 101 ; // D: `
 TypeScript additionally has a `readonly` modifier for properties.

 ts ` interface Rx { readonly x : number ; } let rx : Rx = { x: 1 }; rx . x = 12 ; // error `
 It also ships with a mapped type `Readonly&#x3C;T>` that makes
all properties `readonly`:

 ts ` interface X { x : number ; } let rx : Readonly < X > = { x: 1 }; rx . x = 12 ; // error `
 And it has a specific `ReadonlyArray&#x3C;T>` type that removes
side-affecting methods and prevents writing to indices of the array,
as well as special syntax for this type:

 ts ` let a : ReadonlyArray < number > = [ 1 , 2 , 3 ]; let b : readonly number [] = [ 1 , 2 , 3 ]; a . push ( 102 ); // error b [ 0 ] = 101 ; // error `
 You can also use a const-assertion, which operates on arrays and
object literals:

 ts ` let a = [ 1 , 2 , 3 ] as const ; a . push ( 102 ); // error a [ 0 ] = 101 ; // error `
 However, none of these options are the default, so they are not
consistently used in TypeScript code.

### Next Steps

 This doc is a high level overview of the syntax and types you would use in everyday code. From here you should:

- Read the full Handbook from start to finish

- Explore the Playground examples

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: OT UJ MF JRSDS RC 11+ Last updated: Jun 15, 2026

## Typescript Tooling In 5 Minutes

Was this page helpful?

# TypeScript Tooling in 5 minutes
 Let’s get started by building a simple web application with TypeScript.

## Installing TypeScript

 There are two main ways to add TypeScript to your project:

- Via npm (the Node.js package manager)

- By installing TypeScript’s Visual Studio plugins

Visual Studio 2017 and Visual Studio 2015 Update 3 include TypeScript language support by default but does not include the TypeScript compiler, `tsc`.
If you didn’t install TypeScript with Visual Studio, you can still download it .

For npm users:

 shell ` > npm install -g typescript `

## Building your first TypeScript file

 In your editor, type the following JavaScript code in `greeter.ts`:

 ts ` function greeter ( person ) { return "Hello, " + person ; } let user = "Jane User" ; document . body . textContent = greeter ( user ); ` Try

## Compiling your code

 We used a `.ts` extension, but this code is just JavaScript.
You could have copy/pasted this straight out of an existing JavaScript app.

At the command line, run the TypeScript compiler:

 shell ` tsc greeter.ts `
 The result will be a file `greeter.js` which contains the same JavaScript that you fed in.
We’re up and running using TypeScript in our JavaScript app!

Now we can start taking advantage of some of the new tools TypeScript offers.
Add a `: string` type annotation to the ‘person’ function parameter as shown here:

 ts ` function greeter ( person : string ) { return "Hello, " + person ; } let user = "Jane User" ; document . body . textContent = greeter ( user ); ` Try

## Type annotations

 Type annotations in TypeScript are lightweight ways to record the intended contract of the function or variable.
In this case, we intend the greeter function to be called with a single string parameter.
We can try changing the call greeter to pass an array instead:

 ts ` function greeter ( person : string ) { return "Hello, " + person ; } let user = [ 0 , 1 , 2 ]; document . body . textContent = greeter ( user ); Argument of type 'number[]' is not assignable to parameter of type 'string'. 2345 Argument of type 'number[]' is not assignable to parameter of type 'string'. ` Try
 Re-compiling, you’ll now see an error:

 shell ` error TS2345: Argument of type 'number[]' is not assignable to parameter of type 'string' . `
 Similarly, try removing all the arguments to the greeter call.
TypeScript will let you know that you have called this function with an unexpected number of arguments.
In both cases, TypeScript can offer static analysis based on both the structure of your code, and the type annotations you provide.

Notice that although there were errors, the `greeter.js` file is still created.
You can use TypeScript even if there are errors in your code. But in this case, TypeScript is warning that your code will likely not run as expected.

## Interfaces

 Let’s develop our sample further. Here we use an interface that describes objects that have a firstName and lastName field.
In TypeScript, two types are compatible if their internal structure is compatible.
This allows us to implement an interface just by having the shape the interface requires, without an explicit `implements` clause.

 ts ` interface Person { firstName : string ; lastName : string ; } function greeter ( person : Person ) { return "Hello, " + person . firstName + " " + person . lastName ; } let user = { firstName : "Jane" , lastName : "User" }; document . body . textContent = greeter ( user ); ` Try

## Classes

 Finally, let’s extend the example one last time with classes.
TypeScript supports new features in JavaScript, like support for class-based object-oriented programming.

Here we’re going to create a `Student` class with a constructor and a few public fields.
Notice that classes and interfaces play well together, letting the programmer decide on the right level of abstraction.

Also of note, the use of `public` on parameters to the constructor is a shorthand that allows us to automatically create properties with that name.

 ts ` class Student { fullName : string ; constructor ( public firstName : string , public middleInitial : string , public lastName : string ) { this . fullName = firstName + " " + middleInitial + " " + lastName ; } } interface Person { firstName : string ; lastName : string ; } function greeter ( person : Person ) { return "Hello, " + person . firstName + " " + person . lastName ; } let user = new Student ( "Jane" , "M." , "User" ); document . body . textContent = greeter ( user ); ` Try
 Re-run `tsc greeter.ts` and you’ll see the generated JavaScript is the same as the earlier code.
Classes in TypeScript are just a shorthand for the same prototype-based OO that is frequently used in JavaScript.

## Running your TypeScript web app

 Now type the following in `greeter.html`:

 html ` <!DOCTYPE html > <html> <head> <title> TypeScript Greeter </title> </head> <body> <script src = "greeter.js" ></script> </body> </html> `
 Open `greeter.html` in the browser to run your first simple TypeScript web application!

Optional: Open `greeter.ts` in Visual Studio, or copy the code into the TypeScript playground.
You can hover over identifiers to see their types.
Notice that in some cases these types are inferred automatically for you.
Re-type the last line, and see completion lists and parameter help based on the types of the DOM elements.
Put your cursor on the reference to the greeter function, and hit F12 to go to its definition.
Notice, too, that you can right-click on a symbol and use refactoring to rename it.

The type information provided works together with the tools to work with JavaScript at application scale.
For more examples of what’s possible in TypeScript, see the Samples section of the website.

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: OT H DS M Last updated: Jun 15, 2026