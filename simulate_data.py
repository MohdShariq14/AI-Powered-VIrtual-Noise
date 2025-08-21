# 🎯 This file will simulate sensor readings + labels.

#  simulate_data.py
# import numpy as np
# import pandas as pd

# def simulate_data(n=100):
#     data = []
#     labels = ['LPG', 'Alcohol', 'Smoke', 'Ammonia', 'Fresh Air']
#     for label in labels:
#         for _ in range(n):
#             if label == 'LPG':
#                 mq2 = np.random.uniform(600, 800)
#                 mq3 = np.random.uniform(200, 300)
#                 mq135 = np.random.uniform(400, 600)
#             elif label == 'Alcohol':
#                 mq2 = np.random.uniform(200, 300)
#                 mq3 = np.random.uniform(700, 900)
#                 mq135 = np.random.uniform(300, 500)
#             elif label == 'Smoke':
#                 mq2 = np.random.uniform(800, 1000)
#                 mq3 = np.random.uniform(400, 600)
#                 mq135 = np.random.uniform(700, 900)
#             elif label == 'Ammonia':
#                 mq2 = np.random.uniform(200, 400)
#                 mq3 = np.random.uniform(300, 500)
#                 mq135 = np.random.uniform(900, 1100)
#             else:  # Fresh Air
#                 mq2 = np.random.uniform(100, 200)
#                 mq3 = np.random.uniform(100, 200)
#                 mq135 = np.random.uniform(100, 200)
#             data.append([mq2, mq3, mq135, label])
#     df = pd.DataFrame(data, columns=['MQ2', 'MQ3', 'MQ135', 'Label'])
#     return df


import numpy as np
import pandas as pd
def simulate_data(samples=200):
    np.random.seed(42)
    data = []
    labels = ['Smoke', 'LPG', 'Alcohol', 'Ammonia', 'Fresh Air']
    
    for label in labels:
        for _ in range(samples // len(labels)):
            if label == 'Smoke':
                mq2 = np.random.randint(800, 1000)
                mq3 = np.random.randint(300, 500)
                mq135 = np.random.randint(900, 1100)
            elif label == 'LPG':
                mq2 = np.random.randint(700, 900)
                mq3 = np.random.randint(600, 800)
                mq135 = np.random.randint(800, 1000)
            elif label == 'Alcohol':
                mq2 = np.random.randint(300, 500)
                mq3 = np.random.randint(900, 1100)
                mq135 = np.random.randint(400, 600)
            elif label == 'Ammonia':
                mq2 = np.random.randint(400, 600)
                mq3 = np.random.randint(200, 400)
                mq135 = np.random.randint(800, 900)
            elif label == 'Fresh Air':
                mq2 = np.random.randint(100, 300)
                mq3 = np.random.randint(100, 300)
                mq135 = np.random.randint(100, 300)
            data.append([mq2, mq3, mq135, label])
    
    df = pd.DataFrame(data, columns=['MQ2', 'MQ3', 'MQ135', 'Label'])
    return df
