import pymongo
import PWD
pwd = PWD.pwd()
def inquiry_index():
    path = "./DB/INDEX/coin.txt"
    f = open(path,"r")
    coinindex = f.read().splitlines()
    f.close()
    coinindex = coinindex[-2:]
    coinRate = coinindex[0]
    coinProfit = coinindex[1]

    path = "./DB/INDEX/sp500.txt"
    f = open(path,"r")
    sp500index = f.read().splitlines()
    f.close()
    sp500index = sp500index[-2:]
    sp500Rate = sp500index[0]
    sp500Profit = sp500index[1]

    path = "./DB/INDEX/kospi.txt"
    f = open(path,"r")
    kospiindex = f.read().splitlines()
    f.close()
    kospiindex = kospiindex[-2:]
    kospiRate = kospiindex[0]
    kospiProfit = kospiindex[1]

    return coinRate,coinProfit,sp500Rate,sp500Profit,kospiRate,kospiProfit


def db_index():
    client = pymongo.MongoClient("mongodb+srv://maeseok:"+pwd+"@finance.smjhg.mongodb.net/index?retryWrites=true&w=majority")
    db = client.data
    data = db.find()
    print(data)
    return db
# # 저장 - 예시


def KRW_made(symbol,stock_rate,db):
    DOC = {'Symbol':symbol,'Name':stock_rate[1],'Rate':stock_rate[2],'Gap':stock_rate[3],'Profit':stock_rate[4]}
    db.users.insert_one(DOC)

def KRW_inquiry():
    items = db.users.find()
    return items


    #doc = {'name':'bobby','age':21}
#db.users.insert_one(doc)
#
# # 한 개 찾기 - 예시
#user = db.users.find_one({'name':'bobby'})
#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
#same_ages = list(db.users.find({'age':21},{'_id':False}))
#
# # 바꾸기 - 예시
#db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# # 지우기 - 예시
#db.users.delete_one({'name':'bobby'})