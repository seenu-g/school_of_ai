import torch
dtype = torch.float
device = torch.device("cpu")
print(dtype)
print(device)
print("cuda available :", torch.cuda.is_available())

N, D_in, H, D_out = 4, 8, 10, 6
x = torch.randn(N, D_in, device=device, dtype=dtype) #4*8
y = torch.randn(N, D_out, device=device, dtype=dtype) #4*6
print(x)
print(y)
print(x.size(),y.size())
print(x.dim(),y.dim())
print(x.shape)
print(x[:, 1]) # display first column
print(x[2,: ]) # display second row
print("requires_grad :" ,x.requires_grad) 
    
'''NumPy sum is almost identical to what we have in PyTorch except 
that dim in PyTorch is called axis in NumPy '''
def test2D():
    z = torch.tensor([
     [1, 2, 3],
     [4, 5, 6]
    ])
    print(z.shape,z.size())
    print(torch.sum(z, dim=0)) #add values in each //collapse the rows, it becomes just one row (it sums column-wise)
    print(torch.sum(z, dim=1)) #add values in each //collapse the columns
    
def test3D():
    y = torch.tensor([
     [
       [1, 2, 3],
       [4, 5, 6]
     ],
     [
       [1, 2, 3],
       [4, 5, 6]
     ],
     [
       [1, 2, 3],
       [4, 5, 6]
     ]
    ])
    print(y.shape,y.size())
    print(torch.sum(y, dim=0)) #add values in each //ccollapse its 3 elements over one another
    print(torch.sum(y, dim=1)) #add values in each //collapse the rows
    print(torch.sum(y, dim=2)) #add values in each //collapse the columns

def testGradient() :
    print("*******testGradient********")
    N, D_in, H, D_out = 4, 8, 10, 6
    w3 = torch.randn(D_in, H, device=device, dtype=dtype, requires_grad=True)
    w4 = torch.randn(H, D_out, device=device, dtype=dtype, requires_grad=True)
    print(w3.requires_grad,w4.requires_grad) # print default value of requires_grad
    print(w3)
    print(w4) 

test2D()
test3D()
testGradient()
'''
w1 = torch.randn(D_in, H, device=device, dtype=dtype) #8,10
w2 = torch.randn(H, D_out, device=device, dtype=dtype) #10,6
print(w1)
print(w2)
'''