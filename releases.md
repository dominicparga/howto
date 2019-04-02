# Releases

The following template for new releases can be used.
In general, needed information should be optained from commit messages.

```text
## General info

<optional>


## New features

<Short and interesting description about new features of this release.>


## Bug fixes

<Detailed description about fixed bugs of this release.>
```

## Release Checklist

These points should be considered and checked for a new release.

* Has `release` been merged into `master`?
* Is a new teaser picture needed/recommended?

## [Semantic Versioning][website_semantic_versioning]

"Given a version number `MAJOR.MINOR.PATCH`, increment the:

* `MAJOR` version when incompatible API changes are made,
* `MINOR` version when functionality in a backwards-compatible manner is added, and
* `PATCH` version when backwards-compatible bug fixes are made.

Exception could be alpha or beta status, when the software hasn't reached 1.0.0 yet.
Additional labels for pre-release and build metadata are available as extensions to the `MAJOR.MINOR.PATCH`."

For more information, see [the original site][website_semantic_versioning].

[website_semantic_versioning]: https://semver.org
