# another support library

Utility header-only library that can be easily integrated in a project.
asl requires at least a **C++14** conforming compiler, there are no other
dependencies.

## Scope

You can think of this library as something similiar to
[abseil](https://github.com/abseil/abseil-cpp) (but asl is one year older than
abseil) and some cherry-picked features from boost.

This library _does not_ and _will not_ use exceptions because it is designed to
be used with [tewi](https://github.com/andry-dev/tewi) and
[reisen](https://github.com/andry-dev/reisen). Keep this in mind, please.

## asl headers

List of current asl headers:

 * `ct_string` - A basic compile-time string
 * `debug_only` - A class that stores a value only in debug builds
 * `detect_features` - It allows to detect various platform and compiler
                       features
 * `expected` - Something similiar to `std::expected<T, E>` but _without_
                `map()`, `value_or()` and other functions
 * `filesystem` - Various filesystem utilities
 * `functional` - Various useful functions for STL's containers (either
                  wrappers around `<algorithm>` or new functions like a
                  `for_each` that works on `std::tuple`)
 * `meta` - "Concepts" for C++14 and various metaprogramming utils
 * `ring` - Ring buffers (as a view adapter or as a static buffer)
 * `string_view` - constexpr-enabled incomplete `std::string_view` for C++14
 * `types` - Rust-like typedefs, const by default, mutable versions provided
             with the *mut* prefix
 * `write_once` - A class that stores a write-once type. Useful if you need
                  a const variable but you can't initialize it with lambdas
                  for a reason or another

## GSL headers

List of current GSL headers supported:

 * `assert` - `Ensures()` and `Expects()` that supports additional messages
 * `byte` - Representation of a byte
 * `not_null` - A way to say that a pointer must not be null
 * `span` - A read-write view on an array
 * `string_span` - `std::string_view` but read-write
 * `util` - Various utilities

## TODO

 * asl
    - [ ] `algorithm` - constexpr-enabled versions of `<algorithm>`
    - [x] `expected` - Something similiar to Boost.Outcome
    - [x] `string_view` - constexpr-enabled `std::string_view` for C++14
    - [ ] Implement something similiar to Boost.MPL in `meta`
 * gsl
    - [ ] Implement `gsl::narrow` and `gsl::narrow_cast` in `util`

## Why not just use Boost?

Because it's an hell to setup in small project, it's a chore to setup on
Windows, it's a huge dependency, some of its components come as a dynamic
library, and it's too much complex.
This library is designed to be integrated in a project as a git submodule or by
simply copying the `include` folder.
