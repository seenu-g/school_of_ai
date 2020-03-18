import torch
# Creating the graph
x = torch.tensor(1.0, requires_grad = True)
# Check if tracking is enabled
print(x.requires_grad) #True
y = x * 2
print(y.requires_grad) #True

def test_no_grad(x) :
    print('with orch.no_grad() gradient becomes false')
    with torch.no_grad():
        # Check if tracking is enabled
	    y = x*2
	    print(x.requires_grad,y.requires_grad,x,y) # True False
 
def testBackward() :
    print('\n','testBackward() : with z.backward() gradient created for scalar outputs')
	# Creating the graph
    p = torch.tensor(1.0, requires_grad = True)
    z = p * 2
    print(p,z)
    print(z.backward())

def testBackwardError() :
    print('\n','testBackwardError() : with z.backward() gradient created for scalar outputs')
    x = torch.tensor([0.0,2.0,8.0], requires_grad = True)
    y = torch.tensor([5.0,1.0,7.0], requires_grad = True)
    z = x * y
    print(x,y,z)
    try :
        z.backward()
    except :
        print('RuntimeError: grad can be implicitly created only for scalar outputs')
   
test_no_grad(x)
testBackward()
testBackwardError()