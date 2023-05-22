from bs4 import BeautifulSoup

html_code = '<span data-v-bd539a1a="" aria-label="LuvFlakkedCheeks" class="summoner-name hint--top">LuvFlakkedCheeks</span>'
soup = BeautifulSoup(html_code, "html.parser")

span_element = soup.find("span", class_="summoner-name")
if span_element:
    summoner_name = span_element["aria-label"]
    if summoner_name and "unranked" not in summoner_name.lower():
        print("Summoner Name:", summoner_name)
    else:
        print("Skipping unranked account")
else:
    print("No summoner name found in the HTML code.")