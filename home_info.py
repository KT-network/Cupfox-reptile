'''
获取网站首页的轮播图，推荐视频信息
'''

import requests as req
from bs4 import BeautifulSoup

base_url = "https://www.cbportal.org"

res_html = req.get(base_url).text

analysis_html = BeautifulSoup(res_html, "html.parser")

# 获取轮播图
for_pic_parent = (analysis_html.find(class_="head flex")
                  .find(class_='banner').find(class_="swiper-wrapper")
                  .find_all(class_="swiper-slide Lazy br"))
# print(for_pic_parent)
for pic in for_pic_parent:
    print("图片跳转链接：", base_url + pic.a.get("href"))
    print("图片地址：", base_url + pic.a.get("style").split("url(")[1].split(")")[0])
    print("\n\n")

# 获取分类推荐
movie_div_parent_classify = analysis_html.find_all("div", {'id': lambda x: x and x.startswith('listId')})

for classify in movie_div_parent_classify:

    # 分类标题
    movie_div_parent_title = classify.find(class_="movie-list-header").find(class_='movie-list-title').text
    print(movie_div_parent_title)
    # 分类下的推荐列表
    movie_div_parent_list = classify.find(class_="movie-list-body flex")
    for item in movie_div_parent_list.find_all(class_="movie-list-item"):
        print("链接：", base_url + item.a.get("href"))
        print("图片：", item.a.find(class_="movie-post-lazyload Lazy br").get("data-original"))
        print("标题：", item.a.find(class_="movie-info").find(class_="movie-title txtHide").text)
        print("评分：", item.a.find(class_="movie-info").find(class_="movie-rating cor4").text)
        print("\n")

    print("=====================分割线==========================\n")
