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

# GPU 인스턴스 생성
resource "aws_instance" "gpu_server" {
  # Deep Learning AMI GPU PyTorch 2.0.1 (Amazon Linux 2) 
  # AMI ID는 리전별로 다를 수 있으므로 확인 필요
  ami = "ami-0f4f25175965c2240"

  # GPU 인스턴스 타입 선택
  # g4dn.xlarge: NVIDIA T4 GPU
  # p3.2xlarge: NVIDIA V100 GPU
  instance_type = "g4dn.xlarge"

  vpc_security_group_ids = ["sg-041bac05a748dedd1"]
  subnet_id              = "subnet-02a3602902e8905f0"

  root_block_device {
    volume_size = 100 # GB
    volume_type = "gp3"
  }

  # GPU 드라이버 설치를 위한 사용자 데이터
  user_data = <<-EOF
              #!/bin/bash
              nvidia-smi # GPU 상태 확인
              EOF

  tags = {
    Name    = "GPUInstance"
    Purpose = "ML-Training"
  }
}

# EIP 할당 (선택사항)
resource "aws_eip" "gpu_ip" {
  instance = aws_instance.gpu_server.id
  vpc      = true

  tags = {
    Name = "GPU-Instance-IP"
  }
}