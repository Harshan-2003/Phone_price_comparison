import streamlit as st
st.set_page_config(page_title="Code Squad",page_icon=':computer:',layout="wide")
st.header("Welcome")
st.write("###")
st.write("---")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
keyword=st.text_input('search')
with st.sidebar:
   rate = st.radio(("select the rate"), ('all','below 10000', 'below 20000', 'below 30000'))
   ram=st.radio(("select the ram"), ('None','2GB ram', '4GB ram', '6GB ram', '8GB ram'))
   storage = st.radio(('select the storage'), ('None','32GB storage', '64GB storage', '128GB storage', '256GB storage'))
if rate=='all':
    rate=''
if ram=='None':
    ram=''
if storage=="None":
    storage=''
keyword=keyword+" "+ram+" "+storage+" "+rate
if st.button("submit"):
   if keyword==" "+ram+" "+storage+" "+rate:
      keyword = "mobiles"+keyword

   options = webdriver.ChromeOptions()
   options.add_argument("--headless")
   driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
   web = 'https://www.amazon.in'
   driver.get(web)

   search_box = driver.find_element(By.ID, "twotabsearchtextbox")
   search_box.send_keys(keyword)
   search_button = driver.find_element(By.ID, "nav-search-submit-button")
   search_button.click()

   items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
   item_image = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//img[contains(@class, "s-image")]')))
   product_namea = []
   product_pricea = []
   product_ratingsa = []
   product_rating_numa = []
   product_linka = []
   product_imagea = []
   for item in items:
      name = item.find_element(By.XPATH,'.//span[@class="a-size-medium a-color-base a-text-normal"]')
      product_namea.append(name.text)
      link = item.find_element(By.XPATH,'.//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
      product_linka.append(link.get_attribute('href'))
      whole_price = item.find_elements(By.XPATH, './/span[@class="a-price-whole"]')
      if whole_price != []:
         price = whole_price[0].text
      else:
         price = 0
      product_pricea.append(price)
      ratings_box = item.find_elements(By.XPATH, './/div[@class="a-row a-size-small"]/span')
      if ratings_box != []:
         ratings = ratings_box[0].get_attribute('aria-label')
         ratings_num = ratings_box[1].get_attribute('aria-label')
      else:
         ratings, ratings_num = 0, 0
      product_ratingsa.append(ratings)
      product_rating_numa.append(str(ratings_num))
   for item in item_image:
      img = item.get_attribute('src')
      product_imagea.append(img)
   driver.implicitly_wait(100)


   web = 'https://www.flipkart.com'
   driver.get(web)
   close_button = driver.find_element(By.XPATH, './/button[@class="_2KpZ6l _2doB4z"]')
   close_button.click()
   search_boxf = driver.find_element(By.XPATH, './/input[@class="_3704LK"]')
   search_boxf.send_keys(keyword)
   search_buttonf = driver.find_element(By.XPATH, './/button[@class="L0Z3Pu"]')
   search_buttonf.click()
   product_namef = []
   product_ratingsf = []
   product_ratings_numf = []
   product_pricef = []
   product_detailsf = []
   product_linkf = []
   product_imagef = []
   itemsf = WebDriverWait(driver, 100).until(
       EC.presence_of_all_elements_located((By.XPATH, './/div[contains(@class,"col col-7-12")]')))
   ratingsf = WebDriverWait(driver, 100).until(
       EC.presence_of_all_elements_located((By.XPATH, './/div[contains(@class,"3LWZlK")]')))
   ratings_namef = WebDriverWait(driver, 100).until(
       EC.presence_of_all_elements_located((By.XPATH, './/span[contains(@class,"_2_R_DZ")]')))
   pricef = WebDriverWait(driver, 100).until(
       EC.presence_of_all_elements_located((By.XPATH, './/div[contains(@class,"_30jeq3 _1_WHN1")]')))
   detailsf = WebDriverWait(driver, 100).until(
       EC.presence_of_all_elements_located((By.XPATH, './/ul[contains(@class,"_1xgFaf")]')))
   linksf = WebDriverWait(driver, 100).until(
       EC.presence_of_all_elements_located((By.XPATH, './/a[contains(@class,"_1fQZEK")]')))
   imagesf = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located(
       (By.XPATH, './/div[contains(@class,"CXW8mj")]/img[contains(@class,"_396cs4 _3exPp9")]')))
   for item in itemsf:
       name = item.find_element(By.XPATH, './/div[@class="_4rR01T"]')
       product_namef.append(name.text)
   for rating in ratingsf:
       product_ratingsf.append(rating.text)
   for rating_num in ratings_namef:
       product_ratings_numf.append(rating_num.text)
   for p in pricef:
       product_pricef.append(p.text)
   for d in detailsf:
       p = d.find_elements(By.XPATH, './/li[@class="rgWa7D"]')
       a = []
       for i in p:
           a.append(i.text)
       product_detailsf.append(a)
   for i in linksf:
       product_linkf.append(i.get_attribute("href"))
   for item in imagesf:
       img = item.get_attribute("src")
       product_imagef.append(img)
   driver.implicitly_wait(100)





   product_name = []
   product_ratings = []
   product_ratings_num = []
   product_price = []
   product_details = []
   product_link = []
   product_image = []
   for i in range(min(len(product_rating_numa),len(product_ratings_numf))):
       product_name.append(product_namea[i])
       product_name.append(product_namef[i])
       product_price.append(product_pricea[i])
       product_price.append(product_pricef[i])
       product_ratings.append(product_ratingsa[i])
       product_ratings.append(product_ratingsf[i])
       #product_details.append(product_detailsa[i])
       #product_details.append(product_detailsf[i])
       product_ratings_num.append(product_rating_numa[i])
       product_ratings_num.append(product_ratings_numf[i])
       product_image.append(product_imagea[i])
       product_image.append(product_imagef[i])
       product_link.append(product_linka[i])
       product_link.append(product_linkf[i])
   for i in range(len(product_name)):
         co1, co2 = st.columns((2, 1))
         #price1=int((product_price[i]).strip(","))
         s=""
         s2=""
         if(i%2==0):
            ram2=product_name[i].split(",")
            for j in range(len(ram2)):
               if "GB" in ram2[j] and "Apple" not in ram2[j]:
                  c=0
                  s=""
                  for k in ram2[j]:
                     if (k.isdigit()):
                        s += k
                        continue
                     #break
                  if int(s)<17:
                     break
            for j in range(len(ram2)):
               if "GB" in ram2[j] and ("Storage" in ram2[j] or "ROM" in ram2[j]):
                  s2=""
                  for k in ram2[j]:
                     if k.isdigit():
                        s2+=k
                        continue
                     if (k==" " or k=="|" or k==",") and s2!="":
                        break
                  #if int(s2)>16:
                     #break
         if i%2==1:
            ram2=product_detailsf[(i//2)][0].split("|")
            s=""
            s2=""
            for j in ram2:
               if "RAM" in j:
                  for k in j:
                     if k.isdigit():
                        s+=k
               if "ROM" in j:
                  for k in j:
                     if k.isdigit():
                        s2+=k

         #st.write(s)
         #ram1=int(s)
         #rom1=int(s2)


         with st.container():
               with co1:
                  a = product_link[i]
                  b=product_name[i]
                  st.write("[{}]({})".format(b,a))
                  st.write("Price: ", product_price[i])
                  st.write("Rating: ", product_ratings[i])
                  st.write("No. of ratings: ", product_ratings_num[i])
                  if i%2==0:
                      st.write("from amazon")
                  else:
                      st.write("from flipkart")
                  #st.write("[Learn more->]({})".format(a))
                  #st.write("---aeearyaehte>"+s+s2)
                  #st.write(product_detailsf[i])
                  #st.write(ram2)
               with co2:
                  st.image("{}".format(product_image[i]), width=170)








