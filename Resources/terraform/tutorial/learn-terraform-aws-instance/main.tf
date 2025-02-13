terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0077297a838d6761d"
  instance_type = "t3.micro"
  vpc_security_group_ids = ["sg-041bac05a748dedd1"]
  subnet_id = "subnet-02a3602902e8905f0"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
