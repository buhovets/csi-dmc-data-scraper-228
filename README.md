# **CSI-DMC Data Scraper Project Specification**

---

## **1. Introduction**
The objective of this project is to facilitate the development of two distinct data scraping tools tailored for the `csi-dmc.com` website. The desired tools include a scraper based on the Scrapy framework in Python and an Apify actor. This specification document outlines the requirements, desired outputs, and evaluation criteria for the tools.

---

## **2. Project Scope**

**2.1. Target Website**: `csi-dmc.com`

**2.2. Desired Tools**:
- Scrapy scraper using Python.
- Apify actor.

**2.3. Output**:
- Both tools should generate a JSON file that captures the title, raw text, and images from each page on the website.

---

## **3. Detailed Requirements**

### **3.1. General Requirements**

- **Output Format**: The scraped data must be structured in the JSON format. Each page should have a dedicated JSON object with the following schema:
    ```json
    {
        "title": "Page Title",
        "text": "Raw text content of the page",
        "images": ["url1", "url2", ]
    }
    ```
  
- **Error Handling**: Both tools should be adept at handling unexpected issues. Should a page fail to scrape, the incident must be logged, ensuring that the tool continues with the next page.
  
### **3.2. Scrapy Scraper Specifications**

- **Development Framework**: Utilize Python and the Scrapy framework.
  
- **Output File**: The resulting data must be stored in a file termed `csi-dmc_scrapy_output.json`.

### **3.3. Apify Actor Specifications**

- **Platform Compatibility**: The actor should be engineered to operate seamlessly on the Apify platform.
  
- **Output File**: The resulting data must be stored in a file termed `csi-dmc_apify_output.json`.

---

## **4. Evaluation Criteria**

The deliverables will be assessed based on:

1. **Code Readability and Documentation**: The provided code should adhere to best practices with regards to clarity and documentation. A rich commenting system, coupled with sensible naming conventions for functions and variables, is essential. Accompanying each tool should be a thorough `README.md` document outlining setup and execution instructions.
  
2. **Scalability and Maintainability**: The solutions should be future-proof, ensuring minimal modifications if the website structure undergoes changes. A modular approach is vital for maintainability.
  
3. **Test Driven Development (TDD)**: Emphasis should be placed on crafting tests prior to the primary implementation. Comprehensive unit tests for both tools are expected. Additionally, please include a dedicated section in the documentation detailing the test execution procedure.

---

## **5. Submission Process**

1. Clone the provided repository.
2. Implement the required features and integrate documentation.
3. Commit and push the changes.
4. Notify the project manager or relevant party upon completion.
