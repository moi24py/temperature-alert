import smtplib
from email.message import EmailMessage
from datetime import date
from jinja2 import Environment, FileSystemLoader

def make_body(temps:list, hours:list, user_t:float, unit:str, criteria:str):
    """
    Create the body of the email.
    """
    environment = Environment()
    environment = Environment(loader=FileSystemLoader("project/templates/"))
    results_template = environment.get_template("message.html")
    qty = len(temps)
    context = {
        "temps": temps,
        "hours": hours,
        "unit": unit,
        "criteria": criteria,
        "user_t": user_t,
        "qty": qty
    }
    return results_template.render(context)

def send_email(city:str, temps:list, hours: list, user_t:float, unit:str, criteria:str):
    """
    Send emails to the recipients.
    """
    today = date.today()
    day = today.strftime("%d.%m.%Y")

    # e.g. myemail@gmail.com
    sender = ""

    # e.g. 'contact1@yahoo.com'
    recipient = ""

    # 'Name Surname'
    msg['From'] = ""
  
    # Google Account generated App password
    password = ""

    msg = EmailMessage()
    msg['Subject'] = f"{city.capitalize()} today's temperatures"
    
    # plain text message, if recipient/s disallowed HTML emails
    txt_temps = ""
    for t in temps:
        txt_temps += str(t) + "\n"
    msg.set_content(f"{txt_temps}")

    # HTML message
    msg.add_alternative(make_body(temps, hours, user_t,unit,criteria), subtype = 'html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender, recipients, msg.as_string())

if __name__ == "__main__":
    make_body()
    send_email()
