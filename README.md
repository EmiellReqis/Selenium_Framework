# **Selenium_Framework**
Description TODO.

## **Table of Contents**
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing Dependencies](#installing-dependencies)
    - [Setting Up ChromeDriver](#setting-up-chromedriver)
  - [Running Tests](#running-tests)


## **Getting Started**
### **Prerequisites**
- Python (version 3.11)
- Pip (Python package installer)
  
### **Installing Dependencies**
1. Clone the repository:
  ```
  git clone https://github.com/EmiellReqis/Selenium_Framework.git
  cd path_to_project/Selenium_Framework
  ```
2. Install required Python packages:
  ```
  pip install -r requirements.txt
  ```
  Note: Ensure you have Python installed. If not, download it from python.org.

### **Setting Up ChromeDriver**
1. Download ChromeDriver:
   - Download the appropriate version of ChromeDriver from [ChromeDriver download page](https://googlechromelabs.github.io/chrome-for-testing/).
     
2. Add ChromeDriver to PATH:
  - Windows:
    1. Download ChromeDriver and extract it to a directory (e.g., D:\usr\local\bin).
    2. Add D:\usr\local\bin to the system PATH:
        - Open Start Search, type in 'env', and select 'Edit the system environment variables'.
        - Click the Environment Variables... button.
        - Under System Variables, find the Path variable and click Edit....
        - Add D:\usr\local\bin to the list of paths.  
       
## **Running Tests**
To run the tests for this project, follow these steps:

1. Navigate to the Project Directory:
  Open a terminal or command prompt and navigate to the root directory of your project. For example:
  ```
  cd path/to/your/project
  ```
2. Run Tests with pytest:
  Use the pytest command to execute your tests. For example, to run a specific test file:
  ```
  python -m pytest tests/Saucedemo_tests/test_remove_from_cart.py
  ```
  This command will run the test_remove_from_cart.py script located in the tests/Saucedemo_tests directory.

3. View Test Results:
  After running the tests, pytest will display the results in the terminal, showing which tests passed, failed, or were skipped. Additionally, test results and logs will be generated in the reports folder.

  The reports folder structure will look like this:

  ```
  ├── reports/
  │   ├── screenshots/
  │   ├── current_date/
  │       ├── Saucedemo_tests_current_time/
  ```
  The current_date folder will have subfolders named after the test suite, each containing logs and screenshots from the test run at current_time.
