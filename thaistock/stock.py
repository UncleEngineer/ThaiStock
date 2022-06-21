from urllib.request import urlopen
from bs4 import BeautifulSoup


class SET:
    '''
    The Stock Exchange of Thailand

    วันที่ [0]
    ราคาเปิด [1]
    ราคาสูงสุด [2]
    ราคาต่ำสุด [3]
    ราคาเฉลี่ย [4]
    ราคาปิด [5]
    เปลี่ยนแปลง [6]
    %เปลี่ยนแปลง [7]
    ปริมาณ(พันหุ้น) [8]
    มูลค่า(ล้านบาท) [9]
    SET Index [10]
    %เปลี่ยนแปลง [11]

    Example:
    -----------------

    stock = SET()
    current = stock.current('TEAMG',header=True,show=True)

    stock.show_header()
    hisprices = stock.historical('TEAMG',days=180,show=False,select=[0,1,10],showindex=False)
    hisprices = stock.historical('TEAMG', select=[0,5])
    hisprices = stock.historical('TEAMG',select=[0,1,5,2,3],days=7,show=True,header=True)
    stock.plot('TEAMG',days=30,show_num=10) # show_num=10 คือ โชว์ตัวเลข 10-11 รายการ
    -----------------
    '''
    def __init__(self):
        self.base_url = 'https://classic.settrade.com/'
        self.header = ['วันที่','ราคาเปิด','ราคาสูงสุด','ราคาต่ำสุด','ราคาเฉลี่ย','ราคาปิด','เปลี่ยนแปลง','%เปลี่ยนแปลง','ปริมาณ(พันหุ้น)','มูลค่า(ล้านบาท)','SET Index','%เปลี่ยนแปลง']

    def historical(self,CODE,days=30,show=False,**kwargs):
        url = self.base_url + '/C04_02_stock_historical_p1.jsp?txtSymbol={}&selectPage=2&max={}&offset=0'.format(CODE,days)

        webopen = urlopen(url)
        pagehtml = webopen.read()
        webopen.close()

        data = BeautifulSoup(pagehtml,'html.parser')
        table = data.find('table',{'class':'table table-info table-hover'})
        table = table.find_all('tr')[1:]

        result = []
        for row in table:
            try:
                column = row.find_all('td')
                cl = []
                for i,c in enumerate(column):
                    if i!= 0:
                        cl.append(float(c.text.replace(',','')))
                    else:
                        cl.append(c.text)
                result.append(cl)
            except:
                pass

        newresult = []

        
        if kwargs != {}:
            if 'showindex' in kwargs:
                if kwargs['showindex']:
                    self.show_header()
                    

            if 'select' in kwargs:
                hdl = [ self.header[s] for s in kwargs['select']]
                if 'header' in kwargs:
                    if kwargs['header']:
                        newresult.append(hdl)

                for day in result:
                    d = [ day[s] for s in kwargs['select']]
                    newresult.append(d)

            elif show:
                for day in result:
                    print(day)

        if show and 'select' in kwargs:
            for rs in newresult:
                print(rs)
            return newresult
        elif 'select' in kwargs:
            return newresult

        if 'header' in kwargs:
            if kwargs['header']:
                result.insert(0,self.header)
        return result

    def show_header(self):
        hd = ['{} [{}]'.format(h,i) for i,h in enumerate(self.header)]
        print('--------index for select--------')
        for h in hd:
            print(h)
        print('--------------------------------')



    def plot(self,CODE,days=7,show=True,show_num=5):
        import matplotlib.pyplot as plt

        price_list = self.historical(CODE,select=[0,5],days=days)
        print(price_list)
        y = [ p[1] for p in price_list]
        title = [ p[0] for p in price_list]
        y.reverse()
        title.reverse()
        print(y)
        x = range(len(y))
        plt.plot(x,y,'.-')


        if len(title) > 20:
            delete = len(title) // show_num
            reset = 0
            for t in range(len(title)):
                if reset == delete:
                    reset = 0
                    reset += 1
                else:
                    if t != 0:
                        title[t] = ''
                        reset += 1


        if show:
            if days > 14:
                plt.xticks(x,title,rotation='vertical')
            else:
                plt.xticks(x,title)

        if show:
            delete = len(title) // show_num
            reset = 0
            for i,(xx,p) in enumerate(zip(x,y)):
                if reset == delete:
                    reset = 0
                    reset += 1
                    plt.text(xx, p ,'{:,.2f}'.format(p))
                elif i == 0:
                    plt.text(xx, p ,'{:,.2f}'.format(p))
                    reset += 1
                else:
                    reset += 1

        
        plt.title('{} ({} - {}) {} days'.format(CODE,title[0],title[-1],days))
        plt.show()



    def current(self,CODE,show=False,header=False):
        hd = ['ชื่อหุ้น','ราคาล่าสุด','เปลี่ยนแปลง','%เปลี่ยนแปลง','อัพเดต วัน-เวลา']
        url = 'https://classic.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={}&ssoPageId=10&selectPage=2'.format(CODE)
        webopen = urlopen(url)
        page_html = webopen.read()
        webopen.close()
        data = BeautifulSoup(page_html,'html.parser')

        price = data.findAll('div',{'class':'col-xs-6'})

        title = price[0].text
        stockprice = price[2].text.replace(',','')

        change = price[3].text
        change = change.replace('\n','')
        change = change.replace('\r','')
        change = change.replace('\t','')
        change = change.replace(' ','')
        change = change[11:]

        pchange = price[4].text
        pchange = pchange.replace('\n','')
        pchange = pchange.replace('\r','')
        pchange = pchange.replace(' ','')
        pchange = pchange[12:].replace('%','')

        update = data.findAll('span',{'class':'stt-remark'})
        stockupdate = update[0].text
        stockupdate = stockupdate[13:]
        try:
            result = [title,float(stockprice),float(change),float(pchange),stockupdate]
        except:
            result = [title,stockprice,change,pchange,stockupdate]

        if show:
            if header:
                print(hd)
            print(result)

        return result


if __name__ == '__main__':
    stock = SET()
    # current = stock.current('TEAMG',header=True,show=True)
    # print(current)
    # stock.show_header()
    # hisprices = stock.historical('TEAMG',days=100,show=True,select=[0,5,6,7],header=True)
    # hisprices = stock.historical('TEAMG', select=[0,5])
    # stock.plot('TEAMG',days=30)
    # stock.plot('TEAMG',days=120)
    # hisprices = stock.historical('TEAMG',select=[0,1,5,2,3],days=7,show=True,header=True)
