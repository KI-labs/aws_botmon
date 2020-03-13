from app.utils.awshelper import AWSHelper


# Main function
def main():
    aws_operations = AWSHelper()
    print("aws_operations.result", aws_operations.result)
    print("type_instances", type(aws_operations.result))


if __name__ == '__main__':
    main()
