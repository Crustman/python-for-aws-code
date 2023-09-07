"""Use a list of AWS services and demonstrate various loop operations.
"""


def main():
    aws_services = ["S3", "Lambda", "EC2", "RDS", "DynamoDB"]
    # print(f"AWS services list: {aws_services}")

    # print("\nUsing a for loop to iterate through the list:")
    for service in aws_services:
        print(service)
        print("")

    index = len(aws_services) - 1
    while index >= 0:
        print(aws_services[index])
        index -= 1

    print("\nUsing enumerate() with a for loop to get both index and value:\n")
    for index, service in enumerate(aws_services):
        print(f"Service # {index + 1}: {service}.")


if __name__ == "__main__":
    main()
