from fastapi import FastAPI

app1 = FastAPI()

buyers = []
products = {} # must hold product name and amount(stock, count)
purchased = {} # holds which (and how many) products where bought by buyer

def getBuyers():
    return(buyers)

def getProducts():
    return(products)

#### Functions which deal with GET, POST... (browser stuff)
@app1.get("/")
async def showMessage():
    return {"result": "This is the root. Nothing else."}


# GET functions to catch errors in link with slash or no slash
@app1.get("/buyers") 
async def getBuyers1():
    return getBuyers()

@app1.get("/buyers/")
async def getBuyers2():
    return getBuyers()

@app1.get("/products") 
async def getProducts1():
    return getProducts()

@app1.get("/products/")
async def getProducts2():
    return getProducts()


# Add new buyers
@app1.post("/buyers")
async def addBuyers(newBuy: str):
    message = "Not specified"
    if (type(newBuy) == str):  # make sure input is a string
        if (newBuy in buyers): # if buyer already exists in list
            return {"result": "Duplicate Entry."}
        else: # a new buyer added which didn't exist before
            message = (f"Successfully added: {newBuy}.")
            buyers.append(newBuy)
    else:
        return("Input is not an string. Please input a string.")

    return {"result": "OK", "message": message}

# Add new products
@app1.post("/products")
async def addProducts(newProd: str, count: int=1):
    message = "Not specified"
    if (type(newProd) == str):  # make sure input is a string
        if (newProd in products): # if product already exists in list
            products[newProd] = products[newProd] + count
            message = (f"Existing and added item(s): {newProd}.")
            return {"result": "Duplicate Entry."}
        else: # a new product added which didn't exist before
            message = (f"Successfully added: {newProd}.")
            products[newProd] = count
    else:
        return("Input is not an string. Please input a string.")

    return {"result": "OK", "message": message}

# Buyers buys a product
@app1.post("/buyers")
async def buyProduct(buyer:str, prod_name:str, amount: int=1):
    message = "Not specified"
    if (type(buyer) == str):  # make sure input is a string
        if (buyer in buyers): # if buyer exists in list, check product

            if (type(prod_name) == str):
                if(prod_name in products): #product exists
                    buyProduct(prod_name, amount) #decrement product count
                    message2 = (f"{prod_name} in stock and purchased.")
                    storePurchase(buyer, prod_name, amount) # store buyer's purchase
            else:
                message2 = (f"Error: no product {prod_name}") 

        else: # buyer doesn't exist
            message = (f"Error: no buyer {buyer}.")
    else:
        return("Input is not an string. Please input a string.") 
    return{"result": message, "result": message2}

# Decrement or remove product from list when purchased
@app1.delete("/products")
async def buyProduct(prod, count):
    message = "Not Specified"
    if prod in products:
        if products[prod] >= count:
            products[prod] = products[prod] - count
            message = (f"Product {prod} Purchsed.")
        else:
            message = (f"Not enough stock: {prod}")
    else:
        message = (f"Error: no product {prod}")

    return {"result": message}

# Store a buyer's purchases (receives parameters at time of purchase)
@app1.post("/buyers/BUYER_NAME/purchased")           #######not sure how to accept buyer_nme here
async def storePurchase(buyer, prod_name, amount): 
    purchased = {"buyer99": ["prod_name", "amount"]} # format key:buyer, value: list[prod,amount]
    if (buyer in purchased.keys()): # buyer exists (purchased before)
        message = (f"{buyer} exists.")
        purchased[buyers].append(prod_name, amount)

    else: # a new buyer (with no previous purchases) to dictionary
        purchased[buyer] = [prod_name, amount]
        message = (f"Purchase history updated.")
    
    print("result: ", message)
