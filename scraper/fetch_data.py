from playwright.sync_api import sync_playwright

main_class = "_historyList_zyo9v_30"  # Main container for each_container_class, question_mark_class, class_container_inner

each_container_class = (
    "_flex_66fzx_11 _historyItem_zyo9v_64"  # Contains class_container_inner
)

question_mark_class = "_historyItem_zyo9v_64 _question_zyo9v_85"  # Shows up temporarily; contains a '?' and a svg element

class_container_inner = "_rate_mxw16_1 _low_mxw16_5"  # Contains the actual value

class_number_of_player_x_class_total_seeds = "_amount_1p5ki_26"  # There are two elements in total with this class. When question_mark_class shows up, store these values

# LOGIC:
# - When `question_mark_class` shows up (it becomes the first element within `_historyList_zyo9v_30`), store the values in `class_number_of_player_x_class_total_seeds` as a tuple (two numbers : X, Y)
# - When `question_mark_class` goes away (it is no longer the first element), get the content of class_container_inner (one number, Z) .
# - Store the values [X, Y, Z] in a csv file


def run(playwright):
    # Create a new browser
    browser = playwright.chromium.launch(headless=False)

    # Create a new browser tab
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    page = context.new_page()

    # Go to the website
    page.goto("https://1wecob.top/casino/play/1play_1play_fastcrash")

    # TODO: Implement the logic here

    # Close the browser
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
