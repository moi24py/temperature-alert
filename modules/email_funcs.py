import smtplib
from email.message import EmailMessage
from datetime import date
from jinja2 import Environment, FileSystemLoader


def make_body(temps:list[str], user_temp:float, unit:str, criteria:str) -> str:
    """
    Creates the email body.

    Parameters
    ----------
    temps : list[str]
        A list of strings representing the matching temperatures and hours
    user_temp : float
        A float representing the temperature entered by the user
    unit : str
        The string that represents the temperature unit ('c'/'f')
    criteria : str
        A string representing the criteria ('below'/'above') entered by the user

    Returns
    -------
    string
        The template as a string

    """
    environment = Environment()
    environment = Environment(loader=FileSystemLoader("project/templates/"))
    results_template = environment.get_template("message.html")
    qty = len(temps)
    context = {
        "temps": temps,
        "unit": unit,
        "criteria": criteria,
        "user_t": user_temp,
        "qty": qty
    }
    return results_template.render(context)

def send_email(city:str, temps:list[str], user_temp:float, unit:str, criteria:str):
    """
    Sends emails to the recipients.

    Parameters
    ----------
    city: str
        The city enedeted by the user and found it the database
    temps : list[str]
        A list of strings representing the matching temperatures and hours
    user_temp : float
        A float representing the temperature entered by the user
    unit : str
        The string that represents the temperature unit ('c'/'f')
    criteria : str
        A string representing the criteria ('below'/'above') entered by the user

    """
    today = date.today()
    day = today.strftime("%d.%m.%Y")

    # myemail@gmail.com
    sender = ""

    # e.g. ["contact1@yahoo.com", "contact2@gmail.com"]
    contacts = []

    recipients = ', '.join(contacts)

    msg = EmailMessage()
    msg['To'] = recipients
    msg['Subject'] = f"{city} {day} alert"
    
    # my name
    msg['From'] = ""
    # App password generated via Google Account
    password = ""

    msg.set_content(
    f"""\
    Hello there!
    \n
    Here are the temperatures {criteria} {user_temp}°{unit.upper()}:
    {temps}
    \n
    Have a nice day.

    ----------------
    Github: @moi24py
    """)

    # HTML message
    msg.add_alternative(make_body(temps, user_temp, unit, criteria), subtype = 'html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender,password)
        smtp.send_message(msg)


if __name__ == "__main__":
    make_body([9.8,10.4,15.8,19.7,23.4], ["10:00","11:00","12:00","13:00","14:00", 15.0,'c','above'])
    send_email("Dublin",[9.8,10.4,15.8,19.7,23.4], ["10:00","11:00","12:00","13:00","14:00", 15.0,'c','above'])
