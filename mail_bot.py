import smtplib, ssl, requests, json


port = 465
smtp_server = "smtp.gmail.com"
sender_email = "enter here"  # Enter your address
receiver_email = "enter here"  # Enter receiver address
password = "enter here"  #  Enter password of your email address

message = """"""

url1 = "enter api url from newsapi.org"
url2 = "enter api url from newsapi.org"
url3 = "enter api url from newsapi.org"
url4 = "enter api url from newsapi.org"
url5 = "enter api url from newsapi.org"

urls = [url1, url2, url3, url4, url5]

i = 0

# news = requests.get(url).text
# news_dict = json.loads(news)
# arts = news_dict['articles']
# for article in arts:
#     message += f"{article['title']} \n"
# message = message.encode("ascii","ignore")
# # print(message)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    for url in urls:
        news = requests.get(url).text
        news_dict = json.loads(news)
        arts = news_dict['articles']
        for article in arts:
            message += f"{article['title']} \n"
        message = message.encode("ascii", "ignore")
        server.sendmail(sender_email, receiver_email, message)
        message = """"""
        i+=1
        print(f"DONE - {i}")
        if i == len(urls):
            print("Completed!!!")








