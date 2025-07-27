from prompt_functions import prompt_ai,add_history,prompt_ai_2
from check_holidays import check_holiday
from weather import forecast_7days
from image_generation import generate_image
from email_functions import send_mail_html

system_prompt='''
You are a helpful assistant that is creative. Ensure to maintain an OPEN, FRIENDLY, UPBEAT tone. Do not provide any extra texts beyond the json. Using the data that user gives, return a json with the following format:

{
  "subject": A short, positive, upbeat greeting email subject,
  "fact": An interesting fact that happened on today in a different year, relevant to everyday life - specify the full date,
  "precaution": A short, generic and relevant tip based strictly on the user's weather input. The tip must be logical, specific to the weather, and not contradict the weather. Example- Do not advice to use sunscreen on rainy or overcast days, tip on something more relevant. Do not give hydration reminders. (limit to 10 words),
  "week_summary": A short, fun witty and engaging summary of the week's upcoming weather, using the descriptions shared by the user(limit to 15 words),
  "holiday_name": The holiday name if specified, otherwise None,
  "holiday_fact": An India-related fact about the holiday, or None,
  "holiday_image_prompt": A descriptive and detailed prompt to generate a creative image for the holiday in a modern art style, specify that there should not be any text in the image, or None
}

Rules:
Use None for holiday_name, holiday_fact, and holiday_image_description if holiday is not provided.
Do not provide any extra texts beyond the json asked. Provide json as plain text and do not use extra quotes.
Do not use any formatting, only plain text. No code blocks.
'''
lat=17.08784
lon=80.27847

def get_response():
    weather_data=forecast_7days(lat,lon)
    # holiday_data=check_holiday()
    holiday_data={
        "is_holiday":True,
        "holiday name":"Independence Day",
        "date":"2025-08-15"
    }
    user_prompt=f'''
    Weather info - {weather_data}
    Holiday info - {holiday_data}'''
    
    his=add_history('user',system_prompt)
    response= prompt_ai(user_prompt,his)
    return format_response(response)

def format_response(response):
    if "null" in response:
        response=response.replace("null","None")
    if "```" in response:
        response=response[3:-3]
    if response[:4].lower() == "json":
        response=response[4:]
    return eval(response)

def get_image_prompt(response):
    return response.get("holiday_image_prompt")

def get_image(response):
    prompt = response.get("holiday_image_prompt")
    if prompt is not None:
      generate_image(prompt)
    return prompt

def build_email(response):
    parts = []
    
    subject = response["subject"]
    fact = response["fact"]
    precaution = response["precaution"]
    week_summary = response["week_summary"]
    parts.append(f"""\
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                <h2 style="color: #333;">🌞 Rise and Shining!</h2>
                <p style="font-size: 16px;">"""+subject+"""</p>""")

    if response['holiday_name']:
        hol_name=response["holiday_name"]
        hol_info=response["holiday_fact"]
        parts.append("""<h3 style="color: #0056b3;">🎉 Upcoming Holiday: """+hol_name+"""</h3>
                <p>"""+hol_info+"""</p>""")
    parts.append("""
                <h3 style="color: #0056b3;">🌟 Fact of the Day</h3>
                <p>"""+fact+"""</p>

                <h3 style="color: #0056b3;">☂️ Weather Precaution</h3>
                <p>"""+precaution+"""</p>

                <h3 style="color: #0056b3;">📅 Weekly Summary</h3>
                <p>"""+week_summary+"""</p>

                <hr style="margin-top: 30px;"/>
                <p style="font-size: 14px; color: #888;">Stay informed and inspired – have a wonderful day!</p>
                <p style="font-size: 14px; color: #888;">- Mort E Mail</p>
            </div>
        </body>
        </html>
    """)

    return "".join(parts)


response = get_response()
email_content=build_email(response)
print(email_content)

send_mail_html("Mort E Mail greets you :D",email_content,"abdullahmctm@gmail.com")