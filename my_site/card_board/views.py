from email.policy import default
from django.shortcuts import render
from itertools import count
import requests
from lxml import etree
from card_board.models import Cardinfo
from django.core.paginator import Paginator
from card_board.models import  Kobecardinfo
from card_board.models import  Jamescardinfo
from card_board.models import  Jordanscardinfo
from .form import Rform
# Create your views here.

def scaler(url,x):
    resp = requests.get(url,allow_redirects=False)
    html = etree.HTML(resp.text)
  
    if x == 1:
        picturesrc = html.xpath("//*[@id='ListViewInner']//li//div//div//a//img/@src")
        #picturesrc = html.xpath("//*[@id='srp-river-main']//div[2]//ul//li//div//div[1]//div//a//div//img/@src")      
        oldlink = html.xpath("//*[@id='ListViewInner']//li//h3//a/@href")
        name = html.xpath("//*[@id='ListViewInner']//li/h3/a/text()")
        enddate = html.xpath("//*[@id='ListViewInner']//li//ul//li[1]//span//span/text()")
        price = html.xpath("//*[@id='ListViewInner']//li//ul[1]//li[1]//span/text()")
        
        for a,b,c,d,e in zip(picturesrc,name,enddate,price,oldlink):
            
            strbb = str(b)
            strbb = strbb.replace('Click this link to access ','') 
            strpic1 = str(a)
            strpic1 = strpic.replace('l225','l1600') 
            # print(strbb)
            cardinfo1 = Cardinfo(picture = strpic1,name = strbb,enddata = c,price = d,oldlink = e)
            listcard = list(Cardinfo.objects.all().filter(name__exact = strbb))
            if listcard == []:
                cardinfo1.save()

    elif x == 2:
        picturesrc = html.xpath("//*[@id='ListViewInner']//li//div//div//a//img/@src")
        #picturesrc = html.xpath("//*[@id='srp-river-main']//div[2]//ul//li//div//div[1]//div//a//div//img/@src")      
        oldlink = html.xpath("//*[@id='ListViewInner']//li//h3//a/@href")
        name = html.xpath("//*[@id='ListViewInner']//li/h3/a/@title")
        enddate = html.xpath("//*[@id='ListViewInner']//li//ul//li[1]//span//span/text()")
        price = html.xpath("//*[@id='ListViewInner']//li//ul[1]//li[1]//span/text()")

        for a,b,c,d,e in zip(picturesrc,name,enddate,price,oldlink):
            strb = str(b)
            strb = strb.replace('Click this link to access ','') 
            strpic = str(a)
            strpic = strpic.replace('l225','l1600') 
            cardinfo2 = Kobecardinfo(picture = strpic,name = strb,enddata = c,price = d,oldlink = e)
            listcard2 = list(Kobecardinfo.objects.all().filter(name__exact = strb))
            if listcard2 == []:
                cardinfo2.save()
    
    elif x == 3:
        Jamescardinfo.objects.all().delete()
        picturesrc = html.xpath("//*[@id='ListViewInner']//li//div//div//a//img/@src") 
        oldlink = html.xpath("//*[@id='ListViewInner']//li//h3//a/@href")
        name = html.xpath("//*[@id='ListViewInner']//li/h3/a/@title")
        #name = html.xpath("/html/body/div[5]/div[2]/div[1]/div[1]/div/div[1]/div/div[3]/div/div[1]/div/w-root/div/div/ul/li[1]/h3/a/@title")
        #//*[@id="item492064cd3b"]/h3/a
        #//*[@id="item492065e89e"]/h3/a
        #/html/body/div[5]/div[2]/div[1]/div[1]/div/div[1]/div/div[3]/div/div[1]/div/w-root/div/div/ul/li[1]/h3/a
        #/html/body/div[5]/div[2]/div[1]/div[1]/div/div[1]/div/div[3]/div/div[1]/div/w-root/div/div/ul/li[1]/h3/a
        #//*[@id="item1d340f0acd"]/h3/a
        enddate = html.xpath("//*[@id='ListViewInner']//li//ul//li[1]//span//span/text()")
        price = html.xpath("//*[@id='ListViewInner']//li//ul[1]//li[1]//span/text()")

        for a,b,c,d,e in zip(picturesrc,name,enddate,price,oldlink):
            strb3 = str(b)
            strb3 = strb3.replace('Click this link to access ','') 
            strpic = str(a)
            strpic = strpic.replace('l225','l1600') 
            cardinfo2 = Jamescardinfo(picture = a,name = strb3,enddata = c,price = d,oldlink = e)
            listcard2 = list(Jamescardinfo.objects.all().filter(name__exact = strb3))
            if listcard2 == []:
                cardinfo2.save()
    
    elif x == 4:
        Jordanscardinfo.objects.all().delete()
        for a,b,c,d,e in zip(picturesrc,name,enddate,price,oldlink):
            cardinfo4 = Jordanscardinfo(picture = a,name = b,enddata = c,price = d,oldlink = e)
            cardinfo4.save()
    return()






