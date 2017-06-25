def main():
    try:
        print("Do Something")
    except (FirstException, SecondException) as e:
        # Handle Your Exceptions
        print(e)