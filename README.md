# Decision-Tree-for-mushroom-type-prediction
##Decision Tree which predicts if a mush room is consumable or not
##The data is in a CSV file format:
e,x,s,y,t,l,f,c,b,g,e,c,s,s,w,w,p,w,o,p,k,n,g <br />
e,f,s,n,f,n,a,c,b,o,e,?,s,s,o,o,p,n,o,p,b,v,l <br />
p,k,s,e,f,f,f,c,n,b,t,?,k,k,p,p,p,w,o,e,w,v,d <br />
e,f,f,g,f,n,f,w,b,k,t,e,s,f,w,w,p,w,o,e,k,s,g <br />
e,x,f,n,t,n,f,c,b,w,t,b,s,s,p,w,p,w,o,p,n,v,d <br />
e,f,y,n,t,l,f,c,b,w,e,r,s,y,w,w,p,w,o,p,k,s,p <br />
p,x,y,g,f,f,f,c,b,h,e,b,k,k,p,n,p,w,o,l,h,v,g <br />
p,f,s,w,t,n,f,c,b,w,e,b,s,s,w,w,p,w,t,p,r,v,m <br />
e,x,f,g,t,n,f,c,b,w,t,b,s,s,w,w,p,w,o,p,n,y,d <br />
... <br />
Each row corresponds to a mushroom. The first column is the label indicating whether the mushroom is edible (e) or poisonous (p). (This is the output that we wish to predict from the other columns). Information about the meaning of the other columns is listed in the file agaricus-lepiota.names.

##How to run:

bash-3.2$ python id3.py train test 1 <br />
The provided code simply “learns” a decision tree consisting of a root node with no children that always predicts “Yes”. The program prints out this tree (consisting of a single node with no children), and then prints it’s evaluated accuracy on the test set.
The command line arguments are: the training, test file and a threshold on the minimum information gain
