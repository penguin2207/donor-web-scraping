#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 21:13:29 2023

@author: jluciano
"""
from googlesearch import search
import requests
from urllib.parse import urlparse
import time

def is_company_website(url, company_name):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace("www.", "").lower()
    return company_name.lower() in domain

def search_website_for_philanthropy(company_name):
    query = f"{company_name} official website"
    for url in search(query, num=3, stop=3, pause=2):
        if is_company_website(url, company_name):
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    if "philanthropy" in response.text.lower() or "corporate social responsibility" in response.text.lower():
                        print(f"{url} valid")
                        return True
                print(f"{url} response not 200")
        
            except requests.RequestException:
                print(f"{url} invalid")
                pass
        else:
            print(f"{url} not company website")
        time.sleep(3)  # Add a delay of 3 seconds between successive searches
    return False

if __name__ == "__main__":
    with open("companies.txt", "r") as file:
        company_names = [line.strip() for line in file]

    for company_name in company_names:
        result = search_website_for_philanthropy(company_name)
        if result:
            print(f"{company_name} engages in philanthropic activity.")
        else:
            print(f"{company_name} does not engage in philanthropic activity or website information not found.")
