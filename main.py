#!/usr/bin/env python
import requests
from defaults import target_url
from bs4 import BeautifulSoup
import sendgrid_helper


def tell_matt(ridley_present):
    if ridley_present:
        sendgrid_helper.send_mail("Ridley report found!")
        print("Ridley report found!")
        return True
    else:
        sendgrid_helper.send_mail("No Ridley report found")
        print("No Ridley report found")
        return False


def handler(event, context):
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
            return_bool = tell_matt(True)

    return_bool = tell_matt(False)
    return return_bool


if __name__ == "__main__":
    handler(None, None)
