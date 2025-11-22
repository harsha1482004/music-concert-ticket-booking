import pickle
N=['ram','abhi','arya','gowda']
fb=open("model.h","wb")
pickle.dump(N,fb)
fb.close()