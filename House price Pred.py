def price_prediction(bhk, price_per_sqft):
    size_map = {
        1: 600,
        2: 900,
        3: 1200
    }

    if bhk not in size_map:
        return None

    return size_map[bhk] * price_per_sqft


def main():
    bhk = int(input("Enter the number of BHK (1/2/3): "))
    price_per_sqft = int(input("Enter the price per square feet: "))

    price = price_prediction(bhk, price_per_sqft)

    if price is None:
        print("Invalid BHK selection!")
    else:
        print(f"The predicted price for a {bhk} BHK apartment is: ₹{price:,}")


main()
