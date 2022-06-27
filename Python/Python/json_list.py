import json


def terraformQuery(json):
    json.dumps(json)
    # for block in json:
        # print(block['resources'][0]['instances'][0]['attributes']['capacity_reservation_specification'][0]['capacity_reservation_preference'])
        # for res_block in resources:
            # print(res_block['type'])

        # print(type(block['resources']))

terraform_state = [{
  "version": 4,
  "terraform_version": "1.1.4",
  "serial": 11,
  "lineage": "967415b8-5051-c432-aff0-003a7c34cc0e",
  "outputs": {},
  "resources": [
    {
      "mode": "managed",
      "type": "aws_instance",
      "name": "app_server",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 1,
          "attributes": {
            "ami": "ami-0c635ee4f691a2310",
            "arn": "arn:aws:ec2:ap-southeast-2:553986872300:instance/i-0408a19b7a396afdc",
            "associate_public_ip_address": "true",
            "availability_zone": "ap-southeast-2b",
            "capacity_reservation_specification": [
              {
                "capacity_reservation_preference": "open",
                "capacity_reservation_target": []
              }
            ],
            "cpu_core_count": 1,
            "cpu_threads_per_core": 1,
            "credit_specification": [
              {
                "cpu_credits": "standard"
              }
            ],
            # "disable_api_termination": false,
            "ebs_block_device": [],
            # "ebs_optimized": false,
            "enclave_options": [
              {
                # "enabled": false
              }
            ],
            "ephemeral_block_device": [],
            # "get_password_data": false,
            # "hibernation": false,
            # "host_id": null,
            "iam_instance_profile": "",
            "id": "i-0408a19b7a396afdc",
            "instance_initiated_shutdown_behavior": "stop",
            "instance_state": "running",
            "instance_type": "t2.micro",
            "ipv6_address_count": 0,
            "ipv6_addresses": [],
            "key_name": "",
            "launch_template": [],
            "metadata_options": [
              {
                "http_endpoint": "enabled",
                "http_put_response_hop_limit": 1,
                "http_tokens": "optional",
                "instance_metadata_tags": "disabled"
              }
            ],
            # "monitoring": false,
            "network_interface": [],
            "outpost_arn": "",
            "password_data": "",
            "placement_group": "",
            # "placement_partition_number": null,
            "primary_network_interface_id": "eni-09d953f4889c91ac0",
            "private_dns": "ip-172-31-34-199.ap-southeast-2.compute.internal",
            "private_ip": "172.31.34.199",
            "public_dns": "ec2-3-26-206-220.ap-southeast-2.compute.amazonaws.com",
            "public_ip": "3.26.206.220",
            "root_block_device": [
              {
                # "delete_on_termination": true,
                "device_name": "/dev/xvda",
                # "encrypted": false,
                "iops": 100,
                "kms_key_id": "",
                "tags": {},
                "throughput": 0,
                "volume_id": "vol-02838d372cf7ee079",
                "volume_size": 8,
                "volume_type": "gp2"
              }
            ],
            "secondary_private_ips": [],
            "security_groups": [
              "default"
            ],
            "source_dest_check": "true",
            "subnet_id": "subnet-3868b870",
            "tags": {
              "Name": "TestInstance",
              "password": "secret"
            },
            "tags_all": {
              "Name": "TestInstance",
              "password": "secret"
            },
        #     "tenancy": "default",
        #     "timeouts": null,
        #     "user_data": null,
        #     "user_data_base64": null,
        #     "volume_tags": null,
        #     "vpc_security_group_ids": [
        #       "sg-43b42d00"
        #     ]
        #   },
          "sensitive_attributes": [],
          "private": "eyJlMmJmYjczMC1lY2FhLTExZTYtOGY4OC0zNDM2M2JjN2M0YzAiOnsiY3JlYXRlIjo2MDAwMDAwMDAwMDAsImRlbGV0ZSI6MTIwMDAwMDAwMDAwMCwidXBkYXRlIjo2MDAwMDAwMDAwMDB9LCJzY2hlbWFfdmVyc2lvbiI6IjEifQ=="
        }
        }
      ]
    }
  ]
}
]


terraformQuery(terraform_state)