from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestContacts(unittest.TestCase):
    def setUp(self):
        # Setup Firefox options
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Ensures the browser window does not open
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Firefox(options=firefox_options)

    def test_contacts(self):
        driver = self.driver
        driver.get("http://10.48.10.184")  # Replace with your target website

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Check for the presence of all 10 test contacts
        for i in range(10):
            test_name = f'Test Name {i}'
            contact_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{test_name}')]")))
            assert contact_element.is_displayed(), f"Test contact {test_name} not found or not visible on the page"
            print(f"Test contact {test_name} found.")
        print("Test completed successfully. All 10 test contacts were verified.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
