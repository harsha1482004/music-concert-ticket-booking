import pickle
fb=open("model.h","rb")
N=pickle.load(fb)
print(N)
fb.close()