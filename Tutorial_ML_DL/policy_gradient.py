import gym
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical

env = gym.make('CartPole-v1')

# Thiết lập mô hình mạng thần kinh cho Policy
class Policy(nn.Module):
    def __init__(self):
        super(Policy, self).__init__()
        self.state_space = env.observation_space.shape[0]
        self.action_space = env.action_space.n
        self.fc1 = nn.Linear(self.state_space, 128)
        self.fc2 = nn.Linear(128, self.action_space)

    def forward(self, x):
        x = torch.Tensor(x)
        x = x.view(-1, self.state_space)  # reshape input tensor
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.softmax(self.fc2(x), dim=1)  # softmax along the second dimension
        return x

policy = Policy()
optimizer = optim.Adam(policy.parameters(), lr=0.01)
eps = np.finfo(np.float32).eps.item()

# Hàm tính toán giá trị thưởng chiết khấu
def discount_rewards(rewards):
    R = 0
    discounted_rewards = []
    for r in rewards[::-1]:
        R = r + 0.99 * R
        discounted_rewards.insert(0, R)
    return discounted_rewards

# Chạy Policy Gradient
def policy_gradient():
    state = env.reset()
    log_probs = []
    rewards = []
    rewards_sum = 0
    while True:
        # Lấy action dựa trên xác suất của Policy
        action_prob = policy(state)
        dist = Categorical(action_prob)
        action = dist.sample()
        log_prob = dist.log_prob(action)
        log_probs.append(log_prob)
        
        # Thực hiện action trong môi trường
        state, reward, done, _ = env.step(action.item())
        rewards.append(reward)
        rewards_sum += reward
        
        if done:
            # Tính toán giá trị loss và cập nhật Policy
            discounted_rewards = discount_rewards(rewards)
            discounted_rewards = torch.tensor(discounted_rewards)
            discounted_rewards = (discounted_rewards - discounted_rewards.mean()) / (discounted_rewards.std() + eps)
            policy_loss = []
            for log_prob, reward in zip(log_probs, discounted_rewards):
                policy_loss.append(-log_prob * reward)
            optimizer.zero_grad()
            policy_loss = torch.stack(policy_loss).sum()
            policy_loss.backward()
            optimizer.step()
            break
            
    return rewards_sum

# Huấn luyện mô hình
for i in range(1000):
    reward = policy_gradient()
    print(f'Episode {i+1}: {reward}')
