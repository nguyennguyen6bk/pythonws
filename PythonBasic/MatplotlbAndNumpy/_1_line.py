import matplotlib.pyplot as plt
import numpy as np
# plot để vẽ 1 line
xpoints = np.array([0,6])
ypoints = np.array([0,20])
plt.plot(xpoints, ypoints, 'b')

# plot vẽ 2 điểm dữ liệu với hình dáng cho trước
x1points = np.array([2,5])
y1points = np.array([3,7])
plt.plot(x1points, y1points, 'o', mfc = 'g', mec = 'g')

# plot vẽ nhiều line bởi nhiều điểm dữ liệu
x2points = np.array([1, 3, 4, 6])
y2points = np.array([2, 15, 5, 10])
plt.plot(x2points, y2points, marker ='o')

# vẽ những Dot nối liền các Points với màu sắc là r:Red
y3points = np.array([3,19, 17,6])
plt.plot(x2points, y3points, 'o:r')



plt.show()