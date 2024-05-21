from database.DB_connect import DBConnect
from model.Product import Product


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllColors():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gp.Product_color  
                    from go_products gp"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["Product_color"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getProducts_color(color):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct  * 
                    from go_products gp
                    where gp.Product_color = %s"""

        cursor.execute(query,(color,))

        for row in cursor:
            result.append(Product(**row))

        cursor.close()
        conn.close()
        return result

    '''select gds1.Product_number as p1, gds2.Product_number as p2, count(*)  as n
from go_daily_sales gds1, go_daily_sales gds2
where gds1.Retailer_code = gds2.Retailer_code  and year(gds1.`Date`) = '2015'
and gds2.`Date` = gds1.`Date` and gds1.Product_number = "143120" and gds2.Product_number ="147180"
'''

