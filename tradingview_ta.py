# Tradingview Technical Analysis Scraper
# Author: deathlyface (https://github.com/deathlyface)
# Licence: MIT

from selenium import webdriver
from time import sleep

# YOU MAY CHANGE THIS #
delay = 0.1
driver = None
# END OF VARIABLE DECLARATION #

def set_driver(str_driver):
    """ set_driver Function

    This function will set the webdriver.

    Default webdriver:
    If you have not use this set_driver function, the following webdriver will be used:
        chrome (Chrome webdriver is needed, https://sites.google.com/a/chromium.org/chromedriver/home).

    Webdriver available:
        chrome
        edge
        firefox
        safari
        
        Please see Selenium's documentation for more details.
        https://www.selenium.dev/selenium/docs/api/py/#drivers

    Parameters:
        str_driver (string): Webdriver name, not case-sensitive (ex: chrome).

    Returns:
        boolean: True if success, False if fail.
        
    """
    #Globalize
    global driver
    
    #Quit the previous driver, if opened
    if driver != None:
        driver.quit()

    #Case fix
    str_driver = str_driver.lower()

    #Set webdriver
    if str_driver == "chrome":
        driver = webdriver.Chrome()
        return True
    elif str_driver == "edge":
        driver = webdriver.Edge()
        return True
    elif str_driver == "firefox":
        driver = webdriver.Firefox()
        return True
    elif str_driver == "safari":
        driver = webdriver.Safari()
        return True
    else:
        return False

def get_analysis(pair, interval):
    """ get_analysis Function

    This function will return a list containing recommendation (buy/sell) and counters (number of analysis of buy, neutral, and sell).
    This function will scrape TradingView's website, as they do not offer API.
    
    Parameters:
        pair (string): Pair name, not case-sensitive (ex: XLMBTC)
        interval (string): Interval rate, not case-sensitive (ex: 1m for 1 minute)

    Returns:
        list: Recommendation and counters, format: ["Buy/Sell", buy_count, neutral_count, sell_count](ex: ["Buy", 3, 8, 17])
    """
    #Driver check
    if driver == None:
        set_driver("chrome")
    
    #Declare variables
    analysis = []

    #Case fix
    pair = pair.upper()
    interval = interval.lower()

    #Open tradingview's site
    driver.get("https://s.tradingview.com/embed-widget/technical-analysis/?locale=en#%7B%22interval%22%3A%22{}%22%2C%22width%22%3A%22100%25%22%2C%22isTransparent%22%3Afalse%2C%22height%22%3A%22100%25%22%2C%22symbol%22%3A%22{}%22%2C%22showIntervalTabs%22%3Atrue%2C%22colorTheme%22%3A%22dark%22%2C%22utm_medium%22%3A%22widget_new%22%2C%22utm_campaign%22%3A%22technical-analysis%22%7D".format(interval, pair))

    #Wait for site to load
    while len(driver.find_elements_by_class_name("speedometerSignal-pyzN--tL")) == 0:
        sleep(delay)

    #Recommendation
    recommendation_element = driver.find_element_by_class_name("speedometerSignal-pyzN--tL")
    analysis.append(recommendation_element.get_attribute('innerHTML'))

    #Counters
    counter_elements = driver.find_elements_by_class_name("counterNumber-3l14ys0C")

    #Sell
    analysis.append(int(counter_elements[0].get_attribute('innerHTML')))

    #Neutral
    analysis.append(int(counter_elements[1].get_attribute('innerHTML')))
    
    #Buy
    analysis.append(int(counter_elements[2].get_attribute('innerHTML')))
    
    driver.quit()

    return analysis

if __name__ == "__main__":
    set_driver("chrome")
    analysis = get_analysis("btcusdt", "1m")
    print("Recommendation: {}".format(analysis[0]))
    print("Sell: {}".format(analysis[1]))
    print("Neutral: {}".format(analysis[2]))
    print("Buy: {}".format(analysis[3]))
