# Python

The following conventions help keeping overview and the code clear.

Keep [`The Zen of Python`][website_wikipedia_zen_of_python] in mind when coding python.
From [Wikipedia - Python][website_wikipedia_python]:  
In general, the language's core philosophy (...) includes

```text
Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Readability counts.
```

which may be called `pythonic`.

## File Style

* Header files should __NOT__ contain redundant information (like date, license).
  Authors and credits are accepted.
  This is not only to prevent copying code without its authors, it also helps to find a person who (hopefully) understands the code.

  _For instance date and license are stored through your VCS (`git`) or repo.
  Writing this information in the header would cause confusion about its reliability._

  ```python
  '''
  This is an example for a python file.
  The header should explain this file/module.

  Important:
  (1) Empty lines are on purpose.
  (2) Sort imports in alphabetical order.
  '''
  __author__ = 'Dominic Parga Cacheiro'
  __credits__ = 'Dominic Parga Cacheiro, Nicolas Parga Cacheiro,'

  # first: built-in imports
  import argparse

  # then: third-party-modules
  import matplotlib

  # last: own modules
  import my_module

  # content
  ```

* Maximum line width is `79`, for documentation `72`.

  _Humans have trouble reading the code with increasing line width.
  In general, more than `80` is not recommended.
  Since python is not such a verbose language, you should stick with this._

* Use `4 spaces` for indention (p.s.: [could help your salary][website_salary]!).

## Coding Conventions

* Class names are written in `CamelCase`, functions, fields in `snake_case`.

  In python, more or less every field in a file can be accessed __from any file__.
  Hence, you should mark "private" fields with a single underscore before its name.

  ```python
  class SuperCircle:

      def __init__(self, super_radius):
          # BAD
          self.super_radius = super_radius

          # GOOD
          self._super_radius = super_radius
  ```

  They still can be accessed from outside the class, but shouldn't.
  For more information about the underscore (especially dunderscore) in python, reading [this pretty site][website_python_underscore] is highly recommended.

* Use `constants` over `magic numbers`!

  _Even you as the author will not know the meaning of every number after several months.
  And if you know, you will probably forget the precision of your constant and the places, where you put them (-> bad for debugging)._

  ```python
  # BAD

  area = 3.1 * radius * radius
  # (...)
  # somewhere else in the code
  circum = 2 * 3.1415 * radius
  # or
  circum = 6.283 * radius



  # GOOD

  # maybe inside a wrapper class?
  PI   = 3.1415
  PI_2 = 6.2832

  area = PI * radius * radius
  # (...)
  # somewhere else in the code
  circum = 2 * PI * radius
  # or
  circum = PI_2 * radius
  ```

* Use `'` for strings, not `"`, because it looks cleaner.

  ```python
  def do_stuff():
    '''
    Some python doc
    '''
    x = 42

  def do_more_stuff():
    """
    More text, but its marks are looking kind of fuzzy
    """
    x = 24
    ```

* Make __visibility as closest__ as possible.

  _Usually, you tend to not bother with visibility, but visibility helps a lot with getting nice and persistent interfaces._

* __Use `getter`/`setter`__ (pythonic) instead of direct access.

  _This is important for maintenance.
  Changing the implementation of a class should tend to make no difference for users of this class.
  Furthermore, debugging with breakpoints is much more easier when you only have to make one breakpoint instead of many at different positions.
  Same argument counts for synchronization code snippets._

  Python supports this issue a lot by the keyword `@property` in combination with `@<property_name>.setter`.

  ```python
  class Length:

      def __init__(self, metres):
          self._metres = metres

      @property
      def metres(self):
          return self._metres

      @property
      def kilometres(self):
          return self._metres / 1000.0

      @kilometres.setter
      def kilometres(self, kilometres):
          self._metres = 1000.0 * kilometres


  # access
  length = Length(42.0)
  print(length.metres)        # prints 42.0
  print(length.kilometres)    # prints 0.042

  # set properties
  length.kilometres = 0.043   # allowed
  length.metres = 43.0        # no setter -> error
  ```

  It's very handy to use this, but keep in mind that these properties will be used for quick access.
  Thus, they should not be seen as replacement for a function calculating a lot.

* Use __white spaces around binary operators__.
  Exceptions can be made for special cases to improve readability (see below).

  ```diff
  - e = (- a) * b;
  + e = (-a) * b;

  - e = a*b;
  + e = a * b;

  + e = a * b + c * d;    # ok, but not recommended here
  + e = a*b + c*d;        # improves readability
  ```

## Documentation

* Separate module sections with `#######` (whole line).
  Take the following code snippet for inspiration.

  ```python
  '''
  <Header>
  '''

  ##########################################################
  # group 0, e.g. imports

  import numpy as np # unused in this example...

  ##########################################################

  class Chair:

      def __init__(self, color):
          self._color = color

      ######################################################
      # group, e.g. some properties

      @property
      def color(self):
          return self._color

      @color.setter
      def color(self, color):
          self._color = color

      ######################################################
      # group

      def move(self):
        # ...

      def break(self):
        # ...

  ##########################################################
    # group (e.g. static functions or main-method)
  ```

## Project Conventions

* A main file should use

  ```python
  def main():
      pass

  if __name__ == '__main__':
      main() # or similar
  ```

  to execute the script, so importing the script does not execute it.

* The typical way of writing a `python module` is writing a file.
  This follows in less packages as in other languages (like Java).
  Prefer package/folder/file management over class mangement if `meaningful`.  
  __BUT:__ Think in an intuitive, handy and `deterministic`(!) way and don't take structuring and subfolding too far.

  Always ask yourself:  
  `How would most of the people search for this module/class/file?`  
  Someone without knowing your whole project structure should be able to find a file at the first try.  
  `In every folder, there should be only one option to continue searching (-> determinism).`

[website_salary]: https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs

[website_python_underscore]: https://shahriar.svbtle.com/underscores-in-python
[website_wikipedia_zen_of_python]: https://en.wikipedia.org/wiki/Zen_of_Python
[website_wikipedia_python]: https://en.wikipedia.org/wiki/Python_(programming_language)#Features_and_philosophy
