def main():
    aws_services = ["S3", "Lambda", "EC2", "RDS", "DynamoDB"]
    for service in aws_services:
        print(service)

    # Use a while loop to iterate through the list in reverse order
    print("\nUsing a while loop to iterate through the list in reverse order:\n")

    index = len(aws_services) - 1
    while index >= 0:
        print(aws_services[index])
        index -= 1

    print("\nUsing enumerate() with a for loop to get both index and value:")

    for index, service in enumerate(aws_services):
        print(f"Service # {index}: {service}.")


if __name__ == "__main__":
    main()
