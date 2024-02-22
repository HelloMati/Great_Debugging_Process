from playwright.sync_api import Page, expect

def test_form_submission(page, test_web_address):
    
    page.goto(f"http://{test_web_address}")
    
    # Fill and submit the form
    page.fill('input#content', 'This is a test submission')
    page.click('button[type="submit"]')

    # Get all list items
    list_items = page.query_selector_all('h2:has-text("Thoughts of the day...") ~ ul li')

    # Assert that the last list item contains the submitted content
    assert list_items[-1].text_content() == 'This is a test submission'
