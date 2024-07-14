# loan-prediction using Random Forest(RF)
    refer Documendation.pdf for more detail information
      note: R1 = reference 1, R2 = reference 2, so on....
      
    how to run:
    - download github zip file, unzip
    -  open VScode, "open folder"
    - all should run smoothly

# data
    data.csv: Raw data with a total of 38,480 records and 25 features (excluding the id and repay_fail columns).
    
    cleanData.csv: Cleaned data with a total of 37,426 records and 25 features (excluding the id and repay_fail columns).
    
    Book25features.csv: Sampled data with 2,500 records and 25 features (excluding the id and repay_fail columns).
    
    Book9features.csv: Sampled data with 2,500 records and 9 features (excluding the repay_fail column).
    
    remainingdata.csv: Remaining data with 34,926 records and 25 features (excluding the id and repay_fail columns).

# file
    dataclean.ipynb:    Cleans data.csv, saves it as cleanData.csv, takes a random sample of 2,500 records and saves it as
                        Book25features.csv, and saves the remaining data as remainingdata.csv.
                        
    RF25features.ipynb: Trains a Random Forest model using remainingdata.csv with 25 features and saves the trained model 
                        as modelDataInbalance_25features.
    
    RF9features.ipynb:  Uses remainingdata.csv, deletes 16 features, balances the data, trains a Random Forest model with 
                        9 features, and saves the trained model as modelDataBalance_9features.

# model
    modelDataInbalance_25features: Trained using 34,926 records and 25 features.
    
    modelDataBalance_9features: Trained using 10,180 records and 9 features.

# gui 
    gui25features.py: GUI using the trained model modelDataInbalance_25features.
    
    gui9features.py: GUI using the trained model modelDataBalance_9features.

# auto testing sample data
    AutoEvaluation25features.py: Tests sample data Book25features.csv using the trained model modelDataInbalance_25features.
    
    AutoEvaluation9features.py: Tests sample data Book9features.csv using the trained model modelDataBalance_9features.





  
