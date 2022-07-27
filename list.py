

##Create a list of AWS Service Inventory using Python.

#1. The list should be empty initially.
service_list = []

#2. Populate the list using append or insert.
service_list += ['ec2', 's3', 'CloudWatch', 'CloudTrail', 'Xray', 'CloudFormation', 'ElasticBeanStalk', 'CodeDeploy', 'CodeCommit', 'Lambda', 'ECS', 'CloudFront', 'IAM', 'RDS']

#3. Print the list and the length of the list.
print(service_list)
print(len(service_list))
#4. Remove two specific services from the list by name or by index.
del service_list[0:2]    # This deletes the first 2 services from the list

#5. Print the new list and the new length of the list.
print(service_list)
print(len(service_list))

