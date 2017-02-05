from collections import namedtuple
import sys
import math
from Data import *

DtNode = namedtuple("DtNode", "fVal, nPosNeg, gain, left, right")

POS_CLASS = 'e'

def InformationGain(data, f):
    #TODO: compute information gain of this dataset after splitting on feature F
    from math import log
    log2=lambda x:log(x)/log(2)  
    results={}
    for row in data:
    # The result is the first column
        r=row[0]
        if r not in results: results[r]=0
        results[r]+=1

    #Calculating the entropy
    ent=0.0
    for r in results.keys():
        p=float(results[r])/len(data)
        ent=ent-p*log2(p)
    return ent

def Classify(tree, instance):
    if tree.left == None and tree.right == None:
        return tree.nPosNeg[0] > tree.nPosNeg[1]
    elif instance[tree.fVal.feature] == tree.fVal.value:
        return Classify(tree.left, instance)
    else:
        return Classify(tree.right, instance)

def Accuracy(tree, data):
    nCorrect = 0
    for d in data:
        if Classify(tree, d) == (d[0] == POS_CLASS):
            nCorrect += 1
    return float(nCorrect) / len(data)

def PrintTree(node, prefix=''):
    print("%s>%s\t%s\t%s" % (prefix, node.fVal, node.nPosNeg, node.gain))
    if node.left != None:
        PrintTree(node.left, prefix + '-')
    if node.right != None:
        PrintTree(node.right, prefix + '-')        

def ID3(data, features, MIN_GAIN=0.1):

    
    #TODO: implement decision tree learning
    if len(data)==0: return DtNode() #if data size is zero return an empty node
    current_score=InformationGain(data,features)

    best_gain=0.0
    fvalue=FeatureVal(1,'x')
    best_sets=None
  
    column_count=len(data[0])-1   #counting the # of attributess. 
                                
    for col in range(1,column_count+1): #first attribute is the target attribute
    # Generate the list of all possible different values in the considered column
        global column_values        
        column_values={}            
        for row in data:
            column_values[row[col]]=1   
    # Dividing the rows up for each value in this column
        for value in column_values.keys(): 
            split_function=None
            if isinstance(value,int) or isinstance(value,float): # check if the value is a number i.e int or float
                split_function=lambda row:row[col]>=value
            else:
                split_function=lambda row:row[col]==value
   
            # Divide the rows into two sets 
            set1=[row for row in data if split_function(row)]
            set2=[row for row in data if not split_function(row)]
            # Information gain
            p=float(len(set1))/len(data) #p is the fraction of a child set relative to its parent
            gain=current_score-p*InformationGain(set1,features)-(1-p)*InformationGain(set2,features) #formula for information gain
            if gain>best_gain and len(set1)>0 and len(set2)>0: 
                best_gain=gain
                fvalue=FeatureVal(col,value)
                best_sets=(set1,set2)
           
    if best_gain>MIN_GAIN : #check for the min gain
        trueBranch=ID3(best_sets[0],features,MIN_GAIN)
        falseBranch=ID3(best_sets[1],features,MIN_GAIN)
        ne=0
        np=0
        for s in best_sets[0]:
            if s[0]==POS_CLASS:
                ne=ne+1
            else:
                np=np+1
        for s in best_sets[1]:
            if s[0]==POS_CLASS:
                ne=ne+1
            else:
                np=np+1

        return DtNode(fvalue,(ne,np),best_gain,trueBranch,falseBranch) 
    else:
        ne=0
        np=0
        for s in set1:
            if s[0]==POS_CLASS:
                ne=ne+1
            else:
                np=np+1
        for s in set2:
            if s[0]==POS_CLASS:
                ne=ne+1
            else:
                np=np+1

        return DtNode(FeatureVal(col,value), (ne,np), gain, None, None)

if __name__ == "__main__":
    train = MushroomData(sys.argv[1])
    dev = MushroomData(sys.argv[2])

    dTree = ID3(train.data, train.features, MIN_GAIN=float(sys.argv[3]))
    
    PrintTree(dTree)
    #print(train.features)
    print (Accuracy(dTree, dev.data))
