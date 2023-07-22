use pyo3::prelude::*;

#[no_mangle]
#[pyfunction]
fn add_numbers(a: i32, b: i32) -> i32 {
    a + b
}

#[no_mangle]
#[pyfunction]
fn subtract_number(a: i32, b: i32) -> i32 {
    a - b
}

#[no_mangle]
#[pyfunction]
fn multiply_numbers(a: i32, b: i32) -> i32 {
    a * b
}


#[no_mangle]
#[pyfunction]
fn divide_numbers(a: i32, b: i32) -> f64 {
    (a as f64/b as f64)
}

#[pymodule]
fn arithmetic_operations(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_numbers, m)?)?;
    m.add_function(wrap_pyfunction!(subtract_number, m)?)?;
    m.add_function(wrap_pyfunction!(multiply_numbers, m)?)?;
    m.add_function(wrap_pyfunction!(divide_numbers, m)?)?;
    Ok(())
}
