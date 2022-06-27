def bill(order,menu):
    bill=0
    for item in order:
        bill+=int(menu[item])
    return bill

def order(menu):
    orders=[]
    order=input("Place your order. Type Q to quit\n")
    while order.upper()!='Q':
        found=menu.get(order)
        if found:
            orders.append(order)
        else:
            print("sorry not on menu")
        order=input("Place your order. Type Q to quit\n")
    return orders

def menu(menu):
    print("Menu\n")
    for k,v in menu.items():
        print(k,':',v)

def main():
    menu1={'idli':'50','dosa':'100','uppit':'60','coffee':'20'}
    menu(menu1)
    order_res = order(menu1)
    print("your order is",order_res)
    total_bill=bill(order_res,menu1)
    print("Total bill is", total_bill)

main()