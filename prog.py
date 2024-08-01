
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

# Path to your ChromeDriver
path = "C:\chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.jiomart.com")
print("Page title is:", driver.title)

# Click on login/sign up  -------------Case 1-------------
def login_to_jiomart():
    try:
        button_element = driver.find_element(By.ID, "btn_sign_in")
        button_element.click()
        print("\nLogin button clicked successfully!")
    except Exception as e:
        print(f"\nFailed to find or click the login button: {e}")

# Enter phone number  -------------Case 2-------------
def parsing_phone_number():
    try:
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "phoneNumber"))
        )
        phone_input.clear()
        phone_input.send_keys("7667963240")
        print("\nPhone number entered successfully!")
        time.sleep(2)
        continue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'j-button') and contains(text(), 'Continue')]")
        continue_button.click()
        print("\nContinue button clicked successfully! Please enter OTP manually.")
    except Exception as e:
        print(f"\nFailed to enter the phone number or click continue: {e}")

# Enter OTP  -------------Case 3-------------

def enter_otp(otp):
    try:
        otp_input_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".code-block"))
        )
        
        if len(otp_input_elements) == len(otp):
            for i, otp_input in enumerate(otp_input_elements):
                otp_input.clear()
                otp_input.send_keys(otp[i])
            verify_button = driver.find_element(By.XPATH, "//button[contains(@class, 'j-button') and contains(text(), 'Verify')]")
            verify_button.click()
            print("\nEntered OTP successfully!")
        else:
            print("\nMismatch between OTP length and input fields.")
    except Exception as e:
        print(f"\nFailed to verify the OTP: {e}")

    time.sleep(5)



# Search for a product - ------------Case 4-------------
def product_search(product):
    try:
        search_input_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "autocomplete-0-input"))
        )
        search_input_element.clear()
        search_input_element.send_keys(product)
        search_input_element.send_keys(Keys.RETURN)
        print(f"\nSearched for {product} successfully!")
    except Exception as e:
        print(f"\nFailed to search for {product}: {e}")


# Add an item to the cart - ------------Case 5-------------
def add_to_cart():
    try:
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/div[1]/div/div[2]/div[3]/div/div/ol/li[1]/a/div[2]/div[3]/div/div/button/img'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
        time.sleep(1) 
        button_parent = add_to_cart_button.find_element(By.XPATH, '..')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(button_parent)
        )
        button_parent.click()
        print("\nItem added to cart successfully!")
        time.sleep(4)
    except TimeoutException:
        print("\nFailed to locate the 'Add to Cart' button within the timeout period.")
    except ElementClickInterceptedException:
        print("\nElement click intercepted. Attempting to click using JavaScript.")
        try:
            driver.execute_script("arguments[0].click();", add_to_cart_button)
            print("\nClicked the 'Add to Cart' button using JavaScript.")
        except Exception as js_e:
            print(f"\nFailed to click the 'Add to Cart' button using JavaScript: {js_e}")
    except ElementNotInteractableException:
        print("\nElement is not interactable. Ensure the button is visible and enabled.")
    except Exception as e:
        print(f"\nFailed to add item to cart: {e}")

def increment_item():
    try:
        increment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/div[1]/div/div[2]/div[3]/div/div/ol/li[1]/a/div[2]/div[3]/div/div/button[2]/img'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", increment_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", increment_button)
        print("\nItem incremented in cart successfully!")
        time.sleep(4)
    except TimeoutException:
        print("\nFailed to locate the increment button within the timeout period.")
    except ElementClickInterceptedException:
        print("\nElement click intercepted. Attempting to click using JavaScript.")
        try:
            driver.execute_script("arguments[0].click();", increment_button)
            print("\nClicked the increment button using JavaScript.")
        except Exception as js_e:
            print(f"\nFailed to click the increment button using JavaScript: {js_e}")
    except ElementNotInteractableException:
        print("\nElement is not interactable. Ensure the button is visible and enabled.")
    except Exception as e:
        print(f"\nFailed to increment item in cart: {e}")

