# GUVIApplication_POM_Pytest

The objective of this project is automating the testing of GUVI website.
A robust **Page Object Model (POM)** + **Selenium WebDriver (Python)** + **PyTest** based automation framework for the GUVI web application.  
This project focuses on end-to-end automationtesting, modular framework design, configurable test data, and maintainable code, ideal for showcasing Automation skills.

---

##  Tech Stack & Tools

- **Python**  
- **Selenium WebDriver**  
- **PyTest**  
- **Page Object Model (POM)** design pattern  
- **pytest.ini** – Global PyTest configuration  
- **Reports** – Test report folder (HTML / Allure)  
- **Git & GitHub** – Version control & code hosting  

---

##  Project Structure

```
Project_1/
│
├── POM/                                          # Page classes → locators + actions
│ ├── HomePage.py
│ └── Login.py
│ └── User_page.py
│
├── TestData/                                            # External test data files
│ └── data.py
│
├── TestLocators
| └── locators.py
│
├── Reports/                                             # Test execution reports (HTML / Allure)
│
├── conftest.py # PyTest fixtures (setup/teardown)
├── requirements.txt # Python dependencies
├── test_project1_execution
└── README.md # Project documentation

```

##  Features / What this Framework Provides

- **Modular design using POM** — Page classes cleanly separate locators and page methods for maintainability.  
- **PyTest-based test suite** — Easily add, manage, and run test cases with fixtures, and configurations.  
- **Externalized test data** — Keep test data in separate file, keeps test logic separate from data.  
- **Clean reporting support** — Reports folder set up for HTML or other report generation after test execution.  
- **Scalable & extendable** — You can easily add more PageObjects, test scripts, utilities, or integrations (API, CI/CD) without breaking structure. 
---

## **Test Cases Covered**
```
1. URL and title validation
2. Menu bar items validation
3. Dobby assistant verification
4. Sign-in and sign-up verification
5. Login functionalities
6. Logout functionalities
```
