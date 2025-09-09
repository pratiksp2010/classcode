from mean_var_std import calculate
test_input = [0,1,2,3,4,5,6,7,8]
result = calculate(test_input)
print("Input:", test_input)
print("Output:")
for key, value in result.items():
    print(f"{key}: {value}")
