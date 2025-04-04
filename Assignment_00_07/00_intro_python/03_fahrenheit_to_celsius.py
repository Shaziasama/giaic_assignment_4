def main():
    fahrenheit = float(input("\033[1;3mEnter the temperature in Fahrenheit: "))
    
    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"The temperature in Celsius is {celsius:.2f} degrees.")
if __name__ == "__main__":
    main()