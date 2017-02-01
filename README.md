# another support library

## What's this

This is my personal "support library" that includes common stuff that I use
(like thin wrappers around STL algorithms) and an incomplete GSL implementation.

I made this because I didn't want to include Boost in my projects just to get
some basic functionality.

**This library requires C++14/17**

## So, what do you have?

 * asl/ct_string - A basic compile-time string
 * asl/debug_only - A class that stores a value only in debug builds
 * asl/detect_features - It allows to detect various platform and compiler
   features
 * asl/filesystem - Various filesystem utilities
 * asl/functional - Various useful functions for STL's containers (either
   wrappers around `algorithm` or new functions like a for_each that works on
   std::tuple)
 * asl/types - Rust-like typedefs, const by default, mutable versions provided
   with *mut_*
 * asl/write_once - A class that stores a write-once type. Useful if you need a
   const variable but you can't initialize it with lambdas for a reason or
   another

 * gsl/assert - Ensures() and Expects() that supports additional messages
