# Testing Automation

This project demonstrates a real-world automation framework for testing the OpenCart e-commerce platform. It covers both UI (end-to-end) and API testing, integrates with CI/CD, and generates detailed HTML reports with screenshots for failed tests.

---

## Features

- **UI Automation:**  
  Uses Selenium WebDriver to automate browser-based tests for OpenCart user flows (login, add to cart, etc.).

- **API Testing:**  
  Uses `requests` and `pytest` to validate REST API endpoints.

- **Pytest Framework:**  
  All tests are written using `pytest` for easy parametrization, fixtures, and scalability.

- **Screenshots on Failure:**  
  Automatically captures and attaches browser screenshots to HTML reports for any failed UI test, aiding in debugging.

- **HTML Reporting:**  
  Generates a self-contained HTML report after every test run using `pytest-html`, including screenshots for failed tests.

- **CI/CD Integration:**  
  Includes a ready-to-use GitHub Actions workflow to run all tests and upload HTML reports as artifacts on every push or pull request.

- **Best Practices:**  
  - Page Object Model for UI tests
  - Test isolation via fixtures
  - Requirements management
  - Organized test structure

---

## How to Run Locally

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Run all tests and generate an HTML report:**
   ```sh
   pytest --html=report.html --self-contained-html
   ```

3. **View the report:**  
   Open `report.html` in your browser. Screenshots for failed UI tests will appear in the "Links" column.

---

## CI/CD

- On every push or pull request, GitHub Actions will:
  - Install dependencies
  - Run all tests
  - Generate an HTML report
  - Upload the report as an artifact

You can download the latest report from the "Actions" tab in your GitHub repository.

---

## Key Concepts Demonstrated

- **Test Automation:**  
  Automated both UI and API layers for comprehensive coverage.

- **Page Object Model:**  
  UI tests use the POM pattern for maintainability and scalability.

- **Pytest Fixtures:**  
  Shared setup/teardown logic for browser and API tests.

- **Continuous Integration:**  
  Automated test execution and reporting on every code change.

- **Reporting & Debugging:**  
  Rich HTML reports with screenshots for fast feedback and troubleshooting.

---