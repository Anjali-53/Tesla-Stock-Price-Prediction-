import pickle


def price_prediction(features):
    pickled_model = pickle.load(open('E:\\python program\\newapi\\Teslastockprice.pkl', 'rb'))
    stock_price =float(pickled_model.predict(features))
    
    return  stock_price
  
test_features = [[20.406668	,21.008667,	19.92,	174879000]] #Passed in the order 'Open''High','Volume' respectively

print(f'The stock price the next day will be $ {price_prediction(test_features)}')