import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.dropout_value = 0.15
                                                                                  #RF = rin+(k-1)*jin
                                                                                  #jout = jin*s
        self.conv_block1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=(3, 3), padding=0, bias=False),#Rf = 3, j = 1
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.Dropout(self.dropout_value), 

            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=(3, 3), padding=1, bias=False), #Rf = 5, j = 1
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.Dropout(self.dropout_value), 

            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1, bias=False), #Rf = 7, j = 1
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(self.dropout_value), 
            
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1, bias=False), #Rf = 9, j = 1
            nn.ReLU(),
            nn.BatchNorm2d(128),
            nn.Dropout(self.dropout_value), 

            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=(3, 3), padding=1, bias=False),#Rf = 11, j = 1
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.Dropout(self.dropout_value), 
        )

        self.conv_block2 = nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=16, kernel_size=(3, 3), padding=1,dilation=2, bias=False), #jin=jout=2, kernel_size = 5, rf = 12+(4)*2 = 20
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.Dropout(self.dropout_value),

            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=(3, 3), padding=1,dilation=1, bias=False), #jin=jout=2, kernel_size = 5, rf = 20+(2)*2 = 24
            nn.ReLU(),
            nn.BatchNorm2d(32),
             nn.Dropout(self.dropout_value),

            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1,dilation=1, bias=False), #jin=jout=2, kernel_size = 5, rf = 24+(2)*2 = 28
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(self.dropout_value),

            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1,dilation=1, bias=False), #jin=jout=2, kernel_size = 5, rf = 28+(2)*2 = 32
            nn.ReLU(),
            nn.BatchNorm2d(128),
            nn.Dropout(self.dropout_value),
            )

        self.conv_block3 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=16, kernel_size=(3, 3), padding=1, bias=False), #jin = jout = 4, rf = 34+(2)*4 = 42
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.Dropout(self.dropout_value),

            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=(3, 3), padding=1,groups=16, bias=False), #jin = jout = 4, rf = 42+(2)*4 = 50
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.Dropout(self.dropout_value),

            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1,groups=32, bias=False), #jin = jout = 4, rf = 50+(2)*4 = 58
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(self.dropout_value),

            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1,groups=64, bias=False), #jin = jout = 4, rf = 58+(2)*4 = 66
            nn.ReLU(),
            nn.BatchNorm2d(128),
            nn.Dropout(self.dropout_value),
            
            )
        self.conv_block4 = nn.Sequential(
           nn.Conv2d(in_channels=128, out_channels=16, kernel_size=(3, 3), padding=1, bias=False), #jin = jout = 8, rf = 70 +(2) *8 = 86
            nn.ReLU(),
            nn.BatchNorm2d(16),
            nn.Dropout(self.dropout_value),

            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=(3, 3), padding=1, bias=False), #jin = jout = 8, rf = 86 +(2) *8 = 102
            nn.ReLU(),
            nn.BatchNorm2d(32),
            nn.Dropout(self.dropout_value),

            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1, bias=False), #jin = jout = 8, rf = 102 +(2) *8 = 118
            nn.ReLU(),
            nn.BatchNorm2d(64),
            nn.Dropout(self.dropout_value),

            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1, bias=False), #jin = jout = 8, rf = 118 +(2) *8 = 134
            nn.ReLU(),
            nn.BatchNorm2d(128),
            nn.Dropout(self.dropout_value), 
        )
        self.conv_block5 = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(in_channels=128, out_channels=10, kernel_size=(1, 1), padding=0, bias=False)#Op_size = 1, RF = 
        )
 
        self.pool = nn.MaxPool2d(2, 2)

    def forward(self, x):
        x = self.conv_block1(x) # i/p= 32 o/p=32 Rf = 11
        x = self.pool(x) # jin = 1, Rf = 12 j out= 2
        x = self.conv_block2(x) # Rf = 32 jout = 2, 
        x = self.pool(x) # jout = 4, s =2, Rf = 32+1*2 = 34
        x = self.conv_block3(x) #RF = 66
        x = self.pool(x) 
        x = self.conv_block4(x)  
        x = self.conv_block5(x)  
        x = x.view(-1, 10)
        return x