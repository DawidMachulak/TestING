import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(params=["chromium", "firefox", "webkit"], scope="function")
def browser_page(request):
    browser_name = request.param
    with sync_playwright() as p:
        
        browser = getattr(p, browser_name).launch(headless=True)
        page = browser.new_page()

        yield page  

        browser.close()

def test_ing_analytic_cookies_acceptance(browser_page):

    page = browser_page
# 1. Wejdź na stronę ing.pl
    try:

        page.goto("https://www.ing.pl/", wait_until="networkidle")
        page.wait_for_selector(".cookie-policy-content")

# 2. W menu wyboru ciasteczek wybierz "Dostosuj"
        page.get_by_role("button", name="Dostosuj").click()
    
    except Exception as e:
        assert False, f"Wystąpił błąd podczas szukania przycisku 'Dostosuj': {e}"

# 3. Wyraź zgodę na cookie analityczne
    try:
        switch_dict = {
            "technical": "CpmTechnicalOption",
            "analytical": "CpmAnalyticalOption",
            "marketing": "CpmMarketingOption"
        }

        for switch_type, locator in switch_dict.items():
            switch = page.locator(f'[name="{locator}"]')
            match switch_type:
                case "analytical":
                    if switch.get_attribute("aria-checked") == "false":
                        switch.click()
                    expect(switch).to_have_attribute("aria-checked", "true")

                case "marketing":
                    if switch.get_attribute("aria-checked") == "true":
                        switch.click()
                    expect(switch).to_have_attribute("aria-checked", "false")

                case "technical":
                    expect(switch).to_have_attribute("aria-checked", "true")
                    expect(switch).to_have_attribute("aria-disabled", "true")

    except Exception as e:
        assert False, f"Wystąpił błąd podczas ustawiania preferencji cookies: {e}"

# 4. Kliknij "Zaakceptuj wybrane"
    page.locator('.js-cookie-policy-settings-decline-button').click()
    expect(page.locator("cpm-wrapper")).not_to_be_visible()

# # 5. Zweryfikuj, że odpowiednie ciasteczka zostały zapisane w pamięci przeglądarki

    cookies = page.context.cookies()
    cookie = next((c for c in cookies if c['name'] == 'cookiePolicyGDPR'), None)

    assert cookie is not None, "Nie znaleziono ciasteczka cookiePolicyGDPR"
    assert cookie['value'] == '3', f"Spodziewana wartość 3, otrzymano: {cookie['value']}"