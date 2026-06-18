# TypeScript - Reference


## Utility Types

Was this page helpful?

# Utility Types
 TypeScript provides several utility types to facilitate common type transformations. These utilities are available globally.

## `Awaited&#x3C;Type>`

 Released:
 4.5

This type is meant to model operations like `await` in `async` functions, or the
`.then()` method on `Promise`s - specifically, the way that they recursively
unwrap `Promise`s.

 Example

```
 ts ` type A = = T extends null | undefined ? T : T extends object & {
 then(onfulfilled: infer F, ...args: infer _): any;
} ? F extends (value: infer V, ...args: infer _) => any ? Awaited<V> : never : T' >Awaited < ' >Promise < string >>; type A = string type B = = T extends null | undefined ? T : T extends object & {
 then(onfulfilled: infer F, ...args: infer _): any;
} ? F extends (value: infer V, ...args: infer _) => any ? Awaited<V> : never : T' >Awaited < ' >Promise < ' >Promise < number >>>; type B = number type C = = T extends null | undefined ? T : T extends object & {
 then(onfulfilled: infer F, ...args: infer _): any;
} ? F extends (value: infer V, ...args: infer _) => any ? Awaited<V> : never : T' >Awaited < boolean | ' >Promise < number >>; type C = number | boolean ` Try
```

## `Partial&#x3C;Type>`

 Released:
 2.1

Constructs a type with all properties of `Type` set to optional. This utility will return a type that represents all subsets of a given type.

 Example

```
 ts ` interface Todo { title : string ; description : string ; } function ): {
 title: string;
 description: string;
}' >updateTodo ( todo : Todo , ' >fieldsToUpdate : = { [P in keyof T]?: T[P] | undefined; }' >Partial < Todo >) { return { ... todo , ... ' >fieldsToUpdate }; } const todo1 = { title : "organize desk" , description : "clear clutter" , }; const todo2 = ): {
 title: string;
 description: string;
}' >updateTodo ( todo1 , { description : "throw out trash" , }); ` Try
```

## `Required&#x3C;Type>`

 Released:
 2.8

Constructs a type consisting of all properties of `Type` set to required. The opposite of `Partial` .

 Example

```
 ts ` interface Props { a ?: number ; b ?: string ; } const obj : Props = { a : 5 }; const ' >obj2 : = { [P in keyof T]-?: T[P]; }' >Required < Props > = { a : 5 }; Property 'b' is missing in type '{ a: number; }' but required in type 'Required<Props>'. 2741 Property 'b' is missing in type '{ a: number; }' but required in type 'Required<Props>'. ` Try
```

## `Readonly&#x3C;Type>`

 Released:
 2.1

Constructs a type with all properties of `Type` set to `readonly`, meaning the properties of the constructed type cannot be reassigned.

 Example

```
 ts ` interface Todo { title : string ; } const ' >todo : = { readonly [P in keyof T]: T[P]; }' >Readonly < Todo > = { title : "Delete inactive users" , }; ' >todo . title = "Hello" ; Cannot assign to 'title' because it is a read-only property. 2540 Cannot assign to 'title' because it is a read-only property. ` Try
```

 This utility is useful for representing assignment expressions that will fail at runtime (i.e. when attempting to reassign properties of a frozen object ).

 `Object.freeze`

```
 ts ` function freeze < Type >( obj : Type ): Readonly < Type >; `
```

## `Record&#x3C;Keys, Type>`

 Released:
 2.1

Constructs an object type whose property keys are `Keys` and whose property values are `Type`. This utility can be used to map the properties of a type to another type.

 Example

```
 ts ` type CatName = "miffy" | "boris" | "mordred" ; interface CatInfo { age : number ; breed : string ; } const ' >cats : = { [P in K]: T; }' >Record < CatName , CatInfo > = { miffy : { age : 10 , breed : "Persian" }, boris : { age : 5 , breed : "Maine Coon" }, mordred : { age : 16 , breed : "British Shorthair" }, }; ' style='border-bottom: solid 2px lightgrey;'>cats . boris ; const cats: Record<CatName, CatInfo> ` Try
```

## `Pick&#x3C;Type, Keys>`

 Released:
 2.1

Constructs a type by picking the set of properties `Keys` (string literal or union of string literals) from `Type`.

 Example

```
 ts ` interface Todo { title : string ; description : string ; completed : boolean ; } type TodoPreview = = { [P in K]: T[P]; }' >Pick < Todo , "title" | "completed" >; const todo : TodoPreview = { title : "Clean room" , completed : false , }; todo ; const todo: TodoPreview ` Try
```

## `Omit&#x3C;Type, Keys>`

 Released:
 3.5

Constructs a type by picking all properties from `Type` and then removing `Keys` (string literal or union of string literals). The opposite of `Pick` .

 Example

```
 ts ` interface Todo { title : string ; description : string ; completed : boolean ; createdAt : number ; } type TodoPreview = = { [P in Exclude<keyof T, K>]: T[P]; }' >Omit < Todo , "description" >; const todo : TodoPreview = { title : "Clean room" , completed : false , createdAt : 1615544252770 , }; todo ; const todo: TodoPreview type TodoInfo = = { [P in Exclude<keyof T, K>]: T[P]; }' >Omit < Todo , "completed" | "createdAt" >; const todoInfo : TodoInfo = { title : "Pick up kids" , description : "Kindergarten closes at 5pm" , }; todoInfo ; const todoInfo: TodoInfo ` Try
```

## `Exclude&#x3C;UnionType, ExcludedMembers>`

 Released:
 2.8

Constructs a type by excluding from `UnionType` all union members that are assignable to `ExcludedMembers`.

 Example

```
 ts ` type T0 = = T extends U ? never : T' >Exclude < "a" | "b" | "c" , "a" >; type T0 = "b" | "c" type T1 = = T extends U ? never : T' >Exclude < "a" | "b" | "c" , "a" | "b" >; type T1 = "c" type T2 = = T extends U ? never : T' >Exclude < string | number | (() => void ), Function >; type T2 = string | number type Shape = | { kind : "circle" ; radius : number } | { kind : "square" ; x : number } | { kind : "triangle" ; x : number ; y : number }; type T3 = = T extends U ? never : T' >Exclude < Shape , { kind : "circle" }> type T3 = {
 kind: "square";
 x: number;
} | {
 kind: "triangle";
 x: number;
 y: number;
} ` Try
```

## `Extract&#x3C;Type, Union>`

 Released:
 2.8

Constructs a type by extracting from `Type` all union members that are assignable to `Union`.

 Example

```
 ts ` type T0 = = T extends U ? T : never' >Extract < "a" | "b" | "c" , "a" | "f" >; type T0 = "a" type void' style='border-bottom: solid 2px lightgrey;'>T1 = = T extends U ? T : never' >Extract < string | number | (() => void ), Function >; type T1 = () => void type Shape = | { kind : "circle" ; radius : number } | { kind : "square" ; x : number } | { kind : "triangle" ; x : number ; y : number }; type T2 = = T extends U ? T : never' >Extract < Shape , { kind : "circle" }> type T2 = {
 kind: "circle";
 radius: number;
} ` Try
```

## `NonNullable&#x3C;Type>`

 Released:
 2.8

Constructs a type by excluding `null` and `undefined` from `Type`.

 Example

```
 ts ` type T0 = = T & {}' >NonNullable < string | number | undefined >; type T0 = string | number type T1 = = T & {}' >NonNullable < string [] | null | undefined >; type T1 = string[] ` Try
```

## `Parameters&#x3C;Type>`

 Released:
 3.1

Constructs a tuple type from the types used in the parameters of a function type `Type`.

For overloaded functions, this will be the parameters of the last signature; see Inferring Within Conditional Types .

 Example

```
 ts ` declare function f1 ( arg : { a : number ; b : string }): void ; type T0 = any> = T extends (...args: infer P) => any ? P : never' >Parameters <() => string >; type T0 = [] type T1 = any> = T extends (...args: infer P) => any ? P : never' >Parameters <( s : string ) => void >; type T1 = [s: string] type T2 = any> = T extends (...args: infer P) => any ? P : never' >Parameters << (arg: T): T' >T >( arg : (arg: T): T' >T ) => (arg: T): T' >T >; type T2 = [arg: unknown] type T3 = any> = T extends (...args: infer P) => any ? P : never' >Parameters < typeof f1 >; type T3 = [arg: {
 a: number;
 b: string;
}] type T4 = any> = T extends (...args: infer P) => any ? P : never' >Parameters < any >; type T4 = unknown[] type T5 = any> = T extends (...args: infer P) => any ? P : never' >Parameters < never >; type T5 = never type T6 = any> = T extends (...args: infer P) => any ? P : never' >Parameters < string >; Type 'string' does not satisfy the constraint '(...args: any) => any'. 2344 Type 'string' does not satisfy the constraint '(...args: any) => any'. type T6 = never type T7 = any> = T extends (...args: infer P) => any ? P : never' >Parameters < Function >; Type 'Function' does not satisfy the constraint '(...args: any) => any'.
 Type 'Function' provides no match for the signature '(...args: any): any'. 2344 Type 'Function' does not satisfy the constraint '(...args: any) => any'.
 Type 'Function' provides no match for the signature '(...args: any): any'. type T7 = never ` Try
```

## `ConstructorParameters&#x3C;Type>`

 Released:
 3.1

Constructs a tuple or array type from the types of a constructor function type. It produces a tuple type with all the parameter types (or the type `never` if `Type` is not a function).

 Example

```
 ts ` type T0 = any> = T extends abstract new (...args: infer P) => any ? P : never' >ConstructorParameters < ErrorConstructor >; type T0 = [message?: string] type T1 = any> = T extends abstract new (...args: infer P) => any ? P : never' >ConstructorParameters < FunctionConstructor >; type T1 = string[] type T2 = any> = T extends abstract new (...args: infer P) => any ? P : never' >ConstructorParameters < RegExpConstructor >; type T2 = [pattern: string | RegExp, flags?: string] class C { constructor ( a : number , b : string ) {} } type T3 = any> = T extends abstract new (...args: infer P) => any ? P : never' >ConstructorParameters < typeof C >; type T3 = [a: number, b: string] type T4 = any> = T extends abstract new (...args: infer P) => any ? P : never' >ConstructorParameters < any >; type T4 = unknown[] type T5 = any> = T extends abstract new (...args: infer P) => any ? P : never' >ConstructorParameters < Function >; Type 'Function' does not satisfy the constraint 'abstract new (...args: any) => any'.
 Type 'Function' provides no match for the signature 'new (...args: any): any'. 2344 Type 'Function' does not satisfy the constraint 'abstract new (...args: any) => any'.
 Type 'Function' provides no match for the signature 'new (...args: any): any'. type T5 = never ` Try
```

## `ReturnType&#x3C;Type>`

 Released:
 2.8

Constructs a type consisting of the return type of function `Type`.

For overloaded functions, this will be the return type of the last signature; see Inferring Within Conditional Types .

 Example

```
 ts ` declare function f1 (): { a : number ; b : string }; type T0 = any> = T extends (...args: any) => infer R ? R : any' >ReturnType <() => string >; type T0 = string type T1 = any> = T extends (...args: any) => infer R ? R : any' >ReturnType <( s : string ) => void >; type T1 = void type T2 = any> = T extends (...args: any) => infer R ? R : any' >ReturnType << (): T' >T >() => (): T' >T >; type T2 = unknown type T3 = any> = T extends (...args: any) => infer R ? R : any' >ReturnType << (): T' >T extends (): T' >U , (): T' >U extends number []>() => (): T' >T >; type T3 = number[] type T4 = any> = T extends (...args: any) => infer R ? R : any' >ReturnType < typeof f1 >; type T4 = {
 a: number;
 b: string;
} type T5 = any> = T extends (...args: any) => infer R ? R : any' >ReturnType < any >; type T5 = any type T6 = any> = T extends (...args: any) => infer R ? R : any' >ReturnType < never >; type T6 = never type T7 = any> = T extends (...args: any) => infer R ? R : any' >ReturnType < string >; Type 'string' does not satisfy the constraint '(...args: any) => any'. 2344 Type 'string' does not satisfy the constraint '(...args: any) => any'. type T7 = any type T8 = any> = T extends (...args: any) => infer R ? R : any' >ReturnType < Function >; Type 'Function' does not satisfy the constraint '(...args: any) => any'.
 Type 'Function' provides no match for the signature '(...args: any): any'. 2344 Type 'Function' does not satisfy the constraint '(...args: any) => any'.
 Type 'Function' provides no match for the signature '(...args: any): any'. type T8 = any ` Try
```

## `InstanceType&#x3C;Type>`

 Released:
 2.8

Constructs a type consisting of the instance type of a constructor function in `Type`.

 Example

```
 ts ` class C { x = 0 ; y = 0 ; } type T0 = any> = T extends abstract new (...args: any) => infer R ? R : any' >InstanceType < typeof C >; type T0 = C type T1 = any> = T extends abstract new (...args: any) => infer R ? R : any' >InstanceType < any >; type T1 = any type T2 = any> = T extends abstract new (...args: any) => infer R ? R : any' >InstanceType < never >; type T2 = never type T3 = any> = T extends abstract new (...args: any) => infer R ? R : any' >InstanceType < string >; Type 'string' does not satisfy the constraint 'abstract new (...args: any) => any'. 2344 Type 'string' does not satisfy the constraint 'abstract new (...args: any) => any'. type T3 = any type T4 = any> = T extends abstract new (...args: any) => infer R ? R : any' >InstanceType < Function >; Type 'Function' does not satisfy the constraint 'abstract new (...args: any) => any'.
 Type 'Function' provides no match for the signature 'new (...args: any): any'. 2344 Type 'Function' does not satisfy the constraint 'abstract new (...args: any) => any'.
 Type 'Function' provides no match for the signature 'new (...args: any): any'. type T4 = any ` Try
```

## `NoInfer&#x3C;Type>`

 Released:
 5.4

Blocks inferences to the contained type. Other than blocking inferences, `NoInfer&#x3C;Type>` is
identical to `Type`.

 Example

```
 ts ` function createStreetLight < C extends string >( colors : C [], defaultColor ?: NoInfer < C >, ) { // ... } createStreetLight ([ "red" , "yellow" , "green" ], "red" ); // OK createStreetLight ([ "red" , "yellow" , "green" ], "blue" ); // Error `
```

## `ThisParameterType&#x3C;Type>`

 Released:
 3.3

Extracts the type of the this parameter for a function type, or unknown if the function type has no `this` parameter.

 Example

```
 ts ` function toHex ( this : Number ) { return this . toString ( 16 ); } function ): string' >numberToString ( n : = T extends (this: infer U, ...args: never) => any ? U : unknown' >ThisParameterType < typeof toHex >) { return toHex . (this: (this: Number) => string, thisArg: Number): string (+1 overload)' >apply ( n ); } ` Try
```

## `OmitThisParameter&#x3C;Type>`

 Released:
 3.3

Removes the `this` parameter from `Type`. If `Type` has no explicitly declared `this` parameter, the result is simply `Type`. Otherwise, a new function type with no `this` parameter is created from `Type`. Generics are erased and only the last overload signature is propagated into the new function type.

 Example

```
 ts ` function toHex ( this : Number ) { return this . toString ( 16 ); } const string' >fiveToHex : = unknown extends ThisParameterType<T> ? T : T extends (...args: infer A) => infer R ? (...args: A) => R : T' >OmitThisParameter < typeof toHex > = toHex . string>(this: (this: Number) => string, thisArg: Number): () => string (+1 overload)' >bind ( 5 ); console . log ( string' >fiveToHex ()); ` Try
```

## `ThisType&#x3C;Type>`

 Released:
 2.3

This utility does not return a transformed type. Instead, it serves as a marker for a contextual `this` type. Note that the `noImplicitThis` flag must be enabled to use this utility.

 Example

