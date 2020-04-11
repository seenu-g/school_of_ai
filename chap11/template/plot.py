import numpy as np
import torch
from matplotlib import pyplot as plt


def plot_acc_loss(train_acc_series, test_acc_series, train_loss_series, test_loss_series):
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle("Training & Test")

    for line in train_acc_series.items():
        axs[0, 0].plot(line[1], label=line[0])
    axs[0, 0].set_title("Training Accuracy")
    axs[0, 0].set_xlabel("Epoch")
    axs[0, 0].set_ylabel("Accuracy")
    axs[0, 0].legend()

    for line in train_loss_series.items():
        axs[0, 1].plot(line[1], label=line[0])
    axs[0, 1].set_title("Training Loss")
    axs[0, 1].set_xlabel("Epoch")
    axs[0, 1].set_ylabel("Loss")
    axs[0, 1].legend()

    for line in test_acc_series.items():
        axs[1, 0].plot(line[1], label=line[0])
    axs[1, 0].set_title("Test Accuracy")
    axs[1, 0].set_xlabel("Epoch")
    axs[1, 0].set_ylabel("Accuracy")
    axs[1, 0].legend()

    for line in test_loss_series.items():
        axs[1, 1].plot(line[1], label=line[0])
    axs[1, 1].set_title("Test Loss")
    axs[1, 1].set_xlabel("Epoch")
    axs[1, 1].set_ylabel("Loss")
    axs[1, 1].legend()


def plot_accuracy(train_history, test_history):
    plt.plot(train_history)
    plt.plot(test_history)
    plt.title("Model Accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train", "test"], loc="upper left")
    plt.show()


def plot_loss(train_history, test_history):
    plt.plot(train_history)
    plt.plot(test_history)
    plt.title("Model Loss")
    plt.ylabel("Loss")
    plt.xlabel("Epoch")
    plt.legend(["train", "test"], loc="upper left")
    plt.show()
    
def plot_train_test_accuracy(train_acc,test_acc):
    plt.figure(figsize=(10, 5))
    ax = plt.subplot(111)
    ax.plot(train_acc,color = 'g',label="Train Accuracy")
    ax.plot(test_acc,color = 'b',label="Test Accuracy")
    ax.set(title="Accuracy Plot", xlabel="Epoch", ylabel="Accuracy")
    ax.legend()
    plt.show()