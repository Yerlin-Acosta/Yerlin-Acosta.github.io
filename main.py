import webbrowser
import time
import os

url = input("Enter URL: ")
duration = int(input("Enter Duration (in seconds): "))
times = int(input("How many times would you like to open the URL?: "))

total_views = 0  # To track total views added

# Loop through the number of times and close 5 tabs after every 10 are opened
for i in range(times):
    webbrowser.open_new(url)
    total_views += 1  # Increment total views each time a tab is opened
    time.sleep(duration)

    # Every time 10 tabs are opened, close 5
    if (i + 1) % 10 == 0:
        print(f"Opened {total_views} tabs. Now closing 5...")
        for _ in range(5):
            os.system("taskkill /IM chrome.exe /F")  # Adjust the process name if needed
        print(f"Added {total_views} views so far.")

print(f"Final total views added: {total_views}")