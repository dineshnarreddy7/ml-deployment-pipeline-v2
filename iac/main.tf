provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "ml_app_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "ML Deployment App Server"
  }
}
