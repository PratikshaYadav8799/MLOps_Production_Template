def data_preprocessiong(df):
    #Step1 : Drop duplicated values
    #Step2 : Feature Engineering  (optional)**
    #Step3 : Split the dataset into Independent Columns {x} and target column {y}
    #Step4 : Split the dataset into train {Seen} and test {unseen} data
    #Step5 : Build Ene pipeline for numerical and categorical
    #Step6 : Build categorical pipeline with imputation and scaling
    #Step7 : Build categorical pipeline with imputation and encoding
    #Step8 : Concate the numerical and cateogorical pipeline using Column Transformer
    #Step9 : Fit transformer on train and test
    #Step10 : Return the preprocess train and test : X_train,X_test,y_train,y_test