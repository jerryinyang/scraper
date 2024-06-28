from playwright.sync_api import sync_playwright
import csv
import time

main_class = "_historyList_zyo9v_30"
each_container_class = "_flex_66fzx_11 _historyItem_zyo9v_64"
question_mark_class = "_historyItem_zyo9v_64 _question_zyo9v_85"
class_container_inner = "_rate_mxw16_1 _low_mxw16_5"
class_number_of_player_x_class_total_seeds = "_amount_1p5ki_26"


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

    # Prepare CSV file
    with open("values.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["X", "Y", "Z"])

        while True:
            # Check if question_mark_class is present
            if page.locator(f".{question_mark_class}").count() > 0:
                print(True)
                # Get the values of class_number_of_player_x_class_total_seeds
                values = page.locator(
                    f".{class_number_of_player_x_class_total_seeds}"
                ).all_inner_texts()
                if len(values) == 2:
                    X, Y = values
                else:
                    continue

                # Wait for question_mark_class to disappear
                while page.locator(f".{main_class} .{question_mark_class}").count() > 0:
                    time.sleep(1)

                # Get the value of class_container_inner
                Z = page.locator(f".{class_container_inner}").inner_text()

                # Write the values to the CSV file
                writer.writerow([X, Y, Z])
                print(f"Stored values: {X}, {Y}, {Z}")

            else:
                time.sleep(0.3)
                continue

            time.sleep(1)  # Adjust the sleep time as necessary

    # Close the browser
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
