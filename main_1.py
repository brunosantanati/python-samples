def calculate_total(price, tax):
    return price * (1 + tax)

def main():
    print("Starting financial calculator...")
    result = calculate_total(100, 0.08)
    print(f"Total: ${result}")

# This tells Python to execute the main function when running this file
if __name__ == "__main__":
    main()