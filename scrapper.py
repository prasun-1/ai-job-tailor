import os
from google import genai 
from playwright.sync_api import sync_playwright 

client=genai.Client()
link=input("enter the weburl")

with sync_playwright() as p:
	browser_type=p.chromium
	browser=browser_type.launch(headless=False)
	page=browser.new_page()
	try:
	 	page.goto(link)
	except Exception as e:
		print(f'broken link {link}')
		print(f'error details:{e}')
		exit()
	ask=input("Whats the divsion of the HTMl upon inspection?")
	try:
		if ask=="data-automation":
			value=input("whats the keyword")
			description = page.locator(f'[data-automation="{value}"]').inner_text()
		elif ask=="class":
			value=input("whats the keyword")
			description = page.locator("." + value).inner_text()
		elif ask=="id":
			value=input("whats the keyword")
			description = page.locator("#" + value).inner_text()
		else:
    			print("invalid option, please type: data-automation, class, or id")
    			exit()
	except Exception as e:
		print(f'error:{e}')
		exit()
def load_resume():
	with open("my_cv.txt","r", encoding="utf-8") as file:
	     cv_text=file.read()
	return cv_text

cv_content=load_resume()

prompt=(f"""you are an highly intellectual HR(irony) who recently added a job description, I would like you to read this {description} and generate me a custom cv, using {cv_content} for this job and also write me a cover letter so that it matches the job description, remember no lying, no over exaggeration, and no emdashes at all, do it in a humanized way.also no commentary, no preamble, just the CV and cover letter
fill in your actual details (add your address to the prompt)
plain text, no markdown symbols
ready to copy paste and send, 
my full name : (#Enter your name) 
email: (Enter your email)
address: (Enter your address)
phone :(Enter your phone number)
""")



def ai_response():
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt, 
        )
    except Exception as e:
        print(f"error:{e}")
        exit() 
    
    
    output_file = "curated.doc"
    
    with open(output_file, "w", encoding="utf-8") as file:  
        file.write(response.text)

   
    os.startfile(output_file)