def decrement_item():
    try:
        decrement_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/div[1]/div/div[2]/div[3]/div/div/ol/li[1]/a/div[2]/div[3]/div/div/button[1]/img'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", decrement_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", decrement_button)
        print("\nItem decremented in cart successfully!")
        time.sleep(4)
    except TimeoutException:
        print("\nFailed to locate the decrement button within the timeout period.")
    except ElementClickInterceptedException:
        print("\nElement click intercepted. Attempting to click using JavaScript.")
        try:
            driver.execute_script("arguments[0].click();", decrement_button)
            print("\nClicked the decrement button using JavaScript.")
        except Exception as js_e:
            print(f"\nFailed to click the decrement button using JavaScript: {js_e}")
    except ElementNotInteractableException:
        print("\nElement is not interactable. Ensure the button is visible and enabled.")
    except Exception as e:
        print(f"\nFailed to decrement item in cart: {e}")

def go_to_cart():
    try:
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/header/section[1]/div/section[2]/div[2]/div/button/img'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", profile_button)
        time.sleep(1)
        profile_button.click()
        print("\nNavigated to the cart page successfully!")
    except TimeoutException:
        print("\nFailed to locate the cart button within the timeout period.")
    except ElementClickInterceptedException:
        print("\nElement click intercepted. Attempting to click using JavaScript.")
        try:
            driver.execute_script("arguments[0].click();", profile_button)
            print("\nClicked the cart button using JavaScript.")
        except Exception as js_e:
            print(f"\nFailed to click the cart button using JavaScript: {js_e}")
    except ElementNotInteractableException:
        print("\nElement is not interactable. Ensure the button is visible and enabled.")
    except Exception as e:
        print(f"\nFailed to navigate to the Cart page: {e}")

def go_to_profile():
    try:
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/jds-theme/jds-container/app-layout-ds/div/header/app-header-ds/div[1]/div/div/div[5]/a'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", profile_button)
        time.sleep(1)
        profile_button.click()
        print("\nNavigated to the profile page successfully!")
    except TimeoutException:
        print("\nFailed to locate the profile button within the timeout period.")
    except ElementClickInterceptedException:
        print("\nElement click intercepted. Attempting to click using JavaScript.")
        try:
            driver.execute_script("arguments[0].click();", profile_button)
            print("\nClicked the profile button using JavaScript.")
        except Exception as js_e:
            print(f"\nFailed to click the profile button using JavaScript: {js_e}")
    except ElementNotInteractableException:
        print("\nElement is not interactable. Ensure the button is visible and enabled.")
    except Exception as e:
        print(f"\nFailed to navigate to the profile page: {e}")
def go_to_home():
    try:
        home_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/header/section[1]/div/section[1]/div[1]/a/img'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", home_button)
        time.sleep(1)
        home_button.click()
        print("\nNavigated to the home page successfully!")
    except TimeoutException:
        print("\nFailed to locate the home button within the timeout period.")
    except ElementClickInterceptedException:
        print("\nElement click intercepted. Attempting to click using JavaScript.")
        try:
            driver.execute_script("arguments[0].click();", home_button)
            print("\nClicked the home button using JavaScript.")
        except Exception as js_e:
            print(f"\nFailed to click the home button using JavaScript: {js_e}")
    except ElementNotInteractableException:
        print("\nElement is not interactable. Ensure the button is visible and enabled.")
    except Exception as e:
        print(f"\nFailed to navigate to the home page: {e}")

def main():
    try:
        login_to_jiomart()
        parsing_phone_number()
        
        input("\nPlease enter the OTP manually and press Enter here to continue...")

        otp = input("\nEnter the OTP for completing login process: ")
        time.sleep(2)
        enter_otp(otp)
        
        while True:
            print("\nMenu:")
            print("1. Search for a new item")
            print("2. Increment item")
            print("3. Decrement item")
            print("4. Go to Cart page")
            print("5. Go to Profile page")
            print("6. Go to Home page")
            print("7. End")
            choice = input("Enter your choice: ")

            if choice == "1":
                product = input("\nEnter the product that you want to search for: ")
                product_search(product)
                add_to_cart()
            elif choice == "2":
                increment_item()
            elif choice == "3":
                decrement_item()
            elif choice == "4":
                go_to_cart()
            elif choice == "5":
                go_to_profile()
            elif choice == "6":
                go_to_home()
            elif choice =="7":
                print("\nYou have chosen to end searching. The browser will remain open.")
                break
            else:
                print("Invalid choice, please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(10000)

if __name__ == "__main__":
    main()
