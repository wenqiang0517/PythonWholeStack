import urllib.parse
import urllib.request
import ssl

# https://www.screenshotmaster.com/docs

ssl._create_default_https_context = ssl._create_unverified_context

# 参数
token = "6040610640746"
url = urllib.parse.quote_plus("https://www.cnblogs.com/Eva-J/articles/7228075.html")
width = 1280
height = 800
full_page = 1

# 构造URL
query = "https://www.screenshotmaster.com/api/v1/screenshot"
query += "?token=%s&url=%s&width=%d&height=%d&full_page=%s" % (token, url, width, height, full_page)

# 调用API
urllib.request.urlretrieve(query, "./screenshot.png")

