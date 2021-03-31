import pickle

#doc_new = ['obama is running for president in 2016']




#function to run for prediction
def detecting_fake_news(var):
	
	load_model = pickle.load(open('final_model.sav', 'rb'))
	prediction = load_model.predict([var])
	prob = load_model.predict_proba([var])
	return ("The given statement is "+str(prediction[0]),
        "The truth probability score is "+str(prob[0][1]))


