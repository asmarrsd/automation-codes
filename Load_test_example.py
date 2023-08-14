import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Define the number of users to simulate
NUM_USERS = 10

# Define the Selenium test script
def run_test(user_id):
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    
    # Simulate user interactions
    search_box = driver.find_element_by_name("q")
    search_box.send_keys("Load testing with Selenium")
    search_box.send_keys(Keys.RETURN)
    
    # Add more interactions here
    
    time.sleep(2)  # Simulate user staying on the page for a while
    
    driver.quit()

# Create and start user threads
threads = []
for i in range(NUM_USERS):
    thread = threading.Thread(target=run_test, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("Load testing complete.")
