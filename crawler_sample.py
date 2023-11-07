import requests
from bs4 import BeautifulSoup

# Define the base URL of the faculty directory page
base_url = 'https://www.cs.sjtu.edu.cn/Faculty.aspx'

# Make a request to the faculty directory page
response = requests.get(base_url)

# Parse the page using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
# for item in soup.find_all("a"): 
# 	print(item.get("href")) 
# print(soup)

# Find all the links to faculty members' pages (you would need to adjust the selector)
faculty_links = soup.select('a[class="red"]')
# print(faculty_links)

# Iterate over each link and collect the homepage and image URLs
for link in faculty_links:
    faculty_response = requests.get(link['href'])
    faculty_soup = BeautifulSoup(faculty_response.text, 'html.parser')
    
    # Extract the homepage URL (you would need to adjust the selector)
    homepage_url = faculty_soup.select_one('a[homepage_link_selector]').get('href', '')
    
    # Extract the image URL (you would need to adjust the selector)
    image_url = faculty_soup.select_one('img[faculty_image_selector]').get('src', '')
    
    print(f"Faculty Member: {link.text}")
    print(f"Homepage URL: {homepage_url}")
    print(f"Image URL: {image_url}")
