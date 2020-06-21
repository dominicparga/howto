# Licensing

> Licensing can be a mess and confusing.
> This info-sheet should help understanding the licenses, but __does not__ guarantee correctness in a legal sense.
> Please read the licenses by yourself and, if needed, ask a lawyer for advice.


## Table of Contents <a name="toc"></a>

1. [General info](#general_info)
    1. [Copyright vs licensing](#copyright_vs_licensing)
    1. [SPDX-lists](#spdx_lists)
    1. [How I write my license](#how_i_write_my_license)
1. [Some licenses](#some_licenses)
    1. [Apache 2.0](#apache_2.0)
    1. [Apache 2.0 vs. MIT](#apache_2.0_vs_mit)
    1. [CC0-1.0](#cc0)
    1. [MIT](#mit)
    1. [GPL](#gpl)
    1. [WTFPL](#wtfpl)


## General info <a name="general_info"></a>

General info and a quick overview can be found here:

- [https://choosealicense.com/][choosealicense]

### Copyright vs licensing <a name="copyright_vs_licensing"></a>

First of all, there is copyright and there is licensing.
Copyright states out the owner of the object (e.g. your code).
Licensing is a legal way of defining, how others are allowed to use your object.
An example making the difference clearer: Let you write a library `A` and license it under the `GPL`, demanding every code depending on your library `A` being licensed under the `GPL` as well.
Although it is not welcome, you could use your own library `A` in another libary `B` and not license it under `GPL`, since only you are the copyright-holder and hence only you could sue yourself for violating the license.


### SPDX-lists <a name="spdx_lists"></a>

In some build-systems (e.g. `cargo` for the programming-language `Rust`), you can add a license-notice.
The [`SPDX`-syntax][spdx.org/licenses] provides a standardized way of writing these notices.
By the way, they are already used above.

Some licenses allows exceptions, which are [standardized as well][spdx.org/licenses/exceptions]V


### How I write my license <a name="how_i_write_my_license"></a>

As far as I see it, just copying the license is, strictly speaking, not enough to set your project under the respective license.
Instead of copying the license, you should just mention it and describe shortly the licensed object (e.g. your code, your binary, your library).
Further, I use `markdown` for my licenses (`LICENSE` becomes `LICENSE.md`).

Besides that, it is quite helpful to mention all used libraries/dependencies and their licenses, to check compatibility.
For an `Apache-2.0`-license, which changes to `GPL-3.0` depending on your built features (e.g. only some binaries depend on `GPL`-licensed code), this could look like this:

```markdown
# Copyright and License

## Mentioning this Copyright in own projects

Please include this Copyright- and License-notice in your project.
As suggested in the `Apache License, Version 2.0`, you may choose a separate file like "NOTICE" for this.
Instead of copying the whole file, you may copy only the following short version.

\```text
REPOSITORY-NAME
https://github.com/dominicparga/REPOSITORY-NAME
Copyright 2020 Dominic Parga Cacheiro
License Apache-2.0


Only needed, if the GPL-SCRIPT-XY is used

SCRIPT-NAME
https://github.com/dominicparga/REPOSITORY-NAMEhblob/nightly/PATH/TO/SCRIPT
Copyright 2020 Dominic Parga Cacheiro
License GPL-3.0-only
\```

The following description gives an (incomplete) overview about this repository (and resulting binaries), for which the above copyright-notice holds.

...


## Apache-2.0

This work is licensed under the `Apache License, Version 2.0`.
You may not use content of this repository or its files, which are directly or indirectly related to above mentioned parts, except in compliance with the `Apache License, Version 2.0`.
You may obtain a copy of the License at

`https://www.apache.org/licenses/LICENSE-2.0`

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.


## GPL-3.0

This repository contains one script `GPL-SCRIPT-XY`, which uses `GPL-LIBRARY` licensed under `GPL-3.0`.
Thus, this particular script is licensed under the `GPL-3.0` as well.
You may obtain a copy of the License at

`https://www.gnu.org/licenses/`


## Dependencies

\```text
SOME_LIBRARY
https://github.com/USER/SOME_LIBRARY
Copyright YYYY USER
License Apache-2.0
\```

\```text
ANOTHER_LIBRARY
https://github.com/USER/ANOTHER_LIBRARY
Copyright (c) YYYY USER
License Apache-2.0
\```

\```text
GPL-LIBRARY
https://github.com/USER/GPL-LIBRARY
Copyright (c) YYYY USER
License GPL-3.0-only
\```
```


## Some licenses <a name="some_licenses"></a>

In the following, some info about some licenses is given.


### Apache 2.0 <a name="apache_2.0"></a>

The `Apache-2.0`-license can be found [here][apache.org/license].
An example for a `NOTICE`-file can be found [here][apache.org/notice].


### Apache 2.0 vs. MIT <a name="apache_2.0_vs_mit"></a>

> As already mentioned, please read the licenses by yourself and view the following descriptions as guideline, not as a legally solid document.

While the `MIT`-license and `Apache-2.0`-license are quite similar in their basic concept, the `Apache-2.0`-license provides much more details and describes the issues from a more lawyer-centered perspective.Though they are comparable from a legal perspective they are not totally identical, which, obviously, affects the use of code licensed under them. To be more precise, the `Apache-2.0` has some extras and small restrictions compared to the `MIT`-license.

Basically, with both licenses, you are allowed to distribute, change and commercially use the code as you wish, as long as you are mentioning its original creator.
The main difference lays in `§4-Redistribution` and `§6-Trademarks` of the `Apache-2.0`-license.
While the `MIT`-license tries to simplify these topics, leading to more freedom, the `Apache-2.0` specifies some conditions.

- `Redistribution`: The `Apache-2.0`-license demands mentioning changes somewhere.
  The `NOTICE`-file can be added for the `Apache-2.0` for additional comments.
  As far as I understand the license, you may use it for these changes as well.
- `Trademarks`: The `Apache-2.0`-license does not permit the usage of trademarks.

Long story short, `Apache-2.0` grants more protection to the creator and his/her work by mentioning changes and protecting trademarks, while `MIT` focusses on the redistribution of the work.


### CC0-1.0 <a name="cc0"></a>

The `CC0-1.0`-license can be found [here][cc.org/publicdomain/zero/1.0].
This license basically means, that you can do almost whatever you want to.
Look at [creativecommons.org (German)][cc.org/publicdomain/zero/1.0/summary/de] or [creativecommons.org (English)][cc.org/publicdomain/zero/1.0/summary/en] for more details.


### MIT  <a name="mit"></a>

The `MIT`-license can be found [here][opensource.org/mit].


### GPL <a name="gpl"></a>

Good and official source is [gnu.org][gnu.org/licenses/gplv3], e.g. when it comes to using GPL-software in own projects.
There, you can find a nice pictured overview about compatible licenses and some explanations.


### WTFPL <a name="wtfpl"></a>

The `WTFPL`-license can be found [here][wtfpl].
It is what it's called: "You just DO WHAT THE FUCK YOU WANT TO".


[apache.org/license]: https://www.apache.org/licenses/LICENSE-2.0
[apache.org/notice]: https://www.apache.org/licenses/example-NOTICE.txt
[cc.org/publicdomain/zero/1.0]: https://creativecommons.org/publicdomain/zero/1.0/legalcode
[cc.org/publicdomain/zero/1.0/summary/de]: https://creativecommons.org/publicdomain/zero/1.0/deed.de
[cc.org/publicdomain/zero/1.0/summary/en]: https://creativecommons.org/publicdomain/zero/1.0/deed.en
[choosealicense]: https://choosealicense.com/
[gnu.org/licenses/gplv3]: https://www.gnu.org/licenses/quick-guide-gplv3.html
[opensource.org/mit]: https://opensource.org/licenses/mit-license.php
[spdx.org/licenses]: https://spdx.org/licenses/
[spdx.org/licenses/exceptions]: https://spdx.org/licenses/exceptions-index.html
[wtfpl]: http://www.wtfpl.net/about/
