#!/usr/bin/env python
import requests
from lxml import html
from defaults import target_url
import hashlib
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import sendgrid_helper


def tell_matt(ridley_present):
    if ridley_present:
        sendgrid_helper.send_mail("Ridley report found!")
        print("Ridley report found!")
    else:
        sendgrid_helper.send_mail("No Ridley report found")
        print("No Ridley report found")


def main():
    response = requests.get(target_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    block_content = soup.find("div", {"id": "block-cofe-content"})
    article = block_content.article
    reports_div = article.find_all("div")[16].div.div
    reports_2019 = reports_div.ul.find_all("li")
    for report in reports_2019:
        title = report.text
        institution_name = title.split("-")[0].rstrip()
        print(institution_name)
        if "Ridley" in institution_name:
            tell_matt(True)
            return True

    tell_matt(False)


if __name__ == "__main__":
    main()
