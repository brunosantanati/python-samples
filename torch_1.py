import torch

# Create a tensor
tensor_a = torch.tensor([1.0, 2.0, 3.0])
tensor_b = torch.tensor([4.0, 5.0, 6.0])

# Basic tensor addition
result = tensor_a + tensor_b

print("Result:", result)
print("Is GPU (CUDA) available in this Colab session?:", torch.cuda.is_available())