def get_Page_list(url):
    url_list=[]
    for page in range(44,101):
        url_list.append(url+str(page)+'/')
    return url_list