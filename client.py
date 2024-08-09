from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the target website with URL parameters for placeholder text
    driver.get("https://www.lipsum.com/feed/html?amount=5")  # Fetch 5 paragraphs of text

    # Wait for the page to load and the content to be visible
    driver.implicitly_wait(5)  # Adjust wait time as needed

    # Locate and print the generated text
    result_text = driver.find_element('tag name', 'div').text
    print(result_text)

finally:
    # Close the WebDriver
    driver.quit()
