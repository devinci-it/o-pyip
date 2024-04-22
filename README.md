```text
                                             _/_/_/  _/_/_/    
    _/_/                _/_/_/    _/    _/    _/    _/    _/   
 _/    _/  _/_/_/_/_/  _/    _/  _/    _/    _/    _/_/_/      
_/    _/              _/    _/  _/    _/    _/    _/           
 _/_/                _/_/_/      _/_/_/  _/_/_/  _/            
                    _/              _/                         
                   _/          _/_/                            
```
# o-pyIP | Network Interface Manager CLI Tool

This CLI tool allows users to manage network interfaces on their system. It provides functionality to list available network interfaces, set IP addresses for specific interfaces, and display help information.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/devinci-it/o-pyip.git
    ```

2. Navigate to the project directory:

    ```bash
    cd o-pyip
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:
    ```bash
    venv\Scripts\activate
    ```

    On Unix or MacOS:
    ```bash
    source venv/bin/activate
    ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
## Usage

### Building and Using with pip

1. **Build the Package:**

    Run the following command to build the package:

    ```bash
    python setup.py sdist bdist_wheel
    ```

    This command will create a `dist` directory containing the built distribution files.

2. **Install the Package Locally:**

    You can install the package locally to test it before publishing. Navigate to the `dist` directory and run:

    ```bash
    pip install *-0.1.0-py3-none-any.whl
    ```

3. **Usage:**

    Once installed, users can use your CLI tool as follows:

    ```bash
    sudo pi [OPTIONS]
    ```

    Options:

    - `--interface INTERFACE`: Name of the interface.
    - `--ip IP_ADDRESS`: IP address to set.
    - `--netmask NETMASK`: Netmask to set.
    - `--list`: List available network interfaces.

    Example usage:

    - List available network interfaces:

        ```bash
        sudo pi --list
        ```

    - Set IP address for a specific interface:

        ```bash
        sudo pi --interface eth0 --ip 192.168.1.10 --netmask 255.255.255.0
        ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
