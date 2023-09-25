def linearSearchProduct(productList, targetProduct):
    indices = []
    for index, product in enumerate(productList):
        if product == targetProduct:
            indices.append(index)
    return indices

# Define the products list and target
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2= 'apple'
# Call the function and print the result
result = linearSearchProduct(products, target)
print(result)
