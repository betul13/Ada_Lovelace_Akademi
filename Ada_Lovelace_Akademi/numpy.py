import numpy as np

array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([0, .5, 1, 1.5])

array_b

array_b[-1]

array_a[:2]

array_a.dtype  #içindeki verininin tipini verir.

np.array([1, 2, 3, 4], dtype = np.float_)

## Dimensions and shapes

my_array = np.array([[1, 2, 3],
                     [4, 5, 6]])


my_array.ndim #boyut sayısı
my_array.shape #boyut bilgisi
my_array.size #eleman sayısı


#indexing and slicing

my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

my_array[1][2]

my_array[1,2]

my_array[0:2, 1:2]

my_array[1] = np.array([2, 4, 10])

my_array[0,2] = 11

my_array = np.arange(0, 10)
my_array.reshape(5,2)
np.arange(1,10.1,2)

np.random.random((5,2)) #0 ile 1 arasında 5,2 boyutlu matris
np.random.normal(10, 4, (3, 4)) # ort : 10 std : 4 rastgele boyutu 3,4
np.random.randint(0, 10, size = 10) # 0 ile 10 arasında rastgele 10 sayı
np.zeros((10,2), dtype = float)
np.ones((2,5))

np.eye(5,4)
np.linspace(5,10,4)
#any(), all(), full(), concatenate()
my_list = [False, True, False]
result = any(my_list)

my_list = [True, True, True]
result = all(my_list)
print(result)  # True
import numpy as np

# 3x3 boyutunda, değeri 7 olan bir dizi oluştur
arr = np.full((3, 3), 7)
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Dizileri birleştir
result = np.concatenate((arr1, arr2, axis = 1))

#statistics

arr1.sum() #arrayin içindeki değerleri topluyor
my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
my_array.sum(axis =1)

arr1 += 10
arr1[arr1 < 2]

#fancy index
catch = [1,2]
my_array[catch]

my_array[~(my_array > my_array.mean())]

my_arr = np.random.randint(0, 100,(3,3))
my_arr[my_arr > 30]

np.dot(arr1,arr2)
my_array.T #transpoze

#matematiksel işlemler daha kısa sürede yapılabilir.