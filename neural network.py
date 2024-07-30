import pandas as pd 
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
import numpy as np 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Đọc dữ liệu từ file và tách thành tập đặc trưng(X), tập nhãn (Y)
data = pd.read_csv('C:/Users/admin/Documents/Zalo Received Files/BTL/Credit Score Classification Dataset.csv')
data=data.values
X = data[:, :7]
y = data[:, 7]

#Tách tập dữ liệu thành tập train và test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#Mã hóa tập dữ X_train. Vì X_train là một ma trận 2 chiều của tập mẫu huấn luyện, nên dùng OrdinalEncoder để mã hóa.
#Trong X_train, chỉ các cột 4, 5, 6 chứa text, nên chỉ cần mã hóa những cột này. Lưu ý cách chọn các cột mã hóa.
ordinal_encoder = OrdinalEncoder()
ordinal_encoder.fit(X_train[:, [1,3,4,6]])
X_train[:, [1,3, 4, 6]] = ordinal_encoder.transform(X_train[:, [1,3,4,6]])

#Dùng mã hóa của tập X_train (ordinal_encoder) để mã hóa tập X_test
X_test[:, [1,3,4,6]] = ordinal_encoder.transform(X_test[:, [1,3,4,6]])

#Mã hóa tập dữ y_train. Vì y_train là một vector 1 chiều của tập nhãn, nên dùng LabelEncoder để mã hóa
label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(y_train)

#Dùng mã hóa của tập y_train (label_encoder) để mã hóa tập y_test
y_test = label_encoder.transform(y_test)

#Khai báo mô hình Perceptron
model = MLPClassifier(hidden_layer_sizes=(75,25,25),max_iter=2000)
#Huấn luyện model trên tập (X_train, y_train)
model.fit(X_train, y_train)
#Dùng model để dự báo nhãn của tập X_test
y_pred = model.predict(X_test)

#Đánh giá chất lượng của model bằng cách so sánh y_test với y_pred qua các độ đo(ví dụ Accuracy, Precision)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro',zero_division=1)
recall = recall_score(y_test,y_pred,average='macro')
f1 = f1_score(y_test, y_pred,average='macro')
print('Accuracy', accuracy)
print('Precision', precision)
print('Recall', recall)
print('F1',f1)

#form
#Tạo giao diện người dùng bằng Tkinter
window = Tk()
window.title('Phân loại điểm của thẻ tín dụng')
window.geometry('800x500')
window.configure(background= '#F3F0E7')
#Tạo các nhãn và ô nhập liệu trên giao diện 
lable_Age = Label(window, text="Age:", bg="#F3F0E7")
lable_Age.grid(row=1, column=1, pady=10)
lable_Gender = Label(window, text="Gender:", bg="#F3F0E7")
lable_Gender.grid(row=2, column=1, pady=10)
lable_Income = Label(window, text="Income:", bg="#F3F0E7")
lable_Income.grid(row=3, column=1, pady=10)
lable_Education = Label(window, text="Education:", bg="#F3F0E7")
lable_Education.grid(row=4, column=1, pady=10)
lable_Marital_Status = Label(window, text="Martial Status:", bg="#F3F0E7")
lable_Marital_Status.grid(row=5, column=1, pady=10)
lable_Number_of_Children = Label(window, text="Number of children:", bg="#F3F0E7")
lable_Number_of_Children.grid(row=6, column=1, pady=10)
lable_Home_Ownership = Label(window, text="Home Ownership:", bg="#F3F0E7")
lable_Home_Ownership.grid(row=7, column=1, pady=10)
# textbox_IDKhachHang = Entry(window)
# textbox_IDKhachHang.grid(row=1, column=2)
textbox_Age = Entry(window)
textbox_Age.grid(row=1, column=2)
textbox_Gender = Entry(window)
textbox_Gender.grid(row=2, column=2)
textbox_Income = Entry(window)
textbox_Income.grid(row=3, column=2)
textbox_Education = Entry(window)
textbox_Education.grid(row=4, column=2)
textbox_Marital_Status = Entry(window)
textbox_Marital_Status.grid(row=5, column=2)
textbox_Number_of_Children = Entry(window)
textbox_Number_of_Children.grid(row=6, column=2)
textbox_Home_Ownership = Entry(window)
textbox_Home_Ownership.grid(row=7, column=2)
#Định nghĩa hàm dự  đoán và kiểm tra đầu vào

def dudoan():
    Age = textbox_Age.get()
    Gender = textbox_Gender.get()
    Income = textbox_Income.get()
    Education = textbox_Education.get()
    Marital_Status = textbox_Marital_Status.get()
    Number_of_Children = textbox_Number_of_Children.get()
    Home_Ownership = textbox_Home_Ownership.get()
    if ((Gender == '') or (Age == '') or (Income == '') or (Education == '') or (Marital_Status == '') or (Number_of_Children == '') or (Home_Ownership == '')):
        messagebox.showinfo("Thông báo", "Bạn cần nhập đầy đủ thông tin!")
    else:
        dudoan = model.predict([[int(Age),int(Gender), int(Income), int(Education), int(Marital_Status), int(Number_of_Children), int(Home_Ownership)]])
        if (dudoan == 0):
            str = "High"
        if (dudoan == 1):
            str = "Average"
        if (dudoan == 2):
            str = "low"    
        Nhan.configure(text="Dự đoán: " + str, bg="#F3F0E7")
style = ttk.Style()
style.configure('#F3F0E7.TButton', background='#F3F0E7')
XacNhan = ttk.Button(window, text="Dự đoán",command=dudoan, style='#F3F0E7.TButton')
XacNhan.grid(row=8, column=2, padx=40, pady=10)

accuracy= Label(window)
accuracy.grid(row=9, column=1)
accuracy.configure(text="Độ đo đánh giá accuracy là:"+str(accuracy_score(y_test, y_pred)), bg="#F3F0E7")

precision= Label(window)
precision.grid(row=10, column=1)
precision.configure(text="Độ đo đánh giá Precision là:"+str(precision_score(y_test, y_pred, average='macro',zero_division=1)), bg="#F3F0E7")

recall= Label(window)
recall.grid(row=11, column=1)
recall.configure(text="Độ đo đánh giá Recall là:"+str(recall_score(y_test,y_pred,average='macro')), bg="#F3F0E7")

f1=Label(window)
f1.grid(row=12, column=1)
f1.configure(text="Độ đo đánh giá F1 là:"+str(f1_score(y_test, y_pred,average='macro')), bg="#F3F0E7")

Nhan = Label(window)
Nhan.grid(row=13, column=1)
#Hàm chạy giao diện
window.mainloop()
