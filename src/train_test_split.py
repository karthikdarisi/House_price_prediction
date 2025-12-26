from sklearn.model_selection import train_test_split
def split(x,y,test_size=0.2,random_state=5):
    x_train,x_test,y_train,y_test =train_test_split(
    x,y,
    test_size=test_size,
    random_state=random_state
    )
    return x_train,x_test,y_train,y_test
    

