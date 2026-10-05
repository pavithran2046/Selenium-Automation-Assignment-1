# Selenium Web Automation - Assignment I

**Name:** Pavithran S  
**Registration Number:** 212223240113  
**Date:** 5-10-2026

## Overview
This repository contains three Python scripts demonstrating web automation using the Selenium WebDriver. 

### 1. Bing Search Automation (`bing_search.py`)
* Automates Microsoft Edge to open Bing.
* Searches for a specific keyword and hits Enter.
* Scrapes and prints the top 5 search result titles and their corresponding URLs.

### 2. Sauce Demo Login (`sauce_demo.py`)
* Automates Google Chrome to open the SauceDemo website.
* Validates input fields (checks placeholder text, visibility, and button state).
* Logs in using standard credentials and scrapes the names of all inventory products.

### 3. Flipkart Login Automation (`flipkart_login.py`)
* Automates Microsoft Edge to navigate to Flipkart's login page.
* Uses Explicit Waits to ensure elements are loaded.
* Identifies the phone number input field using XPath and DOM traversal, enters a phone number, and clicks the 'Continue' button to trigger OTP generation.

## Prerequisites
* Python 3.x
* Selenium (`pip install selenium`)
* Relevant WebDrivers (Edge WebDriver / ChromeDriver) configured in system PATH.
