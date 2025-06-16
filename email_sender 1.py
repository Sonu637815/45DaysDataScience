import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()

    ##receiver email
    receiver_mail = input("Enter the receiver email :")

    ##email credentials
    sender_email ="shersiyasonu28@gmail.com"
    password = "ftox cecz ictw dchk"


    #login 
    server.login(sender_email,password)

    #sending email
    subject = input("Enter the subject :")
    body = input("Enter the body :")
    message = f"subject : {subject} \n\n {body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("mail sent successfully")

    server.quit()

except Exception as e:
    print("An Error occured",e)
