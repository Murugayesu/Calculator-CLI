# Simple Calculator CLI

A command-line calculator application built with Python that supports basic arithmetic operations and additional mathematical functions.

## Features

- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Advanced Operations**: Exponentiation (**), Square Root (sqrt)
- **Error Handling**: Comprehensive input validation and error management
- **User-Friendly Interface**: Clear prompts and formatted output
- **Continuous Operation**: Option to perform multiple calculations in one session

## Supported Operations

| Operation | Symbol | Example |
|-----------|--------|---------|
| Addition | + | 5 + 3 = 8 |
| Subtraction | - | 10 - 4 = 6 |
| Multiplication | * | 7 * 6 = 42 |
| Division | / | 15 / 3 = 5 |
| Exponentiation | ** | 2 ** 3 = 8 |
| Square Root | sqrt | √16 = 4 |


## Usage

Run the calculator by executing:

```bash
python main.py
```


## Error Handling

The calculator includes robust error handling for:

- **Invalid Number Input**: Prompts user to re-enter valid numbers
- **Division by Zero**: Prevents division by zero errors
- **Negative Square Roots**: Handles negative numbers for square root operations
- **Invalid Operations**: Validates operation input
- **Overflow Errors**: Manages calculations that result in numbers too large
- **Keyboard Interrupts**: Graceful exit when Ctrl+C is pressed


## Requirements

- Python 3.x
- Built-in `math` module (included with Python)

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- [ ] Support for more advanced mathematical functions (sin, cos, tan, log, etc.)
- [ ] Memory functions (store, recall, clear)
- [ ] Calculation history
- [ ] Support for complex numbers
- [ ] GUI version using tkinter
