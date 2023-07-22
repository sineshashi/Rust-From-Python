# Using Rust Performance in Python

This repository is a simple project to guide how we can take advantage of Rust in Python by calling Rust functions in Python. For that, I have used `pyo3` library which helps us to call methods from Python.

## Guide

After creating simple cargo project with `cargo new project` command, we need to modify `cargo.toml `file. We have to add `pyo3 `library with extenstion-modules features and create on more section `lib `where we have define the library name and type where type must be `cdlyb`.

Now we can take advantage of `pyo3` to define methods in `src/lib.rs` . Sample code can be found in the same file for different arithmetic operations.

After defining the methods which we need call from Python, we create a build by a simple command `cargo build --release`. This will create a `dll` or `so` file based on the operating system in `./target/release/` folder.

Use `ctypes` in Python to load the `dll` or `so` file and redefine the inputs and outputs with `ctypes`. Example code in arithmetic_operations_rust.py where we have wrapped those rust functions with Python and are now callable from any module of Python.