```
 ts ` type = {
 data?: D;
 methods?: M & ThisType<D & M>;
}' >ObjectDescriptor < ' >D , ' >M > = { data ?: ' >D ; ) | undefined' >methods ?: ' >M & ' >ThisType < ' >D & ' >M >; // Type of &apos;this&apos; in methods is D & M }; function (desc: ObjectDescriptor<D, M>): D & M' >makeObject < (desc: ObjectDescriptor<D, M>): D & M' >D , (desc: ObjectDescriptor<D, M>): D & M' >M >( ' >desc : = {
 data?: D;
 methods?: M & ThisType<D & M>;
}' >ObjectDescriptor < (desc: ObjectDescriptor<D, M>): D & M' >D , (desc: ObjectDescriptor<D, M>): D & M' >M >): (desc: ObjectDescriptor<D, M>): D & M' >D & (desc: ObjectDescriptor<D, M>): D & M' >M { let data : object = ' >desc . data || {}; let methods : object = ' >desc . ) | undefined' >methods || {}; return { ... data , ... methods } as (desc: ObjectDescriptor<D, M>): D & M' >D & (desc: ObjectDescriptor<D, M>): D & M' >M ; } let obj = (desc: ObjectDescriptor<{
 x: number;
 y: number;
}, {
 moveBy(dx: number, dy: number): void;
}>): {
 x: number;
 y: number;
} & {
 moveBy(dx: number, dy: number): void;
}' >makeObject ({ data : { x : 0 , y : 0 }, ) | undefined' >methods : { moveBy ( dx : number , dy : number ) { this . x += dx ; // Strongly typed this this . y += dy ; // Strongly typed this }, }, }); obj . x = 10 ; obj . y = 20 ; obj . moveBy ( 5 , 5 ); ` Try
```

 In the example above, the `methods` object in the argument to `makeObject` has a contextual type that includes `ThisType&#x3C;D &#x26; M>` and therefore the type of this in methods within the `methods` object is `{ x: number, y: number } &#x26; { moveBy(dx: number, dy: number): void }`. Notice how the type of the `methods` property simultaneously is an inference target and a source for the `this` type in methods.

The `ThisType&#x3C;T>` marker interface is simply an empty interface declared in `lib.d.ts`. Beyond being recognized in the contextual type of an object literal, the interface acts like any empty interface.

## Intrinsic String Manipulation Types

### `Uppercase&#x3C;StringType>`

### `Lowercase&#x3C;StringType>`

### `Capitalize&#x3C;StringType>`

### `Uncapitalize&#x3C;StringType>`

 To help with string manipulation around template string literals, TypeScript includes a set of types which can be used in string manipulation within the type system. You can find those in the Template Literal Types documentation.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: C OT B JB HX 34+ Last updated: Jun 15, 2026

## Decorators

Was this page helpful?

# Decorators

 NOTE  This document refers to an experimental stage 2 decorators implementation. Stage 3 decorator support is available since Typescript 5.0.
See: Decorators in Typescript 5.0

## Introduction

 With the introduction of Classes in TypeScript and ES6, there now exist certain scenarios that require additional features to support annotating or modifying classes and class members.
Decorators provide a way to add both annotations and a meta-programming syntax for class declarations and members.

Further Reading (stage 2): A Complete Guide to TypeScript Decorators

To enable experimental support for decorators, you must enable the `experimentalDecorators` compiler option either on the command line or in your `tsconfig.json`:

 Command Line :

 shell ` tsc --target ES5 --experimentalDecorators `
 tsconfig.json :

 ` { " compilerOptions " : { " target " : "ES5" , " experimentalDecorators " : true } } `

## Decorators

 A Decorator is a special kind of declaration that can be attached to a class declaration , method , accessor , property , or parameter .
Decorators use the form `@expression`, where `expression` must evaluate to a function that will be called at runtime with information about the decorated declaration.

For example, given the decorator `@sealed` we might write the `sealed` function as follows:

 ts ` function sealed ( target ) { // do something with 'target' ... } `

## Decorator Factories

 If we want to customize how a decorator is applied to a declaration, we can write a decorator factory.
A Decorator Factory is simply a function that returns the expression that will be called by the decorator at runtime.

We can write a decorator factory in the following fashion:

 ts ` function color ( value : string ) { // this is the decorator factory, it sets up // the returned decorator function return function ( target ) { // this is the decorator // do something with 'target' and 'value'... }; } `

## Decorator Composition

 Multiple decorators can be applied to a declaration, for example on a single line:

 ts ` @ f @ g x ` Try
 On multiple lines:

 ts ` @ f @ g x ` Try
 When multiple decorators apply to a single declaration, their evaluation is similar to function composition in mathematics . In this model, when composing functions f and g , the resulting composite ( f ∘ g )( x ) is equivalent to f ( g ( x )).

As such, the following steps are performed when evaluating multiple decorators on a single declaration in TypeScript:

- The expressions for each decorator are evaluated top-to-bottom.

- The results are then called as functions from bottom-to-top.

If we were to use decorator factories , we can observe this evaluation order with the following example:

 ts ` function void' >first () { console . log ( "first(): factory evaluated" ); return function ( target : any , propertyKey : string , descriptor : PropertyDescriptor ) { console . log ( "first(): called" ); }; } function void' >second () { console . log ( "second(): factory evaluated" ); return function ( target : any , propertyKey : string , descriptor : PropertyDescriptor ) { console . log ( "second(): called" ); }; } class ExampleClass { @ void' >first () @ void' >second () method () {} } ` Try
 Which would print this output to the console:

 shell ` first (): factory evaluated second (): factory evaluated second (): called first (): called `

## Decorator Evaluation

 There is a well defined order to how decorators applied to various declarations inside of a class are applied:

- Parameter Decorators , followed by Method , Accessor , or Property Decorators are applied for each instance member.

- Parameter Decorators , followed by Method , Accessor , or Property Decorators are applied for each static member.

- Parameter Decorators are applied for the constructor.

- Class Decorators are applied for the class.

## Class Decorators

 A Class Decorator is declared just before a class declaration.
The class decorator is applied to the constructor of the class and can be used to observe, modify, or replace a class definition.
A class decorator cannot be used in a declaration file, or in any other ambient context (such as on a `declare` class).

The expression for the class decorator will be called as a function at runtime, with the constructor of the decorated class as its only argument.

If the class decorator returns a value, it will replace the class declaration with the provided constructor function.

NOTE  Should you choose to return a new constructor function, you must take care to maintain the original prototype.
The logic that applies decorators at runtime will not do this for you.

The following is an example of a class decorator (`@sealed`) applied to a `BugReport` class:

 ts ` @ sealed class BugReport { type = "report" ; title : string ; constructor ( t : string ) { this . title = t ; } } ` Try
 We can define the `@sealed` decorator using the following function declaration:

 ts ` function sealed ( constructor : Function ) { Object . seal ( constructor ); Object . seal ( constructor . prototype ); } `
 When `@sealed` is executed, it will seal both the constructor and its prototype, and will therefore prevent any further functionality from being added to or removed from this class during runtime by accessing `BugReport.prototype` or by defining properties on `BugReport` itself (note that ES2015 classes are really just syntactic sugar to prototype-based constructor functions). This decorator does not prevent classes from sub-classing `BugReport`.

Next we have an example of how to override the constructor to set new defaults.

 ts ` function (constructor: T): {
 new (...args: any[]): (Anonymous class);
 prototype: reportableClassDecorator<any>.(Anonymous class);
} & T' >reportableClassDecorator < (constructor: T): {
 new (...args: any[]): (Anonymous class);
 prototype: reportableClassDecorator<any>.(Anonymous class);
} & T' >T extends { new (... args : any []): {} }>( constructor : (constructor: T): {
 new (...args: any[]): (Anonymous class);
 prototype: reportableClassDecorator<any>.(Anonymous class);
} & T' >T ) { return class extends constructor { reportingURL = "http://www..." ; }; } @ (constructor: T): {
 new (...args: any[]): (Anonymous class);
 prototype: reportableClassDecorator<any>.(Anonymous class);
} & T' >reportableClassDecorator class BugReport { type = "report" ; title : string ; constructor ( t : string ) { this . title = t ; } } const bug = new BugReport ( "Needs dark mode" ); console . log ( bug . title ); // Prints "Needs dark mode" console . log ( bug . type ); // Prints "report" // Note that the decorator _does not_ change the TypeScript type // and so the new property `reportingURL` is not known // to the type system: bug . reportingURL ; Property 'reportingURL' does not exist on type 'BugReport'. 2339 Property 'reportingURL' does not exist on type 'BugReport'. ` Try

## Method Decorators

 A Method Decorator is declared just before a method declaration.
The decorator is applied to the Property Descriptor for the method, and can be used to observe, modify, or replace a method definition.
A method decorator cannot be used in a declaration file, on an overload, or in any other ambient context (such as in a `declare` class).

The expression for the method decorator will be called as a function at runtime, with the following three arguments:

- Either the constructor function of the class for a static member, or the prototype of the class for an instance member.

- The name of the member.

- The Property Descriptor for the member.

NOTE  The Property Descriptor will be `undefined` if your script target is less than `ES5`.

If the method decorator returns a value, it will be used as the Property Descriptor for the method.

NOTE  The return value is ignored if your script target is less than `ES5`.

The following is an example of a method decorator (`@enumerable`) applied to a method on the `Greeter` class:

 ts ` class Greeter { greeting : string ; constructor ( message : string ) { this . greeting = message ; } @ void' >enumerable ( false ) greet () { return "Hello, " + this . greeting ; } } ` Try
 We can define the `@enumerable` decorator using the following function declaration:

 ts ` function void' >enumerable ( value : boolean ) { return function ( target : any , propertyKey : string , descriptor : PropertyDescriptor ) { descriptor . enumerable = value ; }; } ` Try
 The `@enumerable(false)` decorator here is a decorator factory .
When the `@enumerable(false)` decorator is called, it modifies the `enumerable` property of the property descriptor.

## Accessor Decorators

 An Accessor Decorator is declared just before an accessor declaration.
The accessor decorator is applied to the Property Descriptor for the accessor and can be used to observe, modify, or replace an accessor’s definitions.
An accessor decorator cannot be used in a declaration file, or in any other ambient context (such as in a `declare` class).

NOTE  TypeScript disallows decorating both the `get` and `set` accessor for a single member.
Instead, all decorators for the member must be applied to the first accessor specified in document order.
This is because decorators apply to a Property Descriptor , which combines both the `get` and `set` accessor, not each declaration separately.

The expression for the accessor decorator will be called as a function at runtime, with the following three arguments:

- Either the constructor function of the class for a static member, or the prototype of the class for an instance member.

- The name of the member.

- The Property Descriptor for the member.

NOTE  The Property Descriptor will be `undefined` if your script target is less than `ES5`.

If the accessor decorator returns a value, it will be used as the Property Descriptor for the member.

NOTE  The return value is ignored if your script target is less than `ES5`.

The following is an example of an accessor decorator (`@configurable`) applied to a member of the `Point` class:

 ts ` class Point { private _x : number ; private _y : number ; constructor ( x : number , y : number ) { this . _x = x ; this . _y = y ; } @ void' >configurable ( false ) get x () { return this . _x ; } @ void' >configurable ( false ) get y () { return this . _y ; } } ` Try
 We can define the `@configurable` decorator using the following function declaration:

 ts ` function configurable ( value : boolean ) { return function ( target : any , propertyKey : string , descriptor : PropertyDescriptor ) { descriptor . configurable = value ; }; } `

## Property Decorators

 A Property Decorator is declared just before a property declaration.
A property decorator cannot be used in a declaration file, or in any other ambient context (such as in a `declare` class).

The expression for the property decorator will be called as a function at runtime, with the following two arguments:

- Either the constructor function of the class for a static member, or the prototype of the class for an instance member.

- The name of the member.

NOTE  A Property Descriptor is not provided as an argument to a property decorator due to how property decorators are initialized in TypeScript.
This is because there is currently no mechanism to describe an instance property when defining members of a prototype, and no way to observe or modify the initializer for a property. The return value is ignored too.
As such, a property decorator can only be used to observe that a property of a specific name has been declared for a class.

We can use this information to record metadata about the property, as in the following example:

 ts ` class Greeter { @ format ( "Hello, %s" ) greeting : string ; constructor ( message : string ) { this . greeting = message ; } greet () { let formatString = getFormat ( this , "greeting" ); return formatString . replace ( "%s" , this . greeting ); } } `
 We can then define the `@format` decorator and `getFormat` functions using the following function declarations:

 ts ` import "reflect-metadata" ; const formatMetadataKey = Symbol ( "format" ); function format ( formatString : string ) { return Reflect . metadata ( formatMetadataKey , formatString ); } function getFormat ( target : any , propertyKey : string ) { return Reflect . getMetadata ( formatMetadataKey , target , propertyKey ); } `
 The `@format("Hello, %s")` decorator here is a decorator factory .
When `@format("Hello, %s")` is called, it adds a metadata entry for the property using the `Reflect.metadata` function from the `reflect-metadata` library.
When `getFormat` is called, it reads the metadata value for the format.

NOTE  This example requires the `reflect-metadata` library.
See Metadata for more information about the `reflect-metadata` library.

## Parameter Decorators

 A Parameter Decorator is declared just before a parameter declaration.
The parameter decorator is applied to the function for a class constructor or method declaration.
A parameter decorator cannot be used in a declaration file, an overload, or in any other ambient context (such as in a `declare` class).

The expression for the parameter decorator will be called as a function at runtime, with the following three arguments:

- Either the constructor function of the class for a static member, or the prototype of the class for an instance member.

- The name of the member.

- The ordinal index of the parameter in the function’s parameter list.

NOTE  A parameter decorator can only be used to observe that a parameter has been declared on a method.

The return value of the parameter decorator is ignored.

The following is an example of a parameter decorator (`@required`) applied to parameter of a member of the `BugReport` class:

 ts ` class BugReport { type = "report" ; title : string ; constructor ( t : string ) { this . title = t ; } @ ): void' >validate print (@ required verbose : boolean ) { if ( verbose ) { return `type: ${ this . type } \n title: ${ this . title } ` ; } else { return this . title ; } } } ` Try
 We can then define the `@required` and `@validate` decorators using the following function declarations:

 ts ` import "reflect-metadata" ; const requiredMetadataKey = symbol' >Symbol ( "required" ); function required ( target : Object , propertyKey : string | symbol , parameterIndex : number ) { let existingRequiredParameters : number [] = Reflect . getOwnMetadata ( requiredMetadataKey , target , propertyKey ) || []; existingRequiredParameters . .push(...items: number[]): number' >push ( parameterIndex ); Reflect . defineMetadata ( requiredMetadataKey , existingRequiredParameters , target , propertyKey ); } function ): void' >validate ( target : any , propertyName : string , ' >descriptor : ' >TypedPropertyDescriptor < Function >) { let method = ' >descriptor . .value?: Function | undefined' >value !; ' >descriptor . .value?: Function | undefined' >value = function () { let requiredParameters : number [] = Reflect . getOwnMetadata ( requiredMetadataKey , target , propertyName ); if ( requiredParameters ) { for ( let parameterIndex of requiredParameters ) { if ( parameterIndex >= arguments . length || arguments [ parameterIndex ] === undefined ) { throw new Error' >Error ( "Missing required argument." ); } } } return method . apply ( this , arguments ); }; } ` Try
 The `@required` decorator adds a metadata entry that marks the parameter as required.
The `@validate` decorator then wraps the existing `print` method in a function that validates the arguments before invoking the original method.

NOTE  This example requires the `reflect-metadata` library.
See Metadata for more information about the `reflect-metadata` library.

## Metadata

 Some examples use the `reflect-metadata` library which adds a polyfill for an experimental metadata API .
This library is not yet part of the ECMAScript (JavaScript) standard.
However, once decorators are officially adopted as part of the ECMAScript standard these extensions will be proposed for adoption.

You can install this library via npm:

 shell ` npm i reflect-metadata --save `
 TypeScript includes experimental support for emitting certain types of metadata for declarations that have decorators.
To enable this experimental support, you must set the `emitDecoratorMetadata` compiler option either on the command line or in your `tsconfig.json`:

 Command Line :

 shell ` tsc --target ES5 --experimentalDecorators --emitDecoratorMetadata `
 tsconfig.json :

 ` { " compilerOptions " : { " target " : "ES5" , " experimentalDecorators " : true , " emitDecoratorMetadata " : true } } `
 When enabled, as long as the `reflect-metadata` library has been imported, additional design-time type information will be exposed at runtime.

We can see this in action in the following example:

 ts ` import "reflect-metadata" ; class Point { constructor ( public x : number , public y : number ) {} } class Line { private _start : Point ; private _end : Point ; @ (target: any, propertyKey: string, descriptor: TypedPropertyDescriptor<T>): void' >validate set start ( value : Point ) { this . _start = value ; } get start () { return this . _start ; } @ (target: any, propertyKey: string, descriptor: TypedPropertyDescriptor<T>): void' >validate set end ( value : Point ) { this . _end = value ; } get end () { return this . _end ; } } function (target: any, propertyKey: string, descriptor: TypedPropertyDescriptor<T>): void' >validate < (target: any, propertyKey: string, descriptor: TypedPropertyDescriptor<T>): void' >T >( target : any , propertyKey : string , ' >descriptor : ' >TypedPropertyDescriptor < (target: any, propertyKey: string, descriptor: TypedPropertyDescriptor<T>): void' >T >) { let void' >set = ' >descriptor . .set?: ((value: T) => void) | undefined' >set !; ' >descriptor . .set?: ((value: T) => void) | undefined' >set = function ( value : (target: any, propertyKey: string, descriptor: TypedPropertyDescriptor<T>): void' >T ) { let type = Reflect . getMetadata ( "design:type" , target , propertyKey ); if (!( value instanceof type )) { throw new TypeError (+1 overload)' >TypeError ( `Invalid type, got ${ typeof value } not ${ type . name } .` ); } void' >set . , [T], void>(this: (this: TypedPropertyDescriptor<T>, args_0: T) => void, thisArg: TypedPropertyDescriptor<T>, args_0: T): void' >call ( this , value ); }; } const line = new Line () line . start = new Point ( 0 , 0 ) // @ts-ignore // line.end = {} // Fails at runtime with: // > Invalid type, got object not Point ` Try
 The TypeScript compiler will inject design-time type information using the `@Reflect.metadata` decorator.
You could consider it the equivalent of the following TypeScript:

 ts ` class Line { private _start : Point ; private _end : Point ; @ validate @ Reflect . metadata ( "design:type" , Point ) set start ( value : Point ) { this . _start = value ; } get start () { return this . _start ; } @ validate @ Reflect . metadata ( "design:type" , Point ) set end ( value : Point ) { this . _end = value ; } get end () { return this . _end ; } } `

 NOTE  Decorator metadata is an experimental feature and may introduce breaking changes in future releases.

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: RB OT MH DR HA 22+ Last updated: Jun 15, 2026

## Declaration Merging

Was this page helpful?

# Declaration Merging

## Introduction

 Some of the unique concepts in TypeScript describe the shape of JavaScript objects at the type level.
One example that is especially unique to TypeScript is the concept of ‘declaration merging’.
Understanding this concept will give you an advantage when working with existing JavaScript.
It also opens the door to more advanced abstraction concepts.

For the purposes of this article, “declaration merging” means that the compiler merges two separate declarations declared with the same name into a single definition.
This merged definition has the features of both of the original declarations.
Any number of declarations can be merged; it’s not limited to just two declarations.

## Basic Concepts

 In TypeScript, a declaration creates entities in at least one of three groups: namespace, type, or value.
Namespace-creating declarations create a namespace, which contains names that are accessed using a dotted notation.
Type-creating declarations do just that: they create a type that is visible with the declared shape and bound to the given name.
Lastly, value-creating declarations create values that are visible in the output JavaScript.

| **

 Declaration Type**
| **Namespace**
| **Type**
| **Value**
|

| Namespace
| X
|
| X
|

| Class
|
| X
| X
|

| Enum
|
| X
| X
|

| Interface
|
| X
|
|

| Type Alias
|
| X
|
|

| Function
|
|
| X
|

| Variable
|
|
| X
|

Understanding what is created with each declaration will help you understand what is merged when you perform a declaration merge.

## Merging Interfaces

 The simplest, and perhaps most common, type of declaration merging is interface merging.
At the most basic level, the merge mechanically joins the members of both declarations into a single interface with the same name.

 ts ` interface Box { height : number ; width : number ; } interface Box { scale : number ; } let box : Box = { height: 5 , width: 6 , scale: 10 }; `
 Non-function members of the interfaces should be unique.
If they are not unique, they must be of the same type.
The compiler will issue an error if the interfaces both declare a non-function member of the same name, but of different types.

For function members, each function member of the same name is treated as describing an overload of the same function.
Of note, too, is that in the case of interface `A` merging with later interface `A`, the second interface will have a higher precedence than the first.

That is, in the example:

 ts ` interface Cloner { clone ( animal : Animal ): Animal ; } interface Cloner { clone ( animal : Sheep ): Sheep ; } interface Cloner { clone ( animal : Dog ): Dog ; clone ( animal : Cat ): Cat ; } `
 The three interfaces will merge to create a single declaration as so:

 ts ` interface Cloner { clone ( animal : Dog ): Dog ; clone ( animal : Cat ): Cat ; clone ( animal : Sheep ): Sheep ; clone ( animal : Animal ): Animal ; } `
 Notice that the elements of each group maintains the same order, but the groups themselves are merged with later overload sets ordered first.

One exception to this rule is specialized signatures.
If a signature has a parameter whose type is a single string literal type (e.g. not a union of string literals), then it will be bubbled toward the top of its merged overload list.

For instance, the following interfaces will merge together:

 ts ` interface Document { createElement ( tagName : any ): Element ; } interface Document { createElement ( tagName : "div" ): HTMLDivElement ; createElement ( tagName : "span" ): HTMLSpanElement ; } interface Document { createElement ( tagName : string ): HTMLElement ; createElement ( tagName : "canvas" ): HTMLCanvasElement ; } `
 The resulting merged declaration of `Document` will be the following:

 ts ` interface Document { createElement ( tagName : "canvas" ): HTMLCanvasElement ; createElement ( tagName : "div" ): HTMLDivElement ; createElement ( tagName : "span" ): HTMLSpanElement ; createElement ( tagName : string ): HTMLElement ; createElement ( tagName : any ): Element ; } `

## Merging Namespaces

 Similarly to interfaces, namespaces of the same name will also merge their members.
Since namespaces create both a namespace and a value, we need to understand how both merge.

To merge the namespaces, type definitions from exported interfaces declared in each namespace are themselves merged, forming a single namespace with merged interface definitions inside.

To merge the namespace value, at each declaration site, if a namespace already exists with the given name, it is further extended by taking the existing namespace and adding the exported members of the second namespace to the first.

The declaration merge of `Animals` in this example:

 ts ` namespace Animals { export class Zebra {} } namespace Animals { export interface Legged { numberOfLegs : number ; } export class Dog {} } `
 is equivalent to:

 ts ` namespace Animals { export interface Legged { numberOfLegs : number ; } export class Zebra {} export class Dog {} } `
 This model of namespace merging is a helpful starting place, but we also need to understand what happens with non-exported members.
Non-exported members are only visible in the original (un-merged) namespace. This means that after merging, merged members that came from other declarations cannot see non-exported members.

We can see this more clearly in this example:

 ts ` namespace Animal { let haveMuscles = true ; export function animalsHaveMuscles () { return haveMuscles ; } } namespace Animal { export function doAnimalsHaveMuscles () { return haveMuscles ; // Error, because haveMuscles is not accessible here } } `
 Because `haveMuscles` is not exported, only the `animalsHaveMuscles` function that shares the same un-merged namespace can see the symbol.
The `doAnimalsHaveMuscles` function, even though it’s part of the merged `Animal` namespace can not see this un-exported member.

## Merging Namespaces with Classes, Functions, and Enums

 Namespaces are flexible enough to also merge with other types of declarations.
To do so, the namespace declaration must follow the declaration it will merge with. The resulting declaration has properties of both declaration types.
TypeScript uses this capability to model some of the patterns in JavaScript as well as other programming languages.

### Merging Namespaces with Classes

 This gives the user a way of describing inner classes.

 ts ` class Album { label : Album . AlbumLabel ; } namespace Album { export class AlbumLabel {} } `
 The visibility rules for merged members is the same as described in the Merging Namespaces section, so we must export the `AlbumLabel` class for the merged class to see it.
The end result is a class managed inside of another class.
You can also use namespaces to add more static members to an existing class.

In addition to the pattern of inner classes, you may also be familiar with the JavaScript practice of creating a function and then extending the function further by adding properties onto the function.
TypeScript uses declaration merging to build up definitions like this in a type-safe way.

 ts ` function buildLabel ( name : string ): string { return buildLabel . prefix + name + buildLabel . suffix ; } namespace buildLabel { export let suffix = "" ; export let prefix = "Hello, " ; } console . log ( buildLabel ( "Sam Smith" )); `
 Similarly, namespaces can be used to extend enums with static members:

 ts ` enum Color { red = 1 , green = 2 , blue = 4 , } namespace Color { export function mixColor ( colorName : string ) { if ( colorName == "yellow" ) { return Color . red + Color . green ; } else if ( colorName == "white" ) { return Color . red + Color . green + Color . blue ; } else if ( colorName == "magenta" ) { return Color . red + Color . blue ; } else if ( colorName == "cyan" ) { return Color . green + Color . blue ; } } } `

## Disallowed Merges

 Not all merges are allowed in TypeScript.
Currently, classes can not merge with other classes or with variables.
For information on mimicking class merging, see the Mixins in TypeScript section.

## Module Augmentation

 Although JavaScript modules do not support merging, you can patch existing objects by importing and then updating them.
Let’s look at a toy Observable example:

 ts ` // observable.ts export class Observable < T > { // ... implementation left as an exercise for the reader ... } // map.ts import { Observable } from "./observable" ; Observable . prototype . map = function ( f ) { // ... another exercise for the reader }; `
 This works fine in TypeScript too, but the compiler doesn’t know about `Observable.prototype.map`.
You can use module augmentation to tell the compiler about it:

 ts ` // observable.ts export class Observable < T > { // ... implementation left as an exercise for the reader ... } // map.ts import { Observable } from "./observable" ; declare module "./observable" { interface Observable < T > { map < U >( f : ( x : T ) => U ): Observable < U >; } } Observable . prototype . map = function ( f ) { // ... another exercise for the reader }; // consumer.ts import { Observable } from "./observable" ; import "./map" ; let o : Observable < number >; o . map (( x ) => x . toFixed ()); `
 The module name is resolved the same way as module specifiers in `import`/`export`.
See Modules for more information.
Then the declarations in an augmentation are merged as if they were declared in the same file as the original.

However, there are two limitations to keep in mind:

- You can’t declare new top-level declarations in the augmentation — just patches to existing declarations.

- Default exports also cannot be augmented, only named exports (since you need to augment an export by its exported name, and `default` is a reserved word - see #14080 for details)

### Global augmentation

 You can also add declarations to the global scope from inside a module:

 ts ` // observable.ts export class Observable < T > { // ... still no implementation ... } declare global { interface Array < T > { toObservable (): Observable < T >; } } Array . prototype . toObservable = function () { // ... }; `
 Global augmentations have the same behavior and limits as module augmentations.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: RC DR OT NS MF 15+ Last updated: Jun 15, 2026

## Enums

Was this page helpful?

# Enums
 Enums are one of the few features TypeScript has which is not a type-level extension of JavaScript.

Enums allow a developer to define a set of named constants.
Using enums can make it easier to document intent, or create a set of distinct cases.
TypeScript provides both numeric and string-based enums.

## Numeric enums

 We’ll first start off with numeric enums, which are probably more familiar if you’re coming from other languages.
An enum can be defined using the `enum` keyword.

 ts ` enum Direction { Up = 1 , Down , Left , Right , } ` Try
 Above, we have a numeric enum where `Up` is initialized with `1`.
All of the following members are auto-incremented from that point on.
In other words, `Direction.Up` has the value `1`, `Down` has `2`, `Left` has `3`, and `Right` has `4`.

If we wanted, we could leave off the initializers entirely:

 ts ` enum Direction { Up , Down , Left , Right , } ` Try
 Here, `Up` would have the value `0`, `Down` would have `1`, etc.
This auto-incrementing behavior is useful for cases where we might not care about the member values themselves, but do care that each value is distinct from other values in the same enum.

Using an enum is simple: just access any member as a property off of the enum itself, and declare types using the name of the enum:

 ts ` enum UserResponse { No = 0 , Yes = 1 , } function respond ( recipient : string , message : UserResponse ): void { // ... } respond ( "Princess Caroline" , UserResponse . Yes ); ` Try
 Numeric enums can be mixed in computed and constant members (see below) .
The short story is, enums without initializers either need to be first, or have to come after numeric enums initialized with numeric constants or other constant enum members.
In other words, the following isn’t allowed:

 ts ` enum E { A = number' >getSomeValue (), B , Enum member must have initializer. 1061 Enum member must have initializer. } ` Try

## String enums

 String enums are a similar concept, but have some subtle runtime differences as documented below.
In a string enum, each member has to be constant-initialized with a string literal, or with another string enum member.

 ts ` enum Direction { Up = "UP" , Down = "DOWN" , Left = "LEFT" , Right = "RIGHT" , } ` Try
 While string enums don’t have auto-incrementing behavior, string enums have the benefit that they “serialize” well.
In other words, if you were debugging and had to read the runtime value of a numeric enum, the value is often opaque - it doesn’t convey any useful meaning on its own (though reverse mapping can often help). String enums allow you to give a meaningful and readable value when your code runs, independent of the name of the enum member itself.

## Heterogeneous enums

 Technically enums can be mixed with string and numeric members, but it’s not clear why you would ever want to do so:

 ts ` enum BooleanLikeHeterogeneousEnum { No = 0 , Yes = "YES" , } ` Try
 Unless you’re really trying to take advantage of JavaScript’s runtime behavior in a clever way, it’s advised that you don’t do this.

## Computed and constant members

 Each enum member has a value associated with it which can be either constant or computed .
An enum member is considered constant if:

-
It is the first member in the enum and it has no initializer, in which case it’s assigned the value `0`:

 ts ` // E.X is constant: enum E { X , } ` Try

-
 It does not have an initializer and the preceding enum member was a numeric constant.
In this case the value of the current enum member will be the value of the preceding enum member plus one.

 ts ` // All enum members in &apos;E1&apos; and &apos;E2&apos; are constant. enum E1 { X , Y , Z , } enum E2 { A = 1 , B , C , } ` Try

-
 The enum member is initialized with a constant enum expression.
A constant enum expression is a subset of TypeScript expressions that can be fully evaluated at compile time.
An expression is a constant enum expression if it is:

 a literal enum expression (basically a string literal or a numeric literal)

- a reference to previously defined constant enum member (which can originate from a different enum)

- a parenthesized constant enum expression

- one of the `+`, `-`, `~` unary operators applied to constant enum expression

- `+`, `-`, `*`, `/`, `%`, `&#x3C;&#x3C;`, `>>`, `>>>`, `&#x26;`, `|`, `^` binary operators with constant enum expressions as operands

It is a compile time error for constant enum expressions to be evaluated to `NaN` or `Infinity`.

In all other cases enum member is considered computed.

 ts ` enum FileAccess { // constant members None , Read = 1 << 1 , Write = 1 << 2 , ReadWrite = Read | Write , // computed member G = "123" . length , } ` Try

## Union enums and enum member types

 There is a special subset of constant enum members that aren’t calculated: literal enum members.
A literal enum member is a constant enum member with no initialized value, or with values that are initialized to

- any string literal (e.g. `"foo"`, `"bar"`, `"baz"`)

- any numeric literal (e.g. `1`, `100`)

- a unary minus applied to any numeric literal (e.g. `-1`, `-100`)

When all members in an enum have literal enum values, some special semantics come into play.

The first is that enum members also become types as well!
For example, we can say that certain members can only have the value of an enum member:

 ts ` enum ShapeKind { Circle , Square , } interface Circle { kind : ShapeKind . Circle ; radius : number ; } interface Square { kind : ShapeKind . Square ; sideLength : number ; } let c : Circle = { kind : ShapeKind . Square , Type 'ShapeKind.Square' is not assignable to type 'ShapeKind.Circle'. 2322 Type 'ShapeKind.Square' is not assignable to type 'ShapeKind.Circle'. radius : 100 , }; ` Try
 The other change is that enum types themselves effectively become a union of each enum member.
With union enums, the type system is able to leverage the fact that it knows the exact set of values that exist in the enum itself.
Because of that, TypeScript can catch bugs where we might be comparing values incorrectly.
For example:

 ts ` enum E { Foo , Bar , } function f ( x : E ) { if ( x !== E . Foo || x !== E . Bar ) { This comparison appears to be unintentional because the types 'E.Foo' and 'E.Bar' have no overlap. 2367 This comparison appears to be unintentional because the types 'E.Foo' and 'E.Bar' have no overlap. // } } ` Try
 In that example, we first checked whether `x` was not `E.Foo`.
If that check succeeds, then our `||` will short-circuit, and the body of the ‘if’ will run.
However, if the check didn’t succeed, then `x` can only be `E.Foo`, so it doesn’t make sense to see whether it’s not equal to `E.Bar`.

## Enums at runtime

 Enums are real objects that exist at runtime.
For example, the following enum

 ts ` enum E { X , Y , Z , } ` Try
 can actually be passed around to functions

 ts ` enum E { X , Y , Z , } function f ( obj : { X : number }) { return obj . X ; } // Works, since &apos;E&apos; has a property named &apos;X&apos; which is a number. f ( E ); ` Try

## Enums at compile time

 Even though Enums are real objects that exist at runtime, the `keyof` keyword works differently than you might expect for typical objects. Instead, use `keyof typeof` to get a Type that represents all Enum keys as strings.

 ts ` enum LogLevel { ERROR , WARN , INFO , DEBUG , } /** * This is equivalent to: * type LogLevelStrings = &apos;ERROR&apos; | &apos;WARN&apos; | &apos;INFO&apos; | &apos;DEBUG&apos;; */ type LogLevelStrings = keyof typeof LogLevel ; function printImportant ( key : LogLevelStrings , message : string ) { const num = LogLevel [ key ]; if ( num <= LogLevel . WARN ) { console . log ( "Log level key is:" , key ); console . log ( "Log level value is:" , num ); console . log ( "Log level message is:" , message ); } } printImportant ( "ERROR" , "This is a message" ); ` Try

### Reverse mappings

 In addition to creating an object with property names for members, numeric enums members also get a reverse mapping from enum values to enum names.
For example, in this example:

 ts ` enum Enum { A , } let a = Enum . A ; let nameOfA = Enum [ a ]; // "A" ` Try
 TypeScript compiles this down to the following JavaScript:

 ts ` "use strict" ; var Enum ; ( function ( Enum ) { Enum [ Enum [ "A" ] = 0 ] = "A" ; })( Enum || ( Enum = {})); let a = Enum . A ; let nameOfA = Enum [ a ]; // "A" ` Try
 In this generated code, an enum is compiled into an object that stores both forward (`name` -> `value`) and reverse (`value` -> `name`) mappings.
References to other enum members are always emitted as property accesses and never inlined.

Keep in mind that string enum members do not get a reverse mapping generated at all.

### `const` enums

 In most cases, enums are a perfectly valid solution.
However sometimes requirements are tighter.
To avoid paying the cost of extra generated code and additional indirection when accessing enum values, it’s possible to use `const` enums.
Const enums are defined using the `const` modifier on our enums:

 ts ` const enum Enum { A = 1 , B = A * 2 , } ` Try
 Const enums can only use constant enum expressions and unlike regular enums they are completely removed during compilation.
Const enum members are inlined at use sites.
This is possible since const enums cannot have computed members.

 ts ` const enum Direction { Up , Down , Left , Right , } let directions = [ Direction . Up , Direction . Down , Direction . Left , Direction . Right , ]; ` Try
 in generated code will become

 ts ` "use strict" ; let directions = [ 0 /* Direction.Up */ , 1 /* Direction.Down */ , 2 /* Direction.Left */ , 3 /* Direction.Right */ , ]; ` Try

#### Const enum pitfalls

 Inlining enum values is straightforward at first, but comes with subtle implications.
These pitfalls pertain to ambient const enums only (basically const enums in `.d.ts` files) and sharing them between projects, but if you are publishing or consuming `.d.ts` files, these pitfalls likely apply to you, because `tsc --declaration` transforms `.ts` files into `.d.ts` files.

- For the reasons laid out in the `isolatedModules` documentation , that mode is fundamentally incompatible with ambient const enums.
This means if you publish ambient const enums, downstream consumers will not be able to use `isolatedModules` and those enum values at the same time.

- You can easily inline values from version A of a dependency at compile time, and import version B at runtime.
Version A and B’s enums can have different values, if you are not very careful, resulting in surprising bugs , like taking the wrong branches of `if` statements.
These bugs are especially pernicious because it is common to run automated tests at roughly the same time as projects are built, with the same dependency versions, which misses these bugs completely.

- `importsNotUsedAsValues: "preserve"` will not elide imports for const enums used as values, but ambient const enums do not guarantee that runtime `.js` files exist.
The unresolvable imports cause errors at runtime.
The usual way to unambiguously elide imports, type-only imports , does not allow const enum values , currently.

Here are two approaches to avoiding these pitfalls:

-
Do not use const enums at all.
You can easily ban const enums with the help of a linter.
Obviously this avoids any issues with const enums, but prevents your project from inlining its own enums.
Unlike inlining enums from other projects, inlining a project’s own enums is not problematic and has performance implications.

-
Do not publish ambient const enums, by deconstifying them with the help of `preserveConstEnums` .
This is the approach taken internally by the TypeScript project itself .
 `preserveConstEnums` emits the same JavaScript for const enums as plain enums.
You can then safely strip the `const` modifier from `.d.ts` files in a build step .

This way downstream consumers will not inline enums from your project, avoiding the pitfalls above, but a project can still inline its own enums, unlike banning const enums entirely.

## Ambient enums

 Ambient enums are used to describe the shape of already existing enum types.

 ts ` declare enum Enum { A = 1 , B , C = 2 , } ` Try
 One important difference between ambient and non-ambient enums is that, in regular enums, members that don’t have an initializer will be considered constant if its preceding enum member is considered constant.
By contrast, an ambient (and non-const) enum member that does not have an initializer is always considered computed.

## Objects vs Enums

 In modern TypeScript, you may not need an enum when an object with `as const` could suffice:

 ts ` const enum EDirection { Up , Down , Left , Right , } const ODirection = { Up : 0 , Down : 1 , Left : 2 , Right : 3 , } as const ; EDirection . Up ; (enum member) EDirection.Up = 0 ODirection . Up ; (property) Up: 0 // Using the enum as a parameter function walk ( dir : EDirection ) {} // It requires an extra line to pull out the values type Direction = typeof ODirection [ keyof typeof ODirection ]; function run ( dir : Direction ) {} walk ( EDirection . Left ); run ( ODirection . Right ); ` Try
 The biggest argument in favour of this format over TypeScript’s `enum` is that it keeps your codebase aligned with the state of JavaScript, and when/if enums are added to JavaScript then you can move to the additional syntax.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: OT AG FDG-S G TA 11+ Last updated: Jun 15, 2026

## Iterators And Generators

Was this page helpful?

# Iterators and Generators

## Iterables

 An object is deemed iterable if it has an implementation for the `Symbol.iterator` property.
Some built-in types like `Array`, `Map`, `Set`, `String`, `Int32Array`, `Uint32Array`, etc. have their `Symbol.iterator` property already implemented.
`Symbol.iterator` function on an object is responsible for returning the list of values to iterate on.

### `Iterable` interface

 `Iterable` is a type we can use if we want to take in types listed above which are iterable. Here is an example:

 ts ` function toArray < X >( xs : Iterable < X >): X [] { return [... xs ] } `

### `for..of` statements

 `for..of` loops over an iterable object, invoking the `Symbol.iterator` property on the object.
Here is a simple `for..of` loop on an array:

 ts ` let someArray = [ 1 , "string" , false ]; for ( let entry of someArray ) { console . log ( entry ); // 1, "string", false } `

### `for..of` vs. `for..in` statements

 Both `for..of` and `for..in` statements iterate over lists; the values iterated on are different though, `for..in` returns a list of keys on the object being iterated, whereas `for..of` returns a list of values of the numeric properties of the object being iterated.

Here is an example that demonstrates this distinction:

 ts ` let list = [ 4 , 5 , 6 ]; for ( let i in list ) { console . log ( i ); // "0", "1", "2", } for ( let i of list ) { console . log ( i ); // 4, 5, 6 } `
 Another distinction is that `for..in` operates on any object; it serves as a way to inspect properties on this object.
`for..of` on the other hand, is mainly interested in values of iterable objects. Built-in objects like `Map` and `Set` implement `Symbol.iterator` property allowing access to stored values.

 ts ` let pets = new Set ([ "Cat" , "Dog" , "Hamster" ]); pets [ "species" ] = "mammals" ; for ( let pet in pets ) { console . log ( pet ); // "species" } for ( let pet of pets ) { console . log ( pet ); // "Cat", "Dog", "Hamster" } `

### Code generation

#### Targeting ES5

 When targeting an ES5-compliant engine, iterators are only allowed on values of `Array` type.
It is an error to use `for..of` loops on non-Array values, even if these non-Array values implement the `Symbol.iterator` property.

The compiler will generate a simple `for` loop for a `for..of` loop, for instance:

 ts ` let numbers = [ 1 , 2 , 3 ]; for ( let num of numbers ) { console . log ( num ); } `
 will be generated as:

 js ` var numbers = [ 1 , 2 , 3 ]; for ( var _i = 0 ; _i < numbers . length ; _i ++) { var num = numbers [ _i ]; console . log ( num ); } `

#### Targeting ECMAScript 2015 and higher

 When targeting an ECMAScript 2015-compliant engine, the compiler will generate `for..of` loops to target the built-in iterator implementation in the engine.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: MH OT GB JB NS 12+ Last updated: Jun 15, 2026

## Jsx

Was this page helpful?

# JSX
 JSX is an embeddable XML-like syntax.
It is meant to be transformed into valid JavaScript, though the semantics of that transformation are implementation-specific.
JSX rose to popularity with the React framework, but has since seen other implementations as well.
TypeScript supports embedding, type checking, and compiling JSX directly to JavaScript.

## Basic usage

 In order to use JSX you must do two things.

- Name your files with a `.tsx` extension

- Enable the `jsx` option

TypeScript ships with several JSX modes: `preserve`, `react` (classic runtime), `react-jsx` (automatic runtime), `react-jsxdev` (automatic development runtime), and `react-native`.
The `preserve` mode will keep the JSX as part of the output to be further consumed by another transform step (e.g. Babel ).
Additionally the output will have a `.jsx` file extension.
The `react` mode will emit `React.createElement`, does not need to go through a JSX transformation before use, and the output will have a `.js` file extension.
The `react-native` mode is the equivalent of `preserve` in that it keeps all JSX, but the output will instead have a `.js` file extension.

| **

 Mode**
| **Input**
| **Output**
| **Output File Extension**
|

| `preserve`
| `&#x3C;div />`
| `&#x3C;div />`
| `.jsx`
|

| `react`
| `&#x3C;div />`
| `React.createElement("div")`
| `.js`
|

| `react-native`
| `&#x3C;div />`
| `&#x3C;div />`
| `.js`
|

| `react-jsx`
| `&#x3C;div />`
| `_jsx("div", {}, void 0);`
| `.js`
|

| `react-jsxdev`
| `&#x3C;div />`
| `_jsxDEV("div", {}, void 0, false, {...}, this);`
| `.js`
|

You can specify this mode using either the `jsx` command line flag or the corresponding option `jsx` in your tsconfig.json file.

*Note: You can specify the JSX factory function to use when targeting react JSX emit with `jsxFactory` option (defaults to `React.createElement`)

## The `as` operator

 Recall how to write a type assertion:

 ts ` const foo = < Foo > bar ; `
 This asserts the variable `bar` to have the type `Foo`.
Since TypeScript also uses angle brackets for type assertions, combining it with JSX’s syntax would introduce certain parsing difficulties. As a result, TypeScript disallows angle bracket type assertions in `.tsx` files.

Since the above syntax cannot be used in `.tsx` files, an alternate type assertion operator should be used: `as`.
The example can easily be rewritten with the `as` operator.

 ts ` const foo = bar as Foo ; `
 The `as` operator is available in both `.ts` and `.tsx` files, and is identical in behavior to the angle-bracket type assertion style.

## Type Checking

 In order to understand type checking with JSX, you must first understand the difference between intrinsic elements and value-based elements.
Given a JSX expression `&#x3C;expr />`, `expr` may either refer to something intrinsic to the environment (e.g. a `div` or `span` in a DOM environment) or to a custom component that you’ve created.
This is important for two reasons:

- For React, intrinsic elements are emitted as strings (`React.createElement("div")`), whereas a component you’ve created is not (`React.createElement(MyComponent)`).

- The types of the attributes being passed in the JSX element should be looked up differently.
Intrinsic element attributes should be known intrinsically whereas components will likely want to specify their own set of attributes.

TypeScript uses the same convention that React does for distinguishing between these.
An intrinsic element always begins with a lowercase letter, and a value-based element always begins with an uppercase letter.

### The `JSX` namespace

 JSX in TypeScript is typed by the `JSX` namespace. The `JSX` namespace may be defined in various places, depending on the `jsx` compiler option.

The `jsx` options `preserve`, `react`, and `react-native` use the type definitions for classic runtime. This means a variable needs to be in scope that’s determined by the `jsxFactory` compiler option. The `JSX` namespace should be specified on the top-most identifier of the JSX factory. For example, React uses the default factory `React.createElement`. This means its `JSX` namespace should be defined as `React.JSX`.

 ts ` export function createElement (): any ; export namespace JSX { // … } `
 And the user should always import React as `React`.

 ts ` import * as React from 'react' ; `
 Preact uses the JSX factory `h`. That means its types should be defined as the `h.JSX`.

 ts ` export function h ( props : any ): any ; export namespace h . JSX { // … } `
 The user should use a named import to import `h`.

 ts ` import { h } from 'preact' ; `
 For the `jsx` options `react-jsx` and `react-jsxdev`, the `JSX` namespace should be exported from the matching entry points. For `react-jsx` this is `${jsxImportSource}/jsx-runtime`. For `react-jsxdev`, this is `${jsxImportSource}/jsx-dev-runtime`. Since these don’t use a file extension, you must use the `exports` field in `package.json` map in order to support ESM users.

 json ` { "exports" : { "./jsx-runtime" : "./jsx-runtime.js" , "./jsx-dev-runtime" : "./jsx-dev-runtime.js" , } } `
 Then in `jsx-runtime.d.ts` and `jsx-dev-runtime.d.ts`:

 ts ` export namespace JSX { // … } `
 Note that while exporting the `JSX` namespace is sufficient for type checking, the production runtime needs the `jsx`, `jsxs`, and `Fragment` exports at runtime, and the development runtime needs `jsxDEV` and `Fragment`. Ideally you add types for those too.

If the `JSX` namespace isn’t available in the appropriate location, both the classic and the automatic runtime fall back to the global `JSX` namespace.

### Intrinsic elements

 Intrinsic elements are looked up on the special interface `JSX.IntrinsicElements`.
By default, if this interface is not specified, then anything goes and intrinsic elements will not be type checked.
However, if this interface is present, then the name of the intrinsic element is looked up as a property on the `JSX.IntrinsicElements` interface.
For example:

 tsx ` declare namespace JSX { interface IntrinsicElements { foo : any ; } } <foo /> ; // ok <bar /> ; // error `
 In the above example, `&#x3C;foo />` will work fine but `&#x3C;bar />` will result in an error since it has not been specified on `JSX.IntrinsicElements`.

Note: You can also specify a catch-all string indexer on `JSX.IntrinsicElements` as follows:

 ts ` declare namespace JSX { interface IntrinsicElements { [ elemName : string ]: any ; } } `

### Value-based elements

 Value-based elements are simply looked up by identifiers that are in scope.

 tsx ` import MyComponent from "./myComponent" ; < MyComponent /> ; // ok < SomeOtherComponent /> ; // error `
 There are two ways to define a value-based element:

- Function Component (FC)

- Class Component

Because these two types of value-based elements are indistinguishable from each other in a JSX expression, first TS tries to resolve the expression as a Function Component using overload resolution. If the process succeeds, then TS finishes resolving the expression to its declaration. If the value fails to resolve as a Function Component, TS will then try to resolve it as a class component. If that fails, TS will report an error.

#### Function Component

 As the name suggests, the component is defined as a JavaScript function where its first argument is a `props` object.
TS enforces that its return type must be assignable to `JSX.Element`.

 tsx ` interface FooProp { name : string ; X : number ; Y : number ; } declare function AnotherComponent ( prop : { name : string }); function ComponentFoo ( prop : FooProp ) { return < AnotherComponent name = { prop . name } /> ; } const Button = ( prop : { value : string }, context : { color : string }) => ( <button /> ); `
 Because a Function Component is simply a JavaScript function, function overloads may be used here as well:

 ts ` interface ClickableProps { children : JSX . Element [] | JSX . Element ; } interface HomeProps extends ClickableProps { home : JSX . Element ; } interface SideProps extends ClickableProps { side : JSX . Element | string ; } function MainButton ( prop : HomeProps ): JSX . Element ; function MainButton ( prop : SideProps ): JSX . Element ; function MainButton ( prop : ClickableProps ): JSX . Element { // ... } ` Try

 Note: Function Components were formerly known as Stateless Function Components (SFC). As Function Components can no longer be considered stateless in recent versions of react, the type `SFC` and its alias `StatelessComponent` were deprecated.

#### Class Component

 It is possible to define the type of a class component.
However, to do so it is best to understand two new terms: the element class type and the element instance type .

Given `&#x3C;Expr />`, the element class type is the type of `Expr`.
So in the example above, if `MyComponent` was an ES6 class the class type would be that class’s constructor and statics.
If `MyComponent` was a factory function, the class type would be that function.

Once the class type is established, the instance type is determined by the union of the return types of the class type’s construct or call signatures (whichever is present).
So again, in the case of an ES6 class, the instance type would be the type of an instance of that class, and in the case of a factory function, it would be the type of the value returned from the function.

 ts ` class MyComponent { render () {} } // use a construct signature const myComponent = new MyComponent (); // element class type => MyComponent // element instance type => { render: () => void } function MyFactoryFunction () { return { render : () => {}, }; } // use a call signature const myComponent = MyFactoryFunction (); // element class type => MyFactoryFunction // element instance type => { render: () => void } `
 The element instance type is interesting because it must be assignable to `JSX.ElementClass` or it will result in an error.
By default `JSX.ElementClass` is `{}`, but it can be augmented to limit the use of JSX to only those types that conform to the proper interface.

 tsx ` declare namespace JSX { interface ElementClass { render : any ; } } class MyComponent { render () {} } function MyFactoryFunction () { return { render : () => {} }; } < MyComponent /> ; // ok < MyFactoryFunction /> ; // ok class NotAValidComponent {} function NotAValidFactoryFunction () { return {}; } < NotAValidComponent /> ; // error < NotAValidFactoryFunction /> ; // error `

### Attribute type checking

 The first step to type checking attributes is to determine the element attributes type .
This is slightly different between intrinsic and value-based elements.

For intrinsic elements, it is the type of the property on `JSX.IntrinsicElements`

 tsx ` declare namespace JSX { interface IntrinsicElements { foo : { bar ?: boolean }; } } // element attributes type for 'foo' is '{bar?: boolean}' <foo bar /> ; `
 For value-based elements, it is a bit more complex.
It is determined by the type of a property on the element instance type that was previously determined.
Which property to use is determined by `JSX.ElementAttributesProperty`.
It should be declared with a single property.
The name of that property is then used.
As of TypeScript 2.8, if `JSX.ElementAttributesProperty` is not provided, the type of first parameter of the class element’s constructor or Function Component’s call will be used instead.

 tsx ` declare namespace JSX { interface ElementAttributesProperty { props ; // specify the property name to use } } class MyComponent { // specify the property on the element instance type props : { foo ?: string ; }; } // element attributes type for 'MyComponent' is '{foo?: string}' < MyComponent foo = "bar" /> ; `
 The element attribute type is used to type check the attributes in the JSX.
Optional and required properties are supported.

 tsx ` declare namespace JSX { interface IntrinsicElements { foo : { requiredProp : string ; optionalProp ?: number }; } } <foo requiredProp = "bar" /> ; // ok <foo requiredProp = "bar" optionalProp = { 0 } /> ; // ok <foo /> ; // error, requiredProp is missing <foo requiredProp = { 0 } /> ; // error, requiredProp should be a string <foo requiredProp = "bar" unknownProp /> ; // error, unknownProp does not exist <foo requiredProp = "bar" some-unknown-prop /> ; // ok, because 'some-unknown-prop' is not a valid identifier `

 Note: If an attribute name is not a valid JS identifier (like a `data-*` attribute), it is not considered to be an error if it is not found in the element attributes type.

Additionally, the `JSX.IntrinsicAttributes` interface can be used to specify extra properties used by the JSX framework which are not generally used by the components’ props or arguments - for instance `key` in React. Specializing further, the generic `JSX.IntrinsicClassAttributes&#x3C;T>` type may also be used to specify the same kind of extra attributes just for class components (and not Function Components). In this type, the generic parameter corresponds to the class instance type. In React, this is used to allow the `ref` attribute of type `Ref&#x3C;T>`. Generally speaking, all of the properties on these interfaces should be optional, unless you intend that users of your JSX framework need to provide some attribute on every tag.

The spread operator also works:

 tsx ` const props = { requiredProp: "bar" }; <foo { ... props } /> ; // ok const badProps = {}; <foo { ... badProps } /> ; // error `

### Children Type Checking

 In TypeScript 2.3, TS introduced type checking of children . children is a special property in an element attributes type where child JSXExpression s are taken to be inserted into the attributes.
Similar to how TS uses `JSX.ElementAttributesProperty` to determine the name of props , TS uses `JSX.ElementChildrenAttribute` to determine the name of children within those props.
`JSX.ElementChildrenAttribute` should be declared with a single property.

 ts ` declare namespace JSX { interface ElementChildrenAttribute { children : {}; // specify children name to use } } `

```
 tsx ` <div> <h1> Hello </h1> </div> ; <div> <h1> Hello </h1> World </div> ; const CustomComp = ( props ) => <div> { props . children } </div> < CustomComp > <div> Hello World </div> { "This is just a JS expression..." + 1000 } </ CustomComp > `
```

 You can specify the type of children like any other attribute. This will override the default type from, e.g. the React typings if you use them.

 tsx ` interface PropsType { children : JSX . Element name : string } class Component extends React . Component < PropsType , {}> { render () { return ( <h2> {this . props . children } </h2> ) } } // OK < Component name = "foo" > <h1> Hello World </h1> </ Component > // Error: children is of type JSX.Element not array of JSX.Element < Component name = "bar" > <h1> Hello World </h1> <h2> Hello World </h2> </ Component > // Error: children is of type JSX.Element not array of JSX.Element or string. < Component name = "baz" > <h1> Hello </h1> World </ Component > `

## The JSX result type

 By default the result of a JSX expression is typed as `any`.
You can customize the type by specifying the `JSX.Element` interface.
However, it is not possible to retrieve type information about the element, attributes or children of the JSX from this interface.
It is a black box.

## The JSX function return type

 By default, function components must return `JSX.Element | null`. However, this doesn’t always represent runtime behaviour. As of TypeScript 5.1, you can specify `JSX.ElementType` to override what is a valid JSX component type. Note that this doesn’t define what props are valid. The type of props is always defined by the first argument of the component that’s passed. The default looks something like this:

 ts ` namespace JSX { export type ElementType = // All the valid lowercase tags | keyof IntrinsicElements // Function components | ( props : any ) => Element // Class components | new ( props : any ) => ElementClass ; export interface IntrinsicAttributes extends /*...*/ {} export type Element = /*...*/ ; export type ElementClass = /*...*/ ; } `

## Embedding Expressions

 JSX allows you to embed expressions between tags by surrounding the expressions with curly braces (`{ }`).

 tsx ` const a = ( <div> { [ "foo" , "bar" ]. map (( i ) => ( <span> { i / 2 } </span> )) } </div> ); `
 The above code will result in an error since you cannot divide a string by a number.
The output, when using the `preserve` option, looks like:

 tsx ` const a = ( <div> { [ "foo" , "bar" ]. map ( function ( i ) { return <span> { i / 2 } </span> ; }) } </div> ); `

## React integration

 To use JSX with React you should use the React typings .
These typings define the `JSX` namespace appropriately for use with React.

 tsx ` /// <reference path = "react.d.ts" /> interface Props { foo : string ; } class MyComponent extends React . Component < Props , {}> { render () { return <span> {this . props . foo } </span> ; } } < MyComponent foo = "bar" /> ; // ok < MyComponent foo = { 0 } /> ; // error `

### Configuring JSX

 There are multiple compiler flags which can be used to customize your JSX, which work as both a compiler flag and via inline per-file pragmas. To learn more see their tsconfig reference pages:

- `jsxFactory`

- `jsxFragmentFactory`

- `jsxImportSource`

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: MH OT RC DZ KT 35+ Last updated: Jun 15, 2026

## Mixins

Was this page helpful?

# Mixins
 Along with traditional OO hierarchies, another popular way of building up classes from reusable components is to build them by combining simpler partial classes.
You may be familiar with the idea of mixins or traits for languages like Scala, and the pattern has also reached some popularity in the JavaScript community.

## How Does A Mixin Work?

 The pattern relies on using generics with class inheritance to extend a base class.
TypeScript’s best mixin support is done via the class expression pattern.
You can read more about how this pattern works in JavaScript here .

To get started, we’ll need a class which will have the mixins applied on top of:

 ts ` class Sprite { name = "" ; x = 0 ; y = 0 ; constructor ( name : string ) { this . name = name ; } } ` Try
 Then you need a type and a factory function which returns a class expression extending the base class.

 ts ` // To get started, we need a type which we&apos;ll use to extend // other classes from. The main responsibility is to declare // that the type being passed in is a class. type {}' >Constructor = new (... args : any []) => {}; // This mixin adds a scale property, with getters and setters // for changing it with an encapsulated private property: function (Base: TBase): {
 new (...args: any[]): Scaling;
 prototype: Scale<any>.Scaling;
} & TBase' >Scale < (Base: TBase): {
 new (...args: any[]): Scaling;
 prototype: Scale<any>.Scaling;
} & TBase' >TBase extends {}' >Constructor >( Base : (Base: TBase): {
 new (...args: any[]): Scaling;
 prototype: Scale<any>.Scaling;
} & TBase' >TBase ) { return class Scaling extends Base { // Mixins may not declare private/protected properties // however, you can use ES2020 private fields _scale = 1 ; setScale ( scale : number ) { this . _scale = scale ; } get scale (): number { return this . _scale ; } }; } ` Try
 With these all set up, then you can create a class which represents the base class with mixins applied:

 ts ` // Compose a new class from the Sprite class, // with the Mixin Scale applier: const .Scaling;
 prototype: Scale<any>.Scaling;
} & typeof Sprite' >EightBitSprite = (Base: typeof Sprite): {
 new (...args: any[]): Scale<typeof Sprite>.Scaling;
 prototype: Scale<any>.Scaling;
} & typeof Sprite' >Scale ( Sprite ); const .Scaling & Sprite' >flappySprite = new Scale<typeof Sprite>.Scaling & Sprite' >EightBitSprite ( "Bird" ); .Scaling & Sprite' >flappySprite . .setScale(scale: number): void' >setScale ( 0.8 ); console . log ( .Scaling & Sprite' >flappySprite . .scale: number' >scale ); ` Try

## Constrained Mixins

 In the above form, the mixin’s have no underlying knowledge of the class which can make it hard to create the design you want.

To model this, we modify the original constructor type to accept a generic argument.

 ts ` // This was our previous constructor: type {}' >Constructor = new (... args : any []) => {}; // Now we use a generic version which can apply a constraint on // the class which this mixin is applied to type = new (...args: any[]) => T' >GConstructor < ' >T = {}> = new (... args : any []) => ' >T ; ` Try
 This allows for creating classes which only work with constrained base classes:

 ts ` type {
 setPos: (x: number, y: number) => void;
}' >Positionable = = new (...args: any[]) => T' >GConstructor <{ void' >setPos : ( x : number , y : number ) => void }>; type Sprite' >Spritable = = new (...args: any[]) => T' >GConstructor < Sprite >; type {
 print: () => void;
}' >Loggable = = new (...args: any[]) => T' >GConstructor <{ void' >print : () => void }>; ` Try
 Then you can create mixins which only work when you have a particular base to build on:

 ts ` function (Base: TBase): {
 new (...args: any[]): Jumpable;
 prototype: Jumpable<any>.Jumpable;
} & TBase' >Jumpable < (Base: TBase): {
 new (...args: any[]): Jumpable;
 prototype: Jumpable<any>.Jumpable;
} & TBase' >TBase extends {
 setPos: (x: number, y: number) => void;
}' >Positionable >( Base : (Base: TBase): {
 new (...args: any[]): Jumpable;
 prototype: Jumpable<any>.Jumpable;
} & TBase' >TBase ) { return class Jumpable extends Base { jump () { // This mixin will only work if it is passed a base // class which has setPos defined because of the // Positionable constraint. this . void' >setPos ( 0 , 20 ); } }; } ` Try

## Alternative Pattern

 Previous versions of this document recommended a way to write mixins where you created both the runtime and type hierarchies separately, then merged them at the end:

 ts ` // Each mixin is a traditional ES class class Jumpable { jump () {} } class Duckable { duck () {} } // Including the base class Sprite { x = 0 ; y = 0 ; } // Then you create an interface which merges // the expected mixins with the same name as your base interface Sprite extends Jumpable , Duckable {} // Apply the mixins into the base class via // the JS at runtime applyMixins ( Sprite , [ Jumpable , Duckable ]); let player = new Sprite (); player . jump (); console . log ( player . x , player . y ); // This can live anywhere in your codebase: function applyMixins ( derivedCtor : any , constructors : any []) { constructors . .forEach(callbackfn: (value: any, index: number, array: any[]) => void, thisArg?: any): void' >forEach (( baseCtor ) => { Object . getOwnPropertyNames ( baseCtor . prototype ). .forEach(callbackfn: (value: string, index: number, array: string[]) => void, thisArg?: any): void' >forEach (( name ) => { Object . (o: any, p: PropertyKey, attributes: PropertyDescriptor & ThisType<any>): any' >defineProperty ( derivedCtor . prototype , name , Object . getOwnPropertyDescriptor ( baseCtor . prototype , name ) || Object . create ( null ) ); }); }); } ` Try
 This pattern relies less on the compiler, and more on your codebase to ensure both runtime and type-system are correctly kept in sync.

## Constraints

 The mixin pattern is supported natively inside the TypeScript compiler by code flow analysis.
There are a few cases where you can hit the edges of the native support.

#### Decorators and Mixins `#4881`

 You cannot use decorators to provide mixins via code flow analysis:

 ts ` // A decorator function which replicates the mixin pattern: const typeof Pausable' >Pausable = ( target : typeof Player ) => { return class Pausable extends target { shouldFreeze = false ; }; }; @ typeof Pausable' >Pausable class Player { x = 0 ; y = 0 ; } // The Player class does not have the decorator&apos;s type merged: const player = new Player (); player . shouldFreeze ; Property 'shouldFreeze' does not exist on type 'Player'. 2339 Property 'shouldFreeze' does not exist on type 'Player'. // The runtime aspect could be manually replicated via // type composition or interface merging. type FreezablePlayer = Player & { shouldFreeze : boolean }; const playerTwo = ( new Player () as unknown ) as FreezablePlayer ; playerTwo . shouldFreeze ; ` Try

#### Static Property Mixins `#17829`

 More of a gotcha than a constraint.
The class expression pattern creates singletons, so they can’t be mapped at the type system to support different variable types.

You can work around this by using functions to return your classes which differ based on a generic:

 ts ` function (): typeof Base' >base < (): typeof Base' >T >() { class Base { static prop : (): typeof Base' >T ; } return Base ; } function (): typeof Derived' >derived < (): typeof Derived' >T >() { class Derived extends (): typeof Base' >base < (): typeof Derived' >T >() { static anotherProp : (): typeof Derived' >T ; } return Derived ; } class Spec extends (): typeof Derived' >derived < string >() {} Spec . .prop: string' >prop ; // string Spec . .anotherProp: string' >anotherProp ; // string ` Try The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: OT GM IO DE O 5+ Last updated: Jun 15, 2026

## Namespaces

Was this page helpful?

# Namespaces

 A note about terminology:
It’s important to note that in TypeScript 1.5, the nomenclature has changed.
“Internal modules” are now “namespaces”.
“External modules” are now simply “modules”, as to align with ECMAScript 2015 ’s terminology, (namely that `module X {` is equivalent to the now-preferred `namespace X {`).

This post outlines the various ways to organize your code using namespaces (previously “internal modules”) in TypeScript.
As we alluded in our note about terminology, “internal modules” are now referred to as “namespaces”.
Additionally, anywhere the `module` keyword was used when declaring an internal module, the `namespace` keyword can and should be used instead.
This avoids confusing new users by overloading them with similarly named terms.

## First steps

 Let’s start with the program we’ll be using as our example throughout this page.
We’ve written a small set of simplistic string validators, as you might write to check a user’s input on a form in a webpage or check the format of an externally-provided data file.

## Validators in a single file

```
 ts ` interface StringValidator { isAcceptable ( s : string ): boolean ; } let lettersRegexp = / ^ [ A-Za-z ] + $ / ; let numberRegexp = / ^ [ 0-9 ] + $ / ; class LettersOnlyValidator implements StringValidator { isAcceptable ( s : string ) { return lettersRegexp . test ( s ); } } class ZipCodeValidator implements StringValidator { isAcceptable ( s : string ) { return s . length === 5 && numberRegexp . test ( s ); } } // Some samples to try let strings = [ "Hello" , "98052" , "101" ]; // Validators to use let validators : { [ s : string ]: StringValidator } = {}; validators [ "ZIP code" ] = new ZipCodeValidator (); validators [ "Letters only" ] = new LettersOnlyValidator (); // Show whether each string passed each validator for ( let s of strings ) { for ( let name in validators ) { let isMatch = validators [ name ]. isAcceptable ( s ); console . log ( `' ${ s } ' ${ isMatch ? "matches" : "does not match" } ' ${ name } '.` ); } } `
```

## Namespacing

 As we add more validators, we’re going to want to have some kind of organization scheme so that we can keep track of our types and not worry about name collisions with other objects.
Instead of putting lots of different names into the global namespace, let’s wrap up our objects into a namespace.

In this example, we’ll move all validator-related entities into a namespace called `Validation`.
Because we want the interfaces and classes here to be visible outside the namespace, we preface them with `export`.
Conversely, the variables `lettersRegexp` and `numberRegexp` are implementation details, so they are left unexported and will not be visible to code outside the namespace.
In the test code at the bottom of the file, we now need to qualify the names of the types when used outside the namespace, e.g. `Validation.LettersOnlyValidator`.

## Namespaced Validators

```
 ts ` namespace Validation { export interface StringValidator { isAcceptable ( s : string ): boolean ; } const lettersRegexp = / ^ [ A-Za-z ] + $ / ; const numberRegexp = / ^ [ 0-9 ] + $ / ; export class LettersOnlyValidator implements StringValidator { isAcceptable ( s : string ) { return lettersRegexp . test ( s ); } } export class ZipCodeValidator implements StringValidator { isAcceptable ( s : string ) { return s . length === 5 && numberRegexp . test ( s ); } } } // Some samples to try let strings = [ "Hello" , "98052" , "101" ]; // Validators to use let validators : { [ s : string ]: Validation . StringValidator } = {}; validators [ "ZIP code" ] = new Validation . ZipCodeValidator (); validators [ "Letters only" ] = new Validation . LettersOnlyValidator (); // Show whether each string passed each validator for ( let s of strings ) { for ( let name in validators ) { console . log ( `" ${ s } " - ${ validators [ name ]. isAcceptable ( s ) ? "matches" : "does not match" } ${ name } ` ); } } `
```

## Splitting Across Files

 As our application grows, we’ll want to split the code across multiple files to make it easier to maintain.

## Multi-file namespaces

 Here, we’ll split our `Validation` namespace across many files.
Even though the files are separate, they can each contribute to the same namespace and can be consumed as if they were all defined in one place.
Because there are dependencies between files, we’ll add reference tags to tell the compiler about the relationships between the files.
Our test code is otherwise unchanged.

 Validation.ts

```
 ts ` namespace Validation { export interface StringValidator { isAcceptable ( s : string ): boolean ; } } `
```

 LettersOnlyValidator.ts

```
 ts ` /// <reference path = "Validation.ts" /> namespace Validation { const lettersRegexp = / ^ [ A-Za-z ] + $ / ; export class LettersOnlyValidator implements StringValidator { isAcceptable ( s : string ) { return lettersRegexp . test ( s ); } } } `
```

 ZipCodeValidator.ts

```
 ts ` /// <reference path = "Validation.ts" /> namespace Validation { const numberRegexp = / ^ [ 0-9 ] + $ / ; export class ZipCodeValidator implements StringValidator { isAcceptable ( s : string ) { return s . length === 5 && numberRegexp . test ( s ); } } } `
```

 Test.ts

```
 ts ` /// <reference path = "Validation.ts" /> /// <reference path = "LettersOnlyValidator.ts" /> /// <reference path = "ZipCodeValidator.ts" /> // Some samples to try let strings = [ "Hello" , "98052" , "101" ]; // Validators to use let validators : { [ s : string ]: Validation . StringValidator } = {}; validators [ "ZIP code" ] = new Validation . ZipCodeValidator (); validators [ "Letters only" ] = new Validation . LettersOnlyValidator (); // Show whether each string passed each validator for ( let s of strings ) { for ( let name in validators ) { console . log ( `" ${ s } " - ${ validators [ name ]. isAcceptable ( s ) ? "matches" : "does not match" } ${ name } ` ); } } `
```

 Once there are multiple files involved, we’ll need to make sure all of the compiled code gets loaded.
There are two ways of doing this.

First, we can use concatenated output using the `outFile` option to compile all of the input files into a single JavaScript output file:

 `tsc --outFile sample.js Test.ts`
 The compiler will automatically order the output file based on the reference tags present in the files. You can also specify each file individually:

 `tsc --outFile sample.js Validation.ts LettersOnlyValidator.ts ZipCodeValidator.ts Test.ts`
 Alternatively, we can use per-file compilation (the default) to emit one JavaScript file for each input file.
If multiple JS files get produced, we’ll need to use `&#x3C;script>` tags on our webpage to load each emitted file in the appropriate order, for example:

 MyTestPage.html (excerpt)

```
 html ` <script src = "Validation.js" type = "text/javascript" / > <script src = "LettersOnlyValidator.js" type = "text/javascript" /> <script src = "ZipCodeValidator.js" type = "text/javascript" /> <script src = "Test.js" type = "text/javascript" /> `
```

## Aliases

 Another way that you can simplify working with namespaces is to use `import q = x.y.z` to create shorter names for commonly-used objects.
Not to be confused with the `import x = require("name")` syntax used to load modules, this syntax simply creates an alias for the specified symbol.
You can use these sorts of imports (commonly referred to as aliases) for any kind of identifier, including objects created from module imports.

 ts ` namespace Shapes { export namespace Polygons { export class Triangle {} export class Square {} } } import polygons = Shapes . Polygons ; let sq = new polygons . Square (); // Same as 'new Shapes.Polygons.Square()' `
 Notice that we don’t use the `require` keyword; instead we assign directly from the qualified name of the symbol we’re importing.
This is similar to using `var`, but also works on the type and namespace meanings of the imported symbol.
Importantly, for values, `import` is a distinct reference from the original symbol, so changes to an aliased `var` will not be reflected in the original variable.

## Working with Other JavaScript Libraries

 To describe the shape of libraries not written in TypeScript, we need to declare the API that the library exposes.
Because most JavaScript libraries expose only a few top-level objects, namespaces are a good way to represent them.

We call declarations that don’t define an implementation “ambient”.
Typically these are defined in `.d.ts` files.
If you’re familiar with C/C++, you can think of these as `.h` files.
Let’s look at a few examples.

## Ambient Namespaces

 The popular library D3 defines its functionality in a global object called `d3`.
Because this library is loaded through a `&#x3C;script>` tag (instead of a module loader), its declaration uses namespaces to define its shape.
For the TypeScript compiler to see this shape, we use an ambient namespace declaration.
For example, we could begin writing it as follows:

 D3.d.ts (simplified excerpt)

```
 ts ` declare namespace D3 { export interface Selectors { select : { ( selector : string ): Selection ; ( element : EventTarget ): Selection ; }; } export interface Event { x : number ; y : number ; } export interface Base extends Selectors { event : Event ; } } declare var d3 : D3 . Base ; `
```
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: MH OT DR IO JB 14+ Last updated: Jun 15, 2026

## Namespaces And Modules

Was this page helpful?

# Namespaces and Modules
 This post outlines the various ways to organize your code using modules and namespaces in TypeScript.
We’ll also go over some advanced topics of how to use namespaces and modules, and address some common pitfalls when using them in TypeScript.

See the Modules documentation for more information about ES Modules.
See the Namespaces documentation for more information about TypeScript namespaces.

Note: In very old versions of TypeScript namespaces were called ‘Internal Modules’, these pre-date JavaScript module systems.

## Using Modules

 Modules can contain both code and declarations.

Modules also have a dependency on a module loader (such as CommonJs/Require.js) or a runtime which supports ES Modules.
Modules provide for better code reuse, stronger isolation and better tooling support for bundling.

It is also worth noting that, for Node.js applications, modules are the default and we recommended modules over namespaces in modern code .

Starting with ECMAScript 2015, modules are native part of the language, and should be supported by all compliant engine implementations.
Thus, for new projects modules would be the recommended code organization mechanism.

## Using Namespaces

 Namespaces are a TypeScript-specific way to organize code.
Namespaces are simply named JavaScript objects in the global namespace.
This makes namespaces a very simple construct to use.
Unlike modules, they can span multiple files, and can be concatenated using `outFile` .
Namespaces can be a good way to structure your code in a Web Application, with all dependencies included as `&#x3C;script>` tags in your HTML page.

Just like all global namespace pollution, it can be hard to identify component dependencies, especially in a large application.

## Pitfalls of Namespaces and Modules

 In this section we’ll describe various common pitfalls in using namespaces and modules, and how to avoid them.

### `/// &#x3C;reference>`-ing a module

 A common mistake is to try to use the `/// &#x3C;reference ... />` syntax to refer to a module file, rather than using an `import` statement.
To understand the distinction, we first need to understand how the compiler can locate the type information for a module based on the path of an `import` (e.g. the `...` in `import x from "...";`, `import x = require("...");`, etc.) path.

The compiler will try to find a `.ts`, `.tsx`, and then a `.d.ts` with the appropriate path.
If a specific file could not be found, then the compiler will look for an ambient module declaration .
Recall that these need to be declared in a `.d.ts` file.

-
`myModules.d.ts`

 ts ` // In a .d.ts file or .ts file that is not a module: declare module "SomeModule" { export function fn (): string ; } `

-
 `myOtherModule.ts`

 ts ` /// <reference path = "myModules.d.ts" /> import * as m from "SomeModule" ; `

 The reference tag here allows us to locate the declaration file that contains the declaration for the ambient module.
This is how the `node.d.ts` file that several of the TypeScript samples use is consumed.

### Needless Namespacing

 If you’re converting a program from namespaces to modules, it can be easy to end up with a file that looks like this:

-
`shapes.ts`

 ts ` export namespace Shapes { export class Triangle { /* ... */ } export class Square { /* ... */ } } `

 The top-level namespace here `Shapes` wraps up `Triangle` and `Square` for no reason.
This is confusing and annoying for consumers of your module:

-
`shapeConsumer.ts`

 ts ` import * as shapes from "./shapes" ; let t = new shapes . Shapes . Triangle (); // shapes.Shapes? `

 A key feature of modules in TypeScript is that two different modules will never contribute names to the same scope.
Because the consumer of a module decides what name to assign it, there’s no need to proactively wrap up the exported symbols in a namespace.

To reiterate why you shouldn’t try to namespace your module contents, the general idea of namespacing is to provide logical grouping of constructs and to prevent name collisions.
Because the module file itself is already a logical grouping, and its top-level name is defined by the code that imports it, it’s unnecessary to use an additional module layer for exported objects.

Here’s a revised example:

-
`shapes.ts`

 ts ` export class Triangle { /* ... */ } export class Square { /* ... */ } `

-
 `shapeConsumer.ts`

 ts ` import * as shapes from "./shapes" ; let t = new shapes . Triangle (); `

### Trade-offs of Modules

 Just as there is a one-to-one correspondence between JS files and modules, TypeScript has a one-to-one correspondence between module source files and their emitted JS files.
One effect of this is that it’s not possible to concatenate multiple module source files depending on the module system you target.
For instance, you can’t use the `outFile` option while targeting `commonjs` or `umd`, but with TypeScript 1.8 and later, it’s possible to use `outFile` when targeting `amd` or `system`.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: DR OT MH B MF 15+ Last updated: Jun 15, 2026

## Symbols

Was this page helpful?

# Symbols
 Starting with ECMAScript 2015, `symbol` is a primitive data type, just like `number` and `string`.

`symbol` values are created by calling the `Symbol` constructor.

 ts ` let sym1 = Symbol (); let sym2 = Symbol ( "key" ); // optional string key `
 Symbols are immutable, and unique.

 ts ` let sym2 = Symbol ( "key" ); let sym3 = Symbol ( "key" ); sym2 === sym3 ; // false, symbols are unique `
 Just like strings, symbols can be used as keys for object properties.

 ts ` const sym = Symbol (); let obj = { [sym]: "value" , }; console . log ( obj [ sym ]); // "value" `
 Symbols can also be combined with computed property declarations to declare object properties and class members.

 ts ` const getClassNameSymbol = Symbol (); class C { [ getClassNameSymbol ]() { return "C" ; } } let c = new C (); let className = c [ getClassNameSymbol ](); // "C" `

## `unique symbol`

 To enable treating symbols as unique literals a special type `unique symbol` is available. `unique symbol` is a subtype of `symbol`, and are produced only from calling `Symbol()` or `Symbol.for()`, or from explicit type annotations. This type is only allowed on `const` declarations and `readonly static` properties, and in order to reference a specific unique symbol, you’ll have to use the `typeof` operator. Each reference to a unique symbol implies a completely unique identity that’s tied to a given declaration.

 ts ` declare const sym1 : unique symbol ; // sym2 can only be a constant reference. let sym2 : unique symbol = symbol' >Symbol (); A variable whose type is a 'unique symbol' type must be 'const'. 1332 A variable whose type is a 'unique symbol' type must be 'const'. // Works - refers to a unique symbol, but its identity is tied to &apos;sym1&apos;. let sym3 : typeof sym1 = sym1 ; // Also works. class C { static readonly StaticSymbol : unique symbol = symbol' >Symbol (); } ` Try
 Because each `unique symbol` has a completely separate identity, no two `unique symbol` types are assignable or comparable to each other.

 ts ` const sym2 = symbol' >Symbol (); const sym3 = symbol' >Symbol (); if ( sym2 === sym3 ) { This comparison appears to be unintentional because the types 'typeof sym2' and 'typeof sym3' have no overlap. 2367 This comparison appears to be unintentional because the types 'typeof sym2' and 'typeof sym3' have no overlap. // ... } ` Try

## Well-known Symbols

 In addition to user-defined symbols, there are well-known built-in symbols.
Built-in symbols are used to represent internal language behaviors.

Here is a list of well-known symbols:

### `Symbol.asyncIterator`

 A method that returns async iterator for an object, compatible to be used with for await..of loop.

### `Symbol.hasInstance`

 A method that determines if a constructor object recognizes an object as one of the constructor’s instances. Called by the semantics of the instanceof operator.

### `Symbol.isConcatSpreadable`

 A Boolean value indicating that an object should be flattened to its array elements by Array.prototype.concat.

### `Symbol.iterator`

 A method that returns the default iterator for an object. Called by the semantics of the for-of statement.

### `Symbol.match`

 A regular expression method that matches the regular expression against a string. Called by the `String.prototype.match` method.

### `Symbol.replace`

 A regular expression method that replaces matched substrings of a string. Called by the `String.prototype.replace` method.

### `Symbol.search`

 A regular expression method that returns the index within a string that matches the regular expression. Called by the `String.prototype.search` method.

### `Symbol.species`

 A function valued property that is the constructor function that is used to create derived objects.

### `Symbol.split`

 A regular expression method that splits a string at the indices that match the regular expression.
Called by the `String.prototype.split` method.

### `Symbol.toPrimitive`

 A method that converts an object to a corresponding primitive value.
Called by the `ToPrimitive` abstract operation.

### `Symbol.toStringTag`

 A String value that is used in the creation of the default string description of an object.
Called by the built-in method `Object.prototype.toString`.

### `Symbol.unscopables`

 An Object whose own property names are property names that are excluded from the ‘with’ environment bindings of the associated objects.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: MH OT GB MF MN 9+ Last updated: Jun 15, 2026

## Triple Slash Directives

Was this page helpful?

# Triple-Slash Directives
 Triple-slash directives are single-line comments containing a single XML tag.
The contents of the comment are used as compiler directives.

Triple-slash directives are only valid at the top of their containing file.
A triple-slash directive can only be preceded by single or multi-line comments, including other triple-slash directives.
If they are encountered following a statement or a declaration they are treated as regular single-line comments, and hold no special meaning.

As of TypeScript 5.5, the compiler does not generate reference directives, and does not emit handwritten triple-slash directives to output files unless those directives are marked as `preserve="true"` .

## `/// &#x3C;reference path="..." />`

 The `/// &#x3C;reference path="..." />` directive is the most common of this group.
It serves as a declaration of dependency between files.

Triple-slash references instruct the compiler to include additional files in the compilation process.

They also serve as a method to order the output when using `out` or `outFile` .
Files are emitted to the output file location in the same order as the input after preprocessing pass.

### Preprocessing input files

 The compiler performs a preprocessing pass on input files to resolve all triple-slash reference directives.
During this process, additional files are added to the compilation.

The process starts with a set of root files ;
these are the file names specified on the command-line or in the `files` list in the `tsconfig.json` file.
These root files are preprocessed in the same order they are specified.
Before a file is added to the list, all triple-slash references in it are processed, and their targets included.
Triple-slash references are resolved in a depth-first manner, in the order they have been seen in the file.

A triple-slash reference path is resolved relative to the containing file, if a relative path is used.

### Errors

 It is an error to reference a file that does not exist.
It is an error for a file to have a triple-slash reference to itself.

### Using `--noResolve`

 If the compiler flag `noResolve` is specified, triple-slash references are ignored; they neither result in adding new files, nor change the order of the files provided.

## `/// &#x3C;reference types="..." />`

 Similar to a `/// &#x3C;reference path="..." />` directive, which serves as a declaration of dependency , a `/// &#x3C;reference types="..." />` directive declares a dependency on a package.

The process of resolving these package names is similar to the process of resolving module names in an `import` statement.
An easy way to think of triple-slash-reference-types directives are as an `import` for declaration packages.

For example, including `/// &#x3C;reference types="node" />` in a declaration file declares that this file uses names declared in `@types/node/index.d.ts`;
and thus, this package needs to be included in the compilation along with the declaration file.

For declaring a dependency on an `@types` package in a `.ts` file, use `types` on the command line or in your `tsconfig.json` instead.
See using `@types`, `typeRoots` and `types` in `tsconfig.json` files for more details.

## `/// &#x3C;reference lib="..." />`

 This directive allows a file to explicitly include an existing built-in lib file.

Built-in lib files are referenced in the same fashion as the `lib` compiler option in tsconfig.json (e.g. use `lib="es2015"` and not `lib="lib.es2015.d.ts"`, etc.).

For declaration file authors who rely on built-in types, e.g. DOM APIs or built-in JS run-time constructors like `Symbol` or `Iterable`, triple-slash-reference lib directives are recommended. Previously these .d.ts files had to add forward/duplicate declarations of such types.

For example, adding `/// &#x3C;reference lib="es2017.string" />` to one of the files in a compilation is equivalent to compiling with `--lib es2017.string`.

 ts ` /// <reference lib = "es2017.string" /> "foo" . padStart ( 4 ); `

## `/// &#x3C;reference no-default-lib="true"/>`

 This directive marks a file as a default library .
You will see this comment at the top of `lib.d.ts` and its different variants.

This directive instructs the compiler to not include the default library (i.e. `lib.d.ts`) in the compilation.
The impact here is similar to passing `noLib` on the command line.

Also note that when passing `skipDefaultLibCheck` , the compiler will only skip checking files with `/// &#x3C;reference no-default-lib="true"/>`.

## `/// &#x3C;amd-module />`

 By default AMD modules are generated anonymous.
This can lead to problems when other tools are used to process the resulting modules, such as bundlers (e.g. `r.js`).

The `amd-module` directive allows passing an optional module name to the compiler:

 amdModule.ts

```
 ts ` /// <amd-module name = "NamedModule" /> export class C {} `
```

 Will result in assigning the name `NamedModule` to the module as part of calling the AMD `define`:

 amdModule.js

```
 js ` define ( "NamedModule" , [ "require" , "exports" ], function ( require , exports ) { var C = ( function () { function C () {} return C ; })(); exports . C = C ; }); `
```

## `/// &#x3C;amd-dependency />`

 Note : this directive has been deprecated. Use `import "moduleName";` statements instead.

`/// &#x3C;amd-dependency path="x" />` informs the compiler about a non-TS module dependency that needs to be injected in the resulting module’s require call.

The `amd-dependency` directive can also have an optional `name` property; this allows passing an optional name for an amd-dependency:

 ts ` /// <amd-dependency path = "legacy/moduleA" name = "moduleA" /> declare var moduleA : MyType ; moduleA . callStuff (); `
 Generated JS code:

 js ` define ([ "require" , "exports" , "legacy/moduleA" ], function ( require , exports , moduleA ) { moduleA . callStuff (); }); `

## `preserve="true"`

 Triple-slash directives can be marked with `preserve="true"` to prevent the compiler from removing them from the output.

For example, these will be erased in the output:

 ts ` /// <reference path = "..." /> /// <reference types = "..." /> /// <reference lib = "..." /> `
 But these will be preserved:

 ts ` /// <reference path="..." preserve="true" /> /// <reference types="..." preserve="true" /> /// <reference lib="..." preserve="true" /> ` The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: MH OT JB JM JB 10+ Last updated: Jun 15, 2026

## Type Compatibility

Was this page helpful?

# Type Compatibility
 Type compatibility in TypeScript is based on structural subtyping.
Structural typing is a way of relating types based solely on their members.
This is in contrast with nominal typing.
Consider the following code:

 ts ` interface Pet { name : string ; } class Dog { name : string ; } let pet : Pet ; // OK, because of structural typing pet = new Dog (); `
 In nominally-typed languages like C# or Java, the equivalent code would be an error because the `Dog` class does not explicitly describe itself as being an implementer of the `Pet` interface.

TypeScript’s structural type system was designed based on how JavaScript code is typically written.
Because JavaScript widely uses anonymous objects like function expressions and object literals, it’s much more natural to represent the kinds of relationships found in JavaScript libraries with a structural type system instead of a nominal one.

## A Note on Soundness

 TypeScript’s type system allows certain operations that can’t be known at compile-time to be safe. When a type system has this property, it is said to not be “sound”. The places where TypeScript allows unsound behavior were carefully considered, and throughout this document we’ll explain where these happen and the motivating scenarios behind them.

## Starting out

 The basic rule for TypeScript’s structural type system is that `x` is compatible with `y` if `y` has at least the same members as `x`. For example consider the following code involving an interface named `Pet` which has a `name` property:

 ts ` interface Pet { name : string ; } let pet : Pet ; // dog's inferred type is { name: string; owner: string; } let dog = { name: "Lassie" , owner: "Rudd Weatherwax" }; pet = dog ; `
 To check whether `dog` can be assigned to `pet`, the compiler checks each property of `pet` to find a corresponding compatible property in `dog`.
In this case, `dog` must have a member called `name` that is a string. It does, so the assignment is allowed.

The same rule for assignment is used when checking function call arguments:

 ts ` interface Pet { name : string ; } let dog = { name: "Lassie" , owner: "Rudd Weatherwax" }; function greet ( pet : Pet ) { console . log ( "Hello, " + pet . name ); } greet ( dog ); // OK `
 Note that `dog` has an extra `owner` property, but this does not create an error.
Only members of the target type (`Pet` in this case) are considered when
checking for compatibility. This comparison process proceeds recursively,
exploring the type of each member and sub-member.

Be aware, however, that object literals may only specify known properties .
For example, because we have explicitly specified that `dog` is
of type `Pet`, the following code is invalid:

 ts ` let dog : Pet = { name: "Lassie" , owner: "Rudd Weatherwax" }; // Error `

## Comparing two functions

 While comparing primitive types and object types is relatively straightforward, the question of what kinds of functions should be considered compatible is a bit more involved.
Let’s start with a basic example of two functions that differ only in their parameter lists:

 ts ` let x = ( a : number ) => 0 ; let y = ( b : number , s : string ) => 0 ; y = x ; // OK x = y ; // Error `
 To check if `x` is assignable to `y`, we first look at the parameter list.
Each parameter in `x` must have a corresponding parameter in `y` with a compatible type.
Note that the names of the parameters are not considered, only their types.
In this case, every parameter of `x` has a corresponding compatible parameter in `y`, so the assignment is allowed.

The second assignment is an error, because `y` has a required second parameter that `x` does not have, so the assignment is disallowed.

You may be wondering why we allow ‘discarding’ parameters like in the example `y = x`.
The reason for this assignment to be allowed is that ignoring extra function parameters is actually quite common in JavaScript.
For example, `Array#forEach` provides three parameters to the callback function: the array element, its index, and the containing array.
Nevertheless, it’s very useful to provide a callback that only uses the first parameter:

 ts ` let items = [ 1 , 2 , 3 ]; // Don't force these extra parameters items . forEach (( item , index , array ) => console . log ( item )); // Should be OK! items . forEach (( item ) => console . log ( item )); `
 Now let’s look at how return types are treated, using two functions that differ only by their return type:

 ts ` let x = () => ({ name: "Alice" }); let y = () => ({ name: "Alice" , location: "Seattle" }); x = y ; // OK y = x ; // Error, because x() lacks a location property `
 The type system enforces that the source function’s return type be a subtype of the target type’s return type.

### Function Parameter Bivariance

 When comparing the types of function parameters, assignment succeeds if either the source parameter is assignable to the target parameter, or vice versa.
This is unsound because a caller might end up being given a function that takes a more specialized type, but invokes the function with a less specialized type.
In practice, this sort of error is rare, and allowing this enables many common JavaScript patterns. A brief example:

 ts ` enum EventType { Mouse , Keyboard , } interface Event { timestamp : number ; } interface MyMouseEvent extends Event { x : number ; y : number ; } interface MyKeyEvent extends Event { keyCode : number ; } function listenEvent ( eventType : EventType , handler : ( n : Event ) => void ) { /* ... */ } // Unsound, but useful and common listenEvent ( EventType . Mouse , ( e : MyMouseEvent ) => console . log ( e . x + "," + e . y )); // Undesirable alternatives in presence of soundness listenEvent ( EventType . Mouse , ( e : Event ) => console . log (( e as MyMouseEvent ). x + "," + ( e as MyMouseEvent ). y ) ); listenEvent ( EventType . Mouse , (( e : MyMouseEvent ) => console . log ( e . x + "," + e . y )) as ( e : Event ) => void ); // Still disallowed (clear error). Type safety enforced for wholly incompatible types listenEvent ( EventType . Mouse , ( e : number ) => console . log ( e )); `
 You can have TypeScript raise errors when this happens via the compiler flag `strictFunctionTypes` .

### Optional Parameters and Rest Parameters

 When comparing functions for compatibility, optional and required parameters are interchangeable.
Extra optional parameters of the source type are not an error, and optional parameters of the target type without corresponding parameters in the source type are not an error.

When a function has a rest parameter, it is treated as if it were an infinite series of optional parameters.

This is unsound from a type system perspective, but from a runtime point of view the idea of an optional parameter is generally not well-enforced since passing `undefined` in that position is equivalent for most functions.

The motivating example is the common pattern of a function that takes a callback and invokes it with some predictable (to the programmer) but unknown (to the type system) number of arguments:

 ts ` function invokeLater ( args : any [], callback : (... args : any []) => void ) { /* ... Invoke callback with 'args' ... */ } // Unsound - invokeLater "might" provide any number of arguments invokeLater ([ 1 , 2 ], ( x , y ) => console . log ( x + ", " + y )); // Confusing (x and y are actually required) and undiscoverable invokeLater ([ 1 , 2 ], ( x ?, y ?) => console . log ( x + ", " + y )); `

### Functions with overloads

 When a function has overloads, each overload in the target type must be matched by a compatible signature on the source type.
This ensures that the source function can be called in all the same cases as the target function.

## Enums

 Enums are compatible with numbers, and numbers are compatible with enums. Enum values from different enum types are considered incompatible. For example,

 ts ` enum Status { Ready , Waiting , } enum Color { Red , Blue , Green , } let status = Status . Ready ; status = Color . Green ; // Error `

## Classes

 Classes work similarly to object literal types and interfaces with one exception: they have both a static and an instance type.
When comparing two objects of a class type, only members of the instance are compared.
Static members and constructors do not affect compatibility.

 ts ` class Animal { feet : number ; constructor ( name : string , numFeet : number ) {} } class Size { feet : number ; constructor ( numFeet : number ) {} } let a : Animal ; let s : Size ; a = s ; // OK s = a ; // OK `

### Private and protected members in classes

 Private and protected members in a class affect their compatibility.
When an instance of a class is checked for compatibility, if the target type contains a private member, then the source type must also contain a private member that originated from the same class.
Likewise, the same applies for an instance with a protected member.
This allows a class to be assignment compatible with its super class, but not with classes from a different inheritance hierarchy which otherwise have the same shape.

## Generics

 Because TypeScript is a structural type system, type parameters only affect the resulting type when consumed as part of the type of a member. For example,

 ts ` interface Empty < T > {} let x : Empty < number >; let y : Empty < string >; x = y ; // OK, because y matches structure of x `
 In the above, `x` and `y` are compatible because their structures do not use the type argument in a differentiating way.
Changing this example by adding a member to `Empty&#x3C;T>` shows how this works:

 ts ` interface NotEmpty < T > { data : T ; } let x : NotEmpty < number >; let y : NotEmpty < string >; x = y ; // Error, because x and y are not compatible `
 In this way, a generic type that has its type arguments specified acts just like a non-generic type.

For generic types that do not have their type arguments specified, compatibility is checked by specifying `any` in place of all unspecified type arguments.
The resulting types are then checked for compatibility, just as in the non-generic case.

For example,

 ts ` let identity = function < T >( x : T ): T { // ... }; let reverse = function < U >( y : U ): U { // ... }; identity = reverse ; // OK, because (x: any) => any matches (y: any) => any `

## Advanced Topics

### Subtype vs Assignment

 So far, we’ve used “compatible”, which is not a term defined in the language spec.
In TypeScript, there are two kinds of compatibility: subtype and assignment.
These differ only in that assignment extends subtype compatibility with rules to allow assignment to and from `any`, and to and from `enum` with corresponding numeric values.

Different places in the language use one of the two compatibility mechanisms, depending on the situation.
For practical purposes, type compatibility is dictated by assignment compatibility, even in the cases of the `implements` and `extends` clauses.

## `any`, `unknown`, `object`, `void`, `undefined`, `null`, and `never` assignability

 The following table summarizes assignability between some abstract types.
Rows indicate what each is assignable to, columns indicate what is assignable to them.
A ” ✓ ” indicates a combination that is compatible only when `strictNullChecks` is off.

| **

 **
| **any**
| **unknown**
| **object**
| **void**
| **undefined**
| **null**
| **never**
|

| any →
|
| ✓
| ✓
| ✓
| ✓
| ✓
| ✕
|

| unknown →
| ✓
|
| ✕
| ✕
| ✕
| ✕
| ✕
|

| object →
| ✓
| ✓
|
| ✕
| ✕
| ✕
| ✕
|

| void →
| ✓
| ✓
| ✕
|
| ✕
| ✕
| ✕
|

| undefined →
| ✓
| ✓
| ✓
| ✓
|
| ✓
| ✕
|

| null →
| ✓
| ✓
| ✓
| ✓
| ✓
|
| ✕
|

| never →
| ✓
| ✓
| ✓
| ✓
| ✓
| ✓
|
|

Reiterating The Basics :

- Everything is assignable to itself.

- `any` and `unknown` are the same in terms of what is assignable to them, different in that `unknown` is not assignable to anything except `any`.

- `unknown` and `never` are like inverses of each other.
Everything is assignable to `unknown`, `never` is assignable to everything.
Nothing is assignable to `never`, `unknown` is not assignable to anything (except `any`).

- `void` is not assignable to or from anything, with the following exceptions: `any`, `unknown`, `never`, `undefined`, and `null` (if `strictNullChecks` is off, see table for details).

- When `strictNullChecks` is off, `null` and `undefined` are similar to `never`: assignable to most types, most types are not assignable to them.
They are assignable to each other.

- When `strictNullChecks` is on, `null` and `undefined` behave more like `void`: not assignable to or from anything, except for `any`, `unknown`, and `void` (`undefined` is always assignable to `void`).

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: RC DR OT MH JB 26+ Last updated: Jun 15, 2026

## Type Inference

Was this page helpful?

# Type Inference
 In TypeScript, there are several places where type inference is used to provide type information when there is no explicit type annotation. For example, in this code

 ts ` let x = 3 ; let x: number ` Try
 The type of the `x` variable is inferred to be `number`.
This kind of inference takes place when initializing variables and members, setting parameter default values, and determining function return types.

In most cases, type inference is straightforward.
In the following sections, we’ll explore some of the nuances in how types are inferred.

## Best common type

 When a type inference is made from several expressions, the types of those expressions are used to calculate a “best common type”. For example,

 ts ` let x = [ 0 , 1 , null ]; let x: (number | null)[] ` Try
 To infer the type of `x` in the example above, we must consider the type of each array element.
Here we are given two choices for the type of the array: `number` and `null`.
The best common type algorithm considers each candidate type, and picks the type that is compatible with all the other candidates.

Because the best common type has to be chosen from the provided candidate types, there are some cases where types share a common structure, but no one type is the super type of all candidate types. For example:

 ts ` let zoo = [ new Rhino (), new Elephant (), new Snake ()]; let zoo: (Rhino | Elephant | Snake)[] ` Try
 Ideally, we may want `zoo` to be inferred as an `Animal[]`, but because there is no object that is strictly of type `Animal` in the array, we make no inference about the array element type.
To correct this, explicitly provide the type when no one type is a super type of all other candidates:

 ts ` let zoo : Animal [] = [ new Rhino (), new Elephant (), new Snake ()]; let zoo: Animal[] ` Try
 When no best common type is found, the resulting inference is the union array type, `(Rhino | Elephant | Snake)[]`.

## Contextual Typing

 Type inference also works in “the other direction” in some cases in TypeScript.
This is known as “contextual typing”. Contextual typing occurs when the type of an expression is implied by its location. For example:

 ts ` window . any) & ((this: Window, ev: MouseEvent) => any)) | null' >onmousedown = function ( mouseEvent ) { console . log ( mouseEvent . button ); console . log ( mouseEvent . kangaroo ); Property 'kangaroo' does not exist on type 'MouseEvent'. 2339 Property 'kangaroo' does not exist on type 'MouseEvent'. }; ` Try
 Here, the TypeScript type checker used the type of the `Window.onmousedown` function to infer the type of the function expression on the right hand side of the assignment.
When it did so, it was able to infer the type of the `mouseEvent` parameter, which does contain a `button` property, but not a `kangaroo` property.

This works because window already has `onmousedown` declared in its type:

 ts ` // Declares there is a global variable called 'window' declare var window : Window & typeof globalThis ; // Which is declared as (simplified): interface Window extends GlobalEventHandlers { // ... } // Which defines a lot of known handler events interface GlobalEventHandlers { onmousedown : (( this : GlobalEventHandlers , ev : MouseEvent ) => any ) | null ; // ... } `
 TypeScript is smart enough to infer types in other contexts as well:

 ts ` window . any) & ((this: Window, ev: Event) => any)) | null' >onscroll = function ( uiEvent ) { console . log ( uiEvent . button ); Property 'button' does not exist on type 'Event'. 2339 Property 'button' does not exist on type 'Event'. }; ` Try
 Based on the fact that the above function is being assigned to `Window.onscroll`, TypeScript knows that `uiEvent` is a UIEvent , and not a MouseEvent like the previous example. `UIEvent` objects contain no `button` property, and so TypeScript will throw an error.

If this function were not in a contextually typed position, the function’s argument would implicitly have type `any`, and no error would be issued (unless you are using the `noImplicitAny` option):

 ts ` const void' >handler = function ( uiEvent ) { console . log ( uiEvent . button ); // <- OK }; ` Try
 We can also explicitly give type information to the function’s argument to override any contextual type:

 ts ` window . any) & ((this: Window, ev: Event) => any)) | null' >onscroll = function ( uiEvent : any ) { console . log ( uiEvent . button ); // <- Now, no error is given }; ` Try
 However, this code will log `undefined`, since `uiEvent` has no property called `button`.

Contextual typing applies in many cases.
Common cases include arguments to function calls, right hand sides of assignments, type assertions, members of object and array literals, and return statements.
The contextual type also acts as a candidate type in best common type. For example:

 ts ` function createZoo (): Animal [] { return [ new Rhino (), new Elephant (), new Snake ()]; } ` Try
 In this example, best common type has a set of four candidates: `Animal`, `Rhino`, `Elephant`, and `Snake`.
Of these, `Animal` can be chosen by the best common type algorithm.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: RC OT DR MH TLAT 12+ Last updated: Jun 15, 2026

## Variable Declarations

Was this page helpful?

# Variable Declaration
 `let` and `const` are two relatively new concepts for variable declarations in JavaScript.
 As we mentioned earlier , `let` is similar to `var` in some respects, but allows users to avoid some of the common “gotchas” that users run into in JavaScript.

`const` is an augmentation of `let` in that it prevents re-assignment to a variable.

With TypeScript being an extension of JavaScript, the language naturally supports `let` and `const`.
Here we’ll elaborate more on these new declarations and why they’re preferable to `var`.

If you’ve used JavaScript offhandedly, the next section might be a good way to refresh your memory.
If you’re intimately familiar with all the quirks of `var` declarations in JavaScript, you might find it easier to skip ahead.

## `var` declarations

 Declaring a variable in JavaScript has always traditionally been done with the `var` keyword.

 ts ` var a = 10 ; `
 As you might’ve figured out, we just declared a variable named `a` with the value `10`.

We can also declare a variable inside of a function:

 ts ` function f () { var message = "Hello, world!" ; return message ; } `
 and we can also access those same variables within other functions:

 ts ` function f () { var a = 10 ; return function g () { var b = a + 1 ; return b ; }; } var g = f (); g (); // returns '11' `
 In this above example, `g` captured the variable `a` declared in `f`.
At any point that `g` gets called, the value of `a` will be tied to the value of `a` in `f`.
Even if `g` is called once `f` is done running, it will be able to access and modify `a`.

 ts ` function f () { var a = 1 ; a = 2 ; var b = g (); a = 3 ; return b ; function g () { return a ; } } f (); // returns '2' `

### Scoping rules

 `var` declarations have some odd scoping rules for those used to other languages.
Take the following example:

 ts ` function f ( shouldInitialize : boolean ) { if ( shouldInitialize ) { var x = 10 ; } return x ; } f ( true ); // returns '10' f ( false ); // returns 'undefined' `
 Some readers might do a double-take at this example.
The variable `x` was declared within the `if` block , and yet we were able to access it from outside that block.
That’s because `var` declarations are accessible anywhere within their containing function, module, namespace, or global scope - all which we’ll go over later on - regardless of the containing block.
Some people call this `var`-scoping or function-scoping .
Parameters are also function scoped.

These scoping rules can cause several types of mistakes.
One problem they exacerbate is the fact that it is not an error to declare the same variable multiple times:

 ts ` function sumMatrix ( matrix : number [][]) { var sum = 0 ; for ( var i = 0 ; i < matrix . length ; i ++) { var currentRow = matrix [ i ]; for ( var i = 0 ; i < currentRow . length ; i ++) { sum += currentRow [ i ]; } } return sum ; } `
 Maybe it was easy to spot out for some experienced JavaScript developers, but the inner `for`-loop will accidentally overwrite the variable `i` because `i` refers to the same function-scoped variable.
As experienced developers know by now, similar sorts of bugs slip through code reviews and can be an endless source of frustration.

### Variable capturing quirks

 Take a quick second to guess what the output of the following snippet is:

 ts ` for ( var i = 0 ; i < 10 ; i ++) { setTimeout ( function () { console . log ( i ); }, 100 * i ); } `
 For those unfamiliar, `setTimeout` will try to execute a function after a certain number of milliseconds (though waiting for anything else to stop running).

Ready? Take a look:

 ` 10 10 10 10 10 10 10 10 10 10 `
 Many JavaScript developers are intimately familiar with this behavior, but if you’re surprised, you’re certainly not alone.
Most people expect the output to be

 ` 0 1 2 3 4 5 6 7 8 9 `
 Remember what we mentioned earlier about variable capturing?
Every function expression we pass to `setTimeout` actually refers to the same `i` from the same scope.

Let’s take a minute to consider what that means.
`setTimeout` will run a function after some number of milliseconds, but only after the `for` loop has stopped executing;
By the time the `for` loop has stopped executing, the value of `i` is `10`.
So each time the given function gets called, it will print out `10`!

A common work around is to use an IIFE - an Immediately Invoked Function Expression - to capture `i` at each iteration:

 ts ` for ( var i = 0 ; i < 10 ; i ++) { // capture the current state of 'i' // by invoking a function with its current value ( function ( i ) { setTimeout ( function () { console . log ( i ); }, 100 * i ); })( i ); } `
 This odd-looking pattern is actually pretty common.
The `i` in the parameter list actually shadows the `i` declared in the `for` loop, but since we named them the same, we didn’t have to modify the loop body too much.

## `let` declarations

 By now you’ve figured out that `var` has some problems, which is precisely why `let` statements were introduced.
Apart from the keyword used, `let` statements are written the same way `var` statements are.

 ts ` let hello = "Hello!" ; `
 The key difference is not in the syntax, but in the semantics, which we’ll now dive into.

### Block-scoping

 When a variable is declared using `let`, it uses what some call lexical-scoping or block-scoping .
Unlike variables declared with `var` whose scopes leak out to their containing function, block-scoped variables are not visible outside of their nearest containing block or `for`-loop.

 ts ` function f ( input : boolean ) { let a = 100 ; if ( input ) { // Still okay to reference 'a' let b = a + 1 ; return b ; } // Error: 'b' doesn't exist here return b ; } `
 Here, we have two local variables `a` and `b`.
`a`’s scope is limited to the body of `f` while `b`’s scope is limited to the containing `if` statement’s block.

Variables declared in a `catch` clause also have similar scoping rules.

 ts ` try { throw "oh no!" ; } catch ( e ) { console . log ( "Oh well." ); } // Error: 'e' doesn't exist here console . log ( e ); `
 Another property of block-scoped variables is that they can’t be read or written to before they’re actually declared.
While these variables are “present” throughout their scope, all points up until their declaration are part of their temporal dead zone .
This is just a sophisticated way of saying you can’t access them before the `let` statement, and luckily TypeScript will let you know that.

 ts ` a ++; // illegal to use 'a' before it's declared; let a ; `
 Something to note is that you can still capture a block-scoped variable before it’s declared.
The only catch is that it’s illegal to call that function before the declaration.
If targeting ES2015, a modern runtime will throw an error; however, right now TypeScript is permissive and won’t report this as an error.

 ts ` function foo () { // okay to capture 'a' return a ; } // illegal call 'foo' before 'a' is declared // runtimes should throw an error here foo (); let a ; `
 For more information on temporal dead zones, see relevant content on the Mozilla Developer Network .

### Re-declarations and Shadowing

 With `var` declarations, we mentioned that it didn’t matter how many times you declared your variables; you just got one.

 ts ` function f ( x ) { var x ; var x ; if ( true ) { var x ; } } `
 In the above example, all declarations of `x` actually refer to the same `x`, and this is perfectly valid.
This often ends up being a source of bugs.
Thankfully, `let` declarations are not as forgiving.

 ts ` let x = 10 ; let x = 20 ; // error: can't re-declare 'x' in the same scope `
 The variables don’t necessarily need to both be block-scoped for TypeScript to tell us that there’s a problem.

 ts ` function f ( x ) { let x = 100 ; // error: interferes with parameter declaration } function g () { let x = 100 ; var x = 100 ; // error: can't have both declarations of 'x' } `
 That’s not to say that a block-scoped variable can never be declared with a function-scoped variable.
The block-scoped variable just needs to be declared within a distinctly different block.

 ts ` function f ( condition , x ) { if ( condition ) { let x = 100 ; return x ; } return x ; } f ( false , 0 ); // returns '0' f ( true , 0 ); // returns '100' `
 The act of introducing a new name in a more nested scope is called shadowing .
It is a bit of a double-edged sword in that it can introduce certain bugs on its own in the event of accidental shadowing, while also preventing certain bugs.
For instance, imagine we had written our earlier `sumMatrix` function using `let` variables.

 ts ` function sumMatrix ( matrix : number [][]) { let sum = 0 ; for ( let i = 0 ; i < matrix . length ; i ++) { var currentRow = matrix [ i ]; for ( let i = 0 ; i < currentRow . length ; i ++) { sum += currentRow [ i ]; } } return sum ; } `
 This version of the loop will actually perform the summation correctly because the inner loop’s `i` shadows `i` from the outer loop.

Shadowing should usually be avoided in the interest of writing clearer code.
While there are some scenarios where it may be fitting to take advantage of it, you should use your best judgement.

### Block-scoped variable capturing

 When we first touched on the idea of variable capturing with `var` declaration, we briefly went into how variables act once captured.
To give a better intuition of this, each time a scope is run, it creates an “environment” of variables.
That environment and its captured variables can exist even after everything within its scope has finished executing.

 ts ` function theCityThatAlwaysSleeps () { let getCity ; if ( true ) { let city = "Seattle" ; getCity = function () { return city ; }; } return getCity (); } `
 Because we’ve captured `city` from within its environment, we’re still able to access it despite the fact that the `if` block finished executing.

Recall that with our earlier `setTimeout` example, we ended up needing to use an IIFE to capture the state of a variable for every iteration of the `for` loop.
In effect, what we were doing was creating a new variable environment for our captured variables.
That was a bit of a pain, but luckily, you’ll never have to do that again in TypeScript.

`let` declarations have drastically different behavior when declared as part of a loop.
Rather than just introducing a new environment to the loop itself, these declarations sort of create a new scope per iteration .
Since this is what we were doing anyway with our IIFE, we can change our old `setTimeout` example to just use a `let` declaration.

 ts ` for ( let i = 0 ; i < 10 ; i ++) { setTimeout ( function () { console . log ( i ); }, 100 * i ); } `
 and as expected, this will print out

 ` 0 1 2 3 4 5 6 7 8 9 `

## `const` declarations

 `const` declarations are another way of declaring variables.

 ts ` const numLivesForCat = 9 ; `
 They are like `let` declarations but, as their name implies, their value cannot be changed once they are bound.
In other words, they have the same scoping rules as `let`, but you can’t re-assign to them.

This should not be confused with the idea that the values they refer to are immutable .

 ts ` const numLivesForCat = 9 ; const kitty = { name: "Aurora" , numLives: numLivesForCat , }; // Error kitty = { name: "Danielle" , numLives: numLivesForCat , }; // all "okay" kitty . name = "Rory" ; kitty . name = "Kitty" ; kitty . name = "Cat" ; kitty . numLives --; `
 Unless you take specific measures to avoid it, the internal state of a `const` variable is still modifiable.
Fortunately, TypeScript allows you to specify that members of an object are `readonly`.
The chapter on Interfaces has the details.

## `let` vs. `const`

 Given that we have two types of declarations with similar scoping semantics, it’s natural to find ourselves asking which one to use.
Like most broad questions, the answer is: it depends.

Applying the principle of least privilege , all declarations other than those you plan to modify should use `const`.
The rationale is that if a variable didn’t need to get written to, others working on the same codebase shouldn’t automatically be able to write to the object, and will need to consider whether they really need to reassign to the variable.
Using `const` also makes code more predictable when reasoning about flow of data.

Use your best judgement, and if applicable, consult the matter with the rest of your team.

The majority of this handbook uses `let` declarations.

## Destructuring

 Another ECMAScript 2015 feature that TypeScript has is destructuring.
For a complete reference, see the article on the Mozilla Developer Network .
In this section, we’ll give a short overview.

### Array destructuring

 The simplest form of destructuring is array destructuring assignment:

 ts ` let input = [ 1 , 2 ]; let [ first , second ] = input ; console . log ( first ); // outputs 1 console . log ( second ); // outputs 2 `
 This creates two new variables named `first` and `second`.
This is equivalent to using indexing, but is much more convenient:

 ts ` first = input [ 0 ]; second = input [ 1 ]; `
 Destructuring works with already-declared variables as well:

 ts ` // swap variables [ first , second ] = [ second , first ]; `
 And with parameters to a function:

 ts ` function f ([ first , second ]: [ number , number ]) { console . log ( first ); console . log ( second ); } f ([ 1 , 2 ]); `
 You can create a variable for the remaining items in a list using the syntax `...`:

 ts ` let [ first , ... rest ] = [ 1 , 2 , 3 , 4 ]; console . log ( first ); // outputs 1 console . log ( rest ); // outputs [ 2, 3, 4 ] `
 Of course, since this is JavaScript, you can just ignore trailing elements you don’t care about:

 ts ` let [ first ] = [ 1 , 2 , 3 , 4 ]; console . log ( first ); // outputs 1 `
 Or other elements:

 ts ` let [, second , , fourth ] = [ 1 , 2 , 3 , 4 ]; console . log ( second ); // outputs 2 console . log ( fourth ); // outputs 4 `

### Tuple destructuring

 Tuples may be destructured like arrays; the destructuring variables get the types of the corresponding tuple elements:

 ts ` let tuple : [ number , string , boolean ] = [ 7 , "hello" , true ]; let [ a , b , c ] = tuple ; // a: number, b: string, c: boolean `
 It’s an error to destructure a tuple beyond the range of its elements:

 ts ` let [ a , b , c , d ] = tuple ; // Error, no element at index 3 `
 As with arrays, you can destructure the rest of the tuple with `...`, to get a shorter tuple:

 ts ` let [ a , ... bc ] = tuple ; // bc: [string, boolean] let [ a , b , c , ... d ] = tuple ; // d: [], the empty tuple `
 Or ignore trailing elements, or other elements:

 ts ` let [ a ] = tuple ; // a: number let [, b ] = tuple ; // b: string `

### Object destructuring

 You can also destructure objects:

 ts ` let o = { a: "foo" , b: 12 , c: "bar" , }; let { a , b } = o ; `
 This creates new variables `a` and `b` from `o.a` and `o.b`.
Notice that you can skip `c` if you don’t need it.

Like array destructuring, you can have assignment without declaration:

 ts ` ({ a , b } = { a: "baz" , b: 101 }); `
 Notice that we had to surround this statement with parentheses.
JavaScript normally parses a `{` as the start of block.

You can create a variable for the remaining items in an object using the syntax `...`:

 ts ` let { a , ... passthrough } = o ; let total = passthrough . b + passthrough . c . length ; `

#### Property renaming

 You can also give different names to properties:

 ts ` let { a : newName1 , b : newName2 } = o ; `
 Here the syntax starts to get confusing.
You can read `a: newName1` as ”`a` as `newName1`”.
The direction is left-to-right, as if you had written:

 ts ` let newName1 = o . a ; let newName2 = o . b ; `
 Confusingly, the colon here does not indicate the type.
The type, if you specify it, still needs to be written after the entire destructuring:

 ts ` let { a : newName1 , b : newName2 }: { a : string ; b : number } = o ; `

#### Default values

 Default values let you specify a default value in case a property is undefined:

 ts ` function keepWholeObject ( wholeObject : { a : string ; b ?: number }) { let { a , b = 1001 } = wholeObject ; } `
 In this example the `b?` indicates that `b` is optional, so it may be `undefined`.
`keepWholeObject` now has a variable for `wholeObject` as well as the properties `a` and `b`, even if `b` is undefined.

## Function declarations

 Destructuring also works in function declarations.
For simple cases this is straightforward:

 ts ` type C = { a : string ; b ?: number }; function f ({ a , b }: C ): void { // ... } `
 But specifying defaults is more common for parameters, and getting defaults right with destructuring can be tricky.
First of all, you need to remember to put the pattern before the default value.

 ts ` function f ({ a = "" , b = 0 } = {}): void { // ... } f (); `

 The snippet above is an example of type inference, explained earlier in the handbook.

Then, you need to remember to give a default for optional properties on the destructured property instead of the main initializer.
Remember that `C` was defined with `b` optional:

 ts ` function f ({ a , b = 0 } = { a: "" }): void { // ... } f ({ a: "yes" }); // ok, default b = 0 f (); // ok, default to { a: "" }, which then defaults b = 0 f ({}); // error, 'a' is required if you supply an argument `
 Use destructuring with care.
As the previous example demonstrates, anything but the simplest destructuring expression is confusing.
This is especially true with deeply nested destructuring, which gets really hard to understand even without piling on renaming, default values, and type annotations.
Try to keep destructuring expressions small and simple.
You can always write the assignments that destructuring would generate yourself.

## Spread

 The spread operator is the opposite of destructuring.
It allows you to spread an array into another array, or an object into another object.
For example:

 ts ` let first = [ 1 , 2 ]; let second = [ 3 , 4 ]; let bothPlus = [ 0 , ... first , ... second , 5 ]; `
 This gives bothPlus the value `[0, 1, 2, 3, 4, 5]`.
Spreading creates a shallow copy of `first` and `second`.
They are not changed by the spread.

You can also spread objects:

 ts ` let defaults = { food: "spicy" , price: "$$" , ambiance: "noisy" }; let search = { ... defaults , food: "rich" }; `
 Now `search` is `{ food: "rich", price: "$$", ambiance: "noisy" }`.
Object spreading is more complex than array spreading.
Like array spreading, it proceeds from left-to-right, but the result is still an object.
This means that properties that come later in the spread object overwrite properties that come earlier.
So if we modify the previous example to spread at the end:

 ts ` let defaults = { food: "spicy" , price: "$$" , ambiance: "noisy" }; let search = { food: "rich" , ... defaults }; `
 Then the `food` property in `defaults` overwrites `food: "rich"`, which is not what we want in this case.

Object spread also has a couple of other surprising limits.
First, it only includes an objects’
 own, enumerable properties .
Basically, that means you lose methods when you spread instances of an object:

 ts ` class C { p = 12 ; m () {} } let c = new C (); let clone = { ... c }; clone . p ; // ok clone . m (); // error! `
 Second, the TypeScript compiler doesn’t allow spreads of type parameters from generic functions.
That feature is expected in future versions of the language.

## `using` declarations

 `using` declarations are an upcoming feature for JavaScript that are part of the
 Stage 3 Explicit Resource Management proposal. A
`using` declaration is much like a `const` declaration, except that it couples the lifetime of the value bound to the
declaration with the scope of the variable.

When control exits the block containing a `using` declaration, the `[Symbol.dispose]()` method of the
declared value is executed, which allows that value to perform cleanup:

 ts ` function f () { using x = new C (); doSomethingWith ( x ); } // `x[Symbol.dispose]()` is called `
 At runtime, this has an effect roughly equivalent to the following:

 ts ` function f () { const x = new C (); try { doSomethingWith ( x ); } finally { x [ Symbol . dispose ](); } } `
 `using` declarations are extremely useful for avoiding memory leaks when working with JavaScript objects that hold on to
native references like file handles

 ts ` { using file = await openFile (); file . write ( text ); doSomethingThatMayThrow (); } // `file` is disposed, even if an error is thrown `
 or scoped operations like tracing

 ts ` function f () { using activity = new TraceActivity ( "f" ); // traces entry into function // ... } // traces exit of function `
 Unlike `var`, `let`, and `const`, `using` declarations do not support destructuring.

### `null` and `undefined`

 It’s important to note that the value can be `null` or `undefined`, in which case nothing is disposed at the end of the
block:

 ts ` { using x = b ? new C () : null ; // ... } `
 which is roughly equivalent to:

 ts ` { const x = b ? new C () : null ; try { // ... } finally { x ?.[ Symbol . dispose ](); } } `
 This allows you to conditionally acquire resources when declaring a `using` declaration without the need for complex
branching or repetition.

### Defining a disposable resource

 You can indicate the classes or objects you produce are disposable by implementing the `Disposable` interface:

 ts ` // from the default lib: interface Disposable { [ Symbol . dispose ](): void ; } // usage: class TraceActivity implements Disposable { readonly name : string ; constructor ( name : string ) { this . name = name ; console . log ( `Entering: ${ name } ` ); } [ Symbol . dispose ](): void { console . log ( `Exiting: ${ name } ` ); } } function f () { using _activity = new TraceActivity ( "f" ); console . log ( "Hello world!" ); } f (); // prints: // Entering: f // Hello world! // Exiting: f `

## `await using` declarations

 Some resources or operations may have cleanup that needs to be performed asynchronously. To accommodate this, the
 Explicit Resource Management proposal also introduces
the `await using` declaration:

 ts ` async function f () { await using x = new C (); } // `await x[Symbol.asyncDispose]()` is invoked `
 An `await using` declaration invokes, and awaits , its value’s `[Symbol.asyncDispose]()` method as control leaves the
containing block. This allows for asynchronous cleanup, such as a database transaction performing a rollback or commit,
or a file stream flushing any pending writes to storage before it is closed.

As with `await`, `await using` can only be used in an `async` function or method, or at the top level of a module.

### Defining an asynchronously disposable resource

 Just as `using` relies on objects that are `Disposable`, an `await using` relies on objects that are `AsyncDisposable`:

 ts ` // from the default lib: interface AsyncDisposable { [ Symbol . asyncDispose ]: PromiseLike < void >; } // usage: class DatabaseTransaction implements AsyncDisposable { public success = false ; private db : Database | undefined ; private constructor ( db : Database ) { this . db = db ; } static async create ( db : Database ) { await db . execAsync ( "BEGIN TRANSACTION" ); return new DatabaseTransaction ( db ); } async [ Symbol . asyncDispose ]() { if ( this . db ) { const db = this . db : this . db = undefined ; if ( this . success ) { await db . execAsync ( "COMMIT TRANSACTION" ); } else { await db . execAsync ( "ROLLBACK TRANSACTION" ); } } } } async function transfer ( db : Database , account1 : Account , account2 : Account , amount : number ) { using tx = await DatabaseTransaction . create ( db ); if ( await debitAccount ( db , account1 , amount )) { await creditAccount ( db , account2 , amount ); } // if an exception is thrown before this line, the transaction will roll back tx . success = true ; // now the transaction will commit } `

### `await using` vs `await`

 The `await` keyword that is part of the `await using` declaration only indicates that the disposal of the resource is
`await`-ed. It does not `await` the value itself:

 ts ` { await using x = getResourceSynchronously (); } // performs `await x[Symbol.asyncDispose]()` { await using y = await getResourceAsynchronously (); } // performs `await y[Symbol.asyncDispose]()` `

### `await using` and `return`

 It’s important to note that there is a small caveat with this behavior if you are using an `await using` declaration in
an `async` function that returns a `Promise` without first `await`-ing it:

 ts ` function g () { return Promise . reject ( "error!" ); } async function f () { await using x = new C (); return g (); // missing an `await` } `
 Because the returned promise isn’t `await`-ed, it’s possible that the JavaScript runtime may report an unhandled
rejection since execution pauses while `await`-ing the asynchronous disposal of `x`, without having subscribed to the
returned promise. This is not a problem that is unique to `await using`, however, as this can also occur in an `async`
function that uses `try..finally`:

 ts ` async function f () { try { return g (); // also reports an unhandled rejection } finally { await somethingElse (); } } `
 To avoid this situation, it is recommended that you `await` your return value if it may be a `Promise`:

 ts ` async function f () { await using x = new C (); return await g (); } `

## `using` and `await using` in `for` and `for..of` statements

 Both `using` and `await using` can be used in a `for` statement:

 ts ` for ( using x = getReader (); ! x . eof ; x . next ()) { // ... } `
 In this case, the lifetime of `x` is scoped to the entire `for` statement and is only disposed when control leaves the
loop due to `break`, `return`, `throw`, or when the loop condition is false.

In addition to `for` statements, both declarations can also be used in `for..of` statements:

 ts ` function * g () { yield createResource1 (); yield createResource2 (); } for ( using x of g ()) { // ... } `
 Here, `x` is disposed at the end of each iteration of the loop , and is then reinitialized with the next value. This is
especially useful when consuming resources produced one at a time by a generator.

## `using` and `await using` in older runtimes

 `using` and `await using` declarations can be used when targeting older ECMAScript editions as long as you are using
a compatible polyfill for `Symbol.dispose`/`Symbol.asyncDispose`, such as the one provided by default in recent
editions of NodeJS.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: DR OT NS VR BC 24+ Last updated: Jun 15, 2026