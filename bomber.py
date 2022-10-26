from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from toastify import notify
from art import tprint


def send_wa_msg(phone_number, text, count):
    
    driver = webdriver.Chrome(
        executable_path = 'D:\Development\Projects\Python\Whatsapp_bomber\chromedriver.exe'
    )
    
    try:
        driver.get(url='http://web.whatsapp.com/')
        sleep(15)
        
        driver.get(url=f'http://web.whatsapp.com/send?phone={phone_number}')
        notify("SCAN THE QR CODE, PLEASE!!!")
        print("SCAN THE QR!!!")
        # sleep(10)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
        text_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        
        for i in range(count):
            text_box.send_keys(text)
            text_box.send_keys('\n')
        
        print(f'The message was sent #{count} times.')
        sleep(5)
        
    except Exception as _ex:
        print(_ex)
        
    finally:
        driver.close()
        driver.quit()
        
        return "Work done! Have a good day!"

def main():
    tprint('WA - BOMBER', font='block')
    phone_number = int(input('Phone number: '))
    text = input('Message text: ')
    count = int(input('Count: '))

    send_wa_msg(phone_number=phone_number, text=text, count=count)
    
if __name__ == '__main__':
    main()