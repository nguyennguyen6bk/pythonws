from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dữ liệu Iris từ scikit-learn
iris = load_iris()
X = iris.data
y = iris.target

# Chia tập dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Khởi tạo một bộ phân loại cây quyết định
clf = DecisionTreeClassifier(random_state=42)

# Huấn luyện mô hình trên tập huấn luyện
clf.fit(X_train, y_train)

# Dự đoán nhãn của các mẫu trong tập kiểm tra
y_pred = clf.predict(X_test)

# Đánh giá độ chính xác của mô hình
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)
