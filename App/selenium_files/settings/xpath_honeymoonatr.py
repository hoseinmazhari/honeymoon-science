class all_products():
    tbl = "/html/body/div[1]/div[2]/div[4]/div[1]/div[6]/form[1]/table"
    tbody = '//*[@id="the-list"]'
    product_name = '//td[2]/strong/a'
    product = '//td[2]/strong/a'
    published = '/html/body/div[1]/div[2]/div[4]/div[1]/div[6]/ul/li[2]/a'
    # next_p = '/html/body/div[1]/div[2]/div[4]/div[1]/div[6]/form[1]/div[2]/div[3]/span[2]/a[3]'
    next_p = '//*[@id="posts-filter"]/div[2]/div[3]/span[2]/a[1]'
    
    # "https://honeymoonatr.com/wp-admin/edit.php?post_type=product&paged=2"
    # /html/body/div[1]/div[2]/div[4]/div[1]/div[6]/form[1]/div[2]/div[3]/span[2]/a[3]
class product_details():
    update = '//*[@id="publish"]'
    name = '//*[@id="title"]'
    