# loan-prediction
  

# data
    data.csv = raw data total data 38480, 25 features not including column id and repay_fail.
    cleanData.csv = total data 37426, 25 features not including column id and repay_fail.
    Book25features = total data 2500, 25 features not including column id and repay_fail.
    Book9features = total data 2500, 9 features not including repay_fail.
    remainingdata.csv = total data 34926: 25features not including column id and repay_fail.

# file
  dataclean.jpynb = take data.csv, clean it, save as cleanData.csv, take out sample randomly 2500 and save it as Book25features, then save the remaining data as     remainingdata.csv.
  RF25features.jpynb = take remainingdata.csv, train with random forest and save trained model name "modelDataInbalance_25features".
  RF9features.jpynb = take remainingdata.csv, deleted 16 features, train with random forest and save trained model name "modelDataBalance_9features".

# model
  modelDataInbalance_25features
  modelDataBalance_9features

# gui 
  gui25features.py = gui use trained model modelDataInbalance_25features
  gui9features.py = gui use trained model modelDataBalance_9features

# auto testing sample data
  


  
