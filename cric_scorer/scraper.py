import requests
from bs4 import BeautifulSoup
import re

def scrap():
    URL = "https://www.cricbuzz.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="match_menu_container")
    scrap_results = results.find_all("li", class_="cb-match-card")
    return scrap_results

def get_live_matches():
    details = scrap()
    live_match = {}
    for detail in details:
        live_team_details = {}
        summary = match_summary(detail)
        if summary is not None:
            match_header_text = match_header(detail).text
            teams = teams_name(detail)
            score_card = team_score(detail)
            live_team_details['summary'] = summary.text
            live_team_details['match_header'] = match_header_text
            live_team_details['score_card'] = score_card[0] + " :: " + score_card[1]
            match_anchor = detail.find("a", class_="cb-match-card-link")
            if match_anchor:
                match_url = match_anchor['href']
                live_team_details['scoreboard'] = get_individual_match_scoreboard(match_url)
            live_match[teams[0] + " vs " + teams[1]] = live_team_details
    return live_match

def match_summary(detail):
    return detail.find("div", class_="cb-mtch-crd-state")

def match_header(detail):
    return detail.find("div", class_="cb-mtch-crd-hdr")

def teams_name(detail):
    l = []
    team1_details = detail.find("div", class_="cb-hmscg-bat-txt").text
    team1_index = re.search(r"\d", team1_details).start() if re.search(r"\d", team1_details) else len(team1_details)
    team2_details = detail.find("div", class_="cb-hmscg-bwl-txt").text
    team2_index = re.search(r"\d", team2_details).start() if re.search(r"\d", team2_details) else len(team2_details)
    l.append(team1_details[:team1_index])
    l.append(team2_details[:team2_index])
    return l

def team_score(detail):
    l = []
    team1_details = detail.find("div", class_="cb-hmscg-bat-txt").text
    team2_details = detail.find("div", class_="cb-hmscg-bwl-txt").text
    l.append(team1_details)
    l.append(team2_details)
    return l

def get_individual_match_scoreboard(url):
    match_url = "https://www.cricbuzz.com" + url
    page = requests.get(match_url)
    soup = BeautifulSoup(page.content, "html.parser")
    scoreboard = soup.find_all("div", class_="cb-col cb-col-100 cb-ltst-wgt-hdr")
    score_details = []
    for score in scoreboard:
        score_details.append(score.text.strip())
    return "\n\n".join(score_details)