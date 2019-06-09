from flask import Flask, render_template
import feedparser
app = Flask(__name__)

@app.route("/")
def home():
    toi = feedparser.parse("https://timesofindia.indiatimes.com/rssfeeds/296589292.cms").entries[:5]
    hindu = feedparser.parse("https://www.thehindu.com/news/international/feeder/default.rss").entries[:5]
    indian_express = feedparser.parse("https://indianexpress.com/section/world/feed/").entries[:5]
    first_post = feedparser.parse("https://www.firstpost.com/rss/world.xml").entries[:5]
    india_today = feedparser.parse("https://www.indiatoday.in/rss/1206577").entries[:5]
    telegraph_india = feedparser.parse("https://www.telegraph.co.uk/rss.xml").entries[:5]
    news_18 = feedparser.parse("https://www.news18.com/rss/world.xml").entries[:5]
    dna = feedparser.parse("https://www.dnaindia.com/feeds/world.xml").entries[:5]
    outlook_india = feedparser.parse("https://www.outlookindia.com/rss/section/20").entries[:5]
    return render_template("index.html",toi=toi,hindu=hindu,indian_express=indian_express,
                           first_post=first_post
                           , india_today=india_today,
                           telegraph_india= telegraph_india ,
                           news_18 = news_18,
                           dna=dna,
                           outlook_india=outlook_india)


@app.route("/recent")
def recent():
    toi = feedparser.parse("https://timesofindia.indiatimes.com/rssfeeds/1221656.cms").entries[:5]
    hindu = feedparser.parse("https://www.thehindu.com/news/international/feeder/default.rss").entries[:5]
    indian_express = feedparser.parse("https://indianexpress.com/section/world/feed/").entries[:5]
    first_post = feedparser.parse("https://www.firstpost.com/rss/world.xml").entries[:5]
    india_today = feedparser.parse("https://www.indiatoday.in/rss/1206577").entries[:5]
    telegraph_india = feedparser.parse("https://www.telegraph.co.uk/rss.xml").entries[:5]
    news_18 = feedparser.parse("https://www.news18.com/rss/world.xml").entries[:5]
    dna = feedparser.parse("https://www.dnaindia.com/feeds/world.xml").entries[:5]
    outlook_india = feedparser.parse("https://www.outlookindia.com/rss/section/20").entries[:5]
    return render_template("recent.html", toi=toi, hindu=hindu, indian_express=indian_express,
                           first_post=first_post
                           , india_today=india_today,
                           telegraph_india=telegraph_india,
                           news_18=news_18,
                           dna=dna,
                           outlook_india=outlook_india)


if __name__ == '__main__':
    app.run(debug=True)