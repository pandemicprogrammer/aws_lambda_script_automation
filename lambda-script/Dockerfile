# Use FROM command for python or Lambda
FROM public.ecr.aws/lambda/python:3.9 

# COPY the files or folders you want copied
COPY app.py .
COPY mappings.json .
# After COPY specify the destination
COPY requirements.txt .

RUN pip install -r requirements.txt
CMD [ "app.run" ]

# Build docker image:
# <docker build -t lambda-script .>