from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def get_results(url, results=[], max_attempts=20):

    w = webdriver.Chrome()
    w.get(url)
    w.maximize_window()

    for _ in range(max_attempts):
        sleep(15)
        teams = w.find_element_by_class_name('sph-EventHeader_Label').text
        try:
            change_res_buttons = w.find_elements_by_class_name(
                "mcs-SelectorButton_Icon")
            actions = ActionChains(w)
            actions.move_to_element(change_res_buttons[1]).perform()
        except IndexError as e:
            print(e)
            continue
        break

    try:
        acc_cookies_but = w.find_element_by_class_name(
            "ccm-CookieConsentPopup_Accept ")
        acc_cookies_but.click()
    except:
        pass

    odds = []

    for res in results:

        match_result = res.split('-')
        home_goals = int(match_result[0])
        away_goals = int(match_result[1])

        for _ in range(home_goals):
            change_res_buttons[1].click()
        for _ in range(away_goals):
            change_res_buttons[3].click()

        r = w.find_element_by_class_name("mcs-ScoreParticipant_Odds")
        print(res, ':', r.text)
        odds.append(float(r.text))

        reset_result(home_goals, away_goals, change_res_buttons)

    return odds, teams.split(' v ')


def reset_result(last_home_goals, last_away_goals, change_res_buttons):
    for _ in range(last_home_goals):
        change_res_buttons[0].click()
    for _ in range(last_away_goals):
        change_res_buttons[2].click()


# if __name__ == '__main__':
#     get_results(
#         'https://www.bet365.bet.ar/?affiliate=365_01133755&bet=1#/AC/B1/C1/D8/E120212133/F3/', ['1-2'])
