'''
Online Store Coupon System:
You are building an online cart. A user can apply a discount coupon, 
but only if every item in their cart costs more than ₹500,
OR if at least one item is a special "Deal of the Day".
'''
Deal_of_the_day=['watter_bottle','glasses','plushie']       #enumerate,any,all,zipgit 
def coupon(item_price,cart_contents):
   
    for i,(item,price) in enumerate(zip(cart_contents,item_price),start=1):
      print(f"{i}:{item}:{price}")

    all_price=all(price>=500 for price in item_price)
    deal=any(content in Deal_of_the_day for content in cart_contents)
 
    if all_price or deal:
       return "Discount applied"
    
    return "NO DISCOUNT"


print(coupon([450,50,250],['cup','plushie','fruit']))