# -------------------------------------------------------------------------------

def example_view(request):
    # urls = "https://www.ebay.com/sch/Sports-Trading-Cards/212/i.html?_from=R40&LH_Sold=1&_udlo=&_udhi=&LH_Auction=1&_samilow=&_samihi=&_sop=13&_dmd=1&LH_Complete=1&_fosrp=1&_nkw=basketball+cards&_pgn=3&_skc=120&rt=nc"
    urls = "https://www.ebay.com/sch/Sports-Trading-Cards/212/i.html?_from=R40&LH_Sold=1&_udlo=&_udhi=&LH_Auction=1&_samilow=&_samihi=&_sop=13&_dmd=1&LH_Complete=1&_fosrp=1&_nkw=basketball+cards&_ipg=120&rt=nc"
    url2 =   "https://www.ebay.com/sch/Sports-Trading-Cards/212/i.html?_from=R40&LH_Sold=1&_udlo=&_udhi=&LH_Auction=1&_samilow=&_samihi=&_sop=13&_dmd=1&LH_Complete=1&_fosrp=1&_nkw=basketball+cards&_pgn=71&_skc=8400&rt=nc"
    url3 =   "https://www.ebay.com/sch/Sports-Trading-Cards/212/i.html?_from=R40&LH_Sold=1&_udlo=&_udhi=&LH_Auction=1&_samilow=&_samihi=&_sop=13&_dmd=1&LH_Complete=1&_fosrp=1&_nkw=basketball+cards&_pgn=70&rt=nc"
#    
#    https://www.ebay.com/sch/Sports-Trading-Cards/212/i.html?_from=R40&LH_Sold=1&_udlo=&_udhi=&LH_Auction=1&_samilow=&_samihi=&_sop=13&_dmd=1&LH_Complete=1&_fosrp=1&_nkw=basketball+cards&_pgn=4&_skc=360&rt=nc
  
    scaler(url2 ,3)
    scaler(urls ,2)
    scaler(url2 ,2)
    # n = 1
    # while n< 155:
    #     urlx = "https://www.ebay.com/sch/Sports-Trading-Cards/212/i.html?_from=R40&LH_Sold=1&_udlo=&_udhi=&LH_Auction=1&_samilow=&_samihi=&_sop=13&_dmd=1&LH_Complete=1&_fosrp=1&_nkw=basketball+cards&_pgn="+str(n+1)+"&_skc="+str(n)*60+"&rt=nc"
    #     scaler(urlx ,1)
    #     n = n+1
    all_cards = Kobecardinfo.objects.all().order_by("-id")
    #all_cards = Cardinfo.objects.all().filter(name__contains = 'kobe')
    
    paginator = Paginator(all_cards, 24) # Show 15 cards per page.
    # request.session['all_cards'] = all_cards
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'card_board/example.html', {'page_obj': page_obj,"ab":['1','2','3']})
  



def card_view(request):
    eg_dict = request.session.get('all_cards')
    return render(request,'card_board/card.html',context=eg_dict)


def player_view(request):
   
    all_cards = Kobecardinfo.objects.all().order_by("-enddata")
    paginator = Paginator(all_cards, 3) # Show 3 cards per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # eg_dict = request.session.get('all_cards')
    return render(request,'card_board/player.html', {'page_obj': page_obj})
    


def kobe_view(request):
   
    all_cards = Kobecardinfo.objects.all().filter(name__contains = 'kobe').order_by("-enddata").distinct()
    paginator = Paginator(all_cards, 12) # Show 15 cards per page.
    # request.session['all_cards'] = all_cards
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'card_board/kobe.html', {'page_obj': page_obj})

def jordan_view(request):
    all_cards = Kobecardinfo.objects.all().filter(name__contains = ' michael jordan').order_by("-enddata").distinct()
    paginator = Paginator(all_cards, 12) # Show 15 cards per page.
    # request.session['all_cards'] = all_cards
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'card_board/jordan.html', {'page_obj': page_obj})

def james_view(request):
    all_cards = Kobecardinfo.objects.all().filter(name__contains = 'lebron james').order_by("-enddata").distinct()
    paginator = Paginator(all_cards, 12) # Show 15 cards per page.
    # request.session['all_cards'] = all_cards
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'card_board/james.html', {'page_obj': page_obj})


def search_view(request):
    searchcard = request.GET.get('search','')
    searchinfo = Kobecardinfo.objects.all().filter(name__contains = searchcard).order_by("-enddata").distinct()
    # paginator = Paginator(searchinfo, 12) # Show 15 cards per page.
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request,'card_board/search.html', {'page_obj': searchinfo})
   

def detail_view(request):
   eg_dict = request.session.get('x.id')
   carddetail = Kobecardinfo.objects.all().filter(id__contains = eg_dict)
   return render(request,'card_board/detail.html', {'info': carddetail})