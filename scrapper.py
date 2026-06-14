import os
from playwright.sync_api import sync_playwright 


with sync_playwright() as p:
	chromium=p.chromium
	browser=chromium.launch(headless=False)
	page=browser.new_page()
	page.goto("https://au.jora.com/job/Technical-Support-Specialist-0bc123b13c3f3e6bca1bb588b8c90e8d?abstract_type=extended_llm&disallow=true&fsv=false&sl=Sydney+NSW&sol_key=c76b590d58c3f00a04fcb53ca2af6e30&sp=serp&sponsored=false&sq=Junior+Helpdesk&sr=2&tk=Z3gvGwyqhXa7UDMOSwAz-O9xUgWRR_xbEyWDVeK0F&trigger_source=serp")
	description=page.locator("#job-description-container").inner_text()
	print(description)
	