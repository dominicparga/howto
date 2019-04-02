# Java

The following conventions help a lot keeping overview and the code clear.
These conventions just extend common Java style, meaning for instance that `camelCase` is used though it is not mentioned below.

## File Style

* Header files should __NOT__ contain redundant information (like date, license).
  Authors and credits are accepted.
  This is not only to prevent copying code without its authors, it also helps to find a person who (hopefully) understands the code.

  _For instance date and license are stored through your VCS (`git`) or repo.
  Writing this information in the header would cause confusion about its reliability._

  ```Java
  package xyz;

  import java.*;  // :)

  /**
   * Class explanations are going -here-.
   *
   * @author Nicolas Parga Cacheiro
   * @author Dominic Parga Cacheiro
   */
  public class Foo {
      // content
  }
  ```

* Maximum line width is `100`.

  _This is a good trade off between `120` and `80`.
  Humans have trouble reading the code with increasing line width.
  In general, more than `80` is not recommended, but Java is a very verbose language._

* Use `4 spaces` for indention (p.s.: [could help your salary][website_salary]!).

## Coding Conventions

* Use `constants` over `magic numbers`!

  _Even you as the author will not know the meaning of every number after several months.
  And if you know, you will probably forget the precision of your constant and the places, where you put them (-> bad for debugging)._

  ```java
  // BAD

  float area = 3.1 * radius * radius;
  // (...)
  // somewhere else in the code
  float circum = 2 * 3.1415 * radius;
  // or
  float circum = 6.283 * radius;



  // GOOD

  public static final float PI   = 3.1415;
  public static final float PI_2 = 6.2832;

  float area = PI * radius * radius;
  // (...)
  // somewhere else in the code
  float circum = 2 * PI * radius;
  // or
  float circum = PI_2 * radius;
  ```

* Make __visibility as closest__ as possible.

  _Usually, you tend to not bother with visibility, but visibility helps a lot with getting nice and persistent interfaces._

* __Use `getter`/`setter`__ instead of direct access, even for private usage.

  _This is unhandy, but important for maintenance.
  Changing the implementation of a class should tend to make no difference for users of this class.
  Furthermore, debugging with breakpoints is much more easier when you only have to make one breakpoint instead of many at different positions.
  Same argument counts for synchronization code snippets.
  [The code is getting inlined][website_java_direct_access]._

  `getter` starts with `get`, `setter` starts with `set`.
  Those `getter` returning a boolean expression may start differently, but with a verb.
  Corresponding fields are named like adjectives/states.
  Field names adapt to their corresponding `getter`/`setter`, not the other way around.

  ```diff
  - count()
  + getCount()

  - boolean isRunning = false;
  + boolean running = true;
  + boolean isRunning() { return running; }
  ```

* Use __white spaces around binary operators__.
  Exceptions can be made for special cases to improve readability (see below).

  ```diff
  - int e = (- a) * b;
  + int e = (-a) * b;

  - int e = a*b;
  + int e = a * b;

  + int e = a * b + c * d;    // ok, but not recommended here
  + int e = a*b + c*d;        // improves readability
  ```

* Use control structures with `curly brackets` and the keyword `else` after the closing bracket for nice commenting.

  _Using control structures without `curly brackets` are easy to write, but usually very uncomfortable to read (especially inside other control structures).
  Most of the time code is read, not written, so `curly brackets` should be used._

  ```java
  // BAD
  // may confuse

  for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
          // Are these comment lines ignored?
          // Can't remember without my IDE...
          if (isRunning)
              doSomething();
          else
              doSomethingElse();
          doAnything(); // NOT in the loop, but seems to be due to wrong indention



  // GOOD
  // clear and easy to read

  for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
          // no problem with comments
          if (isRunning) {
              doSomething();
          }
          // `else` after closing bracket for nice commenting
          else {
              doSomethingElse();
          }
      }
  }
  doAnything();
  ```

## Documentation

* Separate class sections with `/*****/` (whole line).
  Take the following code snippet for inspiration.

  ```java
  public class Chair {
    private Color color;

    /********************************************************/
    // group 0, e.g. constructors and factory methods

    public Chair(Color color) {
      this.color = color;
    }

    public static Chair getRedChair() {
      return new Chair(Color.RED);
    }

    /********************************************************/
    // group 1, e.g. getter/setter

    public Color getColor() {
      return color;
    }

    public void setColor(Color color) {
      this.color = color;
    }

    /********************************************************/
    // group 2

    public void move() {
      // ...
    }

    public void break() {
      // ...
    }

    /********************************************************/
    // group 3 (e.g. private classes)
  }
  ```

* Use annotations and html only where expected and helpful.
  Some useful ones:

  `@author Dominic Parga Cacheiro`  
  declares "Dominic Parga Cacheiro" as author of the class.
  In case of multiple authors, every author gets its own `@author`-tag.
  This tag should be seen as credit.
  See [File Style](#file-style) for more information.

  `@Override`  
  indicates that the annotated method is inherited from the parent class.

  `{@code xyz}`  
  can be used in JavaDocs to format text into code (with literals of the same width).

  `{@literal xyz}`  
  can be used in JavaDocs to use the literals as they are, not interpreted (e.g. as html).

  `<p>...</p>`  
  wraps a paragraph for formatting purpose, for instance it adds empty lines between paragraphs.
  This should be used over `<br>`.

  `<ul>`  
  `<li>` some item  
  `<li>` some other item  
  `</ul>`  
  adds an enumeration.
  This should be used over `&bull;`.

  `&bull;`  
  is a Point (similar to an enumeration item), but not a replacement for enumeration (see `<ul>` above).
  Can be used for dividing text snippets.

  `<br>`  
  is a line break, but it should be avoided and `<p>...</p>` should be used instead.
  Besides "dirty style" another reason is: some IDEs does not parse this linebreak in its JavaDoc preview.

  ```java
  /**
   * <p>
   * This is the JavaDoc of the following method.
   * </p>
   *
   * <p>
   * With {@literal <p>} you start a new paragraph.
   * Possible values for parameter x are:
   * <ul>
   * <li> {@code < 3} e.g. {@code x == 2}
   * <li> {@code >= 3} e.g. {@code x == 3}
   * </ul>
   * </p>
   */
  public void doStuff(int x) {
      if (x < 3) {
          System.out.println("x < 3");
      }
      else {
          System.out.println("x >= 3");
      }
  }
  ```

* A file `package-info.java` in a package can be used for package documentation.

  com/foo/package-info.java:

  ```java
  /**
   * package documentation
   */
  package com.foo;
  ```

## Project Conventions

* Prefer package/folder/file management over class mangement if `meaningful`.  
  __BUT:__ Think in an intuitive, handy and `deterministic`(!) way and don't take structuring and subfolding too far.

  Always ask yourself:  
  `How would most of the people search for this class?`  
  Someone without knowing your whole project structure should be able to find a file at the first try.  
  `In every folder, there should be only one option to continue searching (-> determinism).`

  _Take a math API for instance.
  It is okay to put basic classes like vector and matrix classes in __ONE__ package called `math`, because that's what it is.
  Someone searching for these classes will find them easily in this package even if there are a lot more classes in it.
  Think of creating a subfolder for your matrices and another subfolder for graph data structures.
  Is a matrix describing graph structures belonging to the matrix or the graph folder?
  It would be annoying to look for such a file in such a folder structure due to non-intuitive subfoldering._

[website_java_direct_access]: https://stackoverflow.com/questions/23931546/java-getter-and-setter-faster-than-direct-access
[website_salary]: https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs
