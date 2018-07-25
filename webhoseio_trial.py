import webhoseio
from collections import OrderedDict
import csv

webhoseio.config(token="9f717e05-85b3-4fe1-86cf-60cf38882487")
query_params = {
"q": "text:\"Amazon\" language:english",
# "ts": "1529953938965",
"sort": "crawled"
}
output=OrderedDict()
output = webhoseio.query("filterWebContent", query_params)
pagecount=0
# print(type(output))
# print output['posts'][0]['text'] # Print the text of the first post
# print output['posts'][0]['published'] # Print the text of the first post publication date
with open("output.csv","w",newline='') as f:
    cw = csv.writer(f)
    while pagecount<101:
        for k,v in output.items():
            if k=='next':
                output = webhoseio.get_next()
                print('>>>>>>>>>>>>>>>>>>>>>>>>100 done')
                pagecount=0
                break
            if k=='posts':
                for res in v:
                    result=[]
                    uuid,url,site_full,site_section,section_title,title,published,site_type,country,domain_rank,author,text=("" for i in range(12))
                    pagecount+=1
                    print(pagecount)
                    for l,m in res.items():
                        if l=='thread':
                            for key,value in m.items():
                                if key=='uuid':
                                    uuid=value
                                if key=='url':
                                    url=value
                                if key=='site_full':
                                    site_full=value
                                if key=='site_section':
                                    site_section=value
                                if key=='section_title':
                                    section_title=value
                                if key=='title':
                                    title=value
                                if key=='published':
                                    published=value
                                if key=='site_type':
                                    site_type=value
                                if key=='country':
                                    country=value
                                if key=='domain_rank':
                                    domain_rank=value
                        if l=='author':
                            author=m
                        if l=='text':
                            text=m

                    result=[uuid,url,site_full,site_section,section_title,title,published,site_type,country,domain_rank,author,text]
                    cw.writerow(result)
                    f.flush()




# Get the next batch of posts

# output = webhoseio.get_next()


# Print the site of the first post

# print output['posts'][0]['thread']['site']