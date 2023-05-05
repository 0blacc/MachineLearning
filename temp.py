import numpy as np
import pickle 

#load the saved model
loaded_model = pickle.load(open('C:/Users/motlatso/Downloads/trained_model.sav', 'rb'))



input_data = (6,148,72,35,0,33.6,0.627,50)

#change the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we are predicting for one instance 
#reshape the np array as we are predicting for one instance 
input_data_reshape=(input_data_as_numpy_array.reshape(1,-1))


#stabdardise
prediction = loaded_model.predict(input_data_reshape)
print(prediction)

if (prediction[0] == 1 ):
  print('Diabetic case')
else:
   print('Non diabetic ')
