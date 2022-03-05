import requests
from bs4 import BeautifulSoup
#THIS MODULE IS NOT IMPLEMENTED
#Page URL. 
page_url='https://en.wikipedia.org/wiki/Main_Page'

file_extension=".mp4"


def get_required_link(page_url,file_extension):
    #response object
    r=requests.get(page_url)

    #beautifulsoup object
    soup=BeautifulSoup(r.content,'html5lib')

    #Find links on web-page
    links=soup.findAll('a')

    #links with required file_extension
    file_links=[]
    for link in links:
        try:
            if link["href"].endswith(file_extension):
                file_links.append(page_url+link["href"])
        except:
            pass

    #file_links=[page_url+link["href"] for link in links if link["href"].endswith(file_extension)]

    return file_links

def download_file(file_link,file_name):
    print( "Downloading file:%s"%file_name)  
          
    # create response object  
    r = requests.get(file_link,allow_redirects=True)  
          
    # download started  
    with open(file_name, 'wb') as f:  
    #     for chunk in r.iter_content(chunk_size = 1024):  
    #         if chunk:  
    #             f.write(chunk)
    # print(f"File {file_name} downloaded")
        f.write(r.content)
        f.close()

file_links=get_required_link(page_url,".jpg")
download_file("https://www.facebook.com/favicon.ico",'temp.jpg')
    
