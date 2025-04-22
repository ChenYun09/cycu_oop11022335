# 匯入模組
import mymodule

# 使用模組中的函式
print(mymodule.greet("Alice"))

# 使用模組中的變數
print(f"The value of PI is: {mymodule.PI}")

# 使用模組中的類別
calc = mymodule.Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"5 - 3 = {calc.subtract(5, 3)}")