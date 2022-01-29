import smtplib, ssl, requests, json


port = 465
smtp_server = "smtp.gmail.com"
sender_email = "emailbot946@gmail.com"  # Enter your address
receiver_email = "shivansh0708@gmail.com"  # Enter receiver address
password = "$#%&secure!!"  #  Enter password of your email address

message = """"""

url1 = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ff3ad897d91446ddb484113af3c33571"
url2 = "https://newsapi.org/v2/everything?q=tesla&from=2021-12-06&sortBy=publishedAt&apiKey=ff3ad897d91446ddb484113af3c33571"
url3 = "https://newsapi.org/v2/everything?q=apple&from=2022-01-05&to=2022-01-05&sortBy=popularity&apiKey=ff3ad897d91446ddb484113af3c33571"
url4 = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=ff3ad897d91446ddb484113af3c33571"
url5 = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=ff3ad897d91446ddb484113af3c33571"

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








