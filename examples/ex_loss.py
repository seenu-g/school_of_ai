import torch 
import torch.nn as nn

temp = torch.tensor([23,24,24.5,26,27.2,23.0],dtype=torch.float)
temp.size()

x = torch.rand(10)
x.size()

n_in, n_h, n_out, batch_size = 10, 5, 1, 10
x = torch.randn(batch_size, n_in)
y = torch.tensor([[1.0], [0.0], [0.0], [1.0], [1.0], [1.0], [0.0], [0.0], [1.0], [1.0]])
model = nn.Sequential(nn.Linear(n_in, n_h),
                      nn.ReLU(),
                      nn.Linear(n_h, n_out),
                      nn.Sigmoid())
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(50): 
    y_pred = model(x) # Forward pass: Compute predicted y by passing x to the model
    loss = criterion(y_pred, y) # Compute and print loss
    print('epoch: ', epoch,' loss: ', loss.item())
    optimizer.zero_grad() # Zero gradients, perform a backward pass, and update the weights.
    loss.backward() # perform a backward pass (backpropagation)
    optimizer.step() # Update the parameters
