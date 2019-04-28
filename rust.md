# Rust

The following conventions help keeping overview and the code clear.
Since there exists an [official Rust Style Guide][website_rust_style_guide], this file just adds or summarizes some useful info.
Keep the [guiding principles and rationale][website_rust_principles] in mind when coding rust.

## File Style

* Maximum line width is `100`.
  Exceptions can be made for String-constants and similar.

  _This is a good trade off between `120` and `80`.
  Humans have trouble reading the code with increasing line width.
  In general, more than `80` is not recommended._

* Use `4 spaces` for indention (p.s.: [could help your salary][website_salary]!).

## Coding Conventions

* Class names are written in `CamelCase`, functions, fields in `snake_case`.

* Use `constants` over `magic numbers`!

  _Even you as the author will not know the meaning of every number after several months.
  And if you know, you will probably forget the precision of your constant and the places, where you put them (-> bad for debugging)._

  ```rust
  // BAD

  let area = 3.1 * radius * radius;
  // (...)
  // somewhere else in the code
  let circum = 2 * 3.1415 * radius;
  // or
  let circum = 6.283 * radius;



  // GOOD

  // maybe inside a wrapper struct?
  let PI   = 3.1415;
  let PI_2 = 6.2832;

  let area = PI * radius * radius;
  // (...)
  // somewhere else in the code
  let circum = 2 * PI * radius;
  // or
  let circum = PI_2 * radius;
  ```

* Use __white spaces around binary operators__.
  Exceptions can be made for special cases to improve readability (see below).

  ```diff
  - e = (- a) * b;
  + e = (-a) * b;

  - e = a*b;
  + e = a * b;

  + e = a * b + c * d;    // ok, but not recommended here
  + e = a*b + c*d;        // improves readability
  ```

## Documentation

* Separate module sections with `//---//` (whole line).
  Take the following code snippet for inspiration.

## Project Conventions

* Prefer package/folder/file management over class mangement if `meaningful`.  
  __BUT:__ Think in an intuitive, handy and `deterministic`(!) way and don't take structuring and subfolding too far.

  Always ask yourself:  
  `How would most of the people search for this module/struct/file?`  
  Someone without knowing your whole project structure should be able to find a file at the first try.  
  `In every folder, there should be only one option to continue searching (-> determinism).`

* Bring modules and structs into scope using `use`, but access functions via module or struct.

[website_rust_style_guide]: https://github.com/rust-dev-tools/fmt-rfcs/blob/master/guide/guide.md

[website_rust_principles]: https://github.com/rust-dev-tools/fmt-rfcs/blob/master/guide/principles.md

[website_salary]: https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs
