import pickle

def PredictPrice(a,b,c,d,e,f):
    with open('mainmodel.pickle','rb') as file:
        model= pickle.load(file)
        return int(model.predict([[a,b,c,d,e,f]]))

print(PredictPrice(62,1,26.3,0,2,2))
